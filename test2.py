import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix

from src.miscellaneous.settings_getter import get_settings
from src.miscellaneous.data_loader import *
from src.miscellaneous.logger_initializer import initialize_logger


@logger.catch
def main():
    data = get_datasets()
    # print(data[0].head())
    donor_train = data[0][data[0].columns[:-1]].copy()
    donor_train.columns = [str(c) for c in donor_train.columns]
    print(data[0].head())
    X_train = one_hot(donor_train, donor_train.columns)
    print(X_train.head())
    y_train = data[0][data[0].columns[-1]].copy()
    print(y_train.head())

    donor_test = data[1][data[1].columns[:-1]].copy()
    donor_test.columns = [str(c) for c in donor_test.columns]
    X_test = one_hot(donor_test, donor_test.columns)
    print(X_test.head())
    y_test = data[1][data[1].columns[-1]].copy()
    
    tree = DecisionTreeClassifier(random_state = 42)
    tree.fit(X_train, y_train)
    plt.figure(figsize=(15, 7.5))
    plot_tree(tree,
              filled = True,
              rounded= True,
              class_names= ["Yes", "No"],
              feature_names= X_train.columns)
    
    return

if __name__ == "__main__":
    initialize_logger()
    main()
