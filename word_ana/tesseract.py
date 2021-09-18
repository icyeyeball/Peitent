import pytesseract
from PIL import Image
image = Image.open('35.png')
code = pytesseract.image_to_string(image, lang='chi_tra+chi_tra_vert+eng')
print(code)