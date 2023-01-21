- [Version 0.1.0-prerelease](#org155d0e8)
- [Introduction](#org5db20e1)
- [Questions you'll never have to answer again.](#orgd199bb5)
  - [You got a mod list I can look at?](#org9df42d0)
  - [Who plays on this server?](#orga616716)
  - [What factions are active here?](#org6c495e0)
  - [What's the economy like?](#orgc2f1d1b)
- [Things I hope to see](#org2460304)
  - [Player wallets.](#org9b6d11c)
  - [Faction GPS sharing.](#org099c62d)
  - [Watchdog integration.](#orgc136fd5)
  - [Visual Mapping.](#org6a4dd88)
  - [Grid Registry.](#orgf9991fe)
  - [Discord integration via web api for bot hooks.](#org7dea012)
- [Howto](#org514bea2)
- [Current State](#org31055dc)
  - [Scraping](#org66a804a)
    - [**DONE** *server settings.*](#org118ffff)
    - [**DONE** *player list*.](#orgcdd5c67)
    - [**DONE** *faction List*.](#org1336a2c)
    - [**DONE** *mod List*.](#orgdd6902f)
    - [**DONE** *relative top speed settings*.](#org7ba2859)
    - [player to faction link.](#org5281df7)
    - [crunch econ data.](#org2135590)
    - [server grid list.](#orgeee12fa)
    - [link grids to players.](#orgf141eba)
  - [Publishing](#org0f93210)
    - [**DONE** *publish server settings*.](#org914979c)
    - [**DONE** *publish player list*.](#orga89339a)
    - [**DONE** *publish faction List*.](#org70485f5)
    - [**DONE** *publish mod List*.](#org169d857)
    - [publish player to faction link.](#org4df862c)
    - [publish relative top speed settings.](#org7558af3)
    - [publish crunch econ data.](#org8c56555)
    - [publish server grid list.](#org7f854b4)
    - [publish link grids to players.](#org70de009)
  - [General](#orgaf4bb70)
    - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#org87020e1)
- [Project Goals](#orgb42a57b)
  - [Scrape current information from servers sbc files](#orgecd185d)
  - [Store results](#org4047fc3)
    - [Put data in local sqlite database](#org7b170b8)
    - [Send data to remote database](#org51bfb7d)
- [Open Source](#org2da8a69)



<a id="org155d0e8"></a>

# Version 0.1.0-prerelease


<a id="org5db20e1"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="orgd199bb5"></a>

# Questions you'll never have to answer again.


<a id="org9df42d0"></a>

## You got a mod list I can look at?


<a id="orga616716"></a>

## Who plays on this server?


<a id="org6c495e0"></a>

## What factions are active here?


<a id="orgc2f1d1b"></a>

## What's the economy like?


<a id="org2460304"></a>

# Things I hope to see


<a id="org9b6d11c"></a>

## Player wallets.


<a id="org099c62d"></a>

## Faction GPS sharing.


<a id="orgc136fd5"></a>

## Watchdog integration.


<a id="org6a4dd88"></a>

## Visual Mapping.

think general galactic overview things like planets, & other celestial objects. Trade stations etc&#x2026;


<a id="orgf9991fe"></a>

## Grid Registry.


<a id="org7dea012"></a>

## Discord integration via web api for bot hooks.


<a id="org514bea2"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="org31055dc"></a>

# Current State


<a id="org66a804a"></a>

## Scraping


<a id="org118ffff"></a>

### **DONE** *server settings.*


<a id="orgcdd5c67"></a>

### **DONE** *player list*.


<a id="org1336a2c"></a>

### **DONE** *faction List*.


<a id="orgdd6902f"></a>

### **DONE** *mod List*.


<a id="org7ba2859"></a>

### **DONE** *relative top speed settings*.


<a id="org5281df7"></a>

### TODO player to faction link.


<a id="org2135590"></a>

### TODO crunch econ data.


<a id="orgeee12fa"></a>

### TODO server grid list.


<a id="orgf141eba"></a>

### TODO link grids to players.


<a id="org0f93210"></a>

## Publishing


<a id="org914979c"></a>

### **DONE** *publish server settings*.


<a id="orga89339a"></a>

### **DONE** *publish player list*.


<a id="org70485f5"></a>

### **DONE** *publish faction List*.


<a id="org169d857"></a>

### **DONE** *publish mod List*.


<a id="org4df862c"></a>

### TODO publish player to faction link.


<a id="org7558af3"></a>

### TODO publish relative top speed settings.


<a id="org8c56555"></a>

### TODO publish crunch econ data.


<a id="org7f854b4"></a>

### TODO publish server grid list.


<a id="org70de009"></a>

### TODO publish link grids to players.


<a id="orgaf4bb70"></a>

## General


<a id="org87020e1"></a>

### TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="orgb42a57b"></a>

# Project Goals


<a id="orgecd185d"></a>

## Scrape current information from servers sbc files

Decoupled from the existing server tech, it is it's own daemon


<a id="org4047fc3"></a>

## Store results


<a id="org7b170b8"></a>

### DONE Put data in local sqlite database


<a id="org51bfb7d"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="org2da8a69"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [(yourserver).spaceengineers.social](https://spaceengineers.social/).

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).