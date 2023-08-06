from .io import lmdb_data
import sys


def lmdb_info(lmdb_path):
    import numpy as np
    format_info = "{0:>20},  {1:>8},  {2},  {3}"
    print(format_info.format('Name', 'DType', 'Shape', 'Data'))
    with np.printoptions(suppress=True, threshold=5):
        for key, arr in lmdb_data(lmdb_path):
            dtype = np.dtype(arr.dtype).name
            shape = arr.shape
            print(format_info.format(key.decode(), dtype, shape,
                                     arr.flatten()))


if __name__ == "__main__":
    lmdb_path = sys.argv[1]
    lmdb_info(lmdb_path)
