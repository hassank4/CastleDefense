# System Design 

# Table of Contents
  - [CRC Cards](#crc-cards)
  - [Software Architecture Diagram](#software-architecture-diagram)


## CRC Cards
Class name: Tower

Responsibilities:
- Create a Tower
- Display health
- Take damage from Enemies

Collaborators:
- Enemy


Class name: Map

Responsibilites:
- Display map that game will be played on

Collaborators:
- Supposed to collaborate with all classes in a future sprint


Class name: Enemy

Responsibilities:
- Create an Enemy
- Display health
- Display ID
- Take damage from Projectiles

Collaborators:
- Projectiles
- Tower


Class name: Projectile

Responsibilities:
- Create a Projectile
- Remove it after it hits enemy
- Check whether the enemy has been hit with the projectile
- Damage the enemy

Collaborators:
- Enemy
- Defense


Class name: Defense

Responsibilities:
- Create a Defense character
- Obtain the character's id
- Obtain the character's current health
- Change the health based on the attack damage taken
- Obtain the attack damage of the defense character
- Change the attack damage
- Check whether it is at max level
- Update that character's level
- Obtain the coordinates of the character on the map
- Update the coordinates of the character
- Check whether the defense character has died

Collaborators:
- Projectile


Class name: Start

Responsibilities:
- Create the start screen
- Display the start screen of the game
- Able the quit the start screen

Collaborators:
- Supposed to collaborate with the map class in a future sprint



## Software Architecture Diagram
![uml](https://github.com/UTMCSC301/project-ctrl-alt-elite/tree/master/doc/sprint%201/image/uml.png)