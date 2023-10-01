from typing import Optional
from sqlalchemy import func, Column, DateTime,\
        ForeignKey, String, Identity, Integer, Boolean, BigInteger
from sqlalchemy.orm import declarative_base, relationship, Mapped
import json

# TODO: add model for relative top speed configuration.

Base = declarative_base()


class Setting(Base):
    __tablename__ = "Settings"
    server = relationship("Server", back_populates="settings")
    server_id = Column(BigInteger, ForeignKey("Server.id"))
    key = Column(String, nullable=False, primary_key=True)
    value = Column(String, nullable=False)

    def __str__(self):
        return f"key={self.key}, value={self.value}"


class Mod(Base):
    __tablename__ = "Mods"
    server = relationship("Server", back_populates="mods")
    server_id = Column(BigInteger, ForeignKey("Server.id"))
    name = Column(String)
    workshop_id = Column(String, primary_key=True)

    def __str__(self):
        return f"name={self.name}, workshop_id={self.workshop_id}"


class Faction(Base):
    __tablename__ = "Factions"
    id = Column(BigInteger, Identity(), primary_key=True)
    server = relationship("Server", back_populates="factions")
    server_id = Column(BigInteger, ForeignKey("Server.id"))
    name = Column(String)
    tag = Column(String)
    type = Column(String)
    leader = Column(String)
    founder = Column(String)
    members = Column(String)

    def __str__(self):
        return f"id={self.id}, name={self.name}, tag={self.tag}, type={self.type}, leader={self.leader}, founder={self.founder.__str__()}, members={self.members.__str__()}"


class Player(Base):
    __tablename__ = "Players"
    name = Column(String)
    id = Column(BigInteger, Identity(), primary_key=True)
    server = relationship("Server", back_populates="players")
    server_id = Column(BigInteger, ForeignKey("Server.id"))
    hashed_id = Column(String)
    game_id = Column(String)
    online = Column(Boolean, default=False)
    faction_id = Column(BigInteger, ForeignKey("Factions.id"))
    rank = Column(String)
    last_login = Column(DateTime, default=func.now())
    last_logout = Column(DateTime, default=func.now())

    def __str__(self):
        return f"name={self.name}, id={self.id}, hashed_id={self.hashed_id}, game_id={self.game_id}, faction_id={self.faction_id}, rank={self.rank}, last_login={self.last_login.__str__()}, last_logout={self.last_logout.__str__()}"


class Server(Base):
    __tablename__ = "Server"
    id = Column(BigInteger, Identity(), primary_key=True)
    name = Column(String)
    description = Column(String)
    img_bg = Column(String)
    img_logo = Column(String)
    img_icon = Column(String)
    ip = Column(String)
    port = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    players = relationship("Player", back_populates="server", foreign_keys=[Player.server_id])
    settings = relationship("Setting", back_populates="server",
                            foreign_keys=[Setting.server_id])
    mods = relationship("Mod", back_populates="server", foreign_keys=[Mod.server_id])
    factions = relationship("Faction", back_populates="server",
                            foreign_keys=[Faction.server_id])

    def __str__(self):
        players_json = ""
        settings_json = ""
        mods_json = ""
        factions_json = ""
        for player in self.players:
            players_json += player.__str__() + ", "
        for setting in self.settings:
            settings_json += setting.__str__() + ", "
        for mod in self.mods:
            mods_json += mod.__str__() + ", "
        for faction in self.factions:
            factions_json += faction.__str__() + ", "
        return f"id={self.id}, name={self.name}, ip={self.ip}, port={self.port}, created_at={self.created_at.__str__()}, updated_at={self.updated_at.__str__()}, players={players_json}, settings={settings_json}, mods={mods_json}, factions={factions_json}"
