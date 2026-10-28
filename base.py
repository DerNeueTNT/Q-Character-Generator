import os
import datetime
import json
from typing import Any

veto_log: bool = False
do_log: bool = True
dev_log: bool = True
allow_settings: bool = True

default_settings: dict[str, Any] = {
    "instant_mode": False,
    "theme": "default",
}

def Initial():
    try:
        timestamp: str = datetime.now().strftime("%d.%m.%Y %H:%M")
    except Exception:
        timestamp: str = "???"

        #Check if the files 'log.txt', 'log_prev.txt' and "dev_log.md" can be accessed
    global do_log
    global dev_log
    global allow_settings
    try:
        with open("log.txt", "a") as f:
            pass
        with open("log_prev.txt", "a") as f:
            pass
    except (PermissionError, IOError):
        do_log = False

    try:
        with open("settings.json", "a") as f:
            pass
    except (PermissionError, IOError):
        allow_settings = False

    try:
        with open("dev_log.log", "a") as f:
            pass
    except (PermissionError, IOError):
        dev_log = False

    #Make sure that the files can actually be written to
    if os.access("log.txt", os.W_OK):
        pass
    else:
        do_log = False
    if os.access("log_prev.txt", os.W_OK):
        pass
    else:
        do_log = False
    if os.access("dev_log.log", os.W_OK):
        pass
    else:
        dev_log = False
    if os.access("settings.json", os.W_OK):
        pass
    else:
        allow_settings = False


    #Overrides 'log_prev.txt' with the contents of 'log.txt' and clears 'log.txt' for usage
    if do_log == True:
        if os.path.exists("log.txt"):
            with open("log.txt", "r") as old_file:
                content: str = old_file.read()
            with open("log_prev.txt", "w") as file:
                file.write(content)
            with open("log.txt", "w") as file:
                file.write(f"this log was generated at {timestamp}\n\n")

    #Sets up 'settings.json'
    if allow_settings:
        with open("settings.json", "r+") as settings_file:
            settings_file.seek(0)
            content = settings_file.read()

            changed = False
            
            if content.strip() == "":
                settings = {}
            else:
                settings = json.loads(content)

            for setting, default_value in default_settings.items():
                if setting not in settings:
                    settings[setting] = default_value
                    changed = True

            if changed:
                settings_file.seek(0)
                json.dump(settings, settings_file, indent=4)
                settings_file.truncate()


def Veto_Dev_Logging(do: bool):
    global veto_log
    veto_log = do

def Dev_Write(to_write: str):
    with open("dev_log.log", "a") as dev_file:
        if dev_log and not veto_log:
            dev_file.write(to_write + "\n")

def Change_Setting(setting: str, value: Any):
    with open("settings.json", "r+") as settings_file:
        content = settings_file.read()
        
        if content.strip() == "":
            settings = {}
        else:
            settings = json.loads(content)

        settings[setting] = value

        settings_file.seek(0)
        json.dump(settings, settings_file, indent=4)
        settings_file.truncate()

def Read_Setting(setting: str):
    with open("settings.json", "r") as settings_file:
        content = settings_file.read()
                
        if content.strip() == "":
            settings = {}
        else:
            settings = json.loads(content)
        return settings[setting]
