# Demolisher
Aliens are invading, and you have been called to protect the planet! Your weapon of choice is a giant wrecking ball, capable of smashing the aliens to pieces, but it can also hurt you so be sure to keep it a healthy distance away! You can shoot lasers with the space bar which will bounce the ball around, but the aliens have energy shields so you got to hit them with the wrecking ball! Move your ship with the "<-" and "->" keys.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 demolisher 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the game folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- demolisher          (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Matt Manley (manleym@byui.edu)
* Matt Bencomo (matt.ibencomo@gmail.com)