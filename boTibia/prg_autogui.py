import pyautogui
from time import sleep
import funcoes
import keyboard

pyautogui.useImageNotFoundException()

'''while True:
    mouse = pyautogui.position()
    print(mouse)'''

onscreen = pyautogui.ImageNotFoundException
monster1 = "Rat"
monster2 = "CaveRat"
waypoint =\
    RuntimeError

while keyboard.is_pressed('ESC'):
    try:
        if onscreen :
            funcoes.waypoint()
        else:
            if funcoes.Attack("Rat.jpg") == monster1:
                x, y =  pyautogui.locateCenterOnScreen("Rat.jpg")
                pyautogui.click(x, y)
                sleep(10)
            else:
                break
    except RuntimeError:
        pass
#===============================Waypoint ==========================





