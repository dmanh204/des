from des import *
# Doc gia tri key tu file
with open("cbc_key.txt", "r") as k:

    key = int(k.read(), 16)
    keyblock = []
    for i in range(8):
        a = 0xff << (7-i)*8
        a = a & key
        a = a >> (7-i)*8
        keyblock.append(a)
# Doc gia tri initial tu file
with open("cbc_initial.txt", "r") as initial:
    initial_value = int(initial.read(), 16)
    initial_block = []
    for i in range(8):
        a = 0xff << (7-i)*8
        a = a & key
        a = a >> (7-i)*8
        initial_block.append(a)
# Tao bo key
bokhoa = []
taokey(keyblock, bokhoa)
# Tien hanh giai ma
with open("cbc_ciphertext.txt", "r",encoding="UTF-8") as doc, open("cbc_decrypted.txt", "w",encoding="UTF-8") as kq:  # chon encoding la utf-8
    a = 0
    block = []
    sub_block = initial_block.copy()
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
            # Tien hanh decrypt
            ketqua = decrypt_des(block, bokhoa)
            # Tien hanh xor ket qua voi gia tri phu
            for i in range(8):
                ketqua[i] = ketqua[i] ^ sub_block[i]  # xor khoi text voi gia tri cipher truoc do  
            # Sau khi su dung sub_block, thay gia tri moi cho sub_block                           
            sub_block = block.copy()    
            for i in range(8):                      # viet tung byte cua list ketqua vao file
                kq.write(chr(ketqua[i]))
            block.clear()                           # reset lai gia tri cua block va a
            a = 0
            

    if (a != 0):                                    # padding
        for i in range(8-a):
            block.append(0)
        # Tien hanh decrypt khoi cuoi
        ketqua = encrypt_des(block, bokhoa)
        # Tien hanh xor ket qua voi gia tri phu
        for i in range(8):
                ketqua[i] = ketqua[i] ^ sub_block[i]
        
        for i in range(8):
            kq.write(chr(ketqua[i]))
    block.clear()
    a = 0