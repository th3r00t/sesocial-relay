"""Configuration Object."""
import json
import pathlib
import os
from uuid import uuid1
from loguru import logger


class Config:
    """Main System Configuration.

    >>> config = Config(root)

    Parameters
    ----------
    root : File system root of program

    Attributes
    ----------
    root : str() stores root.
    config_structure : dict() Default Configuration Structure.
    _fp : str() file pointer to main configuration.
    _cp : Path() object of configuration file.
    _data : dict() parsed json of _fp.
    logger : holds logging configuration from get_logger().
    book_path : directory pointer to main books folder.
    TITLE : str() Program title.
    VERSION : str() Program  version.
    TITLE : str() Combines TITLE & VERSION.
    catalogue_db : str() Database Name.
    user : str() Database user name.
    password : str() Database password.
    db_host : str() Database host.
    db_port : int() Database port.
    allowed_hosts : list() Allowed host list.
    db_engine : str() Desired database engine type.
    db_user : str() Database user name. Duplication Warning.
    db_pass : str() Database password. Duplication Warning.
    build_mode : str() Production | Development mode.

    Methods
    -------
    get_logger : Setup loguru.
    open_file : Parse configuration file.
    """

    def __init__(self, root):
        """Initialize main configuration options."""
        self.root = root
        self.config_structure = {
            "TITLE": "Space Engineers Social Relay",
            "VERSION": "0.1.0",
            "SERVER_IP": "127.0.0.1",
            "SERVER_PORT": "27016",
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
            "DB_ENGINE": "sqlite",
            "DATABASE": "eridanus",
            "USER": "eridanus",
            "PASSWORD": "eridanus",
            "ALLOWED_HOSTS": [
                "localhost",
                "127.0.0.1",
                "[::1]",
                "0.0.0.0"
            ],
            "SSHHOST": '',
            "COMMON_PATH": '',
            "SSH_PASSWORD": '',
            "UUID": str(uuid1()),
            "BUILD_MODE": "development"
        }
        env = os.environ.copy()
        self._fp = "config.json"
        try:
            self._cp = pathlib.Path.joinpath(root, self._fp)
        except AttributeError:
            self._cp = pathlib.Path(root, self._fp)
        self._data = self.init_config()
        try:
            self.logger
        except AttributeError:
            self.logger = self.get_logger()
        self.TITLE = env.get("TITLE", self._data["TITLE"])
        self.VERSION = env.get("VERSION", self._data["VERSION"])
        self.TITLE = self.TITLE + " ver " + self.VERSION
        self.catalogue_db = env.get("DATABASE", self._data["DATABASE"])
        self.user = env.get("PYUSER", self._data["USER"])
        self.password = env.get("PYPASS", self._data["PASSWORD"])
        self.server_ip = env.get("SERVER_IP", self._data["SERVER_IP"])
        self.server_port = env.get("SERVER_PORT", self._data["SERVER_PORT"])
        self.db_host = env.get("DB_HOST", self._data["DB_HOST"])
        self.db_port = env.get("DB_PORT", self._data["DB_PORT"])
        self.ssh_host = env.get("SSHHOST", self._data["SSHHOST"])
        self.ssh_password = env.get("SSH_PASSWORD", self._data["SSH_PASSWORD"])
        self.common_path = env.get("COMMON_PATH", self._data["COMMON_PATH"])
        self.uuid = env.get("UUID", self._data["UUID"])
        self.auto_scan = True
        self.allowed_hosts = env.get("ALLOWED_HOSTS",
                                     self._data["ALLOWED_HOSTS"])
        self.db_engine = env.get("DB_ENGINE", self._data["DB_ENGINE"])
        self.db_user = env.get("USER", self._data["USER"])
        self.db_pass = env.get("PASSWORD", self._data["PASSWORD"])
        self.build_mode = env.get("BUILD_MODE", self._data["BUILD_MODE"])

    def init_config(self):
        try:
            return self.open_file()
        except FileNotFoundError:
            with open(self._fp, 'w') as _config_file:
                json.dump(self.config_structure, _config_file)
                _config_file.close()
            return self.open_file()

    def get_logger(self):
        """Instantiate logging system."""
        _logger = logger
        _logger.add(pathlib.PurePath(self.root, 'data', 'sesocial_relay.log'),
                    rotation="2 MB",
                    enqueue=True,
                    colorize=True)
        return _logger

    def open_file(self):
        """Open config.json and reads in configuration options."""
        with open(str(self._cp), "r") as read_file:
            data = json.load(read_file)
        return data
