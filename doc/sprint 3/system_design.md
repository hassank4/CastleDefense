# System Design 

# Table of Contents
  - [CRC Cards](#crc-cards)
  - [Software Architecture Diagram](#software-architecture-diagram)

## CRC Cards
Class name: Database

Responsibilites:
- Create a Database object
- Insert a highscore into the database
- Get a highscore by name from the database
- Get all records in the database

Class name: Enemy

Responsibilities:
- Have a slide method which uses the next point and a slope to move

Collaborators:
- Game Map

Class name: Menu

Responsibilities:
- Create a button
- Create a menu to select defenses and use currency

Collaborators:
- Run

Class name: Points

Responsibilites:
- Create a points object that is used by the game map
- Obtain the current amount of points acquired by the user
- Add to the score depending on what emeny is killed
- Reset the amount of kills and score for when the user plays again
- Update the kill counts depending on which enemy is killed
- Obtain the kill counts for the three enemy types
- Add the final score to the database

Collaborators:
- Assassin
- Mage
- Ogre
- Database

Class name: Run

Responsibilites:
- Display help screens for how to play the game
- Display the highscore screen after the game is over
- Able to pause and resume the game
- Allow the user to select the difficulty of the game

Class name: Defense

Responsibilites:
- Able to display the defense character on the game map window


## Software Architecture Diagram
![uml.png](https://github.com/UTMCSC301/project-ctrl-alt-elite/blob/master/doc/sprint%203/image/uml.png)