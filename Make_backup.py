import pyautogui
from time import sleep

pyautogui.alert('NÃO MEXA NO COMPUTADOR.')
pyautogui.PAUSE = 0.5
#Abrir o Google Drive no Computador

pyautogui.press('winleft')
sleep(1)
pyautogui.write('chro')
pyautogui.press('enter')
sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')

#Acessar a area de trabalho
pyautogui.hotkey('winleft', 'd')
#Point(x=193, y=36)
pyautogui.moveTo(193, 36)
pyautogui.mouseDown() # Clica e segura com o botão esquerdo o mouse
pyautogui.moveTo(534, 867)
sleep(1)
pyautogui.hotkey('alt', 'tab')
pyautogui.mouseUp() # Desclica e segura com o botão esquerdo o mouse
'''mause = pyautogui.position()
print(mause)'''

#Entrar no Google Drive
#Deixar o arquivo.
#Esperar 5 segundos.
