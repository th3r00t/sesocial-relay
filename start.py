#!/usr/bin/env python3
import os
from lib.session import Session
from lib.config import Config

# TODO: Add logging.
# TODO: Generate UUID for each server.

# Define list of files to fetch from server.
# TODO: Refactor this out for production to assume a path relative to itself.
#   This should be based upon standard Space Engineers server folder structure.
files = [
        "SpaceEngineersDedicated_20230109_180024680.log",
        "Saves/Eridanus (SE - PvP)/Sandbox_config.sbc",
        "Saves/Eridanus (SE - PvP)/Sandbox.sbc",
        "Storage/1359618037.sbm_RTS/RelativeTopSpeed.cfg"
        ]

if __name__ == "__main__":
    # initialize the session.
    abs_path = os.path.abspath(__file__).replace("start.py", "")
    config = Config(abs_path)
    session = Session(config, files)
    while True:
        session.run()
