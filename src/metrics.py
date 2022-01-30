from loguru import logger

@logger.catch
def update_label_score(label, letter_score):
    TRUE_INDEX = 0
    FALSE_INDEX = 1
    if label == "1":
        letter_score[TRUE_INDEX] += 1
    else:
        letter_score[FALSE_INDEX] += 1
    return letter_score

@logger.catch
def check_letters_and_labels(column_data, labels):
    # [true_amount, false_amount]
    a_score = [0,0]
    c_score = [0,0]
    g_score = [0,0]
    t_score = [0,0]
    for row_index, letter in enumerate(column_data):
        if letter == "A":
            a_score = update_label_score(label=labels[row_index], letter_score=a_score)
        elif letter == "C":
            c_score = update_label_score(label=labels[row_index], letter_score=c_score)
        elif letter == "G":
            g_score = update_label_score(label=labels[row_index], letter_score=g_score)
        elif letter == "T":
            t_score = update_label_score(label=labels[row_index], letter_score=t_score)
    return a_score, c_score, g_score, t_score

@logger.catch
def get_leafs_gini_impurity(leaf_score: list):
    true_score = leaf_score[0]
    false_score = leaf_score[1]
    true_possibility = (true_score/(true_score + false_score))**2
    false_possibility = (false_score/(true_score + false_score))**2
    gini = 1 - true_possibility - false_possibility
    return leaf_score.append(gini)

@logger.catch
def get_total_gini_impurity(scores: list) -> float:
    pass



if __name__ == "__main__":
    raise NotImplementedError("Use as package")