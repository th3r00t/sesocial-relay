- [Version 0.1.0-prerelease](#org1eb7a1f)
- [Introduction](#orgf852c67)
- [Howto](#org48e543d)
- [Current State](#org7f624d3)
  - [Scraping](#org66cd7d4)
    - [**DONE** *server settings.*](#org6f4e806)
    - [**DONE** *player list*.](#org396da1e)
    - [**DONE** *faction List*.](#orgc9805c7)
    - [**DONE** *mod List*.](#org3211644)
    - [**DONE** *relative top speed settings*.](#org22faf96)
    - [player to faction link.](#orgebf8562)
    - [crunch econ data.](#orge00d2a8)
    - [server grid list.](#org4594af2)
    - [link grids to players.](#orgf2ab5b6)
  - [Publishing](#org4be9bee)
    - [**DONE** *publish server settings*.](#org1360e63)
    - [**DONE** *publish player list*.](#org6f27323)
    - [**DONE** *publish faction List*.](#org7e39006)
    - [**DONE** *publish mod List*.](#org2e78db8)
    - [publish player to faction link.](#org32a8e54)
    - [publish relative top speed settings.](#org1f8b360)
    - [publish crunch econ data.](#orgc4f72bd)
    - [publish server grid list.](#org765a2ed)
    - [publish link grids to players.](#org0143a8a)
  - [General](#orgf414779)
    - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#org725ad97)
- [Project Goals](#org09f3a2a)
  - [Scrape current information from servers sbc files](#org160ac16)
  - [Store results](#org387fa20)
    - [Put data in local sqlite database](#org318ec53)
    - [Send data to remote database](#org841e43a)
- [Open Source](#org34141f3)



<a id="org1eb7a1f"></a>

# Version 0.1.0-prerelease


<a id="orgf852c67"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org48e543d"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="org7f624d3"></a>

# Current State


<a id="org66cd7d4"></a>

## Scraping


<a id="org6f4e806"></a>

### **DONE** *server settings.*


<a id="org396da1e"></a>

### **DONE** *player list*.


<a id="orgc9805c7"></a>

### **DONE** *faction List*.


<a id="org3211644"></a>

### **DONE** *mod List*.


<a id="org22faf96"></a>

### **DONE** *relative top speed settings*.


<a id="orgebf8562"></a>

### TODO player to faction link.


<a id="orge00d2a8"></a>

### TODO crunch econ data.


<a id="org4594af2"></a>

### TODO server grid list.


<a id="orgf2ab5b6"></a>

### TODO link grids to players.


<a id="org4be9bee"></a>

## Publishing


<a id="org1360e63"></a>

### **DONE** *publish server settings*.


<a id="org6f27323"></a>

### **DONE** *publish player list*.


<a id="org7e39006"></a>

### **DONE** *publish faction List*.


<a id="org2e78db8"></a>

### **DONE** *publish mod List*.


<a id="org32a8e54"></a>

### TODO publish player to faction link.


<a id="org1f8b360"></a>

### TODO publish relative top speed settings.


<a id="orgc4f72bd"></a>

### TODO publish crunch econ data.


<a id="org765a2ed"></a>

### TODO publish server grid list.


<a id="org0143a8a"></a>

### TODO publish link grids to players.


<a id="orgf414779"></a>

## General


<a id="org725ad97"></a>

### TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="org09f3a2a"></a>

# Project Goals


<a id="org160ac16"></a>

## Scrape current information from servers sbc files

Decoupled from the existing server tech, it is it's own daemon


<a id="org387fa20"></a>

## Store results


<a id="org318ec53"></a>

### DONE Put data in local sqlite database


<a id="org841e43a"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="org34141f3"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).