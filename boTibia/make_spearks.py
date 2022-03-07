import pyautogui
from time import sleep


def arrows():
    i=0
    mana = int(input("DIGITE A QUANTIDADE DE MANA:" ))
    qtarrow = int(input("QUATIDADE DE ARROWS: "))
    spell = int(100)
    arrow = int(10)
    press = mana/spell
    for i in range (i, qtarrow):

        pyautogui.press("F9", presses=press)