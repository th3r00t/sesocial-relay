- [Introduction](#org25e87dd)
- [Current State](#org12428d9)
  - [Scraping](#org05b27d5)
    - [server settings.](#org295d65d)
    - [player list.](#org26587dc)
    - [faction List.](#org0ad3528)
    - [player to faction link.](#org2658996)
    - [mod List.](#orge1f57d6)
    - [relative top speed settings.](#org79ba3e6)
    - [crunch econ data.](#org188ed97)
    - [server grid list.](#org6bef616)
    - [link grids to players.](#org0da2553)
  - [Publishing](#orgd1b7643)
    - [publish server settings.](#org1470808)
    - [publish player list.](#org51e40a9)
    - [publish faction List.](#orge46ae9f)
    - [publish player to faction link.](#orgc2fb014)
    - [publish mod List.](#orge42780d)
    - [publish relative top speed settings.](#orgdbddb8f)
    - [publish crunch econ data.](#org4bd591d)
    - [publish server grid list.](#org672fffd)
    - [publish link grids to players.](#org6130b85)
- [Project Goals](#org316c55b)
  - [Scrape in-game information from servers sbc files](#orgc56f98c)
  - [Store results](#org8be58b3)
    - [Put data in local sqlite database](#org9349ee8)
    - [Send data to remote database](#org706cf3e)
- [Open Source](#org2d2527b)



<a id="org25e87dd"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org12428d9"></a>

# Current State


<a id="org05b27d5"></a>

## Scraping


<a id="org295d65d"></a>

### DONE server settings.


<a id="org26587dc"></a>

### DONE player list.


<a id="org0ad3528"></a>

### DONE faction List.


<a id="org2658996"></a>

### TODO player to faction link.


<a id="orge1f57d6"></a>

### DONE mod List.


<a id="org79ba3e6"></a>

### DONE relative top speed settings.


<a id="org188ed97"></a>

### TODO crunch econ data.


<a id="org6bef616"></a>

### TODO server grid list.


<a id="org0da2553"></a>

### TODO link grids to players.


<a id="orgd1b7643"></a>

## Publishing


<a id="org1470808"></a>

### DONE publish server settings.


<a id="org51e40a9"></a>

### DONE publish player list.


<a id="orge46ae9f"></a>

### DONE publish faction List.


<a id="orgc2fb014"></a>

### TODO publish player to faction link.


<a id="orge42780d"></a>

### DONE publish mod List.


<a id="orgdbddb8f"></a>

### TODO publish relative top speed settings.


<a id="org4bd591d"></a>

### TODO publish crunch econ data.


<a id="org672fffd"></a>

### TODO publish server grid list.


<a id="org6130b85"></a>

### TODO publish link grids to players.


<a id="org316c55b"></a>

# Project Goals


<a id="orgc56f98c"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="org8be58b3"></a>

## Store results


<a id="org9349ee8"></a>

### DONE Put data in local sqlite database


<a id="org706cf3e"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.


<a id="org2d2527b"></a>

# Open Source

The relay is now, and will remain an opensource project. The source code is hosted on [github](https://github.com/th3r00t/sesocial-relay). The frontend is closed source, and will be hosted free for all to use once it is ready for public use at [[<https://spaceengineers.social/>][(yourserver).spaceengineers.social].

With the relay being opensource, and since it does all the real work of interpreting the data others are encouraged to contribute to the project. If you are interested in helping out, please contact me on my discord server at [discord.gg/H9TbNJS](https://discord.gg/H9TbNJS).