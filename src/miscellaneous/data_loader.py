from loguru import logger
import numpy as np
import pandas as pd


@logger.catch
def load_dataframe(path: str) -> pd:
    # kolumny_lista = list()
    # .. wsadzasz dane [arg1, arg2, ..., etykieta]
    pass


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

if __name__ == "__main__":
    raise NotImplementedError("Use as package")
    # from run import main
    # donor_positive, donor_negative, acceptor_positive, acceptor_negative = main()
    # training, test = split_to_training_and_test(donor_positive, donor_negative)