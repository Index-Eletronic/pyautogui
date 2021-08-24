import pyautogui
from time import sleep

pyautogui.alert('NÃO MEXA NO COMPUTADOR.')
pyautogui.PAUSE = 0.5
#Abrir o Google Drive no Computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
sleep(2)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
#Acessar a area de trabalho
#Clicar no arquivo para back e arrastar ele para o Google Drive
#Entrar no Google Drive
#Deixar o arquivo.
#Esperar 5 segundos.
