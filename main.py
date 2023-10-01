from typing import Union
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from lib.storage import Storage
from lib.models import Server, Setting, Mod, Faction, Player
from lib.config import Config

abs_path = os.path.abspath(__file__).replace("main.py", "")
config = Config(abs_path)
app = FastAPI()
storage = Storage(config)
Session = sessionmaker(bind=storage.engine)
session = Session()

@app.get("/")
async def read_root():
    server_query = session.query(Server)
    return server_query.all()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}