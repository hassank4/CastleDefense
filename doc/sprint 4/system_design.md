# System Design

# Table of Contents
  - [CRC Cards](#crc-cards)
  - [Software Architecture Diagram](#software-architecture-diagram)
  
  
## CRC Cards
Class name: Run

Responsibilites:
- Have a help menu to help the user get familiar with the controls
- Keep track of the user's name when they are playing
- Display the user's points on the screen
- Save the user's score to the high scores database

Collaborators:
- Game Map

Class name: Game Map

Responsibilities:
- Have the enemies spawning with animations
- Have animations for the defenses
- Show the main tower which the enemies attack

Collaborators:
- Points
- Tower

Class name: Defense

Responsibilites:
- Able to attack the enemies and deal damage to health
- Game score increases if an enemiy is killed with an attack
- Able to find the closest enemy on the path to attack
- Animated when idling in one spot
- Animated when attacking an enemy

Class name: Enemy

Responsibilites:
- Obtain whether the enemy is dead
- Able to switch direction it faces on the path
- Is animated to walk on the path

Class name: Tower

Responsibilites:
- Able to draw the tower on the game
- Know whether it was clicked on

## Software Architecture Diagram
![uml.png](https://github.com/UTMCSC301/project-ctrl-alt-elite/blob/master/doc/sprint%204/image/uml.png)
