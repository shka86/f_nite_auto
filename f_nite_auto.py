import sys
import os
import time
import random
import pyautogui as pg
pg.PAUSE = 1

from pyscreeze import ImageNotFoundException

def handler(func, *args):
    return func(*args)

def hoge():
    print("hoge")

def ckick(locate):
    print("click", locate)
    return pg.click(locate)

def wait(locate):
    print("wait", locate)
    pg.click(locate)
    time.sleep(61 * 60)
    # time.sleep(5)
    pg.press('esc')

def sttup(locate):
    print("click", locate)
    pg.click(locate)
    time.sleep(3 * 60)

def crash(locate):
    print("\ndetect crash\n")
    locate = pg.locateCenterOnScreen("crash_ok.png", confidence=0.90)
    click(locate)

d = {
    "sttup": {
        "pic": "sttup.png",
        "func": sttup,
    },
    "creative_button": {
        "pic": "creative_button.png",
        "func": ckick,
    },
    "play": {
        "pic": "play.png",
        "func": ckick,
    },
    "play2": {
        "pic": "play2.png",
        "func": ckick,
    },
    "pickel": {
        "pic": "pickel.png",
        "func": wait,
    },
    "leave": {
        "pic": "leave.png",
        "func": ckick,
    },
    "leave_from_creative": {
        "pic": "leave_from_creative.png",
        "func": ckick,
    },
    "leave_from_creative_red": {
        "pic": "leave_from_creative_red.png",
        "func": ckick,
    },
    "kakutoku": {
        "pic": "kakutoku.png",
        "func": ckick,
    },
    "kakutoku2": {
        "pic": "kakutoku2.png",
        "func": ckick,
    },
    "tojiru": {
        "pic": "tojiru.png",
        "func": ckick,
    },
}

while True:
    locate = None
    for x in d.keys():
        locate = pg.locateCenterOnScreen(d[x]["pic"], confidence=0.90)
        if not locate is None:
            print(">>> ", x, locate)
            handler(d[x]["func"], locate)
            break
            # return x, locate
    if locate is None:
        print("targets not found")
        time.sleep(2)

    pg.moveTo(1, 1, duration=random.random()+0.1)
