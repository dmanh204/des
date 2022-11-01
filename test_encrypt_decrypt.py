from des import *

khoa = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
bokhoa = []
taokey(khoa, bokhoa)
plaintext = [0x02, 0x46, 0x8a, 0xce, 0xec, 0xa8, 0x64, 0x20]
bomahoa = []
bogiaima = []
ciphertext = encrypt(plaintext, bomahoa, bokhoa)

for i in range (17):
    print("Text ", i, ":")
    print("Trai: ", hex(bomahoa[i].left[0]), hex(bomahoa[i].left[1]), hex(bomahoa[i].left[2]), hex(bomahoa[i].left[3]))
    print("Phai: ", hex(bomahoa[i].right[0]), hex(bomahoa[i].right[1]), hex(bomahoa[i].right[2]), hex(bomahoa[i].right[3]))
    print("------")

print("Ciphertext: ", hex(ciphertext[0]), hex(ciphertext[1]), hex(ciphertext[2]), hex(ciphertext[3]),
                        hex(ciphertext[4]), hex(ciphertext[5]), hex(ciphertext[6]), hex(ciphertext[7]))

print("------")
giaima = decrypt(ciphertext, bogiaima, bokhoa)
for i in range (17):
    print("Text ", i, ":")
    print("Trai: ", hex(bogiaima[i].left[0]), hex(bogiaima[i].left[1]), hex(bogiaima[i].left[2]), hex(bogiaima[i].left[3]))
    print("Phai: ", hex(bogiaima[i].right[0]), hex(bogiaima[i].right[1]), hex(bogiaima[i].right[2]), hex(bogiaima[i].right[3]))
    print("------")
print("Text: ", hex(giaima[0]), hex(giaima[1]), hex(giaima[2]), hex(giaima[3]),
                    hex(giaima[4]), hex(giaima[5]), hex(giaima[6]), hex(giaima[7]))
