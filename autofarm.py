import pyautogui
import time

commands = ['/hunt', '/dig', '/beg', '/fish']
while(True):
    for item in commands:
        time.sleep(3)
        pyautogui.write(item)
        time.sleep(1)
        pyautogui.press('enter', presses = 2)        
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
    time.sleep(7)
