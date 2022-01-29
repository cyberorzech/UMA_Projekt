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
    logger.info(f"{donor_dataset=}")
    logger.info(f"{donor_artifact_index=}")

    donor_positive_only = get_positive_only(donor_dataset)
    logger.info(f"{donor_positive_only=}")
    donor_negative_only = get_negative_only(donor_dataset)
    logger.info(f"{donor_negative_only=}")


if __name__ == "__main__":
    initialize_logger()
    main()
