# System Design 

# Table of Contents
  - [CRC Cards](#crc-cards)
  - [Software Architecture Diagram](#software-architecture-diagram)


## CRC Cards
Class name: Map

Responsibilites:
- Keep track of lives and currency
- Store a list of the Enemies
- Be able to generate Enemies in waves
- Have a method to draw the various components on the screen

Collaborators:
- Assassin
- Mage
- Ogre

Class name: Enemy

Enemy Subclasses: Assassin, Mage, Ogre

Responsibilities:
- Keep track of all the points it needs to travel to in a list
- Be able to move to the next point in the list
- Keep track of which point it is currently on and be able to return it
- Be able to store a walk image and attack image
- Keep track of a speed

Collaborators:
- Game Map

## Software Architecture Diagram
![uml.png](https://github.com/UTMCSC301/project-ctrl-alt-elite/blob/master/doc/sprint%202/image/uml.png)
