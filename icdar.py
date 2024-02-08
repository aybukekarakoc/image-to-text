analiz""" #import cv2 #opencv kütüphanemizi import ediyoruz
 import numpy as np

from PIL import Image
import pytesseract
# Pytesseract yolumuzu belirtiyoruz
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

kaynak=""

def metinOku(resim_yolu):
    image=cv2.imread(resim_yolu)#Okuyacağımız resmin yolunu alıyoruz


   
    sonuc=pytesseract.image_to_string(Image.open(),lang='tur')

    return sonuc
print('Okuma Başladı')
print(' ')
#Metin olarak görmek istediğimiz resmin yolunu belirtiyoruz
print(metinOku('kitap.jpg'))
print(' ')
print('Okuma Bitti') """ 
def resim_oku():
    import pytesseract
    from PIL import Image
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    a=pytesseract.image_to_string(Image.open('cumle.jpg'), lang="tur")
    pytesseract.pytesseract.tesseract_cmd= open("a.txt","a")
    pytesseract.pytesseract.tesseract_cmd.readlines()
    pytesseract.pytesseract.tesseract_cmd.close()
    print(a)
resim_oku()
