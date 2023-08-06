from time import sleep
from epics import caget
from .caput import caput
from . import backUpVals, restoreMethods


def writeChannels(chanInfo, bak=backUpVals):
    '''
    writeChannels(chanInfo, bak=backUpVals)

    Write epics channels given in a dictionary format together.

    Arguments
    ---------
    chanInfo (dict): Channel information dictionary. See notes for format.
    bak (dict): Dictionary of backup values during a particular instance
                [restoreEpics.backUpVals]

    Return
    ---------
    retDict (dict): Dictionary with keys as channel names and values as the
                    return value of caput for that channel ie
                    1  on succesful completion
                    -1 or other negative value on failure of the low-level CA
                    put.
                    None on a failure to connect to the PV.

    Notes
    ---------
    chanInfo dictionary minimum required format:
    Required keys:
      channels: Should contain dictionary with channel names as keys and their
                values as:
                  the value to write on teh channel
                  or
                  Dictionary with format:
                  Required keys:
                    value (any): containing value to write on channel
                  Optional keys:
                    tramp (float): Ramp time for change in value [None]
                    wait (bool): whether to wait for processing to complete
                                 [False]
                    timeout (float): maximum time to wait for the processing to
                                     complete [60]
    Optional keys:
    tramp (float): Global ramp time for change in value [None]
    wait (bool): Global variable on whether to wait for processing to complete
                 [False]
    timeout (float): Global maximum time to wait for the processing to
                     complete [60]
    '''
    # Allowing to write the value directly under channel names if no other
    # parameter is required.
    for ch in chanInfo['channels']:
        if not isinstance(chanInfo['channels'][ch], dict):
            chanInfo['channels'][ch] = {'value': chanInfo['channels'][ch]}
        else:
            if 'value' not in chanInfo['channels'][ch]:
                raise RuntimeError('No value found for ' + ch)

    discardBak = {}  # caput used in this function do not need to save backUps
    kwargs = {}
    for ch in chanInfo['channels']:
        kwargs[ch] = {'bak': discardBak}
        # If global timeout is present, use it for all channels.
        if 'timeout' in chanInfo:
            kwargs[ch]['timeout'] = chanInfo['timeout']
        elif 'timeout' in chanInfo['channels'][ch]:
            kwargs[ch]['timeout'] = chanInfo['channels'][ch]['timeout']
        # If global wait is present
        if 'wait' in chanInfo:
            # If global tramp is present, individual wait should be False
            if 'tramp' in chanInfo:
                kwargs[ch]['wait'] = False
            # Else, assign gloabl wait to inidivual channel arguments
            else:
                kwargs[ch]['wait'] = chanInfo['wait']
        elif 'wait' in chanInfo['channels'][ch]:
            kwargs[ch]['wait'] = chanInfo['channels'][ch]['wait']

    curVals = {}
    for arg in ['tramp', 'wait', 'timeout']:
        if arg in chanInfo:
            curVals[arg] = chanInfo[arg]
    curVals['channels'] = {}
    for ch in chanInfo['channels']:
        curVals['channels'][ch] = {}
        for key in chanInfo['channels'][ch]:
            if key == 'value':
                curVals['channels'][ch][key] = caget(ch)
            else:
                curVals['channels'][ch][key] = chanInfo['channels'][ch][key]
    if all([set(curVals['channels']) != set(ele['value']['channels'])
            for ele in bak.values() if ele['type'] == 'group']):
        name = 'group_of|' + '|'.join(list(curVals['channels'].keys()))
        bak[name] = {'type': 'group', 'value': curVals, 'sno': len(bak)}

    retDict = {}
    if 'tramp' in chanInfo:
        oldTramps = {}
        rampYourself = True
        if chanInfo['tramp'] > 0:
            rampYourself = []
            for ch in chanInfo['channels']:
                fus = ch.rfind('_') + 1
                if ch[fus:] in ['GAIN', 'OFFSET']:
                    trampCh = ch[:fus] + 'TRAMP'
                    oldTrampVal = caget(trampCh, timeout=0.2)
                    if oldTrampVal is not None:
                        oldTramps[trampCh] = oldTrampVal
                        rampYourself += [False]
                    else:
                        rampYourself += [True]
                else:
                    rampYourself += [True]
            rampYourself = any(rampYourself)
            if rampYourself:
                for ch in oldTramps:
                    caput(ch, 0, bak=discardBak)
                rampSteps = 100
                sleepTime = chanInfo['tramp'] / rampSteps
                curVals = {}
                for ch in chanInfo['channels']:
                    curVals[ch] = caget(ch)
                stepVals = {}
                for ch in curVals:
                    stepVals[ch] = (chanInfo['channels'][ch]['value']
                                    - curVals[ch]) / rampSteps
                for tstep in range(1, rampSteps):
                    sleep(sleepTime)
                    for ch in chanInfo['channels']:
                        caput(ch, curVals[ch] + tstep * stepVals[ch],
                              **kwargs[ch])
            else:
                for ch in oldTramps:
                    caput(ch, chanInfo['tramp'], bak=discardBak)
        # Write final values
        for ch in chanInfo['channels']:
            retDict[ch] = caput(ch, chanInfo['channels'][ch]['value'],
                                **kwargs[ch])
        if not rampYourself:
            # Sleep for tramp time if global wait is True
            if 'wait' in chanInfo:
                if chanInfo['wait']:
                    sleep(chanInfo['tramp'])
        sleep(0.1)  # Buffer time
        for ch in oldTramps:
            caput(ch, oldTramps[ch], bak=discardBak)
    else:
        for ch in chanInfo['channels']:
            if 'tramp' in chanInfo['channels'][ch]:
                kwargs[ch]['tramp'] = chanInfo['channels'][ch]['tramp']
            retDict[ch] = caput(ch, chanInfo['channels'][ch]['value'],
                                **kwargs[ch])
    return retDict


def restoreGroup(bakVal):
    writeChannels(chanInfo=bakVal['value'], bak={})


restoreMethods['group'] = restoreGroup
