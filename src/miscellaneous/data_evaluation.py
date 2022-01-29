from loguru import logger

@logger.catch
def get_roc():
    pass

@logger.catch
def get_tpc():
    pass

@logger.catch
def get_fpr():
    pass

# the ability of the classifier not to label as positive a sample that is negative
@logger.catch
def get_precision():
    pass

# the ability of the classifier to find all the positive samples
@logger.catch
def get_recall():
    pass

# the harmonic mean of the precision and recall
@logger.catch
def get_f1():
    pass

# the weighted harmonic mean of the precision and recall
@logger.catch
def get_fbeta():
    pass


if __name__ == "__main__":
    raise NotImplementedError("Use as package")