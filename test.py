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

    check_data_length(donor_positive_only); check_data_length(donor_negative_only)
    check_data_length(acceptor_positive_only); check_data_length(acceptor_negative_only)
    logger.success("Data is valid")

    df = load_dataframe(donor_positive_only, 1)
    donor_positive = df

    # print(type(donor_positive))
    # print(len(donor_positive))
    # print(donor_positive.head())
    
    df = load_dataframe(donor_negative_only, 0)
    # [print(df[c].unique()) for c in df.columns]
    # l = len(df.loc[ (df[('12', '13')] == 'N') ] )
    # l = len(df.loc[ (df['12'] == 'N') | (df['13'] == 'N') ] )
    # print(l)
    # missing = (df.loc[ (df['12'] == 'N') | (df['13'] == 'N') ] )
    # print(missing)
    donor_negative = df.loc[ (df['12'] != 'N') & (df['13'] != 'N') ]
    # print(type(donor_negative))
    # [print(donor_negative[c].unique()) for c in donor_negative.columns]
    
    df = load_dataframe(acceptor_positive_only, 1)
    # [print(df[c].unique()) for c in df.columns]
    
    # acceptor_negative = load_dataframe(acceptor_negative_only, 0)

    logger.success(f"Summary\n{len(donor_positive)=}\n{len(donor_negative)=}\n{len(acceptor_positive_only)=}\n{len(acceptor_negative_only)=}")

    return donor_positive, donor_negative, acceptor_positive_only, acceptor_negative_only



if __name__ == "__main__":
    initialize_logger()
    main()
