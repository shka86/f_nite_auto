import sys
import os
import time
import pyautogui as pg
pg.PAUSE = 1

# pyscreeze の設定(画像が見当たらない場合に"ImageNotFoundException"を受け取る)
from pyscreeze import ImageNotFoundException
# pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = True

# Logを残す
sys.stdout = open("pyautogui.log", "w")

# pyautogui.locateOnScreen('someButton.png', grayscale=True,tolerance=10 ,region=(0,0, 300, 400))

#画像ファイルから座標を取得する関数
def get_locate_from_filename(filename):
    locate = None
    while locate == None:
        time.sleep(0.1)
        #グレイスケールで検索(95%一致で判定)
        # locate = pg.locateCenterOnScreen(filename, grayscale=True, confidence=0.900)
        # #フルカラーで検索(遅い)
        locate = pg.locateCenterOnScreen(filename, confidence=0.850)
    return locate

def picture_search_click(filename):
    print(f'searching {filename}')
    pg.moveTo(1, 1, duration=1)
    nsec = 0
    timeout = 5
    while True:
        try:
            button_position = get_locate_from_filename(filename)
            pg.moveTo(button_position[0], button_position[1], duration=1)
            time.sleep(3)
            pg.click(button_position)
            break
        except ImageNotFoundException:
            time.sleep(1)
            nsec += 1
            if nsec > timeout:
                pg.alert(text='タイムアウト', button='OK')
                break

def picture_search_wait(filename):
    print(f'searching {filename}')
    pg.moveTo(1, 1, duration=1)
    nsec = 0
    timeout = 5
    while True:
        try:
            # time.sleep(80 * 60) # 1h15min
            time.sleep(5) # 1h15min
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

def start_creative():
    picture_search_click('play.png')
    picture_search_click('play2.png')

def wait_to_get_xp():
    picture_search_wait('pickel.png')

def leave_creative():
    pg.press('esc')
    time.sleep(3)
    picture_search_click('leave_from_creative_red.png')
    time.sleep(3)
    picture_search_click('leave.png')

#以下、メインルーチン
if __name__ == "__main__":

    #画面サイズの取得
    screen_x, screen_y = pg.size()

    #マウスを(1,1)に移動しておく
    pg.moveTo(1, 1, duration=1)

    while True:
        start_creative()
        wait_to_get_xp()
        leave_creative()
        time.sleep(10)
