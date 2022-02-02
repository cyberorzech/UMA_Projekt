from src.miscellaneous.data_loader import *
from src.metrics import *
from src.node import Node
from src.miscellaneous.logger_initializer import initialize_logger

@logger.catch
def get_purest_node(dataset):
    # Under development: prepare data for the node
    labels = dataset["label"]
    gini_results = list()
    for column_index in dataset:
        if column_index == "label":
            continue
        #logger.info(f"Begin processing {column_index} column")
        column_data = dataset[column_index]
        scores = [a_score, c_score, g_score, t_score] = check_letters_and_labels(column_data, labels)
        #logger.info(f"{column_index=}{a_score=}{c_score=}{g_score=}{t_score=}")
        for score in scores:
            score = get_leafs_gini_impurity(score)
        total_gini = get_total_gini_impurity(scores)
        #logger.success(f"{total_gini=}")
        gini_results.append({"column_index": column_index, "total_gini": total_gini})
    # logger.success(gini_results)
    least_gini = 1
    least_gini_column = None
    for res in gini_results:
        if res["total_gini"] < least_gini:
            least_gini = res["total_gini"]
            least_gini_column = res["column_index"]
    logger.success(f"{least_gini=} {least_gini_column=}")
    return least_gini_column, least_gini

@logger.catch
def create_node(dataset, edges):
    purest_node_label, gini_impurity = get_purest_node(dataset)
    node = Node(dataset, purest_node_label, edges)
    splitted_dataset = node.get_splitted_dataset()
    return splitted_dataset, gini_impurity, purest_node_label

@logger.catch
def build_tree(splitted_dataset: list, edges=["A", "C", "G", "T"], gini_impurity=1, purest_node_label=None):
    if not purest_node_label:
        splitted_dataset, gini_impurity, purest_node_label = create_node(splitted_dataset, edges)
    


@logger.catch
def main():
    # Get datasets
    donor_training_set, donor_test_set, acceptor_training_set, acceptor_test_set, donor_artifact_index, acceptor_artifact_index = get_datasets()
    edges = ["A", "C", "G", "T"]
    
    purest_node_label, gini_impurity = get_purest_node(donor_training_set)
    node = Node(donor_training_set, purest_node_label, edges)
    splitted_dataset = node.get_splitted_dataset()
    logger.success(splitted_dataset)
    
    




if __name__ == "__main__":
    initialize_logger()
    main()
