import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES, DES


class AESCipher(object):

    def __init__(self, key):
        self.bs = DES.block_size
        self.key = key #hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(DES.block_size)
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:DES.block_size]
        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        ciphered = cipher.decrypt(enc[DES.block_size:])
        return self._unpad(ciphered)

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        pad_count = ord(s[len(s)-1:])
        if pad_count < 0 or pad_count > self.bs:
            raise Exception
        padding = s[-pad_count:]
        for c in padding:
            if c != pad_count:
                raise Exception

        return s[:-ord(s[len(s)-1:])]
