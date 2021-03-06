import sys as __sys
from loguru import logger
from pprint import pformat
from pprint import pprint
import inspect
import os

__config = {
    "handlers": [
        {
            "sink": __sys.stdout, 
            # "format": "{time:MM-DD HH:mm:ss} [{icon}] {message}",
            "format": '<green>{time:MM-DD HH:mm:ss}</green> <level>{level:4.4}</level> {message}',
            "level": "TRACE",
        },
        # {"sink": "file.log", "serialize": True},
    ],
    # "extra": {"user": "someone"}
}
logger.configure(**__config)

def Trace(*message):
    messages = []
    jstr = " "
    for msg in message:
        if type(msg) == int or type(msg) == float:
            msg = str(msg)
        if type(msg) != str:
            msg = "\n" + pformat(msg, indent=4)
        p = inspect.stack()[1]
        if message.count("\n") != 0 and jstr == " ":
            jstr = "\n"
        messages.append(msg)
    
    logger.opt(ansi=True).trace(
        "<cyan>{filename}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> <level>{message}</level>", 
        message=jstr.join(messages), 
        function=p.function,
        line=p.lineno,
        filename=os.path.basename(p.filename),
    )

def Debug(*message):
    messages = []
    jstr = " "
    for msg in message:
        if type(msg) == int or type(msg) == float:
            msg = str(msg)
        if type(msg) != str:
            msg = "\n" + pformat(msg, indent=4)
        p = inspect.stack()[1]
        if message.count("\n") != 0 and jstr == " ":
            jstr = "\n"
        messages.append(msg)
    
    logger.opt(ansi=True).debug(
        "<cyan>{filename}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> <level>{message}</level>", 
        message=jstr.join(messages), 
        function=p.function,
        line=p.lineno,
        filename=os.path.basename(p.filename),
    )

def Info(*message):
    messages = []
    jstr = " "
    for msg in message:
        if type(msg) == int or type(msg) == float:
            msg = str(msg)
        if type(msg) != str:
            msg = "\n" + pformat(msg, indent=4)
        p = inspect.stack()[1]
        if message.count("\n") != 0 and jstr == " ":
            jstr = "\n"
        messages.append(msg)
    
    logger.opt(ansi=True).info(
        "<cyan>{filename}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> <level>{message}</level>", 
        message=jstr.join(messages), 
        function=p.function,
        line=p.lineno,
        filename=os.path.basename(p.filename),
    )

def Warn(*message):
    messages = []
    jstr = " "
    for msg in message:
        if type(msg) == int or type(msg) == float:
            msg = str(msg)
        if type(msg) != str:
            msg = "\n" + pformat(msg, indent=4)
        p = inspect.stack()[1]
        if message.count("\n") != 0 and jstr == " ":
            jstr = "\n"
        messages.append(msg)
    
    logger.opt(ansi=True).warning(
        "<cyan>{filename}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> <level>{message}</level>", 
        message=jstr.join(messages), 
        function=p.function,
        line=p.lineno,
        filename=os.path.basename(p.filename),
    )

def Error(*message):
    messages = []
    jstr = " "
    for msg in message:
        if type(msg) == int or type(msg) == float:
            msg = str(msg)
        if type(msg) != str:
            msg = "\n" + pformat(msg, indent=4)
        p = inspect.stack()[1]
        if message.count("\n") != 0 and jstr == " ":
            jstr = "\n"
        messages.append(msg)
    
    logger.opt(ansi=True).error(
        "<cyan>{filename}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> <level>{message}</level>", 
        message=jstr.join(messages), 
        function=p.function,
        line=p.lineno,
        filename=os.path.basename(p.filename),
    )

def SetLevel(level: str):
    """
    It sets the logging level of the logger to the level passed in
    
    :param level: The level of messages to log. canbe: trace,debug,info,warn,error
    :type level: str
    """
    __config['handlers'][0]['level'] = level.upper()
    logger.configure(**__config)

def SetFile(path: str, size: int, during: int, color:bool=True, json:bool=False):
    """
    It sets the file handler for the logger.
    
    :param path: The path to the log file
    :type path: str
    :param size: The size of the file before it rotates, in MB
    :type size: int
    :param during: how long to keep the log file, in Day
    :type during: int
    :param color: If True, the output will be colorized, defaults to True
    :type color: bool (optional)
    :param json: If True, the log records will be serialized to JSON, defaults to False
    :type json: bool (optional)
    """
    logger.add(
        path, 
        rotation=str(size)+" MB", 
        retention=str(during)+" days", 
        format=__config['handlers'][0]['format'], 
        colorize=color,
        serialize=json,
    )

if __name__ == "__main__":
    # SetLevel("info")
    # SetFile("test.log", 1, 1, json=True)
    Trace("trace")
    Debug("debug")
    Info("info")
    Warn("warn")
    Error("error")
    Debug("text debug message", [ ['spam', 'eggs', 'lumberjack', 'knights', 'ni'], 'spam', 'eggs', 'lumberjack', 'knights', 'ni'])
    Debug("first", "second", "third")
    Trace("???????????????", 1)