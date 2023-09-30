# Objects for parsing various game files, and data from logs.
import xml.etree.ElementTree as ET

# TODO: Add Log Parser.

def speed_file_parser(path):
    conv = "<Settings>\n"
    with open(path, 'r') as f:
        for line in f.readlines()[2:]:
            conv = conv + line
    SpeedFile = ET.fromstring(conv.replace('\n', ''))
    return SpeedFile


class LOGParser:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def game_log_file_parser(self):
        with open(self.path, 'r') as f:
            return f.read()

    def parser(self):
        if self.name == "GameLog":
            return self.game_log_file_parser()


class CFGParser:
    def __init__(self, name, path):
        self.name = name
        self.path = path
