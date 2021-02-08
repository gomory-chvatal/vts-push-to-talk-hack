import keyboard
import time


# function to press a key
def slow_press(key):
    keyboard.press(key)
    time.sleep(0.15) # wait a little bit so VTS sees the keypress
    keyboard.release(key)


# callbacks (set these to "undo" the hotkey)
def left_up(e):
    slow_press('F13')
def right_up(e):
    slow_press('F14')
def up_up(e):
    slow_press('F15')
def down_up(e):
    slow_press('F16')
def a_up(e):
    slow_press('F17')


# hooks (these are "watching" for the VTS hotkeys to be released)
keyboard.on_release_key('left', left_up)
keyboard.on_release_key('right', right_up)
keyboard.on_release_key('up', up_up)
keyboard.on_release_key('down', down_up)
keyboard.on_release_key('right ctrl', a_up)


# loop forever (remember to kill process when done with VTS)
keyboard.wait()
