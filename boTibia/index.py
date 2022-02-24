from time import sleep
import pyautogui
import pytesseract
import cv2
import funcoes
from time import sleep

# passo 1: ler a imagem
#imagem = cv2.imread("dwarf.jpg") #imread é o metodo cv2 que le a imagem ' ('caminho da imagem')

#caminho = r"C:\Users\Acer\AppData\Local\Programs\Tesseract-OCR"
# passo 2: pedir para tesseract extrair o texto da imagem
#pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
#texto = pytesseract.image_to_string(imagem)
#list(texto)
#m=texto[0]
#print(m)

'''sleep(3)
sc = pyautogui.screenshot(region=(1567,393,150,40))
sc.save("Monster.png")'''

'''while True:
    mouse = pyautogui.position()
    print(mouse)'''
#814, 859
#926, 860

#funcoes.semfun()
#funcoes.lermouse()
mouse = pyautogui.locateOnScreen("qrcode.png")
#pyautogui.moveTo(x, y)
pyautogui.doubleClick(mouse)