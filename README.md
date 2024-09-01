# Chrome Dinosaur Game Bot

## Description
This project is an automated bot that plays the Chrome Dinosaur Game. It uses image recognition to detect obstacles and automatically make the dinosaur jump or duck accordingly.

### Features

* Automatically starts the game.
* Detects and avoids cacti by jumping.
* Detects and avoids birds by ducking.
* Adapts to increasing game speed.
* Works in both day and night modes of the game.

### Technologies
* Python

### Python Libs
* import pyautogui
* PIL
* time
* webbrowser

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Install [requirements](requirements.txt).
4. Run [script](main.py) in Python. 

## Usage
1. The script will automatically open the Chrome Dinosaur Game in your default web browser and start playing.
2. To stop the bot, simply close the game window or terminate the Python script.

## How It Works

* The bot opens the game URL using the `webbrowser` module.
* It starts the game by simulating an "Up" key press.
* The bot continuously captures screenshots of the game area.
* It analyzes pixel data to detect obstacles:
    * Cacti are detected in a lower area of the screen
    * Birds are detected in a higher area of the screen
* When an obstacle is detected, the bot simulates the appropriate key press:
    * "Up" key to jump over cacti
    * "Down" key to duck under birds
* The bot adapts to the increasing speed of the game by expanding its search area over time.
* It can detect both day and night modes of the game and adjust its detection accordingly.
* The game ends when the bot detects the "Game Over" screen.

## Customization
* You can adjust the `BIRD_SEARCH` and `CACTUS_SEARCH` variables to fine-tune the detection range.
* The script is currently optimized for 1920x1080 resolution. You may need to adjust the pixel coordinates if using a different resolution.
