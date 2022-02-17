from time import sleep
import pyautogui
import pytesseract
import cv2
import funcoes


# passo 1: ler a imagem
imagem = cv2.imread("dwarf.jpg") #imread é o metodo cv2 que le a imagem ' ('caminho da imagem')

caminho = r"C:\Users\Acer\AppData\Local\Programs\Tesseract-OCR"
# passo 2: pedir para tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem)
print(texto)




#funcoes.semfun()
funcoes.lermouse()

