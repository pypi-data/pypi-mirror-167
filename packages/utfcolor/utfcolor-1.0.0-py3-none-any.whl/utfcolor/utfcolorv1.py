import math
import re
from typing import Tuple


class UtfColor:
    def __init__(self):
        self.encoding = {
            "e": "00",#0
            "n": "ff",#255
            "i": "80",#128
            "s": "40",#64
            "r": "c0",#192
            "a": "20",#32
            "t": "e0",#224
            "d": "60",#96
            "h": "a0",#160
            "u": "10",#16
            "l": "f0",#240
            "c": "30",#48
            "g": "d0",#208
            "m": "50",#80
            "o": "b0",#176
            "b": "70",#112
            "w": "90",#144
            "f": "08",#8
            "k": "f8",#248
            "z": "18",#24
            "p": "e8",#232
            "v": "28",#40
            "j": "d8",#216
            "y": "38",#56
            "x": "c8",#200
            "q": "48",#72
            "1": "b8",#184
            "2": "58",#88
            "3": "a8",#168
            "4": "68",#104
            "5": "98",#152
            "6": "78",#120
            "7": "88",#136
            "8": "04",#4
            "9": "fb",#251
            "0": "0c",#12
            ".": "f4",#244
            ",": "14",#20
            " ": "ec",#236
        }

    def encode(self, txt:str)->str:
        '''encodes text to utf-color'''
        encodedText = ""
        for c in txt:
            encodedText += self.encoding[c]
        return(encodedText)

    def prepareText(self, txt:str)->str:
        '''prepare the input text for usage of utf-color. This will remove all chars that are unsupported by utf-color'''
        #convert capital letters to lower case
        txt = txt.lower()
        #remove unsupported characters
        txt = re.sub("[^a-z0-9,. ]", "", txt)
        #return result
        return(txt)

    def adjustTextLen(self, txt:str, x:int, y:int)->str:
        '''fill the last column with whitespaces (+16 extra whitespaces to avoid errors)'''
        return(txt.ljust((x*y*3)+16))

    def getSize(self, n:int)->Tuple[int,int]:
        '''calculate the size of the resulting image'''
        #divide n by 3 because every pixel will represent 3 chars
        n = n/3
        #calculate the x-len
        x = int(math.sqrt(n))
        #calculate the y-len
        y = n / x
        #if is not a float with a 0 after the dot, then add an extra column of pixels, so every char will be in the image
        if y - int(y) > 0.0: x += 1
        #return result
        return(x, int(y))