try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

img = Image.open('test.png')
img.load()
i = pytesseract.image_to_string(img, config='--tessdata-dir digits')
print i
