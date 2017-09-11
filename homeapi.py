import subprocess
import os
from flask import Flask, current_app

APP = Flask(__name__)
PORT = 4567
EMPTY_RESPONSE = ('', 204)


# Open Steam

STEAM_PROCESS = "Steam.exe"
STEAM_PATH = "C:\\Program Files (x86)\\Steam\\"


def is_steam_running ():
    """Identifies if Steam is running."""
    tasks = subprocess.check_output("tasklist")
    return STEAM_PROCESS in str(tasks)


@APP.route("/opensteam")
def opensteam():
    """Opens steam in big picture mode."""
    if is_steam_running():
        subprocess.call([STEAM_PATH + STEAM_PROCESS, "steam://open/bigpicture"])
    else:
        subprocess.call([STEAM_PATH + STEAM_PROCESS, "-bigpicture"])
    return EMPTY_RESPONSE


# Change screen

TV_SCREEN = "internal"
TV_SOUND = "TV"
MONITOR_SCREEN = "external"
MONITOR_SOUND = "Speakers"


def change_screen(screen, sound):
    """Changes the screen and sound output"""
    subprocess.call(["DisplaySwitch.exe", "/{device}".format(device=screen)])
    subprocess.call(["timeout", "/t", "1"])
    subprocess.call(["nircmdc", "setdefaultsounddevice", """{device}""".format(device=sound), "1"])


@APP.route("/gotv")
def gotv():
    """Endpoint to switch screen."""
    change_screen(TV_SCREEN, TV_SOUND)
    return EMPTY_RESPONSE


@APP.route("/gomonitor")
def gomonitor():
    """Endpoint to switch screen."""
    change_screen(MONITOR_SCREEN, MONITOR_SOUND)
    return EMPTY_RESPONSE

# Utils


@APP.route("/opendownloads")
def opendownloads():
    """Opens Downloads folder."""
    subprocess.call(["explorer", os.path.expanduser("~\\Downloads")])
    return EMPTY_RESPONSE


@APP.route("/reboot")
def reboot():
    """Reboots PC."""
    subprocess.call(["shutdown", "-r", "-t", "1"])
    return EMPTY_RESPONSE


@APP.route("/shutdown")
def shutdown():
    """Shuts down PC."""
    subprocess.call(["shutdown", "-s", "-t", "1"])
    return EMPTY_RESPONSE


# Main


@APP.route("/")
def home():
    """Index for front-end."""
    return current_app.send_static_file('index.html')


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=PORT)