from random import sample
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
from loguru import logger

class Node:
    # pierwotna wersja
    # def __init__(cls, label, edges, leafs ) -> None:
    #     pass
    #     # edges, leafs, node_label
    @logger.catch
    def __init__(cls, dataset: pd.DataFrame, label: int, edges) -> None:
        sample_row = dataset.iloc[0]
        sample_row = sample_row.drop([label])
        cls.__splitted_dataset =  [pd.DataFrame(columns=sample_row.index)] * len(edges)
        for index, edge in enumerate(edges):
            for indice, row in dataset.iterrows():
                if str(row[label]) == str(edge):
                    row = row.drop([label])
                    cls.__splitted_dataset[index] = cls.__splitted_dataset[index].append(row, ignore_index=True)
            # dla kazdej krawedzi, dla kazdego row w dataset, jesli row w kolumnie o id label jest rowny edge to dopisz do splitted_dataset na swoje miejsce

    @logger.catch
    def get_splitted_dataset(cls):
        return cls.__splitted_dataset

if __name__ == "__main__":
    raise NotImplementedError("Use as class")