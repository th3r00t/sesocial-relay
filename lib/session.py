from datetime import datetime
from re import S
import socket
import xml.etree.ElementTree as ET
import asyncio
import os
import threading
from .parsers import speed_file_parser, LOGParser  # , CFGParser
from .storage import Storage


# Main Session Object.
class Session():
    """Create a new Session object.

    >>> session = Session(abs_path, host, password, common_path, files, storage)

    Parameters
    ----------
    abs_path : str
        Absolute path to the local directory where the data will be stored.
    host : str
        The remote host to connect to. This is used in development for remote
        file fetching.
    password : str
        The password for the remote host. This is used in development for remote
        file fetching.
    common_path : str
        The common path to the Space Engineers data directory. This is used in
        development for remote file fetching. Specifically the path to the data
        is constructed as follows: host + common_path + file.
    files : list
        A list of files to fetch to aggregate data from.
    storage : Storage()
        A Storage object to store the data in.
    config : Config(

    Attributes
    ----------
    timer : datetime object used to run the session in intervals.
    name : The name of the host.
    ip : The ip address of the host.
    abs_path : Absolute path to the local directory where the data will be stored.
    remote_host : The remote host to connect to.
    sshpass : The password for the remote host.
    common_path : The common path to the Space Engineers data directory.
    storage : A Storage object to store the data in.
    game_file : A SBCParser object for the Sandbox.sbc file.
    server_file : A SBCParser object for the Sandbox_config.sbc file.
    relative_top_speed : A SBCParser object for the RelativeTopSpeed.xml file.
    log_file : A LOGParser object for the SpaceEngineersDedicated.log file.
    """
    def __init__(self, config, path):
        self.timer = datetime.now()
        self.name = socket.gethostname()
        self.instance_name = path.split('/')[-1]
        self.ip = socket.gethostbyname(self.name)
        self.abs_path = config.root
        self.remote_host = config.ssh_host
        self.sshpass = config.ssh_password
        self.common_path = config.common_path
        self.config = config
        self.storage = Storage(self.config)
        self.game_file_path = f'{path}/Sandbox.sbc'
        self.server_file_path = f'{path}/Sandbox_config.sbc'
        self.speed_file_path = f'{path}/Storage/1359618037.sbm_RTS/RelativeTopSpeed.cfg'
        self.log_file_path = f'{path}/SpaceEngineersDedicated.log'
        # self.get_data()
        # self.game_file = SBCParser(
        #     'GameFile',
        #     f'{self.abs_path}Instance/Saves/Sandbox.sbc').parser()
        # self.server_file = SBCParser(
        #     'ServerFile',
        #     f'{self.abs_path}Instance/Saves/Sandbox_config.sbc').parser()
        # self.relative_top_speed = SBCParser(
        #     'SpeedFile',
        #     f'{self.abs_path}data/RelativeTopSpeed.xml').parser()
        # self.log_file = LOGParser(
        #     'GameLog',
        #     f'{self.abs_path}data/SpaceEngineersDedicated_20230109_180024680.log').parser()

    def get_instances(self):
        """Get a list of instances.
        >>> session.get_instances()
        Returns
        -------
        list
        """
        instances = []
        for instance in self.config.server_paths:
            instances.append(instance.split('/')[-1])

    async def game_settings(self):
        """Session Settings.

        >>> settings = session.game_settings()

        Returns
        -------
        dict
        """
        # TODO: type fields correctly handing type conversions here.
        sbc = ET.parse(self.game_file_path)
        _obj = sbc.find('Settings')
        _game_name = sbc.find('SessionName').text
        _game_description = sbc.find('Description').text
        return {
                'GameName': _game_name,
                'GameMode': _obj.find('GameMode').text,
                'InventorySizeMultiplier': _obj.find('InventorySizeMultiplier').text,
                'AssemblerSpeedMultiplier': _obj.find('AssemblerSpeedMultiplier').text,
                'AssemblerEfficiencyMultiplier': _obj.find('AssemblerEfficiencyMultiplier').text,
                'RefinerySpeedMultiplier': _obj.find('RefinerySpeedMultiplier').text,
                'WelderSpeedMultiplier': _obj.find('WelderSpeedMultiplier').text,
                'GrinderSpeedMultiplier': _obj.find('GrinderSpeedMultiplier').text,
                'OnlineMode': _obj.find('OnlineMode').text,
                'MaxPlayers': _obj.find('MaxPlayers').text,
                'MaxFloatingObjects': _obj.find('MaxFloatingObjects').text,
                'TotalBotLimit': _obj.find('TotalBotLimit').text,
                'MaxGridSize': _obj.find('MaxGridSize').text,
                'MaxBlocksPerPlayer': _obj.find('MaxBlocksPerPlayer').text,
                'BlockLimitsEnabled': _obj.find('BlockLimitsEnabled').text,
                'EnvironmentHostility': _obj.find('EnvironmentHostility').text,
                'AutoHealing': _obj.find('AutoHealing').text,
                'EnableCopyPaste': _obj.find('EnableCopyPaste').text,
                'WeaponsEnabled': _obj.find('WeaponsEnabled').text,
                'ShowPlayerNamesOnHud': _obj.find('ShowPlayerNamesOnHud').text,
                'ThrusterDamage': _obj.find('ThrusterDamage').text,
                'CargoShipsEnabled': _obj.find('CargoShipsEnabled').text,
                'WorldSizeKm': _obj.find('WorldSizeKm').text,
                'RespawnShipDelete': _obj.find('RespawnShipDelete').text,
                'RealisticSound': _obj.find('RealisticSound').text,
                'HackSpeedMultiplier': _obj.find('HackSpeedMultiplier').text,
                'AutoSaveInMinutes': _obj.find('AutoSaveInMinutes').text,
                'EnableContainerDrops': _obj.find('EnableContainerDrops').text,
                'SpawnShipTimeMultiplier': _obj.find('SpawnShipTimeMultiplier').text,
                'DestructibleBlocks': _obj.find('DestructibleBlocks').text,
                'EnableIngameScripts': _obj.find('EnableIngameScripts').text,
                'ViewDistance': _obj.find('ViewDistance').text,
                'EnableToolShake': _obj.find('EnableToolShake').text,
                'EnableOxygen': _obj.find('EnableOxygen').text,
                'EnableOxygenPressurization': _obj.find('EnableOxygenPressurization').text,
                'EnableEncounters': _obj.find('EnableEncounters').text,
                'EnableConvertToStation': _obj.find('EnableConvertToStation').text,
                'StationVoxelSupport': _obj.find('StationVoxelSupport').text,
                'EnableSunRotation': _obj.find('EnableSunRotation').text,
                'Enable3rdPersonView': _obj.find('Enable3rdPersonView').text,
                'EnableJetpack': _obj.find('EnableJetpack').text,
                'SunRotationIntervalMinutes': _obj.find('SunRotationIntervalMinutes').text,
                'SpawnWithTools': _obj.find('SpawnWithTools').text,
                'MaxDrones': _obj.find('MaxDrones').text,
                'EnableDrones': _obj.find('EnableDrones').text,
                'EnableWolfs': _obj.find('EnableWolfs').text,
                'EnableSpiders': _obj.find('EnableSpiders').text,
                'EnableScripterRole': _obj.find('EnableScripterRole').text,
                'SyncDistance': _obj.find('SyncDistance').text,
                'ExperimentalMode': _obj.find('ExperimentalMode').text
                }

    async def mods(self):
        """Session Mods.

        >>> mods = session.mods()

        Returns
        -------
        list
        """
        # TODO: urlsafe base64 encode the mod url.
        sbc = ET.parse(self.server_file_path)
        _obj = sbc.find('Mods')
        _mods = []
        for mod in _obj.findall('ModItem'):
            _mod_name = mod.attrib['FriendlyName']
            _file_host = mod.find('PublishedServiceName').text
            _file_id = int(mod.find('PublishedFileId').text)
            if _file_host == 'Steam':
                _mod_url = f'https://steamcommunity.com/sharedfiles/filedetails/?id={_file_id}'
            else:
                _mod_url = f'https://www.nexusmods.com/spaceengineers/mods/{_file_id}'
            _mods.append({
                    'Name': _mod_name,
                    'WorkshopId': _file_id,
                    'ModUrl': _mod_url
                    })
        return _mods

    async def factions(self):
        """Session Factions.

        >>> factions = session.factions()

        Returns
        -------
        list
        """
        sbc = ET.parse(self.game_file_path)
        _obj = sbc.find('Factions')
        _faction_list = _obj.find('Factions')
        _factions = []
        for faction in _faction_list:
            _faction_name = faction.find('Name').text
            _faction_tag = faction.find('Tag').text
            _faction_id = faction.find('FactionId').text
            _faction_type = faction.find('FactionType').text
            _faction_members = []
            _faction_leader = ""
            _faction_founder = ""
            for member in faction.findall('Members/MyObjectBuilder_FactionMember'):
                _faction_members.append(member.find('PlayerId').text)
                if member.find('IsLeader').text == 'true':
                    _faction_leader = member.find('PlayerId').text
                if member.find('IsFounder').text == 'true':
                    _faction_founder = member.find('PlayerId').text
            _factions.append({
                    'Id': _faction_id,
                    'Name': _faction_name,
                    'Tag': _faction_tag,
                    'Type': _faction_type,
                    'Founder': _faction_founder,
                    'Leader': _faction_leader,
                    'Members': _faction_members
                    })
        return _factions

    async def players(self):
        """Session Players.

        >>> players = session.players()

        Returns
        -------
        list
        """
        sbc = ET.parse(self.game_file_path)
        _obj = sbc.find('AllPlayersData/dictionary')
        _player_list = _obj.findall('item')
        _players = []
        for player in _player_list:
            _player_game_id = player.find('Key/HashedId').text
            _player_hashed_id = player.find('Value/IdentityId').text
            _player_name = player.find('Value/DisplayName').text
            _player_online = player.find('Value/Connected').text
            _player_level = player.find('Value/PromoteLevel').text
            _players.append({
                'game_id': _player_game_id,
                'hashed_id': _player_hashed_id,
                'name': _player_name,
                'online': _player_online,
                'level': _player_level
                })
        return _players

    async def speed_settings(self):
        """Session Speed Settings.

        >>> speed = session.speed_settings()

        Returns
        -------
        dict
        """
        speed_file = speed_file_parser(self.speed_file_path)
        return {
                'EnableBoosting': speed_file.find('EnableBoosting').text,
                'IgnoreGridsWithoutThrust': speed_file.find('IgnoreGridsWithoutThrust').text,
                'IgnoreGridsWithoutCockpit': speed_file.find('IgnoreGridsWithoutCockpit').text,
                'ParachuteDeployHeight': speed_file.find('ParachuteDeployHeight').text,
                'SpeedLimit': speed_file.find('SpeedLimit').text,
                'RemoteControlSpeedLimit': speed_file.find('RemoteControlSpeedLimit').text,
                'LargeGrid_MinCruise': speed_file.find('LargeGrid_MinCruise').text,
                'LargeGrid_MidCruise': speed_file.find('LargeGrid_MidCruise').text,
                'LargeGrid_MaxCruise': speed_file.find('LargeGrid_MaxCruise').text,
                'LargeGrid_MinMass': speed_file.find('LargeGrid_MinMass').text,
                'LargeGrid_MidMass': speed_file.find('LargeGrid_MidMass').text,
                'LargeGrid_MaxMass': speed_file.find('LargeGrid_MaxMass').text,
                'LargeGrid_MaxBoostSpeed': speed_file.find('LargeGrid_MaxBoostSpeed').text,
                'LargeGrid_ResistanceMultiplier': speed_file.find('LargeGrid_ResistanceMultiplier').text,
                'SmallGrid_MinCruise': speed_file.find('SmallGrid_MinCruise').text,
                'SmallGrid_MidCruise': speed_file.find('SmallGrid_MidCruise').text,
                'SmallGrid_MaxCruise': speed_file.find('SmallGrid_MaxCruise').text,
                'SmallGrid_MinMass': speed_file.find('SmallGrid_MinMass').text,
                'SmallGrid_MidMass': speed_file.find('SmallGrid_MidMass').text,
                'SmallGrid_MaxMass': speed_file.find('SmallGrid_MaxMass').text,
                'SmallGrid_MaxBoostSpeed': speed_file.find('SmallGrid_MaxBoostSpeed').text,
                'SmallGrid_ResistanceMultiplyer': speed_file.find('SmallGrid_ResistanceMultiplyer').text
                }

    async def run(self):
        """Run the session update loop.

        """
        while True:
            if (datetime.now() - self.timer).seconds > 5:
                self.timer = datetime.now()
                pack = {
                    'name': self.instance_name,
                    'settings': await self.game_settings(),
                    'speed_settings': await self.speed_settings(),
                    'mods': await self.mods(),
                    'factions': await self.factions(),
                    'players': await self.players()
                }
                self.storage.update_remote(pack)
                await asyncio.sleep(.05, "Switching to other task")
                os.system('cls')
                print(f"SE Social Now Monitoring {len(self.config.server_paths)} Servers.")
                print(f"hostname: {self.name} - {self.ip}")
                print(f"last updated: {datetime.now().strftime('%H:%M:%S')}")
                # print(f"Settings: {pack['settings']}")
