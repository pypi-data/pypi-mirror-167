from . import backUpVals, restoreMethods


def restoreEpics(bak=backUpVals, restoreMethods=restoreMethods):
    '''
    restoreEpics(bak=backUpVals)

    Restores EPICS channels to their backed up values using predefind
    restoreMethods.

    Arguments
    ---------
    bak (dict): Dictionary of backup values during a particular instance
                [restoreEpics.backUpVals]
    restoreMethods (dict): Dictionary containing restortion methods for
                           different kinds of backed up values
                           [restoreEpics.restoreMethods]

    Notes
    --------
    bak dictionary minimum required format:
      * The key value of the dictionary does not matter.
      * Each element must be a dictionary containing atleast:
        * 'sno' key which is uniquely defined to store chronology of changes.
        * 'type' key matching a restoreMethods type to select the appropriate
          restoration method.
    restoreMethods dictionary minimum required format:
      * The keys of this dictionary should correspond to the type of object
        they would restore eg channel, matrix etc.
      * The value of the dictionary should be a method that takes in entire
        backed up element dictionary as argument and restores that element.

    Examples
    --------
    Use without arguments to restore everything that was changed using methods
    of this package:
    >> restoreEpics()
    If you want to restore a particular set of backed up values only, provide
    them as a dictionary:
    >> restoreEpics(bak=bak)
    If you want to use new custom restoration methods, define them in a
    dictionary and pass them along
    >> restoreEpics(bak=bak, restoreMethods=customMethods)
    '''
    print('Restoring channel values...')
    for ii in range(len(bak)-1, -1, -1):
        for ele in bak.values():
            if ii == ele['sno']:
                restoreMethods[ele['type']](ele)
