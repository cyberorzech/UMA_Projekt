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
    logger.success(f"Data loaded successfully as {type(donor_dataset)}")


if __name__ == "__main__":
    initialize_logger()
    main()
