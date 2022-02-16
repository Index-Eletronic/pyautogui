import pyautogui
from time import sleep
import funcoes

'''left = int(input('Digite a quantidade de vezes para esquerda:' ))
right = int(input('Digite a quantidade de vezes para direita:' ))
up = int(input('Digite a quantidade de vezes para cima:' ))
down = int(input('Digite a quantidade de vezes para baixo:' ))
sleep(1)
funcoes.esq(left)
sleep(1)
funcoes.right(right)
sleep(1)
funcoes.up(up)
sleep(1)
funcoes.down(down)
sleep(1)'''
'''while True:
    mouse = pyautogui.position()
    print(mouse)'''

monster1 = "Rat"
monster2 = "CaveRat"
waypoint = TypeError

while True:
    try:
        if funcoes.imagem("Rat.jpg") == monster1:
            pyautogui.click(1759, 480)
            sleep(10)
        else:
            if funcoes.esq(0) != waypoint:
                funcoes.esq(1)
                sleep(0.3)
            elif funcoes.right(0) != waypoint:
                 funcoes.right(1)
                 sleep(0.3)
            elif funcoes.up(0) != waypoint:
                 funcoes.up(1)
                 sleep(0.3)
            elif funcoes.down(0) != waypoint:
                 funcoes.down(1)
                 sleep(0.3)
            else:
                break
    except ValueError:
        pass



