from PIL import Image
from pytesseract import pytesseract
import string

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Freizeit\CarDectect\Images\th.jpeg"

myConfig = r"--psm 12 --oem 3"

img = Image.open(image_path)
text = pytesseract.image_to_string(img, config=myConfig)
table = str.maketrans('', '', string.ascii_lowercase)
for c in text:
    if c.islower():
        text = text.replace(c, ' ')
for char in string.punctuation:
    text = text.replace(char, ' ')
print(text)
