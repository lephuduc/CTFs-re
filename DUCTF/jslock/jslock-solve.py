

import hashlib
from pwn import *
C = [62, 223, 233, 153, 37, 113, 79, 195, 9, 58, 83, 39, 245, 213, 253, 138, 225, 232, 123, 90, 8, 98, 105, 1, 31, 198, 67, 83, 41, 139, 118, 138, 252, 165, 214, 158, 116, 173, 174, 161, 6, 233, 37, 35, 86, 7, 108, 223, 97, 251, 2, 245, 129, 118, 227, 120, 26, 70, 40, 26, 183, 90, 172, 155]
ls = open('text.txt','rb').read()
print(ls)

hash = hashlib.sha512(ls).digest()
print(xor(C,hash))
