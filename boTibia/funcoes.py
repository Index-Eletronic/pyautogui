from time import sleep
import pyautogui
import pytesseract
import cv2

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

#======================================= Função Waypoint  ===================================
def esq(num):
    if pyautogui.ImageNotFoundException:
        c = 0
        while c <= num:
            pyautogui.press('left')
            sleep(0.3)
            c += 1
            print(c)
    else:
        pass

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
#==========================================================================================================
#======================================= Função Trata imagem para Texto ===================================
def Attack(texto):
    img = cv2.imread("dwarf.jpg")  # imread é o metodo cv2 que le a imagem ' ('caminho da imagem')
    caminho = r"C:\Users\Acer\AppData\Local\Programs\Tesseract-OCR"
    # passo 2: pedir para tesseract extrair o texto da imagem
    pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
    texto = pytesseract.image_to_string(img)
    return texto

#print(imagem("battle2.jpg"))
#==========================================================================================================
#======================================= SEM FUNCIONALIDADE ===================================
def semfun():
    fileObj = "Waypoint.txt"
    while True:

            x, y = pyautogui.locateCenterOnScreen("floor1.jpg", confidence=0.1)
            mouse = pyautogui.position()
            posicao = str(mouse)
            #pyautogui.click(x, y)
            way = open("Waypoint.txt", "a")
            way.write(posicao)
            way.close()

    pass
    '''O argumento de palavra-chave opcional confidenceespecifica a precisão com que a função deve 
    localizar a imagem na tela. Isso é útil caso a função não consiga localizar uma imagem devido a diferenças insignificantes de pixel:'''
#==========================================================================================================


def lermouse():
    with open('Waypoint.txt', 'r') as w:
        caminho = w.readlines()
        list(caminho)
        x = caminho[0]
        print(x)

'''        x = caminho[0]
        y = caminho[1]
    for x, y in lista:
        print(f'{x} {y}', end='')'''


#======================================= Função Trata imagem para Texto ===================================
def Sorry(texto):
    msg = "Sorry, not possible."
    while True:
        img = cv2.imread("sorry.jpg")  # imread é o metodo cv2 que le a imagem ' ('caminho da imagem')
        caminho = r"C:\Users\Acer\AppData\Local\Programs\Tesseract-OCR"
        # passo 2: pedir para tesseract extrair o texto da imagem
        pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
        texto = pytesseract.image_to_string(img)
        if texto == msg:
           texto = True
        return texto


#print(imagem("battle2.jpg"))
#==========================================================================================================

def utanihur():
    while True:
        pyautogui.press('f4')
        sleep(100)
    pass

def waypoint():
    while True:
        esq(20)
        pyautogui.click(1758, 464)
        sleep(20)
        esq(20)
        pyautogui.click(1758, 464)
        sleep(20)
        esq(10)
        pyautogui.click(1758, 464)
        sleep(20)
        right(20)
        pyautogui.click(1758, 464)
        sleep(20)
        pyautogui.click(1758, 464)
        sleep(20)
        pyautogui.click(1758, 464)
        sleep(10)


    pass