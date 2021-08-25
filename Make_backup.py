import pyautogui
from time import sleep
import urllib
import urllib.request

pyautogui.alert('NÃO MEXA NO COMPUTADOR.')
pyautogui.PAUSE = 0.5

#Abrir o Google Drive no Computador

pyautogui.press('winleft')
sleep(1)
pyautogui.write('chro')
pyautogui.press('enter')
sleep(1)
pyautogui.write('https://drive.google.com/drive/my-drive')
sleep(1)
pyautogui.press('enter')
sleep(1)
#Acessar a area de trabalho
pyautogui.hotkey('winleft', 'd')
#Point(x=193, y=36)
pyautogui.moveTo(193, 36)
pyautogui.mouseDown() # Clica e segura com o botão esquerdo o mouse
pyautogui.moveTo(534, 867)
sleep(1)
pyautogui.hotkey('alt', 'tab')
sleep(1)
pyautogui.mouseUp() # Desclica e segura com o botão esquerdo o mouse
sleep(2)

pyautogui.alert('ARQUIVO TRANSFERIDO PARA O GOOGLE DRIVE. LIBERADO !')
'''mause = pyautogui.position()
print(mause)'''

#Entrar no Google Drive
#Deixar o arquivo.
#Esperar 5 segundos.
