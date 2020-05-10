from PIL import Image, ImageGrab
import pytesseract

"""
Gets contents of clipboard. If an image, get as an image.
For now, just assume an image
"""
def get_from_clip():
    img = ImageGrab.grabclipboard()
