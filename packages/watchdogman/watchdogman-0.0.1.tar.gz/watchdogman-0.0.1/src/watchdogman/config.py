import json, os

CONFIG = None

def load_config():
    path = os.path.join(".", ".watchdogman")

    with open(path) as f:
        json_config = json.load(f)
        return Config(json_config["directory"], json_config["allow_patterns"], json_config["ignore_patterns"], json_config["ignore_directories"], json_config["command"])

class Config():
    def __init__(self, directory, allow_patterns, ignore_patterns, ignore_dirs, command):
        self.directory = os.path.abspath(directory)
        self.allow_patterns = allow_patterns
        self.ignore_patterns = ignore_patterns
        self.ignore_dirs = ignore_dirs
        self.command = command