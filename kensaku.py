from PIL import Image, ImageGrab
import pytesseract as ptess
import pyperclip
import sys
import re

"""
Gets contents of clipboard. If an image, get as an image.
For now, just assume an image
"""
def blow_up_image(img, factor=2):
    return img.resize((img.size[0] * factor, img.size[1] * factor))

def get_from_clip():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        img = blow_up_image(img)
    else:
        print("no image found", flush=True)
    isimage = True
    return img, isimage

if __name__ == "__main__":
    vert = len(sys.argv) > 1 # hacky, change later
    isvert = 'jpn-vert' if vert else 'jpn'
    img, isimage = get_from_clip()
    if isimage:
        out = ptess.image_to_string(img, lang=isvert, config='--psm 6')
        out = re.sub('\\s', '', out)
        pyperclip.copy(out)
        out = out.encode('utf8')
        sys.stdout.buffer.write(out)
