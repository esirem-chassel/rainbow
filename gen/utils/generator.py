
import hashlib
import random
import string


class Generator():
    CHARS_ASCII = 'abcdefghijklmnopqrstuvwxyz'
    CHARS_SYMBOLS = '-_=+*%!:/;.,?<>&#@([])$µ§²'
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.src = None
    def getSrc(self):
        return self.src
    def setSrc(self, src):
        self.src = src
    def generateSrc(self):
        self.src = ''.join(random.choices(string.ascii_letters+string.digits, k=self.maxlen))
        return self.src
    def generateTrg(self, algo, salt=''):
        if self.src != None:
            h = hashlib.new(algo)
            h.update((salt+self.src).encode())
            return h.hexdigest()
        else:
            return None
