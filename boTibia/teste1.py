import pytesseract
import pyautogui
from time import sleep
import cv2
import  keyboard



chao = 0
msg = False
monster = False

a = print("Digite um valor 1 a 4 para andar com mause:\n [1]: Esquerda \n [2]: Direita")
floor = int(input("Digite o valor: "))

while not keyboard.is_pressed('Esc'):
    if floor == 1:
        while msg == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('left')
            print('left')
    elif floor == 2:
        while msg == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('right')
            print('right')
    elif floor == 3:
        while msg == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('up')
            print('up')
    elif floor ==4 :
        while msg == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('dowm')
            print('down')
    else:
        pyautogui.press('Esc')
        msg = True