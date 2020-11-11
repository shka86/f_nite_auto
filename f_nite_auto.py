import sys
import os
import time
import random
import pyautogui as pg
pg.PAUSE = 1

# pyscreeze の設定(画像が見当たらない場合に"ImageNotFoundException"を受け取る)
from pyscreeze import ImageNotFoundException
# pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True

# # Logを残す
# sys.stdout = open("pyautogui.log", "w")

# pyautogui.locateOnScreen('someButton.png', grayscale=True,tolerance=10 ,region=(0,0, 300, 400))

#画像ファイルから座標を取得する関数
def get_locate_from_filename(filename):
    locate = None
    ntimes = 0
    retry = 10
    while locate == None and ntimes < retry:
        time.sleep(1)
        ntimes += 1
        print(f" {ntimes}", end="")
        #グレイスケールで検索(95%一致で判定)
        # locate = pg.locateCenterOnScreen(filename, grayscale=True, confidence=0.900)
        # #フルカラーで検索(遅い)
        locate = pg.locateCenterOnScreen(filename, confidence=0.90)
    print("")
    return locate

def picture_search_and_click(filename):
    print(f'searching {filename}')
    pg.moveTo(1, 1, duration=random.random()+0.1)
    nsec = 0
    timeout = 5
    while True:
        try:
            button_position = get_locate_from_filename(filename)
            if button_position == None:
                print(f"not found {filename}")
                break
            else:
                pg.moveTo(button_position[0], button_position[1],
                      duration=random.random()+0.1)
                time.sleep(3)
                pg.click(button_position)
                break
        except ImageNotFoundException:
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

def creative_wait(filename):
    print(f'wait in creative')
    print(f'searching {filename}')
    pg.moveTo(1, 1, duration=random.random()+0.1)
    nsec = 0
    timeout = 5
    while True:
        try:
            time.sleep(random.uniform(61, 69) * 60) # 1h15min
            # time.sleep(5) # 1h15min
            button_position = get_locate_from_filename(filename)
            time.sleep(3)
            pg.click(button_position)
            break
        except ImageNotFoundException:
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

def start_up():
    picture_search_and_click('sttup.png')
    picture_search_and_click('creative_button.png')

def tojiru():
    picture_search_and_click('tojiru.png')

def kakutoku():
    picture_search_and_click('kakutoku.png')

def start_creative():
    picture_search_and_click('play.png')
    picture_search_and_click('play2.png')

def wait_in_creative():
    creative_wait('pickel.png')

def leave_creative():
    pg.press('esc')
    time.sleep(3)
    picture_search_and_click('leave_from_creative_red.png')
    time.sleep(3)
    picture_search_and_click('leave.png')

#以下、メインルーチン
if __name__ == "__main__":

    screen_x, screen_y = pg.size()
    pg.moveTo(1, 1, duration=random.random()+0.1)

    start_up()

    while True:
        start_creative()
        tojiru()
        wait_in_creative()
        leave_creative()
        kakutoku()
        time.sleep(10)
