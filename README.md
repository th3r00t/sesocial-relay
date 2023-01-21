- [Version 0.1.0-prerelease](#org77d66a6)
- [Introduction](#org3db833e)
- [Howto](#org40dac98)
  - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#org5251df0)
- [Current State](#orgb606909)
  - [Scraping](#orgb250e2f)
    - [server settings.](#orgee8b590)
    - [player list.](#orged626e6)
    - [faction List.](#org98a8a5c)
    - [player to faction link.](#org8016cb4)
    - [mod List.](#org313b0c0)
    - [relative top speed settings.](#orgc0d7a71)
    - [crunch econ data.](#orgce3e2de)
    - [server grid list.](#org1572335)
    - [link grids to players.](#orgfc9b9ee)
  - [Publishing](#org55c76f9)
    - [publish server settings.](#orgbb1f3c6)
    - [publish player list.](#orgce04376)
    - [publish faction List.](#org305ebc2)
    - [publish player to faction link.](#org1a0fee4)
    - [publish mod List.](#orgf7b0e35)
    - [publish relative top speed settings.](#orga424524)
    - [publish crunch econ data.](#org50e46f7)
    - [publish server grid list.](#org5d358f2)
    - [publish link grids to players.](#org2d602e7)
- [Project Goals](#orgcd70460)
  - [Scrape in-game information from servers sbc files](#org17ca168)
  - [Store results](#orga96d97c)
    - [Put data in local sqlite database](#org0fce1b9)
    - [Send data to remote database](#org4f077d6)
- [Open Source](#orgd76ba79)



<a id="org77d66a6"></a>

# Version 0.1.0-prerelease


<a id="org3db833e"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org40dac98"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="org5251df0"></a>

## TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="orgb606909"></a>

# Current State


<a id="orgb250e2f"></a>

## Scraping


<a id="orgee8b590"></a>

### DONE server settings.


<a id="orged626e6"></a>

### DONE player list.


<a id="org98a8a5c"></a>

### DONE faction List.


<a id="org8016cb4"></a>

### TODO player to faction link.


<a id="org313b0c0"></a>

### DONE mod List.


<a id="orgc0d7a71"></a>

### DONE relative top speed settings.


<a id="orgce3e2de"></a>

### TODO crunch econ data.


<a id="org1572335"></a>

### TODO server grid list.


<a id="orgfc9b9ee"></a>

### TODO link grids to players.


<a id="org55c76f9"></a>

## Publishing


<a id="orgbb1f3c6"></a>

### DONE publish server settings.


<a id="orgce04376"></a>

### DONE publish player list.


<a id="org305ebc2"></a>

### DONE publish faction List.


<a id="org1a0fee4"></a>

### TODO publish player to faction link.


<a id="orgf7b0e35"></a>

### DONE publish mod List.


<a id="orga424524"></a>

### TODO publish relative top speed settings.


<a id="org50e46f7"></a>

### TODO publish crunch econ data.


<a id="org5d358f2"></a>

### TODO publish server grid list.


<a id="org2d602e7"></a>

### TODO publish link grids to players.


<a id="orgcd70460"></a>

# Project Goals


<a id="org17ca168"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="orga96d97c"></a>

## Store results


<a id="org0fce1b9"></a>

### DONE Put data in local sqlite database


<a id="org4f077d6"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="orgd76ba79"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).