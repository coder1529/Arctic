import pynput
import tkinter

py = pynput.keyboard.Listener

def one_key_press(key):
    try:
        print(f"key pressed! : {key.char}")
    except AttributeError:
        print(f"special key pressed! : {key}")

with py(on_press=one_key_press) as listener:
    listener.join()