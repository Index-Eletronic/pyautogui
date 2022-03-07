import pyautogui
from time import sleep

print("==BOT PARA FAZER ARROWS.=v.1=")
print("==ANTES DE INICIAR, ESVAZIE A MANA==")
mana = int(input("DIGITE A QUANTIDADE DE MANA: "))-100
qtarrow = int(input("DIGITE A QUANTIDADE DE ARROWS: "))-10
hotmana = str(input("DIGITE A HOTKEY DA MANA [F1 a F12]: "))
hotArrow = str(input("DIGITE A HOTKEY DO ARROW [F1 a F12]: "))
manapotion = int(mana / 100)
manamin = int(mana*0.2)
qt = totalarrows = 0

def regenera():
    global mana, manapotion
    i = 0
    while i <= manapotion:
        sleep(2.1)
        pyautogui.press("hotmana")
        sleep(1)
        i += 1
        mana += 100
        print(f'A quatidade de mana potion {i}, {mana}')

def arrowns():
    c = 0
    global  totalarrows,mana
    while c <= qt:
        sleep(2.1)
        pyautogui.press("hotArrow")
        sleep(1)
        c += 1
        mana -= 100
        totalarrows += 10
        if mana < manamin:
            regenera()
        print(f'A quatidade Arrows: {totalarrows}')

while True:
   if totalarrows <= qtarrow:
            arrowns()
   else:
       mana = 0
       qtarrow = 0
       print("~=~= FINALIZADO! ~=~=")
       print("Index Automation")
       msg = ("ENTER PARA SAIR")
       break
#PS C:\Users\Acer\Documents\GitHub> pyinstaller --onefile .\pyautogui\boTibia\make_spearks.py



