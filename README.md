# Castle Defense

## Game Description

Castle Defense is a strategy game that works as most tower defense games do,
where enemies try to reach the end of a map while the player tries to place defenses to stop them from attacking.

![start menu](https://user-images.githubusercontent.com/47669299/78315880-4089b980-752c-11ea-8075-9fde0da29656.png)
![help menu](https://user-images.githubusercontent.com/47669299/78316018-9cecd900-752c-11ea-90b7-6bcb339e75a9.png)
![game](https://user-images.githubusercontent.com/47669299/78320963-c57ad000-7538-11ea-9f89-7dc9e109cea3.png)
![user highscore](https://user-images.githubusercontent.com/47669299/78316072-b68e2080-752c-11ea-96a4-3b05f377a171.png)

### Requirements

Things you will need before installation:
* Windows OS / Mac OS X / Ubuntu
* 512MB of RAM (Minimum)
* 2MB of Hard Disk Space (Minimum)

### Installation
1) You will need to install the latest version of python 3. The link to the
download page will be below.

[Python3](https://www.python.org/downloads/)


2) You will need to install PyCharm for Python if you need to use 
option 2 to run the game (next topic in README). The link to download 
pycharm is below.

[PyCharm IDE](https://www.jetbrains.com/pycharm/download/#section=mac)


3) You will also need to install pygame. Open up Windows PowerShell or the Terminal,
depending on the operating system you are using. Once open, paste and run the command
displayed below.

```
python3 -m pip install -U pygame --user
```

4) Use Windows PowerShell or Terminal again to git clone the Castle Defense files using
the command below. It will usually be saved in your user directory. Alternatively, 
you can download the zip folder from the link below.

```
git clone https://github.com/UTMCSC301/project-ctrl-alt-elite.git
```
or
```
https://github.com/UTMCSC301/project-ctrl-alt-elite/archive/master.zip
```

### Running the Game

There are 2 options to run this game. 'Option 2' is to be used if 
'Option 1' does not work.

* Option 1 
    1) Open up PowerShell or Terminal
    2) Go to the directory you saved the game
    3) Enter the src folder
    4) Type the command that works for you
  
    ```
    py Run.py
    ```
   or
    ```
    python3 Run.py
    ```
 * Option 2
    1) Go to the game directory through file explorer
    2) Enter the 'src' folder
    
    If you saved it in your user directory:
    ```
    C:\Users\<User Name>\project-ctrl-alt-elite\src
    ```
    
    3) Open 'Run.py' with PyCharm
    4) When the file opens, run the game by clicking the green play button at the top of your screen

### How to Play

1) In the start menu, click "Start Quest!".

2) You will be prompted to enter your name. Do so by using your keyboard and click "Advance".

3) Enemies start to spawn as soon as the game starts. You initially have 1000 diamonds.

4) To start attacking, purchase defences by dragging them onto the map from the bottom menu. Each has a unique shooting range, so their 
cost is different, with the most expensive being the most powerful defence. When the amount of diamonds reaches 0, you can no longer
purchase defences and will have to attack enemies to obtain more.

5) Each enemy creates a different amount of damage to the main tower located towards the end of map. Ogres are the most powerful
and assassins are the weakest enemies. When an enemy's health reaches 0, it disappears from the map.

6) Your main goal is to protect the main tower. Click on the tower to see its current health.

7) You can quit the game by clicking the "Quit" button.

8) You can surrender by clicking the button that says "Surrender". Your score will be saved to the highscore table, which you will be 
able to see.

### Built With

* [Python](https://www.python.org/downloads/)
* [Pygame](https://www.pygame.org/wiki/GettingStarted)
* [Pymongo](https://api.mongodb.com/python/current/)
* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=mac)

### Authors

* Humza Afzal
* Thamodh Egodawatte
* Hassan Kamal
* Bikramjit Saini
* Kevin Subhash
* Khadijah Mosaheb

### License

This game is built under the [MIT License](https://tasdikrahman.mit-license.org/).

### Acknowledgements

We give credit to the following people for helping us develop this game:

* [TechWithTim](https://www.youtube.com/watch?v=iLHAKXQBOoA&t=16357s) - With the help of his coding stream, we were able to make a functioning Tower Defence game.
* [Billie Thompson](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - Her README.md template helped guide us in making ours.
