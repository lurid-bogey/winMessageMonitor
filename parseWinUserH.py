import logging
import pprint


def parseWinUserH():
    with open(r'winuser.h', 'r') as inFile:
        rawLines = inFile.readlines()

    with open(r'msgDict.py', 'w') as outFile:

        winUserDefines = {}
        print('MSG_DICT = {', file=outFile)

        for line in rawLines:
            line = line.strip()
            if line.startswith('#define WM_'):
                try:
                    _, msgName, msgIndex, *rest = line.split()
                    try:
                        intMsgIndex = int(msgIndex)
                    except ValueError:
                        intMsgIndex = int(msgIndex, 16)

                    if intMsgIndex in winUserDefines:
                        logging.error(f'Message {intMsgIndex} already present -> old: {winUserDefines[intMsgIndex]}, new: {msgName}')
                    else:
                        ll = len(msgName)
                        nn = len(str(intMsgIndex))
                        print(f"    {intMsgIndex}: '{msgName}', {' ' * (37-ll-nn)}# 0x{intMsgIndex:04X}", file=outFile)

                    winUserDefines[intMsgIndex] = msgName

                except ValueError as e:
                    logging.error(f'{repr(e)} --> {line}')

        print('}', file=outFile)

    return winUserDefines


if __name__ == '__main__':
    msgDict = parseWinUserH()
    pprint.pprint(msgDict)
