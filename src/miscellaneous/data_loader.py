from ast import Str
from loguru import logger
import numpy as np
import pandas as pd

@logger.catch
def verify_missing(df: pd.DataFrame):
    nukes = {'A', 'C', 'G', 'T'}
    try:
        if not all(map(lambda c: set(df[c].unique()).issubset(nukes), df.columns)):
            raise ValueError(f"Attribute value not in set: {nukes}")
    except (TypeError, ValueError) as err:
        logger.critical(err)
        exit(1)
    return True
    

@logger.catch
# def load_dataframe(path: str) -> pd:
def load_dataframe(strings, label) -> pd:
    xx = [list(s) for s in strings]  # 2d array from list of strings
    df = pd.DataFrame(xx)
    # verify_missing(df)
    df.columns = [str(c) for c in df.columns]  # convert columns to strings from series
    df.insert(df.shape[1], "label", [str(label)] * len(strings))  # add label
    
    return df

@logger.catch
def load_data(path: str) -> tuple:
    try:
        if not isinstance(path, str):
            raise TypeError(f"Expected str path to file, got {type(path)} instead.")
        EXPECTED_EXTENSION = ".dat"
        if EXPECTED_EXTENSION not in path:
            raise ValueError(f"Expected .dat file, got {path} instead.")
        with open(path) as f:
            file_contents = f.read()
        file_contents = np.array(file_contents.splitlines())
        return file_contents[0], file_contents[1:]
    except (TypeError, ValueError) as err:
        logger.critical(err)
        exit(1)


@logger.catch
def get_positive_only(data: np) -> np:
    POSITIVE_ETIQUETTE = "1"
    positive_indexes = np.where(data == POSITIVE_ETIQUETTE)[0]
    return data[positive_indexes + 1]

@logger.catch
def get_negative_only(data: np) -> np:
    NEGATIVE_ETIQUETTE = "0"
    negative_indexes = np.where(data == NEGATIVE_ETIQUETTE)[0]
    return data[negative_indexes + 1]

@logger.catch
def check_data_length(data: np) -> bool:
    try:
        FIRST_DATA_SAMPLE = data[0]
        if not all(map(lambda v: len(v) == len(FIRST_DATA_SAMPLE), data)):
            raise ValueError("Data have inconsistent length")
    except ValueError as ve:
        logger.error(ve)
        exit(1)


if __name__ == "__main__":
    raise NotImplementedError("Use as package")
