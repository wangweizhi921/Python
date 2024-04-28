import keyboard
import time

def callbacks(keyword):
    print(keyword.name)
    

keyboard.on_press(callbacks)
keyboard.wait(0)