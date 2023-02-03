import json
from sqlalchemy import create_engine, select
from sqlalchemy.exc import OperationalError, IntegrityError
from sqlalchemy.orm import Session, joinedload
from .models import Setting, Mod, Faction, Player, Server


class Storage:
    """Create a new Storage object.

    >>> db = Storage(config)

    Parameters
    ----------
    config : Config()
        Main program configuration.

    Attributes
    ----------
    config : Stores configuration
    sql : Database Name
    user : Database User Name
    password : Database Password
    db_host : Database Host
    db_port : Database Port
    engine : sqlalchemy.create_engine(url, executor, kw)
    """

    def __init__(self, config):
        """Initialize storage object."""
        self.config = config
        self.sql = self.config.db
        self.user = self.config.user
        self.password = self.config.password
        self.db_host = self.config.db_host
        self.db_port = self.config.db_port
        self.engine = create_engine(self.get_connection_string(),
                                    pool_pre_ping=True)
        self.create_tables()
        # TODO: Refactor methods to use the following
        # server=False, settings=False, mods=False,
        # factions=False, players=False, speed=False

    def get_connection_string(self):
        """Get connection string.

        Engine type references config.json:DB_ENGINE.

        Returns
        -------
        str : sqlalchemy Connection String
        """
        if self.config.db_engine == "sqlite":
            return f"sqlite:////{self.config.root}/{self.config.db}.sqlite"
        elif self.config.db_engine == "psql":
            return f"postgresql://{self.user}:{self.password}\
            @{self.db_host}:{self.db_port}/{self.sql}"
        elif self.config.db_engine == "mysql":
            return f"mysql://{self.user}:{self.password}\
            @{self.db_host}:{self.db_port}/{self.sql}"

    def create_tables(self):
        """Create table structure."""
        tables = [Setting, Faction, Player, Server, Mod]
        for table in tables:
            table.metadata.create_all(self.engine)

    def get_server_object(self, server_id, session, server):
        try:
            _server_obj = session.execute(select(Server).where(Server.id == server_id))
            _server = _server_obj.fetchone()[0]
        except (OperationalError, TypeError):
            _server = Server(
                id=server_id,
                name=server['GameName'],
                ip=self.config.server_ip,
                port=self.config.server_port,
                )
        return _server

    def put_settings(self, _server, game_settings):
        for setting in game_settings:
            setting_handled = False
            try:
                for _setting in _server.settings:
                    if _setting.key == setting:
                        if _setting.value != game_settings[setting]:
                            _setting.value = game_settings[setting]
                            setting_handled = True
                            break
                        else:
                            # Setting is the same, no need to update
                            setting_handled = True
                            break
            except (OperationalError, AttributeError):
                pass
            if not setting_handled:
                _setting = Setting(key=setting, value=game_settings[setting])
                _server.settings.append(_setting)
                setting_handled = True

    def put_factions(self, _server, factions):
        # TODO: create &| update factions
        for faction in factions:
            faction_handled = False
            try:
                if faction['Type'] == 'PlayerMade':
                    for _faction in _server.factions:
                        if _faction.id == int(faction['Id']):
                            faction_handled = True
                            if _faction.leader != faction['Leader']:
                                _faction.leader = faction['Leader']
                    # Faction is new, create it
                    if not faction_handled:
                        _members = ""
                        for i in faction['Members']:
                            _members += i + ","
                        _faction = Faction(
                            id=faction['Id'],
                            name=faction['Name'],
                            tag=faction['Tag'],
                            type=faction['Type'],
                            leader=faction['Leader'],
                            founder=faction['Founder'],
                            members=json.dumps(_members[0:-1]),
                            )
                        _server.factions.append(_faction)
            except KeyError:
                pass

    def put_players(self, _server, players):
        for player in players:
            def player_online(p): return True if p == 'true' else False
            player_handled = False
            for _player in _server.players:
                if _player.hashed_id == player['hashed_id']:
                    player_handled = True
                    _player = Player(
                        game_id=player['game_id'],
                        hashed_id=player['hashed_id'],
                        name=player['name'],
                        rank=player['level'],
                        online=player_online(player['online']),
                        )
            if not player_handled:
                # Player is new, create it
                _player = Player(
                    game_id=player['game_id'],
                    hashed_id=player['hashed_id'],
                    name=player['name'],
                    rank=player['level'],
                    online=player_online(player['online']),
                    )
                _server.players.append(_player)

    def put_mods(self, _server, mods):
        for mod in mods:
            mod_handled = False
            for _mod in _server.mods:
                if _mod.workshop_id == str(mod['WorkshopId']):
                    mod_handled = True
                    break
            if not mod_handled:
                _mod = Mod(
                    name=mod['Name'],
                    workshop_id=mod['WorkshopId']
                    )
                _server.mods.append(_mod)

    def update_remote(self, session):
        """Update remote data on spaceengineers.social.

        Returns
        -------
        bool
            True on success False on failure
        """
        with Session(self.engine) as remote_session:
            server_id = self.config.uuid
            _server = self.get_server_object(server_id, remote_session, session.game_settings())
            self.put_settings(_server, session.game_settings())
            self.put_factions(_server, session.factions())
            self.put_players(_server, session.players())
            self.put_mods(_server, session.mods())
            remote_session.flush()
            remote_session.add(_server)
            try:
                remote_session.commit()
            except IntegrityError:
                import pudb; pudb.pm()
            remote_session.close()

    def session(self):
        return Session(self.engine)

    def get_server(self, server_id=None):
        with Session(self.engine) as session:
            if server_id is None:
                _server = session.query(Server).options(
                        joinedload(Server.factions),
                        joinedload(Server.players),
                        joinedload(Server.mods),
                        joinedload(Server.settings)
                        ).all()
            else:
                _server = session.execute(select(Server).where(Server.id == server_id)).fetchone()[0]
            return _server
