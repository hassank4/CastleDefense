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

Class name: Defense

Defense Subclasses: WeakArcher, IntermediateArcher, StrongArcher, WeakKnight, IntermediateKnight, StrongKnight, WeakWizard, IntermediateWizard, StrongWizard

Responsibilities:
- Be able to store an idle image or attack image
- Obtain the idle image
- Obtain the attack image
- Place the defense object at valid locations

Class name: Projectile

Responsibilities:
- Be able to store an image
- Obtain the image

Class name: WeakArcher

Parent Class: Defense

Responsibilities:
- Create an Archer with weak attack damage
- Create and store an arrow projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: IntermediateArcher

Parent Class: Defense

Responsibilities:
- Create an Archer with intermediate attack damage
- Create and store an arrow projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: StrongArcher

Parent Class: Defense

Responsibilities:
- Create an Archer with a strong amount of attack damage
- Create and store an arrow projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: WeakKnight

Parent Class: Defense

Responsibilities:
- Create a Knight with weak attack damage
- Create and store a spear projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: IntermediateKnight

Parent Class: Defense

Responsibilities:
- Create a Knight with intermediate attack damage
- Create and store a spear projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: StrongKnight

Parent Class: Defense

Responsibilities:
- Create a Knight with a strong amount of attack damage
- Create and store a spear projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: WeakWizard

Parent Class: Defense

Responsibilities:
- Create a Wizard with weak attack damage
- Create and store a magic orb projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: IntermediateWizard

Parent Class: Defense

Responsibilities:
- Create a Wizard with intermediate attack damage
- Create and store a magic orb projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: StrongWizard

Parent Class: Defense

Responsibilities:
- Create a Wizard with a strong amount of attack damage
- Create and store a magic orb projectile for the character
- Obtain the projectile

Collaborators:
- Projectile

Class name: Spritesheet

Responsibilities:
- Create a sprite sheet
- Draw a specific image cell from the spritesheet
- Set or change the image file used

Collaborators:
- Enemy
- Supposed to also collaborate with the Defense, Projectile and Game_map classes in future sprint


## Software Architecture Diagram
![uml.png](https://github.com/UTMCSC301/project-ctrl-alt-elite/blob/master/doc/sprint%202/image/uml.png)
