
class PowerEvent(object):
    # window message
    MESSAGE = 0x218         # WM_POWERBROADCAST, winuser.h
    # events (wParam)
    EVENTS = {
        0x04: 'PBT_APMSUSPEND',
        0x07: 'PBT_APMRESUMESUSPEND',
        0x0a: 'PBT_APMPOWERSTATUSCHANGE',
        0x12: 'PBT_APMRESUMEAUTOMATIC',
        0x8013: 'PBT_POWERSETTINGCHANGE',
    }
