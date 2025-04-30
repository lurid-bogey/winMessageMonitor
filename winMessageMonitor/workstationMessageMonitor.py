import atexit
import logging
import sys
import time
import win32api
import win32con
import win32gui
import win32ts
import ctypes
import signal

from winMessageMonitor.evtSessionEvent import SessionEvent
from winMessageMonitor.evtTimeChangeEvent import TimeChangeEvent
from winMessageMonitor.evtPowerEvent import PowerEvent
from winMessageMonitor.evtThemeChangeEvent import ThemeChangeEvent
from winMessageMonitor.msgDict import MSG_DICT as winUserMessages


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
        try:
            window_class = win32gui.RegisterClass(wndClass)
        except win32gui.error as e:
            logging.error(f"Failed to register window class: {e}")
            raise

        style = 0
        self.windowHandle = win32gui.CreateWindow(
            window_class,         # Window class
            self.WINDOW_TITLE,    # Window text
            style,                # Window style
            0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,  # Size and position
            0, 0, handleInstance, None  # Parent window, Menu, Instance handle, Additional application data
        )

        if not self.windowHandle:
            logging.error("Failed to create window")
            sys.exit(1)

        win32gui.UpdateWindow(self.windowHandle)

        # Register for session notifications
        scope = win32ts.NOTIFY_FOR_ALL_SESSIONS
        win32ts.WTSRegisterSessionNotification(self.windowHandle, scope)

    @staticmethod
    def listen():
        logging.info("Listening for Windows messages...")

        continueProcessing = True
        while continueProcessing:
            try:
                win32gui.PumpWaitingMessages()
                time.sleep(0.5)
            except KeyboardInterrupt:
                continueProcessing = False

    def stop(self):
        logging.info("Exiting")
        exitCode = 0
        try:
            win32ts.WTSUnRegisterSessionNotification(self.windowHandle)
        except Exception as e:
            logging.error(f"Error unregistering session notification: {e}")
        win32gui.PostQuitMessage(exitCode)

    def _windowProcedure(self, hWnd: int, uMsg: int, wParam, lParam) -> int:
        """
        WindowProc callback function.
        """
        if uMsg == PowerEvent.MESSAGE:
            event = PowerEvent.EVENTS.get(wParam, f"Unknown Power Event ({wParam})")
            logging.info(f"{event}, lParam: {lParam}")
        elif uMsg == TimeChangeEvent.MESSAGE:
            logging.info(f"WM_TIMECHANGE")
        elif uMsg == ThemeChangeEvent.MESSAGE:
            logging.info(f"WM_THEMECHANGED")
        elif uMsg == 0x001A:  # WM_SETTINGCHANGE, WM_WININICHANGE
            changedSetting = self.getStringFromLparam(lParam)
            logging.info(
                f'{winUserMessages.get(uMsg, "WM_SETTINGCHANGE")}, '
                f"wParam: {wParam} ({hex(wParam)}), lParam: {changedSetting or lParam}"
            )
        elif uMsg == SessionEvent.MESSAGE:
            session_event = SessionEvent.EVENTS.get(wParam, f"Unknown Session Event ({wParam})")
            logging.info(f"{session_event}, session: {lParam}")
        else:
            if uMsg in winUserMessages:
                logging.info(f"{winUserMessages[uMsg]}, " f"wParam: {wParam} ({hex(wParam)}), lParam: {lParam}")
            else:
                logging.warning(
                    f"Unknown message {uMsg} ({hex(uMsg)}), " f"wParam: {wParam} ({hex(wParam)}), lParam: {lParam}"
                )

        return win32gui.DefWindowProc(hWnd, uMsg, wParam, lParam)

    def getStringFromLparam(self, lParam):
        """
        Extracts a string from the lParam pointer.

        :param lParam: The lParam value from the message.
        :return: Decoded string if available, else None.
        """
        try:
            # Cast lParam to a pointer to a wide character string
            ptr = ctypes.cast(lParam, ctypes.c_wchar_p)
            if ptr:
                return ptr.value
        except Exception as e:
            logging.error(f"Error extracting string from lParam: {e}")
        return None


def main():
    logging.basicConfig(level=logging.DEBUG)
    m = WorkstationMessageMonitor()
    m.listen()


if __name__ == '__main__':
    main()
