from loguru import logger
import numpy as np


@logger.catch
def load_data(path: str) -> np:
    try:
        if not isinstance(path, str):
            raise TypeError(f"Expected str path to file, got {type(path)} instead.")
        EXPECTED_EXTENSION = ".dat"
        if EXPECTED_EXTENSION not in path:
            raise ValueError(f"Expected .dat file, got {path} instead.")
        with open(path) as f:
            file_contents = f.read()
        file_contents = np.array(file_contents.splitlines())
        return file_contents[0], file_contents[1:]
    except (TypeError, ValueError) as err:
        logger.critical(err)
        exit(1)


if __name__ == "__main__":
    raise NotImplementedError("Use as package")
