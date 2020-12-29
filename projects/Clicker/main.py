from pynput import mouse, keyboard
from enum import Enum
import time


class Action(Enum):
    LEFT_SPAM = 1
    OBSIDIAN = 2

myMouse = mouse.Controller()
myKeyboard = keyboard.Controller()

pressing = False
running = True

action = Action(int(input("Modaj tryb: ")))

def on_press(key):
    global pressing
    global running

    try:
        if key == keyboard.Key.f18:
            pressing = not pressing
        if key == keyboard.Key.f17:
            running = not running
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

listener = keyboard.Listener(
    on_press=on_press)
listener.start()


if action == Action.LEFT_SPAM:
    while running:
        if pressing:
            myMouse.press(mouse.Button.left)
            myMouse.release(mouse.Button.left)
            time.sleep(0.01)

elif action == Action.OBSIDIAN:
    while running:
        if pressing:
            with myKeyboard.pressed(keyboard.Key.shift):
                myKeyboard.tap('1')
                time.sleep(0.1)
                for i in range(3):
                    myMouse.press(mouse.Button.right)
                    myMouse.release(mouse.Button.right)
                    time.sleep(0.1)
                
                time.sleep(0.2)
                myKeyboard.tap('2')
                time.sleep(0.2)
                for i in range(3):
                    myMouse.press(mouse.Button.left)
                    time.sleep(2)
                    myMouse.release(mouse.Button.left)
            
        

