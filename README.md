- [Introduction](#org0d75fbc)
- [Project Goals](#org1e1ce68)
  - [Scrape in-game information from servers sbc files](#org8e04307)
  - [Store results](#orgca8eeb5)
    - [Put data in local sqlite database](#org5730996)
    - [Send data to remote database](#orga3d9e97)



<a id="org0d75fbc"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org1e1ce68"></a>

# Project Goals


<a id="org8e04307"></a>

## DONE Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.


<a id="orgca8eeb5"></a>

## Store results


<a id="org5730996"></a>

### DONE Put data in local sqlite database


<a id="orga3d9e97"></a>

### TODO Send data to remote database

-   VERIFY Using sqlalchemy this should be as simple as updating the engine creation routine.