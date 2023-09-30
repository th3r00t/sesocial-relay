#!/usr/bin/env python3
import os
import asyncio
import threading
from lib.session import Session
from lib.config import Config

# TODO: Add logging.
# TODO: Generate UUID for each server.

# Define list of files to fetch from server.
# TODO: Refactor this out for production to assume a path relative to itself.
#   This should be based upon standard Space Engineers server folder structure.

loop = asyncio.get_event_loop()

def spin_server(server):
    loop.create_task(server.run())

if __name__ == "__main__":
    # initialize the session.
    abs_path = os.path.abspath(__file__).replace("start.py", "")
    os.system("clear")
    print("Initializing SE Social Relay. . .")
    config = Config(abs_path)
    Servers = []
    for path in config.server_paths:
        Servers.append(Session(config, path))
    for server in Servers:
        thread = threading.Thread(target=spin_server(server))
        thread.start()
        thread.join()
        # loop.create_task(server.run())

    loop.run_forever()
    print("All servers have been started.")
