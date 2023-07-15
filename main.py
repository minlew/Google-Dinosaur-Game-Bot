# This bot is optimised for: Full screen, 1920x1080.

import pyautogui
from PIL import ImageGrab
import time
import webbrowser

BIRD_SEARCH = 350       # Initial search range for birds
CACTUS_SEARCH = 450     # Initial search range for cacti

webbrowser.open('https://elgoog.im/dinosaur-game/')  # Go to game url
time.sleep(1)  # Give browser time to load game
pyautogui.press("Up")  # Press up key to start game
time.sleep(2)  # Give game time to start

game_is_running = True


# Make dino jump
def jump():
    global CACTUS_SEARCH, BIRD_SEARCH
    pyautogui.press("Up")
    if CACTUS_SEARCH < 900:
        CACTUS_SEARCH += 7  # With each jump, increase search range in front of dinosaur (up to a point)...
        BIRD_SEARCH += 1    # ...This is to account for game accelerating as time goes on


# Make dino duck
def duck():
    pyautogui.keyDown("Down")
    time.sleep(0.2)  # Stay ducked for 200ms
    pyautogui.keyUp("Down")


while game_is_running:
    image = ImageGrab.grab().convert('L')  # Take screenshot, "L" to convert to greyscale
    data = image.load()  # Save pixel data

    # Check collision for cacti
    for i in range(400, CACTUS_SEARCH, 2):
        if data[200, 200] > 100:     # Detect if point in sky has light pixels = Daytime
            if data[i, 660] < 100:   # Detect dark pixels signifying cactus
                jump()
                break
        if data[200, 200] < 100:    # Detect if point in sky has dark pixels = Nighttime
            if data[i, 660] > 100:   # Detect light pixels signifying cactus
                jump()
                break

    # Check collision for birds
    for i in range(300, BIRD_SEARCH, 2):
        if data[200, 200] > 100:    # Detect if point in sky has light pixels = Daytime
            if data[i, 560] < 100:   # Detect dark pixels signifying bird
                duck()
                break
        if data[200, 200] < 100:    # Detect if point in sky has dark pixels = Nighttime
            if data[i, 560] > 100:   # Detect dark pixels signifying bird
                duck()
                break

    if data[735, 440] < 100 and data[815, 440] < 100:  # Detect dark pixels of game over screen
        game_is_running = False
