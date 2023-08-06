from epics import caget
import numpy as np


def readMatrix(basename, rows, cols, firstRow=1, firstCol=1, suffix=None):
    '''
    readMatrix(basename, rows, cols, firstRow=1, firstCol=1, suffix=None

    Reads epics channels from a EPICS channel matrix.

    Arguments
    ---------
    basename (str): Base name of EPICS channel matrix (See notes)
    rows (int): Number of rows to read
    cols (int): Number of columns to read
    firstRow (int): Index of the first row to read from the matrix [1]
    firstCol (int): Index of the first column to read from the matrix [1]
    suffix (str): Suffix after the matrix enumeration in channel names [None]

    Returns
    --------
    mat (numpy.ndarray): Numpy 2-D array containing the read matrix

    Notes
    --------
    The channel names in matrix would be constructed as:
        For i as row index, and j as column index:
            if suffix is None:
                basename_i_j
            else:
                basename_i_j_suffix
    '''
    mat = np.zeros((rows, cols))
    for ii in range(firstRow, firstRow + rows):
        for jj in range(firstCol, firstCol + cols):
            chName = basename + '_' + str(ii) + '_' + str(jj)
            if suffix is not None:
                chName = chName + '_' + suffix
            mat[ii - firstRow, jj-firstCol] = caget(chName)
    return mat
