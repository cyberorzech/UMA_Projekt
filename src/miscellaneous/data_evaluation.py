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

@logger.catch
def get_precision():
    pass

@logger.catch
def get_recall():
    pass


if __name__ == "__main__":
    raise NotImplementedError("Use as package")