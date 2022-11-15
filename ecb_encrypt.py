
from des import *
# Tao key
khoa = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
bokhoa = []
taokey(khoa, bokhoa)

with open("ecb_plaintext.txt", "r",encoding="UTF-8") as doc, open("ecb_ciphertext.txt", "w",encoding="UTF-8") as kq:  # chon encoding la utf-8
    a = 0
    block = []
    while True:
        byte = doc.read(1)      # doc 1 byte tu file
        if byte == "":          # neu doc duoc end of file thi break
            break
        byte = ord(byte)            # Doi str thanh int
        '''if (64< byte < 91) | (96< byte < 123):     # Neu la chu cai alphabet thi them vao ma tran
            block.append(byte)
            a += 1'''
        block.append(byte)
        a += 1
        if a == 8:                                  # neu block da du 8byte = 64 bit, tien hanh ma hoa
            ketqua = encrypt_des(block, bokhoa)     # Tien hanh encrypt
            
            for i in range(8):                      # viet tung byte cua list ketqua vao file
                kq.write(chr(ketqua[i]))
            block.clear()                           # reset lai gia tri cua block va a
            a = 0
    if (a != 0):                                    # padding
        for i in range(8-a):
            block.append(0)
        ketqua = encrypt_des(block, bokhoa)
        for i in range(8):
            kq.write(chr(ketqua[i]))
    block.clear()
    a = 0