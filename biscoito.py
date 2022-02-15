import pyautogui

pyautogui.PAUSE = 0.01

'''mause = pyautogui.position()
print(mause)'''

while pyautogui.position() == (39, 961):
    pyautogui.doubleClick()
    break
