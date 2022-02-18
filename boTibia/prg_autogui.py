import pyautogui
from time import sleep
import cv2
import pytesseract

pyautogui.useImageNotFoundException()

'''while True:
    mouse = pyautogui.position()
    print(mouse)'''
#================================ Texto da imagem ==============================================
# passo 1: ler a imagem
monster = cv2.imread("dwarf.jpg")  # imread é o metodo cv2 que le a imagem ' ('caminho da imagem')
caminho = r"C:\Users\Acer\AppData\Local\Programs\Tesseract-OCR"
# passo 2: pedir para tesseract extrair o texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(monster)
#==============================================================================================
x, y = pyautogui.locateCenterOnScreen("dwarf.jpg", confidence=0.5)
mouse = pyautogui.position()
#================================ Ler a Imagem==============================================
while True:
    try:
        if  texto == mause:
            pyautogui.click(1758, 464)
            sleep(2.5)
        else:
            pyautogui.press('up')
            sleep(1)
            pyautogui.press('up')
            sleep(1)
            pyautogui.press('up')
            sleep(1)
            pyautogui.press('up')
            sleep(1)
            pyautogui.press('down')
            sleep(1)
            pyautogui.press('down')
            sleep(1)
            pyautogui.press('down')
            sleep(1)
            pyautogui.press('down')
            sleep(1)

    except RuntimeError:
        pass



'''            with pyautogui.hold('ctrl'):
                    pyautogui.press('left')
                    sleep(1)
            with pyautogui.hold('ctrl'):
                    pyautogui.press('right')
                    sleep(1)'''


