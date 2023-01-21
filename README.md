- [Version 0.1.0-prerelease](#org3c451d2)
- [Introduction](#orgd8838f0)
- [Questions you'll never have to answer again.](#orgad60906)
  - [You got a mod list I can look at?](#org06faacb)
  - [Who plays on this server?](#orgdf552cb)
  - [What factions are active here?](#orgd0a7215)
  - [What's the economy like?](#org5736261)
- [Things I hope to see](#orgf7cdae1)
  - [Player wallets.](#orge5c1546)
  - [Improved in game economy, and resource trading system.](#org1609a11)
  - [Faction GPS sharing.](#org80061fb)
  - [Watchdog integration.](#orgb8f2c5c)
  - [Visual Mapping.](#org33c3deb)
  - [Grid Registry.](#orge48472e)
  - [Discord integration via web api for bot hooks.](#orgd177299)
- [Howto](#org56c144b)
- [Current State](#orga232cc5)
  - [Scraping](#org9a04a69)
    - [**DONE** *server settings.*](#org09f8e5d)
    - [**DONE** *player list*.](#org510014b)
    - [**DONE** *faction List*.](#org7688a1e)
    - [**DONE** *mod List*.](#org52db196)
    - [**DONE** *relative top speed settings*.](#org9f4a3fe)
    - [player to faction link.](#org387c3d4)
    - [crunch econ data.](#org7cbbc42)
    - [server grid list.](#orgc0ba510)
    - [link grids to players.](#org560432b)
  - [Publishing](#org9aef17e)
    - [**DONE** *publish server settings*.](#org78bc953)
    - [**DONE** *publish player list*.](#orgae32252)
    - [**DONE** *publish faction List*.](#orgeed0949)
    - [**DONE** *publish mod List*.](#org8798b1f)
    - [publish player to faction link.](#org1986009)
    - [publish relative top speed settings.](#org3d08e37)
    - [publish crunch econ data.](#org8c99756)
    - [publish server grid list.](#org732558e)
    - [publish link grids to players.](#orge6cd130)
  - [General](#org1732a8d)
    - [adjust rsync loop to guarantee no changes to the local files will be synced downstream.](#org87c7cc1)
- [Project Goals](#org27ce37e)
  - [Scrape current information from servers sbc files](#org70a1e7d)
  - [Store results](#orgfc98714)
    - [Put data in local sqlite database](#org3dcd6f6)
    - [Send data to remote database](#orgd6bbaed)
- [Open Source](#orga2da108)



<a id="org3c451d2"></a>

# Version 0.1.0-prerelease


<a id="orgd8838f0"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="orgad60906"></a>

# Questions you'll never have to answer again.


<a id="org06faacb"></a>

## You got a mod list I can look at?

sesocial-relay will provide a list of mods that are installed on the server. The front end will generate clickable links for all these mods.


<a id="orgdf552cb"></a>

## Who plays on this server?

sesocial-relay will provide a list of players that are currently on the server, along with a history of who has played before.


<a id="orgd0a7215"></a>

## What factions are active here?

sesocial-relay will provide a list of factions that are operating on your server.


<a id="org5736261"></a>

## What's the economy like?

sesocial-relay will provide a list of all the items that are being traded via crunch economy.


<a id="orgf7cdae1"></a>

# Things I hope to see


<a id="orge5c1546"></a>

## Player wallets.

Gateway feature to hopefully integrate with a full blown economy system.


<a id="org1609a11"></a>

## Improved in game economy, and resource trading system.

Out of game digital marketplace for trading in game resources and setting up said trades.


<a id="org80061fb"></a>

## Faction GPS sharing.

Drop a gps marker, and have it listed on your factions page, for your memebers to see.


<a id="orgb8f2c5c"></a>

## Watchdog integration.

A watchdog integration to allow for a more robust and reliable way to monitor your server. The framework for this integration is already in place, but it needs to be fleshed out.


<a id="org33c3deb"></a>

## Visual Mapping.

think general galactic overview things like planets, & other celestial objects. Trade stations etc&#x2026;


<a id="orge48472e"></a>

## Grid Registry.

All grids are listed in your servers sbc file, lets do something with them. Label them, store them, back them up independently of the server.


<a id="orgd177299"></a>

## Discord integration via web api for bot hooks.

This is almost as simple as setting up a quick set of FastAPI endpoints, This could be done either here in the relay or upstream on the frontend.


<a id="org56c144b"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="orga232cc5"></a>

# Current State


<a id="org9a04a69"></a>

## Scraping


<a id="org09f8e5d"></a>

### **DONE** *server settings.*


<a id="org510014b"></a>

### **DONE** *player list*.


<a id="org7688a1e"></a>

### **DONE** *faction List*.


<a id="org52db196"></a>

### **DONE** *mod List*.


<a id="org9f4a3fe"></a>

### **DONE** *relative top speed settings*.


<a id="org387c3d4"></a>

### TODO player to faction link.


<a id="org7cbbc42"></a>

### TODO crunch econ data.


<a id="orgc0ba510"></a>

### TODO server grid list.


<a id="org560432b"></a>

### TODO link grids to players.


<a id="org9aef17e"></a>

## Publishing


<a id="org78bc953"></a>

### **DONE** *publish server settings*.


<a id="orgae32252"></a>

### **DONE** *publish player list*.


<a id="orgeed0949"></a>

### **DONE** *publish faction List*.


<a id="org8798b1f"></a>

### **DONE** *publish mod List*.


<a id="org1986009"></a>

### TODO publish player to faction link.


<a id="org3d08e37"></a>

### TODO publish relative top speed settings.


<a id="org8c99756"></a>

### TODO publish crunch econ data.


<a id="org732558e"></a>

### TODO publish server grid list.


<a id="orge6cd130"></a>

### TODO publish link grids to players.


<a id="org1732a8d"></a>

## General


<a id="org87c7cc1"></a>

### TODO adjust rsync loop to guarantee no changes to the local files will be synced downstream.


<a id="org27ce37e"></a>

# Project Goals


<a id="org70a1e7d"></a>

## Scrape current information from servers sbc files

Decoupled from the existing server tech, it is it's own daemon


<a id="orgfc98714"></a>

## Store results


<a id="org3dcd6f6"></a>

### DONE Put data in local sqlite database


<a id="orgd6bbaed"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="orga2da108"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [(yourserver).spaceengineers.social](https://spaceengineers.social/).

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).