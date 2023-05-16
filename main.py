import os
import sys
import time
import keyboard
import pyautogui
import ctypes
import hashlib

from datetime import datetime
from termcolor import colored
from colorant import Colorant
from settings import Settings
from keyauth import api

settings = Settings()

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "Colorant",
    ownerid = "XpXJiuVsQu",
    secret = "5f3628628bc9a1261189c940d38278905ad42ecbea7286f54a38ddab8966f5b0",
    version = "1.0",
    hash_to_check = getchecksum()
)

KEY_NAMES = {
 1: "'L Mouse Button'", 2: "'R Mouse Button'", 4: "'MButton'", 5: "'X1 Mouse Button'", 
 6: "'X2 Mouse Button'", 8: "'Backspace'", 9: "'Tab'", 13: "'Enter'", 16: "'Shift'", 
 17: "'Ctrl'", 18: "'Alt'", 20: "'CapsLock'", 27: "'Esc'", 32: "'Spacebar'", 37: "'Left'", 
 38: "'Up'", 39: "'Right'", 40: "'Down'", 48: "'0'", 49: "'1'", 50: "'2'", 51: "'3'", 
 52: "'4'", 53: "'5'", 54: "'6'", 55: "'7'", 56: "'8'", 57: "'9'", 65: "'A'", 66: "'B'", 
 67: "'C'", 68: "'D'", 69: "'E'", 70: "'F'", 71: "'G'", 72: "'H'", 73: "'I'", 74: "'J'", 
 75: "'K'", 76: "'L'", 77: "'M'", 78: "'N'", 79: "'O'", 80: "'P'", 81: "'Q'", 82: "'R'", 
 83: "'S'", 84: "'T'", 85: "'U'", 86: "'V'", 87: "'W'", 88: "'X'", 89: "'Y'", 90: "'Z'", 
 112: "'F1'", 113: "'F2'", 114: "'F3'", 115: "'F4'", 116: "'F5'", 117: "'F6'", 
 118: "'F7'", 119: "'F8'", 120: "'F9'", 121: "'F10'", 122: "'F11'", 123: "'F12'"}

monitor = pyautogui.size()
CENTER_X, CENTER_Y = monitor.width // 2, monitor.height // 2

XFOV = settings.get_int('Settings', 'X-FOV')
YFOV = settings.get_int('Settings', 'Y-FOV')
TOGGLE_KEY = settings.get('Settings', 'TOGGLE-ON/OFF')
AIMBOT_KEY = int(settings.get('AIMBOT', 'KEY-BIND'), 16)
TRIGGERBOT_KEY = int(settings.get('TRIGGERBOT', 'KEY-BIND'), 16)
SILENTBOT_KEY = int(settings.get('SILENTBOT', 'KEY-BIND'), 16)
XSPEED = settings.get_float('AIMBOT', 'X-SPEED')
YSPEED = settings.get_float('AIMBOT', 'Y-SPEED')
YOUR_INGAME_SENSITIVITY = settings.get_float('Settings', 'IN-GAME-SENS')
FLICKSPEED = 1.07437623 * (YOUR_INGAME_SENSITIVITY ** -0.9936827126)

def main():
    os.system('color')
    APP_NAME = settings.get('Settings', 'APP-NAME')
    key = settings.get('Settings', 'KEY')
    if not key:
        key = input(colored('[Auth]', 'white', 'on_light_red') + colored(' Please Enter your Key: ', 'light_red'))
        settings.set('Settings', 'KEY', key)
        settings.save()
    keyauthapp.license(key)
    os.system(f"title {APP_NAME}")
    os.system('cls')
    print(colored(" \t\t\t\t  Welcome Back! " + "● Expiry " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'), 'light_red'))
    bettercmd()
    resize_cmd(120,30)
    toggled = False
    status = 'Disabled'
    colorant = Colorant(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, XSPEED, YSPEED, AIMBOT_KEY, TRIGGERBOT_KEY, SILENTBOT_KEY)
    print(colored(''' ''', 'light_red'))
    print(colored('\t\t\t\t\tStable Supporters Version! v1.4\n', 'white', 'on_light_red'))
    print(colored('[Your Keybinds]', 'white', 'on_light_red'))
    print(colored(f'[x] Hold ({KEY_NAMES[AIMBOT_KEY]})', 'light_red'), colored('→ Aimbot', 'white'))
    print(colored(f'[x] Hold ({KEY_NAMES[TRIGGERBOT_KEY]})', 'light_red'), colored('→ Triggerbot', 'white'))
    print(colored(f'[x] Press ({KEY_NAMES[SILENTBOT_KEY]}) Warning high detection', 'light_red'), colored('→ Silentaim\n', 'white'))
    print(colored('[Information]', 'white', 'on_light_red'))
    print(colored('Set enemies to', 'white'), colored('Purple', 'light_red'))
    print(colored(f'Press {colored(TOGGLE_KEY, "light_red")} to toggle ON/OFF Colorant', 'white'))
    print(colored('Thanks again for your support, welcome to ', 'white') + colored('COLORANT', 'light_red') + colored(' family!\n', 'white'))
    
    try:
        print(f'{colored("[Status]", "white", "on_light_red")}', end='\n')
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = 'Enabled \b' if colorant.toggled else 'Disabled'
            print(f'\r{colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
        sys.exit()
        
def bettercmd():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
        style &= ~0x00040000
        style &= ~0x00010000
        ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

def resize_cmd(width, height):
    STD_OUTPUT_HANDLE_ID = ctypes.c_ulong(0xFFFFFFF5)
    windll = ctypes.windll.kernel32

    handle = windll.GetStdHandle(STD_OUTPUT_HANDLE_ID)
    rect = ctypes.wintypes.SMALL_RECT(0, 0, width - 1, height - 1)  # note: right and bottom are inclusive

    windll.SetConsoleScreenBufferSize(handle, ctypes.wintypes._COORD(width, height))
    windll.SetConsoleWindowInfo(handle, ctypes.c_int(True), ctypes.pointer(rect))
        
if __name__ == '__main__':
    main()
