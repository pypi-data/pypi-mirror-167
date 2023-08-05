import os
import platform
import logging

def get_python_command():
    python_command = ""
    if platform.system().lower() == "windows":
        python_command = "python "
    else:
        python_command = "python3 "

    return python_command

def get_shell_extension():
    extension = ""
    if platform.system().lower() == "windows":
        extension = ".bat"
    else:
        extension = ".sh"

    return extension

def evaluate_statuscode(statusCode, level=logging.DEBUG):
    logger = logging.getLogger("logger")
    logger.setLevel(level)
    logger.addHandler(logging.StreamHandler())

    if platform.system().lower() == "windows":
        logger.debug("Status Code: " + str(statusCode))
        if statusCode != 0:
            logger.error("Error Code: " + str(statusCode))
            return False
    else:
        logger.debug("Status Code: " + str(statusCode))
        if not os.WIFEXITED(statusCode):
            logger.error("Error Code: " + os.WEXITSTATUS(statusCode))
            return False
    
    return True