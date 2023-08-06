from epics import caput
import numpy as np
from .readMatrix import readMatrix
from time import sleep
from . import backUpVals, restoreMethods


def writeMatrix(basename, mat, firstRow=1, firstCol=1, suffix=None,
                tramp=None, bak=backUpVals):
    '''
    writeMatrix(basename, mat, firstRow=1, firstCol=1, suffix=None, tramp=None,
                bak=backUpVals)

    Write epics channels on a EPICS channel matrix.

    Arguments
    ---------
    basename (str): Base name of EPICS channel matrix (See notes)
    mat (numpy.ndarray): Numpy 2-D array matrix to write
    firstRow (int): Index of the first row to read from the matrix [1]
    firstCol (int): Index of the first column to read from the matrix [1]
    suffix (str): Suffix after the matrix enumeration in channel names [None]
    tramp (float): Ramp time for change in value [None]

    Returns
    --------
    retMat (numpy.ndarray): Numpy 2-D array containing output of each matrix
                            element write operation
                            1  on succesful completion
                            -1 or other negative value on failure of the
                            low-level CA put.
                            None  on a failure to connect to the PV.

    Notes
    --------
    The channel names in matrix would be constructed as:
        For i as row index, and j as column index:
            if suffix is None:
                basename_i_j
            else:
                basename_i_j_suffix
    '''
    curMat = readMatrix(basename=basename, rows=mat.shape[0],
                        cols=mat.shape[1], firstRow=firstRow,
                        firstCol=firstCol, suffix=suffix)
    if basename not in bak:
        name = (basename + '_' + str(firstRow) + '_' + str(firstCol)
                + '_' + str(mat.shape[0]) + '_' + str(mat.shape[1]))
        bak[name] = {'type': 'matrix', 'suffix': suffix,
                     'basename': basename,
                     'value': curMat, 'firstRow': firstRow,
                     'firstCol': firstCol, 'tramp': tramp, 'sno': len(bak)}
    if tramp is not None:
        # Special case, changing filter gains, can use TRAMP
        rampYourself = True
        if suffix == 'GAIN':
            try:
                curTramp = readMatrix(basename=basename, rows=mat.shape[0],
                                      cols=mat.shape[1], firstRow=firstRow,
                                      firstCol=firstCol, suffix='TRAMP')
                for ii in range(firstRow, firstRow + np.shape(mat)[0]):
                    for jj in range(firstCol, firstCol + np.shape(mat)[1]):
                        chName = (basename + '_' + str(ii) + '_' + str(jj)
                                  + '_TRAMP')
                        caput(chName, tramp)
                rampYourself = False
            except BaseException:
                rampYourself = True
        if rampYourself:
            rampSteps = 100
            # Get current matrix values
            stepMat = (mat - curMat) / rampSteps
            for tstep in range(1, rampSteps):
                for ii in range(firstRow, firstRow + np.shape(mat)[0]):
                    for jj in range(firstCol, firstCol + np.shape(mat)[1]):
                        chName = basename + '_' + str(ii) + '_' + str(jj)
                        if suffix is not None:
                            chName = chName + '_' + suffix
                        matToWrite = (curMat[ii-firstRow, jj-firstCol]
                                      + tstep * stepMat[ii-firstRow,
                                                        jj-firstCol])
                        caput(chName, matToWrite)
                sleep(tramp/rampSteps)
    # Finally write the required matrix
    retMat = np.zeros_like(mat)
    for ii in range(firstRow, firstRow + np.shape(mat)[0]):
        for jj in range(firstCol, firstCol + np.shape(mat)[1]):
            chName = basename + '_' + str(ii) + '_' + str(jj)
            if suffix is not None:
                chName = chName + '_' + suffix
            matii = ii-firstRow
            matjj = jj-firstCol
            retMat[matii, matjj] = caput(chName, mat[matii, matjj])
    if tramp is not None:
        if not rampYourself:
            sleep(tramp + 0.5)    # Wait for ramping to end
            for ii in range(firstRow, firstRow + np.shape(mat)[0]):
                for jj in range(firstCol, firstCol + np.shape(mat)[1]):
                    chName = (basename + '_' + str(ii) + '_' + str(jj)
                              + '_TRAMP')
                    caput(chName, curTramp[ii-firstRow, jj-firstCol])
    return retMat


def restoreMatrix(bakVal):
    writeMatrix(basename=bakVal['basename'], suffix=bakVal['suffix'],
                mat=bakVal['value'], firstCol=bakVal['firstCol'],
                firstRow=bakVal['firstRow'], tramp=bakVal['tramp'], bak={})


restoreMethods['matrix'] = restoreMatrix
