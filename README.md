- [Version 0.1.0-prerelease](#org6171bab)
- [Introduction](#orgfebd5f4)
- [Howto](#orgac452e6)
  - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#orgfaa3363)
- [Current State](#org93f172a)
  - [Scraping](#org39b0fa7)
    - [**DONE** *server settings.*](#orge7b097a)
    - [**DONE** *player list*.](#orgaaade50)
    - [**DONE** *faction List*.](#org2d91e52)
    - [player to faction link.](#orgb6dd367)
    - [**DONE** *mod List*.](#org80ca050)
    - [**DONE** *relative top speed settings*.](#org2f55fef)
    - [crunch econ data.](#org08527fa)
    - [server grid list.](#orgc325e76)
    - [link grids to players.](#org3053f3c)
  - [Publishing](#orgb677778)
    - [**DONE** *publish server settings*.](#orgfa981a6)
    - [**DONE** *publish player list*.](#orgb618505)
    - [**DONE** *publish faction List*.](#org8e116a2)
    - [publish player to faction link.](#org503823d)
    - [**DONE** *publish mod List*.](#orgf1c8fbe)
    - [publish relative top speed settings.](#org55e03d9)
    - [publish crunch econ data.](#orge2e553a)
    - [publish server grid list.](#org5687cd8)
    - [publish link grids to players.](#org0e6299d)
- [Project Goals](#orgf93dbca)
  - [Scrape in-game information from servers sbc files](#orgd342ea9)
  - [Store results](#orgde9f6d5)
    - [Put data in local sqlite database](#org3620dd1)
    - [Send data to remote database](#org85460d8)
- [Open Source](#orge8fe2a3)



<a id="org6171bab"></a>

# Version 0.1.0-prerelease


<a id="orgfebd5f4"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="orgac452e6"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="orgfaa3363"></a>

## TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="org93f172a"></a>

# Current State


<a id="org39b0fa7"></a>

## Scraping


<a id="orge7b097a"></a>

### **DONE** *server settings.*


<a id="orgaaade50"></a>

### **DONE** *player list*.


<a id="org2d91e52"></a>

### **DONE** *faction List*.


<a id="orgb6dd367"></a>

### TODO player to faction link.


<a id="org80ca050"></a>

### **DONE** *mod List*.


<a id="org2f55fef"></a>

### **DONE** *relative top speed settings*.


<a id="org08527fa"></a>

### TODO crunch econ data.


<a id="orgc325e76"></a>

### TODO server grid list.


<a id="org3053f3c"></a>

### TODO link grids to players.


<a id="orgb677778"></a>

## Publishing


<a id="orgfa981a6"></a>

### **DONE** *publish server settings*.


<a id="orgb618505"></a>

### **DONE** *publish player list*.


<a id="org8e116a2"></a>

### **DONE** *publish faction List*.


<a id="org503823d"></a>

### TODO publish player to faction link.


<a id="orgf1c8fbe"></a>

### **DONE** *publish mod List*.


<a id="org55e03d9"></a>

### TODO publish relative top speed settings.


<a id="orge2e553a"></a>

### TODO publish crunch econ data.


<a id="org5687cd8"></a>

### TODO publish server grid list.


<a id="org0e6299d"></a>

### TODO publish link grids to players.


<a id="orgf93dbca"></a>

# Project Goals


<a id="orgd342ea9"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="orgde9f6d5"></a>

## Store results


<a id="org3620dd1"></a>

### DONE Put data in local sqlite database


<a id="org85460d8"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="orge8fe2a3"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).