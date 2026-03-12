import json
import subprocess
import tkinter as tk
from pynput import keyboard

CONFIG_FILE = "config.json"

print("===== StreamDih =====")

# ----------------------------
# load config
# ----------------------------

def load_config():

    try:
        with open(CONFIG_FILE) as f:
            data = json.load(f)
            print("Config loaded")
            return data

    except:

        print("No config file, creating new")

        data = {}

        for i in range(13,25):
            data[f"F{i}"] = ""

        save_config(data)

        return data


def save_config(data):

    with open(CONFIG_FILE,"w") as f:
        json.dump(data,f,indent=2)

    print("Config saved")


config = load_config()


# ----------------------------
# run command
# ----------------------------

def run_action(cmd):

    if cmd.strip() == "":
        print("mt command")
        return

    print("Running:",cmd)

    try:
        subprocess.Popen(cmd, shell=True)

    except Exception as e:

        print("ERROR:",e)


# ----------------------------
# keyboard listener
# ----------------------------

def on_press(key):

    try:

        print("Key detected:",key)

        name = key.name.upper()

        if name in config:

            print("Mapped action:",config[name])

            run_action(config[name])

    except AttributeError:

        print("Non standard key:",key)

    except Exception as e:

        print("Listener error:",e)


listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Keyboard listener started")


# ----------------------------
# GUI
# ----------------------------

root = tk.Tk()
root.title("StreamDih Config")

entries = {}

row = 0

for key in config:

    label = tk.Label(root,text=key,width=6)
    label.grid(row=row,column=0,padx=5,pady=5)

    entry = tk.Entry(root,width=40)
    entry.insert(0,config[key])
    entry.grid(row=row,column=1)

    entries[key] = entry

    row += 1


def save():

    for key in entries:

        config[key] = entries[key].get()

    save_config(config)


save_btn = tk.Button(root,text="Save",command=save)
save_btn.grid(row=row,column=0,columnspan=2,pady=10)


print("ui ready")

root.mainloop()
