- [Version 0.1.0-prerelease](#org382fc3e)
- [Introduction](#orgfaf7555)
- [Howto](#orgb705b52)
  - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#orgcdfe337)
- [Current State](#orgc30895b)
  - [Scraping](#org62bfd37)
    - [**DONE** *server settings.*](#org9a1e03f)
    - [**DONE** *player list*.](#orga669283)
    - [**DONE** *faction List*.](#orgd4cbe11)
    - [**DONE** *mod List*.](#orgecb98f4)
    - [**DONE** *relative top speed settings*.](#orgde8952e)
    - [player to faction link.](#org8d73dc9)
    - [crunch econ data.](#org7d040d3)
    - [server grid list.](#org52c6eaf)
    - [link grids to players.](#org58c574c)
  - [Publishing](#org04d1000)
    - [**DONE** *publish server settings*.](#org71ceb2b)
    - [**DONE** *publish player list*.](#org40df2ec)
    - [**DONE** *publish faction List*.](#orgf599024)
    - [**DONE** *publish mod List*.](#org440e7cf)
    - [publish player to faction link.](#org477e11c)
    - [publish relative top speed settings.](#org784ed0a)
    - [publish crunch econ data.](#org7e14d15)
    - [publish server grid list.](#orgafbd7c9)
    - [publish link grids to players.](#orgd38c99f)
- [Project Goals](#org8860123)
  - [Scrape in-game information from servers sbc files](#org0ba512d)
  - [Store results](#orgced8bcd)
    - [Put data in local sqlite database](#org7beaa02)
    - [Send data to remote database](#orga48e7cc)
- [Open Source](#org5259710)



<a id="org382fc3e"></a>

# Version 0.1.0-prerelease


<a id="orgfaf7555"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="orgb705b52"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="orgcdfe337"></a>

## TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="orgc30895b"></a>

# Current State


<a id="org62bfd37"></a>

## Scraping


<a id="org9a1e03f"></a>

### **DONE** *server settings.*


<a id="orga669283"></a>

### **DONE** *player list*.


<a id="orgd4cbe11"></a>

### **DONE** *faction List*.


<a id="orgecb98f4"></a>

### **DONE** *mod List*.


<a id="orgde8952e"></a>

### **DONE** *relative top speed settings*.


<a id="org8d73dc9"></a>

### TODO player to faction link.


<a id="org7d040d3"></a>

### TODO crunch econ data.


<a id="org52c6eaf"></a>

### TODO server grid list.


<a id="org58c574c"></a>

### TODO link grids to players.


<a id="org04d1000"></a>

## Publishing


<a id="org71ceb2b"></a>

### **DONE** *publish server settings*.


<a id="org40df2ec"></a>

### **DONE** *publish player list*.


<a id="orgf599024"></a>

### **DONE** *publish faction List*.


<a id="org440e7cf"></a>

### **DONE** *publish mod List*.


<a id="org477e11c"></a>

### TODO publish player to faction link.


<a id="org784ed0a"></a>

### TODO publish relative top speed settings.


<a id="org7e14d15"></a>

### TODO publish crunch econ data.


<a id="orgafbd7c9"></a>

### TODO publish server grid list.


<a id="orgd38c99f"></a>

### TODO publish link grids to players.


<a id="org8860123"></a>

# Project Goals


<a id="org0ba512d"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="orgced8bcd"></a>

## Store results


<a id="org7beaa02"></a>

### DONE Put data in local sqlite database


<a id="orga48e7cc"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="org5259710"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).