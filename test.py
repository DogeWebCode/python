from PIL import Image
import pytesseract
# 影像辨識套件位置
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# 開啟圖片，並把圖片轉成灰階
Image = Image.open(r"C:\Users\james\OneDrive\桌面\test.jpg").convert('L')
# 影像辨識
text = pytesseract.image_to_string(Image)
print(text)
