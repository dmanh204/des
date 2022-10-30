from des import *
def encrypt(plaintext, botext, bokey):
    sauhoanvi = hoanvi(plaintext, initial_permutation)

    left = [0,0,0,0]
    right = [0,0,0,0]
    tach64(sauhoanvi, left, right)
    trai = left.copy()              # copy list left
    phai = right.copy()             # copy list right
    botext.append(text(trai,phai))  # tao object text luu 2 list, object la 1 gia tri cua list botext
    
    for i in range (16):
        temp48 = hoanvi(right, expansion_permutation)   # hoan vi mo rong 32->48
        
        for j in range(6):
            temp48[j] = temp48[j] ^ bokey[i].keyround[j] # XOR voi khoa con
        
        quatrinhsbox(temp48)        # xu li Sbox
        temp48 = hoanvi(temp48, permutation_function)   # hoan vi
        for j in range(4):
            temp48[j] = temp48[j] ^ left[j]    # XOR 32 bit cua temp48 voi left
        
        left = right.copy()        # doi vi tri
        right = temp48.copy()

        trai = left.copy()
        phai = right.copy()
        botext.append(text(trai, phai))
    # final swap
    temp = left.copy()
    left = right.copy()
    right = temp.copy()
    preoutput = [0,0,0,0,0,0,0,0]
    for i in range(4):
        preoutput[i] = left[i]
        preoutput[i+4] = right[i]
    ketqua = hoanvi(preoutput, inverse_initial_permutation)
    return ketqua

def decrypt(ciphertext, botext, bokey):
    sauhoanvi = hoanvi(ciphertext, initial_permutation)
    left = [0,0,0,0]
    right = [0,0,0,0]
    tach64(sauhoanvi, left, right)
    trai = left.copy()              # copy list left
    phai = right.copy()             # copy list right
    botext.append(text(trai,phai))  # tao object text luu 2 list, object la 1 gia tri cua list botext
    for i in range (15, -1, -1):
        temp48 = hoanvi(right, expansion_permutation)   # hoan vi mo rong 32->48
        for j in range(6):
            temp48[j] = temp48[j] ^ bokey[i].keyround[j] # XOR voi khoa con
        quatrinhsbox(temp48)        # xu li Sbox
        temp48 = hoanvi(temp48, permutation_function)
        for j in range(4):
            temp48[j] = temp48[j] ^ left[j]    # XOR 32 bit dau cua temp48 voi left
        left = right.copy()        # doi vi tri 
        right = temp48.copy()

        trai = left.copy()
        phai = right.copy()
        botext.append(text(trai, phai))
    # final swap
    temp = left.copy()
    left = right.copy()
    right = temp.copy()
    preoutput = [0,0,0,0,0,0,0,0]
    for i in range(4):
        preoutput[i] = left[i]
        preoutput[i+4] = right[i]
    ketqua = hoanvi(preoutput, inverse_initial_permutation)
    return ketqua

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
