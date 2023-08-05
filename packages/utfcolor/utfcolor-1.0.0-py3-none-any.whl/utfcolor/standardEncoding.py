from utfcolor import utfcolorv1

class StandardEncoding(utfcolorv1.UtfColor):
    def __init__(self, encoding:str="utf-8"):
        self.encoding = encoding

    def encode(self, txt:str)->str:
        '''encodes text'''
        txt = txt.encode(self.encoding)
        return(txt.hex())

    def prepareText(self, txt:str)->str:
        '''NOOP (no text preparation for standard encodings)'''
        return(txt)