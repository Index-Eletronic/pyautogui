import pyautogui
from time import sleep
import funcoes
sleep(1)
# pyautogui.keyDown('left') # Precionar  a tecla
'''
def esq(num):
    c = 0
    while c <= num:
       print(f'quantidade de vezes: ', c)
       c += 1
valor = 5

esq(valor)
'''
left = int(input('Digite a quantidade de vezes para esquerda:' ))
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
sleep(1)
