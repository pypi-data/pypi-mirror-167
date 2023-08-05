"""
This module helps you to squash bugs by giving you information about the error and how to fix it.
"""

import sys
import re
from termcolor import colored

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s', datefmt='%H:%M:%S')

__version__ = "1.0"

class example:
    class error(Exception):
        def __init__(self):
            super().__init__("Example Error")

class ErrorCatcher():
    def __init__(self):
        self.finished = False
        self.err = ""
    def write(self, msg):
        if re.match(".+:", msg) and not "Traceback (most recent call last):" in msg:
            self.finished = True
        if self.finished:
            self.err += msg
            evaluate(self.err)
            self.err = ""
            self.finished = False
        else:
            self.err += msg

class evaluate():
    def __init__(self, err):
        self.details = {}
        self.details["type"] = re.findall(".+:", err)[1].replace(":", "")
        self.details["message"] = re.search(": .+", err)[0]
        self.details["line_no"] = re.search("line \d+", err)[0].replace("line ", "")
        self.details["file"] = re.search("File \".+?\"", err)[0].replace("File ", "").replace('"', '')

        print(colored("[red]{} on line {} in file {}{}.[/red]".format( str( self.details[ "type" ] ), str( self.details[ "line_no" ] ), str( self.details[ "file" ] ), str( self.details[ "message" ] ) ) ) )


def init():
    """Start catching errors"""
    sys.stderr = ErrorCatcher()
