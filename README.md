- [Version 0.1.0-prerelease](#orgd0cc331)
- [Introduction](#org87bab2f)
- [Howto](#org9b2e88d)
  - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#orgfeb41be)
- [Current State](#org025db9a)
  - [Scraping](#org64716ef)
    - [**DONE** server settings.](#org820d052)
    - [**DONE** player list.](#org11b9537)
    - [**DONE** faction List.](#orgda59e83)
    - [player to faction link.](#org1d5c07a)
    - [**DONE** mod List.](#org6927681)
    - [**DONE** relative top speed settings.](#orgc2be6cf)
    - [crunch econ data.](#org0ef19b1)
    - [server grid list.](#org6bf0794)
    - [link grids to players.](#orgbcc090c)
  - [Publishing](#org01722ea)
    - [**DONE** publish server settings.](#orgca2f8a7)
    - [**DONE** publish player list.](#org5227695)
    - [**DONE** publish faction List.](#org057140e)
    - [publish player to faction link.](#orgdf6f304)
    - [**DONE** publish mod List.](#orge40041c)
    - [publish relative top speed settings.](#orgc719230)
    - [publish crunch econ data.](#orgd05ab22)
    - [publish server grid list.](#orgdc0f1a5)
    - [publish link grids to players.](#org3e602b5)
- [Project Goals](#org099eb83)
  - [Scrape in-game information from servers sbc files](#org9a1653c)
  - [Store results](#org6544bb1)
    - [Put data in local sqlite database](#orgcbf8dc8)
    - [Send data to remote database](#org44787f6)
- [Open Source](#org0756615)



<a id="orgd0cc331"></a>

# Version 0.1.0-prerelease


<a id="org87bab2f"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org9b2e88d"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="orgfeb41be"></a>

## TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="org025db9a"></a>

# Current State


<a id="org64716ef"></a>

## Scraping


<a id="org820d052"></a>

### **DONE** server settings.


<a id="org11b9537"></a>

### **DONE** player list.


<a id="orgda59e83"></a>

### **DONE** faction List.


<a id="org1d5c07a"></a>

### TODO player to faction link.


<a id="org6927681"></a>

### **DONE** mod List.


<a id="orgc2be6cf"></a>

### **DONE** relative top speed settings.


<a id="org0ef19b1"></a>

### TODO crunch econ data.


<a id="org6bf0794"></a>

### TODO server grid list.


<a id="orgbcc090c"></a>

### TODO link grids to players.


<a id="org01722ea"></a>

## Publishing


<a id="orgca2f8a7"></a>

### **DONE** publish server settings.


<a id="org5227695"></a>

### **DONE** publish player list.


<a id="org057140e"></a>

### **DONE** publish faction List.


<a id="orgdf6f304"></a>

### TODO publish player to faction link.


<a id="orge40041c"></a>

### **DONE** publish mod List.


<a id="orgc719230"></a>

### TODO publish relative top speed settings.


<a id="orgd05ab22"></a>

### TODO publish crunch econ data.


<a id="orgdc0f1a5"></a>

### TODO publish server grid list.


<a id="org3e602b5"></a>

### TODO publish link grids to players.


<a id="org099eb83"></a>

# Project Goals


<a id="org9a1653c"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="org6544bb1"></a>

## Store results


<a id="orgcbf8dc8"></a>

### DONE Put data in local sqlite database


<a id="org44787f6"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="org0756615"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).