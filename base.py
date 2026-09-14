import os
import datetime

veto_log = False

def Initial():
    try:
        timestamp: str = datetime.now().strftime("%d.%m.%Y %H:%M")
    except Exception:
        timestamp: str = "???"

        #Check if the files 'log.txt', 'log_prev.txt' and "dev_log.md" can be accessed
    do_log: bool = True
    dev_log: bool = True
    try:
        with open("log.txt", "a") as f:
            pass
        with open("log_prev.txt", "a") as f:
            pass
    except (PermissionError, IOError):
        do_log = False

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


    #Overrides 'log_prev.txt' with the contents of 'log.txt' and clears 'log.txt' for usage
    if do_log == True:
        if os.path.exists("log.txt"):
            with open("log.txt", "r") as old_file:
                content: str = old_file.read()
            with open("log_prev.txt", "w") as file:
                file.write(content)
            with open("log.txt", "w") as file:
                file.write(f"this log was generated at {timestamp}\n\n")

    return do_log, dev_log

do_log, dev_log = Initial()

def Veto_Dev_Logging(do: bool):
    global veto_log
    veto_log = do

def Dev_Write(to_write: str):
    with open("dev_log.log", "a") as dev_file:
        if dev_log and not veto_log:
            dev_file.write(to_write + "\n")
