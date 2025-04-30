# WinMessageMonitor

ChatGPT wants you to know this:

"WinMessageMonitor is a Python-based application designed to monitor and 
log various Windows system messages. It provides real-time insights into 
session events, power changes, time updates, theme changes, and other 
significant system activities by leveraging the Windows API."

I love the "insights" part. 
It's lovely to have "insights".

### Features

* Session Monitoring: Detects and logs session-related events such as logon and logoff.
* Power Events: Monitors power state changes, including suspend and resume.
* Time Changes: Tracks changes to the system time.
* Theme Changes: Observes alterations in the system theme settings.
* Custom Message Logging: Captures and logs a wide range of Windows messages for comprehensive monitoring.


## Installation

```
git clone https://github.com/lurid-bogey/winMessageMonitor.git
cd winMessageMonitor
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
To start the Message Monitor, run the following command:

```
python -m winMessageMonitor
```

The application will begin listening for Windows messages and log relevant events to the console.

Exit with `Ctrl-C`.
