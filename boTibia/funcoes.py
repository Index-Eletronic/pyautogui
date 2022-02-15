from time import sleep
import pyautogui
##Titulos

c = ('\033[m',         # cor 0 = sem cores
     '\033[0;30;41m',  # cor 1 = Vermelho
     '\033[0;30;42m',  # cor 2 = Verde
     '\033[0;30;43m',  # cor 3 = Amarelo
     '\033[0;30;44m',  # cor 4 = Azul
     '\033[0;30;45m',  # cor 5 = Roxo
     '\033[7;30m',  # cor 6 = Branco
    )

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='') # Para ele adicionar as cores
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='') # Para limpar as cores
    sleep(1)


def esq(num):
    c = 0
    while c <= num:
        pyautogui.press('left')
        sleep(0.3)
        c += 1
        print(c)


def right(num):
    c = 0
    while c <= num:
        pyautogui.press('right')
        sleep(0.3)
        c += 1
        print(c)


def up(num):
    c = 0
    while c <= num:
        pyautogui.press('up')
        sleep(0.3)
        c += 1
        print(c)


def down(num):
    c = 0
    while c <= num:
        pyautogui.press('down')
        sleep(0.3)
        c += 1
        print(c)



