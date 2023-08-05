import math
from typing import Tuple

import utfcolor.utfcolorv1 as utfcolorv1


class UtfColorV2(utfcolorv1.UtfColor):
    def __init__(self):
        self.encoding = {
            "e": "FFFF00",#Yellow
            "n": "32CD32",#Green
            "i": "FFA500",#Orange
            "s": "008080",#Blue/Teal
            "r": "DC143C",#Red/Crimson
            "a": "4B0082",#Purple/Indigo
            "t": "6B8E23",#Green
            "d": "6A5ACD",#SlateBlue
            "h": "FF69B4",#HotPink
            "u": "006400",#DarkGreen
            "l": "B8860B",#DarkGoldenRod
            "c": "F0E68C",#Yellow
            "g": "0000FF",#Blue
            "m": "FFE4E1",#MistyRose
            "o": "800080",#Purple
            "b": "8B4513",#Brown/SaddleBrown
            "w": "FA8072",#Red/Salmon
            "f": "ADFF2F",#GreenYellow
            "k": "00CED1",#Blue/DarkTurquoise
            "z": "C71585",#MediumVioletRed
            "p": "FF4500",#OrangeRed
            "v": "BC8F8F",#RosyBrown
            "j": "FFD700",#Yellow
            "y": "000080",#Blue/Navy
            "x": "FF00FF",#Magenta
            "q": "00FFFF",#Blue/Aqua
            "1": "FF0000",#Red
            "2": "2F4F4F",#DarkSlateGray
            "3": "CD853F",#Peru
            "4": "9ACD32",#YellowGreen
            "5": "B22222",#FireBrick
            "6": "00FF7F",#SpringGreen
            "7": "87CEFA",#Blue/LightSkyBlue 
            "8": "FFDAB9",#PeachPuff
            "9": "90EE90",#LightGreen
            "0": "4682B4",#SteelBlue
            ".": "ffffff",#White
            ",": "FFDEAD",#NavajoWhite
            " ": "000000",#Black
        }

    def getSize(self, n:int)->Tuple[int,int]:
        '''calculate the size of the resulting image'''
        #calculate the x-len
        x = int(math.sqrt(n))
        #calculate the y-len
        y = n / x
        #if is not a float with a 0 after the dot, then add an extra column of pixels, so every char will be in the image
        if y - int(y) > 0.0: x += 1
        #return result
        return(x, int(y))

    def adjustTextLen(self, txt:str, x:int, y:int)->str:
        '''fill the last column with whitespaces (+16 extra whitespaces to avoid errors)'''
        return(txt.ljust((x*y)+16))