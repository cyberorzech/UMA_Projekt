from loguru import logger
import numpy as np
import pandas as pd

from src.miscellaneous.settings_getter import get_settings


    
@logger.catch
def one_hot(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    x = pd.get_dummies(df, columns = cols)
    return x
    
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
def get_positive_only(data: np.array) -> np.array:
    POSITIVE_ETIQUETTE = "1"
    positive_indexes = np.where(data == POSITIVE_ETIQUETTE)[0]
    return data[positive_indexes + 1]


@logger.catch
def get_negative_only(data: np.array) -> np.array:
    NEGATIVE_ETIQUETTE = "0"
    negative_indexes = np.where(data == NEGATIVE_ETIQUETTE)[0]
    return data[negative_indexes + 1]


@logger.catch
def check_data_length(data: np.array) -> bool:
    try:
        FIRST_DATA_SAMPLE = data[0]
        if not all(map(lambda v: len(v) == len(FIRST_DATA_SAMPLE), data)):
            raise ValueError("Data have inconsistent length")
    except ValueError as ve:
        logger.error(ve)
        exit(1)

@logger.catch
def split_to_training_and_test(positive_data: np.array, negative_data: np.array, training_set_size=.75) -> np.array:
    POSITIVE_LABEL = "1"
    NEGATIVE_LABEL = "0"

    positive_data_with_labels = np.array([f"{str(dna_sequence)}{POSITIVE_LABEL}" for dna_sequence in positive_data])
    negative_data_with_labels = np.array([f"{str(dna_sequence)}{NEGATIVE_LABEL}" for dna_sequence in negative_data])
    merged_labeled_data = np.concatenate((positive_data_with_labels, negative_data_with_labels))
    merged_size = int(np.shape(merged_labeled_data)[0])
    positive_size = int(np.shape(positive_data_with_labels)[0])
    negative_size = int(np.shape(negative_data_with_labels)[0])
    assert positive_size + negative_size == merged_size

    SHUFFLE_REPEATS = 10
    for _ in range(SHUFFLE_REPEATS):
        np.random.shuffle(merged_labeled_data)

    training_set = merged_labeled_data[:int(training_set_size*len(merged_labeled_data)) - 1]
    test_set = merged_labeled_data[int(training_set_size*len(merged_labeled_data)):]
    return training_set, test_set

@logger.catch
def convert_array_to_dataframe(data_array: np.array) -> pd.DataFrame:
    row_length = len(data_array[0])
    data_with_splitted_rows = [list(str_seq) for str_seq in data_array]
    columns = map(int, range(row_length - 1))
    columns = list(columns)
    columns.append("label")
    return pd.DataFrame(data=data_with_splitted_rows, columns=columns)

@logger.catch
def get_datasets() -> tuple:
    """
    master function which calls all above and prepares datasets in result
    """
    SETTINGS = get_settings()
    DONOR_DATASET_PATH = SETTINGS["DONOR_DATASET_PATH"]
    ACCEPTOR_DATASET_PATH = SETTINGS["ACCEPTOR_DATASET_PATH"]

    donor_artifact_index, donor_dataset = load_data(DONOR_DATASET_PATH)
    acceptor_artifact_index, acceptor_dataset = load_data(ACCEPTOR_DATASET_PATH)
    logger.success("Data loaded")

    donor_positive_only = get_positive_only(donor_dataset)
    donor_negative_only = get_negative_only(donor_dataset)
    acceptor_positive_only = get_positive_only(acceptor_dataset)
    acceptor_negative_only = get_negative_only(acceptor_dataset)

    check_data_length(donor_positive_only)
    check_data_length(donor_negative_only)
    check_data_length(acceptor_positive_only)
    check_data_length(acceptor_negative_only)
    logger.success("Data is valid")
    logger.success(
        f"Raw data summary:\n{len(donor_positive_only)=}\n{len(donor_negative_only)=}\n{len(acceptor_positive_only)=}\n{len(acceptor_negative_only)=}"
    )

    training_set_size = float(SETTINGS["TRAINING_SET_SIZE"])
    donor_training_set, donor_test_set = split_to_training_and_test(donor_positive_only, donor_negative_only, training_set_size)
    acceptor_training_set, acceptor_test_set = split_to_training_and_test(acceptor_positive_only, acceptor_negative_only, training_set_size)
    logger.success(f"Data have been prepared. Summary\n{len(donor_training_set)=}\n{len(donor_test_set)=}\n{len(acceptor_training_set)=}\n{len(acceptor_test_set)=}")

    donor_training_set = convert_array_to_dataframe(donor_training_set)
    donor_test_set = convert_array_to_dataframe(donor_test_set)
    acceptor_training_set = convert_array_to_dataframe(acceptor_training_set)
    acceptor_test_set = convert_array_to_dataframe(acceptor_test_set)

    return donor_training_set, donor_test_set, acceptor_training_set, acceptor_test_set, donor_artifact_index, acceptor_artifact_index


if __name__ == "__main__":
    raise NotImplementedError("Use as package")
