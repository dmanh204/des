initial_permutation =   [58, 50, 42, 34, 26, 18, 10, 2,
                         60, 52, 44, 36, 28, 20, 12, 4,
                         62, 54, 46, 38, 30, 22, 14, 6,
                         64, 56, 48, 40, 32, 24, 16, 8,
                         57, 49, 41, 33, 25, 17,  9, 1,
                         59, 51, 43, 35, 27, 19, 11, 3,
                         61, 53, 45, 37, 29, 21, 13, 5,
                         63, 55, 47, 39, 31, 23, 15, 7]
inverse_initial_permutation =   [40, 8, 48, 16, 56, 24, 64, 32,
                                 39, 7, 47, 15, 55, 23, 63, 31,
                                 38, 6, 46, 14, 54, 22, 62, 30,
                                 37, 5, 45, 13, 53, 21, 61, 29,
                                 36, 4, 44, 12, 52, 20, 60, 28,
                                 35, 3, 43, 11, 51, 19, 59, 27,
                                 34, 2, 42, 10, 50, 18, 58, 26,
                                 33, 1, 41,  9, 49, 17, 57, 25]
expansion_permutation = [32,  1,  2,  3,  4,  5,
                          4,  5,  6,  7,  8,  9,
                          8,  9, 10, 11, 12, 13,
                         12, 13, 14, 15, 16, 17,
                         16, 17, 18, 19, 20, 21,
                         20, 21, 22, 23, 24, 25,
                         24, 25, 26, 27, 28, 29,
                         28, 29, 30, 31, 32,  1]
permutation_function =  [16,  7, 20, 21, 29, 12, 28, 17,
                          1, 15, 23, 26,  5, 18, 31, 10,
                          2,  8, 24, 14, 32, 27,  3,  9,
                         19, 13, 30,  6, 22, 11,  4, 25]
S1 = [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7,
       0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8,
       4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0,
      15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]

S2 = [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10,
       3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5,
       0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15,
      13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]

S3 = [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8,
      13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1,
      13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7,
       1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]

S4 = [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15,
      13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9,
      10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4,
       3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]

S5 = [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9,
      14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6,
       4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14,
      11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]

S6 = [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11,
      10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8,
       9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6,
       4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]

S7 = [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1,
      13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6,
       1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2,
       6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]

S8 = [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7,
       1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2,
       7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8,
       2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]

input_key = [  1,  2,  3,  4,  5,  6,  7,
               9, 10, 11, 12, 13, 14, 15,
              17, 18, 19, 20, 21, 22, 23,
              25, 26, 27, 28, 29, 30, 31,
              33, 34, 35, 36, 37, 38, 39,
              41, 42, 43, 44, 45, 46, 47,
              49, 50, 51, 52, 53, 54, 55,
              57, 58, 59, 60, 61, 62, 63]

permuted_choice_one =   [57, 49, 41, 33, 25, 17,  9,
                          1, 58, 50, 42, 34, 26, 18,
                         10,  2, 59, 51, 43, 35, 27,
                         19, 11,  3, 60, 52, 44, 36,
                         63, 55, 47, 39, 31, 23, 15,
                          7, 62, 54, 46, 38, 30, 22,
                         14,  6, 61, 53, 45, 37, 29,
                         21, 13,  5, 28, 20, 12,  4]

permuted_choice_two =   [14, 17, 11, 24,  1,  5,  3, 28,
                         15,  6, 21, 10, 23, 19, 12,  4,
                         26,  8, 16,  7, 27, 20, 13,  2,
                         41, 52, 31, 37, 47, 55, 30, 40,
                         51, 45, 33, 48, 44, 49, 39, 56,
                         34, 53, 46, 42, 50, 36, 29, 32]

schedule_of_left_shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

class key:
      def __init__(self, left, right):
            self.left = left
            self.right = right

class text:
      def __init__(self, left, right):
            self.left = left
            self.right = right

def hoanvi(dauvao, matran):
      ketqua =[]
      for i in range(len(matran)):
            if (i % 8 )== 0:        # neu chia het cho 8 tuc la bat dau 1 so 8 bit moi
                  ketqua.append(0x00)     # khoi tao so 8 bit de chua ket qua
            a = matran[i] - 1       # a luu gia tri cua phan tu trong ma tran hoan vi
            nhanbit = 0x80 >> (a%8) # tao gia tri de don bit
            nhanbit = nhanbit & (dauvao[a//8])
            if ((i%8) - (a%8)) > 0:
                  nhanbit = nhanbit >> ((i%8) - (a%8))    # dua bit ve vi tri sau hoan vi
            elif ((i%8) - (a%8)) < 0:
                  nhanbit = nhanbit << ((a%8) - (i%8))
            ketqua[i//8] = ketqua[i//8] | nhanbit       # day bit vao ket qua
      return ketqua
# truoc moi lan dung, nho khoi tao gia tri cho left va right

def tach64(giatri, left, right):
      for i in range(4):
            left[i] = giatri[i]
            right[i] = giatri[i+4]

def tach56(giatri, left, right):
    # tao list trai
      for i in range(3):
            left[i] = giatri[i] # 3 byte dau

      temp = 0xf0 # 11110000
      temp = temp & giatri[3]
      left[3] = temp
    # tao list phai
      for i in range(3):
        # nua dau
            temp = 0x0f
            temp = temp & giatri[i+3]
            temp = temp << 4
            right[i] = right[i] | temp
        # nua sau
            temp = 0xf0
            temp = temp & giatri[i+4]
            temp = temp >> 4
            right[i] = right[i] | temp  # 3byte dau
      temp = 0x0f
      temp = temp & giatri [6]
      temp = temp << 4
      right[3] = temp            

def ghep56(giatri, left, right):
      for i in range(4):
            giatri[i] = left[i]
      for i in range(3):
            temp = 0xf0
            temp = temp & right[i]
            temp = temp >> 4
            giatri[i+3] = giatri[i+3] & 0xf0
            giatri[i+3] = giatri[i+3] | temp
            temp = 0x0f
            temp = temp & right[i]
            temp = temp << 4
            giatri[i+4] = giatri[i+4] & 0x0f
            giatri[i+4] = giatri[i+4] | temp
      giatri[6] = giatri[6] & 0xf0
      giatri[6] = giatri[6] | ((0xf0 & right[3]) >> 4) 

# ham dich vong key
def dichvong(giatrikey, giatridichvong):
      if giatridichvong == 1:
            bitdau = 0x80 & giatrikey[0]
            for i in range(3):      # dich trai 3 byte dau
                  giatrikey[i] = (giatrikey[i] << 1) & 0xff
                  bit = 0x80 & giatrikey[i+1]
                  bit = bit >> 7
                  giatrikey[i] = giatrikey[i] | bit
        # dich trai nua byte sau
            giatrikey[3] = (giatrikey[3] << 1) & 0xff
            bitdau = bitdau >> 3
            giatrikey[3] = giatrikey[3] | bitdau
      if giatridichvong == 2:
            bitdau = 0xC0 & giatrikey[0]
            for i in range(3):
                  giatrikey[i] = (giatrikey[i] << 2) & 0xff
                  bit = 0xC0 & giatrikey[i+1]
                  bit = bit >> 6
                  giatrikey[i] = giatrikey[i] | bit
        
            giatrikey[3] = (giatrikey[3] << 2) & 0xff
            bitdau = bitdau >> 2
            giatrikey[3] = giatrikey[3] | bitdau

def xulisbox(dauvao, sbox):
      hang = (dauvao & 0x20) >> 4
      hang = hang | (dauvao & 0x01)
    
      cot = (dauvao & 0x1e) >> 1
      ketqua = sbox[hang*16 + cot]
      return ketqua
def quatrinhsbox(text):
      # S1
      dauvao = (text[0] & 0xfc) >> 2
      ketqua = xulisbox(dauvao, S1)
      text[0] = text[0] & 0x0f    # xoa 4 bit dau de chua ket qua
      ketqua = ketqua << 4
      text[0] = text[0] | ketqua

      # S2
      dauvao = (text[0] & 0x03) << 4
      dauvao = dauvao | ((text[1] & 0xf0) >> 4)
      ketqua = xulisbox(dauvao, S2)
      text[0] = text[0] & 0xf0    # xoa 4 bit sau de chua ket qua
      text[0] = text[0] | ketqua

      # S3
      dauvao = (text[1] & 0x0f) << 2
      dauvao = dauvao | ((text[2] & 0xc0) >> 6)
      ketqua = xulisbox(dauvao, S3)
      text[1] = text[1] & 0x0f    # xoa 4 bit dau de chua ket qua
      ketqua = ketqua << 4
      text[1] = text[1] | ketqua

      # S4
      dauvao = text[2] & 0x3f
      ketqua = xulisbox(dauvao, S4)
      text[1] = text[1] & 0xf0    # xoa 4 bit sau de chua ket qua
      text[1] = text[1] | ketqua

      # S5
      dauvao = (text[3] & 0xfc) >> 2
      ketqua = xulisbox(dauvao, S5)
      text[2] = text[2] & 0x0f    # xoa 4 bit dau de chua ket qua
      ketqua = ketqua << 4
      text[2] = text[2] | ketqua

      # S6
      dauvao = (text[3] & 0x03) << 4
      dauvao = dauvao | ((text[4] & 0xf0) >> 4)
      ketqua = xulisbox(dauvao, S6)
      text[2] = text[2] & 0xf0    # xoa 4 bit sau de chua ket qua
      text[2] = text[2] | ketqua

      # S7
      dauvao = (text[4] & 0x0f) << 2
      dauvao = dauvao | ((text[5] & 0xc0) >> 6)
      ketqua = xulisbox(dauvao, S7)
      text[3] = text[3] & 0x0f    # xoa 4 bit dau de chua ket qua
      ketqua = ketqua << 4
      text[3] = text[3] | ketqua

      # S8
      dauvao = text[5] & 0x3f
      ketqua = xulisbox(dauvao, S8)
      text[3] = text[3] & 0xf0    # xoa 4 bit sau de chua ket qua
      text[3] = text[3] | ketqua

def taokey(khoa, bokhoa):
      hoanvibandau = hoanvi(khoa, permuted_choice_one)
      left = [0,0,0,0]
      right = [0,0,0,0]
      giatrighep = [0,0,0,0,0,0,0]
      tach56(hoanvibandau, left, right)
      for i in range(16):
            dichvong(left, schedule_of_left_shift[i])
            dichvong(right, schedule_of_left_shift[i])
            trai = left.copy()
            phai = right.copy()
            khoacon = key(trai, phai)
            bokhoa.append(khoacon)
            ghep56(giatrighep, trai, phai)
            bokhoa[i].keyround = hoanvi(giatrighep, permuted_choice_two)

def encrypt_des(plaintext, bokey):
    sauhoanvi = hoanvi(plaintext, initial_permutation)

    left = [0,0,0,0]
    right = [0,0,0,0]
    tach64(sauhoanvi, left, right)
    
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

def decrypt_des(ciphertext, bokey):
    sauhoanvi = hoanvi(ciphertext, initial_permutation)
    left = [0,0,0,0]
    right = [0,0,0,0]
    tach64(sauhoanvi, left, right)
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
