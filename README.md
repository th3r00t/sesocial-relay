- [Version 0.1.0-prerelease](#orgd884fee)
- [Introduction](#org70fabaa)
- [Current State](#org9c55d5c)
  - [Scraping](#org32ce2c1)
    - [server settings.](#orgc4c5517)
    - [player list.](#org17b0c79)
    - [faction List.](#org349ecb0)
    - [player to faction link.](#org789c11d)
    - [mod List.](#org22faa97)
    - [relative top speed settings.](#orgf8c0900)
    - [crunch econ data.](#orgea076c5)
    - [server grid list.](#org595eca3)
    - [link grids to players.](#org5b8de29)
  - [Publishing](#org0b22453)
    - [publish server settings.](#org11baffd)
    - [publish player list.](#orgff5c592)
    - [publish faction List.](#orgf9da008)
    - [publish player to faction link.](#org601291b)
    - [publish mod List.](#org167906f)
    - [publish relative top speed settings.](#orgbf4cbf5)
    - [publish crunch econ data.](#org82cbf39)
    - [publish server grid list.](#orgb8eb409)
    - [publish link grids to players.](#org8b7a836)
- [Project Goals](#orga2ae2ca)
  - [Scrape in-game information from servers sbc files](#org79ea567)
  - [Store results](#org17f8b10)
    - [Put data in local sqlite database](#orgf585935)
    - [Send data to remote database](#org73aaf8b)
- [Open Source](#org5e8afc3)



<a id="orgd884fee"></a>

# Version 0.1.0-prerelease


<a id="org70fabaa"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org9c55d5c"></a>

# Current State


<a id="org32ce2c1"></a>

## Scraping


<a id="orgc4c5517"></a>

### DONE server settings.


<a id="org17b0c79"></a>

### DONE player list.


<a id="org349ecb0"></a>

### DONE faction List.


<a id="org789c11d"></a>

### TODO player to faction link.


<a id="org22faa97"></a>

### DONE mod List.


<a id="orgf8c0900"></a>

### DONE relative top speed settings.


<a id="orgea076c5"></a>

### TODO crunch econ data.


<a id="org595eca3"></a>

### TODO server grid list.


<a id="org5b8de29"></a>

### TODO link grids to players.


<a id="org0b22453"></a>

## Publishing


<a id="org11baffd"></a>

### DONE publish server settings.


<a id="orgff5c592"></a>

### DONE publish player list.


<a id="orgf9da008"></a>

### DONE publish faction List.


<a id="org601291b"></a>

### TODO publish player to faction link.


<a id="org167906f"></a>

### DONE publish mod List.


<a id="orgbf4cbf5"></a>

### TODO publish relative top speed settings.


<a id="org82cbf39"></a>

### TODO publish crunch econ data.


<a id="orgb8eb409"></a>

### TODO publish server grid list.


<a id="org8b7a836"></a>

### TODO publish link grids to players.


<a id="orga2ae2ca"></a>

# Project Goals


<a id="org79ea567"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="org17f8b10"></a>

## Store results


<a id="orgf585935"></a>

### DONE Put data in local sqlite database


<a id="org73aaf8b"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="org5e8afc3"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).