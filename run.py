from src.miscellaneous.settings_getter import get_settings
from src.miscellaneous.data_loader import *
from src.miscellaneous.logger_initializer import initialize_logger


@logger.catch
def main():
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

    TRAINING_SET_SIZE = .75
    donor_training_set, donor_test_set = split_to_training_and_test(donor_positive_only, donor_negative_only)
    acceptor_training_set, acceptor_test_set = split_to_training_and_test(acceptor_positive_only, acceptor_negative_only)
    logger.success(f"Data have been prepared. Summary\n{len(donor_training_set)=}\n{len(donor_test_set)=}\n{len(acceptor_training_set)=}\n{len(acceptor_test_set)=}")



if __name__ == "__main__":
    initialize_logger()
    main()
