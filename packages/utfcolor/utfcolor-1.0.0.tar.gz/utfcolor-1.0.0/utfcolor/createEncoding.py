import random

from utfcolor import utfcolorv2


class UtfColorCustom(utfcolorv2.UtfColorV2):
    def __init__(self, space:int=40):
        self.space = space
        self.encoding = self.createEncoding()

    def createEncoding(self)->dict:
        encoding = {}
        letters = {
            "e": "",
            "n": "",
            "i": "",
            "s": "",
            "r": "",
            "a": "",
            "t": "",
            "d": "",
            "h": "",
            "u": "",
            "l": "",
            "c": "",
            "g": "",
            "m": "",
            "o": "",
            "b": "",
            "w": "",
            "f": "",
            "k": "",
            "z": "",
            "p": "",
            "v": "",
            "j": "",
            "y": "",
            "x": "",
            "q": ""
        }
        numbers = {
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "",
            "6": "",
            "7": "",
            "8": "",
            "9": "",
            "0": ""
        }
        special = {
            ".": "",
            ",": "",
            " ": ""
        }

        l = len(letters) + len(numbers) + len(special)
        start = random.randint(0, 16777215 - l * self.space)

        def addChars(chars:dict):
            for n,c in enumerate(chars):
                #encoding[c] = hex(start + n)[2:]
                encoding[c] = hex(start + n*self.space)[2:]
        
        addChars(letters)
        
        start = random.randint(0, 16777215 - l)
        addChars(numbers)
        
        start = random.randint(0, 16777215 - l)
        addChars(special)

        return(encoding)