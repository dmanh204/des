from des import *
# Tao key
khoa = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
bokhoa = []
taokey(khoa, bokhoa)

with open("ecb_ciphertext.txt", "r", encoding="utf=8") as doc, open("ecb_decrypted.txt", "w", encoding="utf-8") as kq:
    a = 0
    block =[]
    while True:
        byte = doc.read(1)      # doc tung byte cua file
        if byte == "":          # neu doc duoc end of file thi break
            break
        byte = ord(byte)        # doi char thanh int
        block.append(byte)      # them gia tri vao list block
        a += 1                  # tang bien dem them 1
        if a == 8:
            ketqua = decrypt_des(block, bokhoa)
            for i in range(8):
                kq.write(chr(ketqua[i]))
            block.clear()
            a = 0