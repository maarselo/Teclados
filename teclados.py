import evdev
import keyboard

scancodes = {
    0: None, 1: u'ESC', 2: u'1', 3: u'2', 4: u'3', 5: u'4', 6: u'5', 7: u'6', 8: u'7', 9: u'8',
    10: u'9', 11: u'0', 12: u'-', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'q', 17: u'w', 18: u'e', 19: u'r',
    20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'[', 27: u']', 28: u'CRLF', 29: u'LCTRL',
    30: u'a', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u';',
    40: u'"', 41: u'`', 42: u'LSHFT', 43: u'\\', 44: u'z', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
    50: u'm', 51: u',', 52: u'.', 53: u'/', 54: u'RSHFT', 56: u'LALT', 57: u' ', 58: u'CAPSLOCK', 100: u'RALT'
}

capscodes = {
    0: None, 1: u'ESC', 2: u'!', 3: u'@', 4: u'#', 5: u'$', 6: u'%', 7: u'^', 8: u'&', 9: u'*',
    10: u'(', 11: u')', 12: u'_', 13: u'+', 14: u'BKSP', 15: u'TAB', 16: u'Q', 17: u'W', 18: u'E', 19: u'R',
    20: u'T', 21: u'Y', 22: u'U', 23: u'I', 24: u'O', 25: u'P', 26: u'{', 27: u'}', 28: u'CRLF', 29: u'LCTRL',
    30: u'A', 31: u'S', 32: u'D', 33: u'F', 34: u'G', 35: u'H', 36: u'J', 37: u'K', 38: u'L', 39: u':',
    40: u'\'', 41: u'~', 42: u'LSHFT', 43: u'|', 44: u'Z', 45: u'X', 46: u'C', 47: u'V', 48: u'B', 49: u'N',
    50: u'M', 51: u'<', 52: u'>', 53: u'?', 54: u'RSHFT', 56: u'LALT', 57: u' ', 100: u'RALT'
}

# Logitech
device_logitech = evdev.InputDevice('/dev/input/event5')
print(device_logitech)
palabra = ""
capslock_on = False 

for event in device_logitech.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        categ = evdev.categorize(event)
        iar = event
        codigo = event.code

        if keyboard.is_pressed('enter'):
            print(palabra)
            break
        
        if event.value == 1:  
            if codigo == 58:  
                capslock_on = not capslock_on  
                continue

            if (keyboard.is_pressed('shift') and not capslock_on) or (not keyboard.is_pressed('shift') and capslock_on):
                letra = capscodes.get(codigo, '')
                letra_minuscula =letra.lower()                    
            else:
                letra = scancodes.get(codigo, '')
                letra_minuscula =letra.lower()
            
            if letra:
                print("Tecla presionada: " + letra)
                palabra += letra





#Device de HP
"""
device_hp = evdev.InputDevice('/dev/input/event2')
print(device_hp)

for event in device_hp .read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
"""
#Device2 de logitech (?)
"""
device2_logitech = evdev.InputDevice('/dev/input/event6')
print(device2_logitech)

for event in device2_logitech.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
"""