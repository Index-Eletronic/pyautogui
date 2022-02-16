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

monster = "Rat"
waypoint = 0

while True:
    if funcoes.imagem("battle2.jpg") == monster:
        pyautogui.click(1759, 480)
    else:
        if funcoes.esq(1) != waypoint:
            funcoes.esq(1)
            sleep(0.3)
        else:
            break
