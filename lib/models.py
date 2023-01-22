from typing import Optional
from sqlalchemy import func, Column, DateTime, ForeignKey, String, Identity
from sqlalchemy.orm import declarative_base, relationship


# TODO: add model for relative top speed configuration.

Base = declarative_base()


class Setting(Base):
    __tablename__ = "Settings"
    server = relationship("Server", back_populates="settings")
    server_id = Column(String, ForeignKey("Server.id"))
    key = Column(String, nullable=False, primary_key=True)
    value = Column(String, nullable=False)


class Mod(Base):
    __tablename__ = "Mods"
    server = relationship("Server", back_populates="mods")
    server_id = Column(String, ForeignKey("Server.id"))
    name = Column(String)
    workshop_id = Column(String, primary_key=True)


class Faction(Base):
    __tablename__ = "Factions"
    id = Column(String, Identity(), primary_key=True)
    server = relationship("Server", back_populates="factions")
    server_id = Column(String, ForeignKey("Server.id"))
    name = Column(String)
    tag = Column(String)
    type = Column(String)
    founder = Column(String, ForeignKey("Players.hashed_id"))
    leader = Column(String, ForeignKey("Players.hashed_id"))


class Player(Base):
    __tablename__ = "Players"
    name = Column(String)
    id = Column(String, Identity(), primary_key=True)
    server = relationship("Server", back_populates="players")
    server_id = Column(String, ForeignKey("Server.id"))
    hashed_id = Column(String)
    faction_id: Column(String, ForeignKey("Factions.id"))
    rank = Column(String)
    last_login = Column(DateTime, default=func.now())
    last_logout = Column(DateTime, default=func.now())


class Server(Base):
    __tablename__ = "Server"
    id = Column(String, primary_key=True)
    name = Column(String)
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
    players = relationship("Player", back_populates="server",
                           foreign_keys=[Player.server_id])
