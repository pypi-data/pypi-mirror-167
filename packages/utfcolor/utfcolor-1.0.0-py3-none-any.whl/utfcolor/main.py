from PIL import Image, ImageDraw

from utfcolor.utfcolorv1 import UtfColor
from utfcolor.utfcolorv2 import UtfColorV2
from utfcolor.utfcolorv3 import UtfColorV3
from utfcolor.createEncoding import UtfColorCustom
from utfcolor.standardEncoding import StandardEncoding
from utfcolor.upScale import upScale
import utfcolor.util as util


def txtToImg(text:str, encoding:str="utf-color", outputFile:str="", scale:int=0) -> None:
    '''convert any text to an image'''

    #create encoding objects
    if encoding == "utf-color":
        encoder = UtfColor()
    elif encoding == "utf-colorv2":
        encoder = UtfColorV2()
    elif encoding == "utf-colorv3":
        encoder = UtfColorV3()
    elif encoding == "rng-utf-color":
        encoder = UtfColorCustom()
    else:
        encoder = StandardEncoding(encoding)

    #prepare text for encoding
    text = encoder.prepareText(text)
    x,y = encoder.getSize(len(text))
    text = encoder.adjustTextLen(text,x,y)
    #encode text
    text = encoder.encode(text)

    #create a new image
    img = Image.new(mode="RGB", size=(x,y))
    draw = ImageDraw.Draw(img)

    #fill the image with pixels
    for px in range(x):
        for py in range(y):
            draw.point((px,py), fill=f"#{text[:6]}")    #put pixel into image
            #img.paste(((f"#{text[:6]}")), (px,py,x,y))
            text = text[6:]     #remove hex value from text

    #save the image
    if outputFile == "": outputFile = util.createFilename()
    if scale != 0: img = upScale(img, scale)
    img.save(outputFile)