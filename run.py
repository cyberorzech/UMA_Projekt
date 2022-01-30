from src.miscellaneous.data_loader import *
from src.metrics import *
from src.miscellaneous.logger_initializer import initialize_logger


@logger.catch
def main():
    # Get datasets
    donor_training_set, donor_test_set, acceptor_training_set, acceptor_test_set, donor_artifact_index, acceptor_artifact_index = get_datasets()

    # Under development: prepare data for the node
    x = donor_training_set
    labels = x["label"]
    gini_results = list()
    for column_index in x:
        logger.info(f"Begin processing {column_index} column")
        column_data = x[column_index]
        scores = [a_score, c_score, g_score, t_score] = check_letters_and_labels(column_data, labels)
        logger.info(f"{column_index=}{a_score=}{c_score=}{g_score=}{t_score=}")
        for score in scores:
            score = get_leafs_gini_impurity(score)
        total_gini = get_total_gini_impurity(scores)
        #logger.success(f"{total_gini=}")
        gini_results.append({"column_index": column_index, "total_gini": total_gini})
    logger.success(gini_results)

if __name__ == "__main__":
    initialize_logger()
    main()
