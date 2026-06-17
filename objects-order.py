from colorama import Fore
from PIL import Image
from random import randint, choice, shuffle
from math import sin, cos, sqrt
from pyperclip import copy as copy_to_clipboard
from pyperclip import paste as paste_clipboard
from time import sleep

def toJSON(level_string):
    result = []

    for object in level_string.split(';'):
        OBJECT = object.split(',')
        if len(OBJECT) <= 2: break
        result.append({})
        for i in range(0, len(OBJECT), 2):
            result[-1][int(OBJECT[i])] = OBJECT[i + 1]

    return result

def fromJSON(array):
    result = ''

    for object in array:
        formated_obj = ''
        for param in list(object.items()):
            formated_obj += f',{param[0]},{param[1]}'
        result += formated_obj[1:] + ';'

    return result

def wait_for_clipboard(level):
    while True:
        sleep(0.5)
        if paste_clipboard() != level:
            break

with open("D:\Documents\Obsidian Vault\Every GD object.md", "r", encoding="utf-8") as f:
    table = f.read().split('\n')[3::]

COLORS = {
    "solid": Fore.BLUE,
    "hazard": Fore.RED,
    "special": Fore.GREEN,
    "decoration": Fore.WHITE,
    "": Fore.WHITE 
}

while True:
    raw_level = paste_clipboard()

    level = toJSON(raw_level)

    if len(level) == 0:
        input()
        continue

    i = 0
    for object in level:
        i += 1
        for object_type in table:
            try:
                if object_type.split("|")[1].strip() == object[1]:
                    obj_type = object_type.split("|")[3].strip()
                    break
            except IndexError:
                obj_type = f'Unknown object #{object[1]}'
        print(f'{Fore.WHITE}{i}. {COLORS[object_type.split("|")[2].strip()]}{obj_type} {Fore.BLACK}(ID = {object[1]})')
        print(f'{Fore.BLACK}  x: {object[2]} y: {object[3]}')


    crop = input(f'{Fore.BLACK}Crop ({Fore.WHITE}{len(level)}{Fore.BLACK} objects): {Fore.BLUE}').strip().split(":")

    try:
        if len(crop) == 1 or crop[0] == '':
            level = level[:int(crop[0])]
        elif crop[1] == '':
            level = level[int(crop[0]):]
        else:
            level = level[int(crop[0]):int(crop[1])]
    except Exception as e:
        print(f'{Fore.RED}{e}')

    copy_to_clipboard(fromJSON(level))
    print(f'{Fore.GREEN}Successfully copied cropped level.')

    # print(f'{Fore.BLACK}Waiting for the next level string.')
    # wait_for_clipboard(raw_level)

    input()

    