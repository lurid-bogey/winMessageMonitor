
class SessionEvent(object):
    # windows message
    MESSAGE = 0x2B1     # WM_WTSSESSION_CHANGE, wtsapi32.h
    # events (wParam)
    EVENTS = {
        0x1: 'WTS_CONSOLE_CONNECT',
        0x2: 'WTS_CONSOLE_DISCONNECT',
        0x3: 'WTS_REMOTE_CONNECT',
        0x4: 'WTS_REMOTE_DISCONNECT',
        0x5: 'WTS_SESSION_LOGON',
        0x6: 'WTS_SESSION_LOGOFF',
        0x7: 'WTS_SESSION_LOCK',
        0x8: 'WTS_SESSION_UNLOCK',
        0x9: 'WTS_SESSION_REMOTE_CONTROL',
    }
