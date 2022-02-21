import pytesseract
import pyautogui
from time import sleep
import cv2
import  keyboard
import funcoes


#=Tirando o Screenshot da tela
'''while True:
    mouse = pyautogui.position()
    print(mouse)
#814, 859
#926, 860
1567, 393
1719,393
'''
def error():
    while True:
        global sorry
        #Vai tirar o screenshot da região Sorry not possible
        sc = pyautogui.screenshot(region=(812,850,126,18))
        width, height = sc.size
        #Percorrer o screenshot
        for x in range(0, width, 1):
            for y in range(0, height, 1):
                r,g,b = (sc.getpixel((x,y)))
                if r == 255 and g == 255 and b == 255:
                    sorry = True
                    print("Sorry, not possible.")
                else:
                    sorry = False
                    #pyautogui.click(812+x, 850+y)

def criature():
    while True:
        m = 0
        global monster

        #Vai tirar o screenshot da região Sorry not possible
        sc = pyautogui.screenshot(region=(1567,393,150,40))
        width, height = sc.size
        #Percorrer o screenshot
        for x in range(0, width, 1):
            for y in range(0, height, 1):
                r,g,b = (sc.getpixel((x,y)))
                if r == 50 and g == 205 and b == 50 or r == 0 and g == 255 and b == 0:
                    monster = True
                    m += 1
                    pyautogui.click(1567+x, 393+y)
                    print(f"Total de Criaturas mortas é: {m}")
                else:
                    monster = False
                    #pyautogui.click(812+x, 850+y)



'''txtm = False
def erro():
    global txtm
    while True:
       if  pyautogui.locateOnScreen('sorry.jpg'):
            print("Esta na tela")
       else:
           print("Não esta na tela")'''

monster = False

a = print("Digite um valor 1 a 4 para andar com mause:\n [1]: Esquerda \n [2]: Direita")
floor = int(input("Digite o valor: "))


while not keyboard.is_pressed('Esc'):
    error()
    if floor == 1:

        while sorry == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('left')

    elif floor == 2:
        while sorry == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('right')

    elif floor == 3:
        while sorry == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('up')

    elif floor ==4 :
        while sorry == False and monster == False and not keyboard.is_pressed('Esc'):
            pyautogui.press('dowm')

    else:
        pyautogui.press('Esc')
        sorry = True