from hashlib import sha1, sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad

digest_full = sha1(bytearray([30, 2, 120])).digest()
digest = digest_full[0:16]
cipherText = bytearray([64, 118, 165, 90, 7, 239, 142, 118, 207, 31, 216, 186, 240, 42, 188, 127, 34, 190, 182, 154, 122, 125, 237, 33, 69, 71, 112, 250, 36, 19, 166, 118])
cipher = AES.new(digest, AES.MODE_ECB)
text = cipher.decrypt(cipherText)[0:16]
print(text.decode("utf-8"))
