import pyautogui
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()

def clickTile(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)

yPosition = 402

while keyboard.is_pressed("a") == False:

    try:
        if pyautogui.pixel(345, yPosition)[0] == 0:
            clickTile(345, yPosition)
            print("Play -_-")
            print("Stop")
        if pyautogui.pixel(285, yPosition)[0] == 0:
            clickTile(285, yPosition)
            print("Play -_-")
            print("Stop")
        if pyautogui.pixel(205, yPosition)[0] == 0:
            clickTile(205, yPosition)
            print("Play -_-")
            print("Stop")
        if pyautogui.pixel(136, yPosition)[0] == 0:
            clickTile(136, yPosition)
            print("Play -_-")
            print("Stop")

    except:
        print("could not find the button ")
