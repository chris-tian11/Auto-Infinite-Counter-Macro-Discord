import pyautogui
import time
#time.sleep(3)
#print(pyautogui.position())
add_number = 1
recent_number = 604
time.sleep(3)
for i in range(10):
    pyautogui.click(463, 1362)
    pyautogui.write(str(recent_number+add_number))
    pyautogui.press("enter")
    time.sleep(0.2)
    add_number += 1
    pyautogui.click(1775, 1318)
    pyautogui.write(str(recent_number+add_number))
    pyautogui.press("enter")
    time.sleep(0.2)
    add_number += 1
