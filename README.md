- [Version 0.1.0-prerelease](#org1df1f21)
- [Introduction](#orgb6407e3)
- [Howto](#org25c1758)
- [Current State](#orgf963d5f)
  - [Scraping](#org607ab73)
    - [**DONE** *server settings.*](#org7fefaa9)
    - [**DONE** *player list*.](#org506cf6c)
    - [**DONE** *faction List*.](#orgf4e88d3)
    - [**DONE** *mod List*.](#org8143fbc)
    - [**DONE** *relative top speed settings*.](#orgb60fb20)
    - [player to faction link.](#org2fdaf49)
    - [crunch econ data.](#orgec30e9d)
    - [server grid list.](#org9462a44)
    - [link grids to players.](#org16e66dd)
  - [Publishing](#org5b78614)
    - [**DONE** *publish server settings*.](#org96d9daf)
    - [**DONE** *publish player list*.](#org66b6c16)
    - [**DONE** *publish faction List*.](#orgc47bf86)
    - [**DONE** *publish mod List*.](#org90b2a28)
    - [publish player to faction link.](#org48b8970)
    - [publish relative top speed settings.](#org0e6daf0)
    - [publish crunch econ data.](#org44fe389)
    - [publish server grid list.](#orgcd13c1a)
    - [publish link grids to players.](#orgd1e6e46)
  - [General](#orgcf51271)
    - [adjust rsync loop to guarantee no changes to the local files will be synced upstream.](#orgce17e4f)
- [Project Goals](#org10b98e3)
  - [Scrape current information from servers sbc files](#org5e0813e)
  - [Store results](#org5829475)
    - [Put data in local sqlite database](#orgbdb5b43)
    - [Send data to remote database](#org049b4da)
- [Open Source](#orgb4f108d)



<a id="org1df1f21"></a>

# Version 0.1.0-prerelease


<a id="orgb6407e3"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org25c1758"></a>

# Howto

During the initial development phase, the project will be developed in a way where the aggregated data will be stored in a local database. Conversly the data being scraped is currently setup with a rsync driven file fetching system.

It is not expected that actual deployment of the relay post development will be done in this manner, but it is a good way to get started. Seemingly as a biproduct of this, the files being scraped are not the same as the files in use by the game server. The work is being done on copies of the files. Which should by virtue of rsync be guaranteed to be latest availavle version.


<a id="orgf963d5f"></a>

# Current State


<a id="org607ab73"></a>

## Scraping


<a id="org7fefaa9"></a>

### **DONE** *server settings.*


<a id="org506cf6c"></a>

### **DONE** *player list*.


<a id="orgf4e88d3"></a>

### **DONE** *faction List*.


<a id="org8143fbc"></a>

### **DONE** *mod List*.


<a id="orgb60fb20"></a>

### **DONE** *relative top speed settings*.


<a id="org2fdaf49"></a>

### TODO player to faction link.


<a id="orgec30e9d"></a>

### TODO crunch econ data.


<a id="org9462a44"></a>

### TODO server grid list.


<a id="org16e66dd"></a>

### TODO link grids to players.


<a id="org5b78614"></a>

## Publishing


<a id="org96d9daf"></a>

### **DONE** *publish server settings*.


<a id="org66b6c16"></a>

### **DONE** *publish player list*.


<a id="orgc47bf86"></a>

### **DONE** *publish faction List*.


<a id="org90b2a28"></a>

### **DONE** *publish mod List*.


<a id="org48b8970"></a>

### TODO publish player to faction link.


<a id="org0e6daf0"></a>

### TODO publish relative top speed settings.


<a id="org44fe389"></a>

### TODO publish crunch econ data.


<a id="orgcd13c1a"></a>

### TODO publish server grid list.


<a id="orgd1e6e46"></a>

### TODO publish link grids to players.


<a id="orgcf51271"></a>

## General


<a id="orgce17e4f"></a>

### TODO adjust rsync loop to guarantee no changes to the local files will be synced upstream.


<a id="org10b98e3"></a>

# Project Goals


<a id="org5e0813e"></a>

## Scrape current information from servers sbc files

Decoupled from the existing server tech, it is it's own daemon


<a id="org5829475"></a>

## Store results


<a id="orgbdb5b43"></a>

### DONE Put data in local sqlite database


<a id="org049b4da"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="orgb4f108d"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [(yourserver).spaceengineers.social](https://spaceengineers.social/).

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).