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
    for column_index in x:
        if column_index > 0:
            break
        column_data = x[column_index]
        scores = [a_score, c_score, g_score, t_score] = check_letters_and_labels(column_data, labels)
        #print(f"{column_index=}{a_score=}{c_score=}{g_score=}{t_score=}")
        for score in scores:
            score = get_leafs_gini_impurity(score)
        total_gini = get_total_gini_impurity(scores)



if __name__ == "__main__":
    initialize_logger()
    main()
