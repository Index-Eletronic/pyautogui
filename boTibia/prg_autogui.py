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

while True:
    try:
        if onscreen :
            if funcoes.Sorry("sorry.jpg") != "Sorry, not possible.":
                funcoes.waypoint()
            else:
                break
        else:
            if funcoes.Attack("Rat.jpg") == monster1:
                x, y =  pyautogui.locateCenterOnScreen("Rat.jpg")
                pyautogui.click(x, y)
                sleep(10)
            else:
                break
    except RuntimeError:
        pass






