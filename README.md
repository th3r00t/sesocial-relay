- [Introduction](#orgcb39321)
- [Project Goals](#org54b81c0)
  - [Scrape in-game information from servers sbc files](#org5eea84d)



<a id="orgcb39321"></a>

# Introduction

Space Engineers Social Relay Project is a project to create a social relay network for the game Space Engineers. The goal is to create a network of relays that can be used to send information from connected servers back to a centralized frontend.

Each relay will be a server that is connected to the game server and will be able to send information back to the frontend. The frontend will be a web application that will allow users to view information about the game servers and their players.

This is just the beginning of the project specification, and further features will be added as the project progresses.


<a id="org54b81c0"></a>

# Project Goals


<a id="org5eea84d"></a>

## Scrape in-game information from servers sbc files

This will be completely decoupled from existing server tech, it will be its own daemon that will run on the server and will be able to scrape the information from the server's sbc files.