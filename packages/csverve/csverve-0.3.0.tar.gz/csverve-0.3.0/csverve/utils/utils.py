from typing import Any
from typing import List, Dict, Union

import pandas as pd  # type: ignore
from csverve.core.csverve_input import CsverveInput
from csverve.core.csverve_output_data_frame import CsverveOutputDataFrame
from csverve.core.csverve_output_file_stream import CsverveOutputFileStream
from csverve.errors import CsverveDtypeError
from csverve.errors import CsverveMergeColumnMismatchException
from csverve.errors import CsverveMergeCommonColException
from csverve.errors import CsverveMergeDtypesEmptyMergeSet
from csverve.errors import CsverveMergeException
from csverve.errors import DtypesMergeException


def pandas_to_std_types(dtype: Any) -> str:
    std_dict = {
        "bool": "bool",
        "int64": "int",
        "int": "int",
        "Int64": "int",
        "float64": "float",
        "float": "float",
        "object": "str",
        "str": "str",
        "category": "category",
    }

    if not isinstance(dtype, str):
        if hasattr(dtype, '__name__'):
            dtype = dtype.__name__
        else:
            raise CsverveDtypeError('Unable to process dtype {}'.format(dtype))

    if dtype not in std_dict:
        raise CsverveDtypeError('Unable to process dtype {}'.format(dtype))

    return std_dict[dtype]


def merge_dtypes(dtypes_all: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Merge pandas dtypes.

    @param dtypes_all: List of dtypes dictionaries, where key = column name, value = pandas dtype.
    @return: Merged dtypes dictionary.
    """

    if not dtypes_all:
        raise CsverveMergeDtypesEmptyMergeSet("must provide dtypes to merge")

    merged_dtypes: Dict[str, str] = {}

    for dtypes in dtypes_all:
        for k, v in dtypes.items():
            if k in merged_dtypes:
                if merged_dtypes[k] != v:
                    raise DtypesMergeException("dtypes not mergeable")
            else:
                merged_dtypes[k] = v

    return merged_dtypes


def concatenate_csv_files_pandas(
        in_filenames: Union[List[str], Dict[str, str]],
        out_filename: str,
        dtypes: Dict[str, str],
        skip_header: bool = False,
        drop_duplicates: bool = False,
        **kwargs
) -> None:
    """
    Concatenate gzipped CSV files.

    @param in_filenames: List of gzipped CSV file paths, or a dictionary where the keys are file paths.
    @param out_filename: Path of resulting concatenated gzipped CSV file and meta YAML.
    @param dtypes: Dictionary of pandas dtypes, where key = column name, value = dtype.
    @param skip_header: boolean, True = write header, False = don't write header.
    @return:
    """

    if kwargs.get('write_header') is not None:
        raise DeprecationWarning('write_header has been deprecated and will be ignored, please use skip_header instead')

    if isinstance(in_filenames, dict):
        in_filenames = list(in_filenames.values())

    data: List[CsverveInput] = [
        CsverveInput(in_filename).read_csv() for in_filename in in_filenames
    ]
    concat_data: pd.DataFrame = pd.concat(data, ignore_index=True)
    if drop_duplicates:
        concat_data = concat_data.drop_duplicates()
    csvoutput: CsverveOutputDataFrame = CsverveOutputDataFrame(
        concat_data, out_filename, dtypes, skip_header=skip_header
    )
    csvoutput.write_df()


def concatenate_csv_files_quick_lowmem(
        inputfiles: List[str],
        output: str,
        dtypes: Dict[str, str],
        columns: List[str],
        skip_header: bool = False,
        **kwargs
) -> None:
    """
    Concatenate gzipped CSV files.

    @param inputfiles: List of gzipped CSV file paths.
    @param output: Path of resulting concatenated gzipped CSV file and meta YAML.
    @param dtypes: Dictionary of pandas dtypes, where key = column name, value = dtype.
    @param columns: List of column names for newly concatenated gzipped CSV file.
    @param skip_header: boolean, True = write header, False = don't write header.
    @return:
    """
    if kwargs.get('write_header') is not None:
        raise DeprecationWarning('write_header has been deprecated and will be ignored, please use skip_header instead')

    csvoutput: CsverveOutputFileStream = CsverveOutputFileStream(
        output, dtypes, skip_header=skip_header, columns=columns
    )
    csvoutput.write_data_streams(inputfiles)


def _validate_merge_cols(frames: List[pd.DataFrame], on: Union[List[str], str]) -> None:
    """
    Make sure frames look good, raise relevant exceptions.

    @param frames: list of pandas DataFrames to merge
    @param on: list of common columns in frames on which to merge
    @return:
    """

    if not on:
        raise CsverveMergeException("unable to merge if given nothing to merge on")

    # check that columns to be merged have identical values
    standard = frames[0][on]
    standard = standard.sort_values(on).reset_index(drop=True)
    for frame in frames:
        comp_df = frame[on].sort_values(on).reset_index(drop=True)
        if not standard.equals(comp_df):
            raise CsverveMergeColumnMismatchException("columns on which to merge must be identical")

    # check that columns to be merged have same dtypes
    for shared_col in on:
        if len(set([frame[shared_col].dtypes for frame in frames])) != 1:
            raise CsverveMergeColumnMismatchException("columns on which to merge must have same dtypes")

    common_cols = set.intersection(*[set(frame.columns) for frame in frames])
    cols_to_check = list(common_cols - set(on))

    for frame1, frame2 in zip(frames[:-1], frames[1:]):
        if not frame1[cols_to_check].equals(frame2[cols_to_check]):
            raise CsverveMergeCommonColException("non-merged common cols must be identical")


def merge_frames(frames: List[pd.DataFrame], how: str, on: List[str]) -> pd.DataFrame:
    """
    Takes in a list of pandas DataFrames, and merges into a single DataFrame.
    #TODO: add handling if empty list is given

    @param frames: List of pandas DataFrames.
    @param how: How to join DataFrames (inner, outer, left, right).
    @param on: Column(s) to join on, comma separated if multiple.
    @return: merged pandas DataFrame.
    """
    if isinstance(on, str):
        on = [on]

    _validate_merge_cols(frames, on)

    if len(frames) == 1:
        return frames[0]
    else:
        left: pd.DataFrame = frames[0]
        right: pd.DataFrame = frames[1]
        cols_to_use: List[str] = list(right.columns.difference(left.columns))
        cols_to_use += on
        cols_to_use = list(set(cols_to_use))

        merged_frame: pd.DataFrame = pd.merge(
            left, right[cols_to_use], how=how, on=on,
        )

        for i, frame in enumerate(frames[2:]):
            merged_frame = pd.merge(
                merged_frame, frame, how=how, on=on,
            )
        return merged_frame
