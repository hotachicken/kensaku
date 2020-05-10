from PIL import Image, ImageGrab
import pytesseract as ptess
import sys

"""
Gets contents of clipboard. If an image, get as an image.
For now, just assume an image
"""
def get_from_clip():
    img = ImageGrab.grabclipboard()
    if isinstance(img, Image.Image):
        img.save('temp.png')
    else:
        print("no image found", flush=True)
    isimage = True
    return img, isimage

if __name__ == "__main__":
    img, isimage = get_from_clip()
    if isimage:
        out = ptess.image_to_string(Image.open('temp.png'), lang='jpn', config='--psm 6')
        out = out.encode('utf8')
        sys.stdout.buffer.write(out)
