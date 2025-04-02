import atexit
import logging
import datetime
import time
import win32api
import win32con
import win32gui
import win32ts

from evtSessionEvent import SessionEvent
from evtTimeChangeEvent import TimeChangeEvent
from evtPowerEvent import PowerEvent
from msgDict import MSG_DICT as winUserMessages


# https://learn.microsoft.com/en-us/windows/win32/winmsg/about-messages-and-message-queues


class WorkstationMessageMonitor:
    CLASS_NAME = "WorkstationMessageMonitor"
    WINDOW_TITLE = "Workstation Message Monitor"

    def __init__(self):
        self.windowHandle = None
        self._registerListener()
        atexit.register(self.stop)

    def _registerListener(self):
        wndClass = win32gui.WNDCLASS()
        wndClass.hInstance = handleInstance = win32api.GetModuleHandle(None)
        wndClass.lpszClassName = self.CLASS_NAME
        wndClass.lpfnWndProc = self._windowProcedure
        window_class = win32gui.RegisterClass(wndClass)

        style = 0
        self.windowHandle = win32gui.CreateWindow(window_class,         # Window class
                                                  self.WINDOW_TITLE,    # Window text
                                                  style,                # Window style
                                                  # size and position
                                                  0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                                                  # Parent window, Menu, Instance handle, Additional application data
                                                  0, 0, handleInstance, None)
        win32gui.UpdateWindow(self.windowHandle)

        # scope = win32ts.NOTIFY_FOR_THIS_SESSION
        scope = win32ts.NOTIFY_FOR_ALL_SESSIONS
        win32ts.WTSRegisterSessionNotification(self.windowHandle, scope)

    @staticmethod
    def listen():
        logging.info('Listening')
        continueProcessing = True
        while continueProcessing:
            try:
                win32gui.PumpWaitingMessages()
                time.sleep(0.5)
            except KeyboardInterrupt:
                continueProcessing = False

    def stop(self):
        logging.info('Exiting')
        exitCode = 0
        win32ts.WTSUnRegisterSessionNotification(self.windowHandle)
        win32gui.PostQuitMessage(exitCode)

    @staticmethod
    def _windowProcedure(hWnd: int, uMsg: int, wParam, lParam) -> bool:
        """
        WindowProc callback function.

        https://learn.microsoft.com/en-us/windows/win32/api/winuser/nc-winuser-wndproc

        :param hWnd: A handle to the window.
        :param uMsg: The message.
        :param wParam: Additional message information.
        :param lParam: Additional message information.

        """
        if uMsg == PowerEvent.MESSAGE:
            logging.info(f'[{datetime.datetime.now().isoformat()}]  {PowerEvent.EVENTS[wParam]}, lParam: {lParam}')
        elif uMsg == TimeChangeEvent.MESSAGE:
            logging.info(f'[{datetime.datetime.now().isoformat()}]  WM_TIMECHANGE')
        elif uMsg == SessionEvent.MESSAGE:
            logging.info(f'[{datetime.datetime.now().isoformat()}]  {SessionEvent.EVENTS[wParam]}, session: {lParam}')
        else:
            if uMsg in winUserMessages:
                logging.info(f'[{datetime.datetime.now().isoformat()}]  {winUserMessages[uMsg]}, wParam: {wParam} ({hex(wParam)}), lParam: {lParam}')
            else:
                logging.info(f'[{datetime.datetime.now().isoformat()}]  Unknown message {uMsg} ({hex(uMsg)}), wParam: {wParam} ({hex(wParam)}), lParam: {lParam}')

        return True


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    m = WorkstationMessageMonitor()
    m.listen()
