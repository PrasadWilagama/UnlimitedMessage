import pyautogui
import time
message = 3
while True >0:
    time.sleep(4)
    pyautogui.typewrite("Hello Guys")
    time.sleep(2)
    pyautogui.press('enter')
    message=message-1