import epics
from . import backUpVals, restoreMethods
from time import sleep


def caput(pvname, value, wait=False, timeout=60.0, tramp=None, bak=backUpVals):
    """
    caput(pvname, value, wait=False, timeout=60.0, bak=backUpVals, tramp=None)

    Put a value to an epics Process Variable (PV) with added option of
    ramping the value lineary. This function stores a backup of the channel
    before changing it that will be reverted by restoreEpics() call.

    Arguments
    ---------
    pvname (str): name of PV
    value (any): value to put to PV
    wait (bool): whether to wait for processing to complete [False]
    timeout (float): maximum time to wait for the processing to complete [60]
    tramp (float): Ramp time for change in value [None]
    bak (dict): Dictionary of backup values during a particular instance

    Returns
    --------
    1  on succesful completion
    -1 or other negative value on failure of the low-level CA put.
    None  on a failure to connect to the PV.

    Examples
    ---------
    To put a value to a PV and return as soon as possible:
    >>> caput('xx', 3.0)
    To wait for processing to finish, use 'wait=True':
    >>> caput('xx', 3.0, wait=True)
    To ramp the change in value linearily in time and wait for it to happen:
    >>> caput('xx', 3.0, wait=True, timeout=5)
    """
    val = epics.caget(pvname, timeout=timeout)
    if pvname not in bak:
        bak[pvname] = {'type': 'channel', 'value': val, 'tramp': tramp,
                       'sno': len(bak), 'name': pvname}
    if tramp is None:
        retVal = epics.caput(pvname=pvname, value=value, wait=wait,
                             timeout=timeout)
    else:
        rampYourself = True
        fus = pvname.rfind('_') + 1
        # If this looks like a GAIN channel, look for TRAMP channel
        if pvname[fus:] in ['GAIN', 'OFFSET']:
            trch = pvname[:-4] + 'TRAMP'
            tbak = epics.caget(pvname=trch, timeout=0.2)
            if tbak is not None:
                rampYourself = False
            else:
                rampYourself = True
        if not rampYourself:
            epics.caput(pvname=trch, value=tramp, wait=wait, timeout=timeout)
            retVal = epics.caput(pvname=pvname, value=value, wait=wait,
                                 timeout=timeout)
            if wait:
                sleep(tramp)
            epics.caput(pvname=trch, value=tbak, wait=wait, timeout=timeout)
        else:
            rampSteps = 100
            valStep = (value - val) / rampSteps
            for tstep in range(1, rampSteps):
                epics.caput(pvname=pvname, value=val + valStep * tstep,
                            wait=wait, timeout=timeout)
                sleep(tramp / rampSteps)
            retVal = epics.caput(pvname=pvname, value=value, wait=wait,
                                 timeout=timeout)
    return retVal


def restoreChannel(bakVal):
    epics.caput(bakVal['name'], bakVal['value'])


restoreMethods['channel'] = restoreChannel
