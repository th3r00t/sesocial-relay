# Objects for parsing various game files, and data from logs.
import xml.etree.ElementTree as ET


# TODO: Add Log Parser.

# SBCParser
class SBCParser:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def game_file_parser(self):
        return ET.parse(self.path)

    def server_file_parser(self):
        return ET.parse(self.path)

    def speed_file_parser(self):
        conv = "<Settings>\n"
        with open(self.path, 'r') as f:
            for line in f.readlines()[2:]:
                conv = conv + line
        SpeedFile = ET.fromstring(conv.replace('\n', ''))
        return SpeedFile

    def parser(self):
        if self.name == "GameFile":
            return self.game_file_parser()
        elif self.name == "ServerFile":
            return self.server_file_parser()
        elif self.name == "SpeedFile":
            return self.speed_file_parser()


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
