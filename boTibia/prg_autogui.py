import pyautogui
from time import sleep
import funcoes
import keyboard

pyautogui.useImageNotFoundException()

'''while True:
    mouse = pyautogui.position()
    print(mouse)'''


while True:
    try:
        if funcoes.Attack(texto="UWall"):
            pyautogui.click(1758, 464)
            with pyautogui.hold('ctrl'):
                 pyautogui.press('>')
            sleep(3)

    except RuntimeError:
        pass






