from des import *

khoa = [0x0f, 0x15, 0x71, 0xc9, 0x47, 0xd9, 0xe8, 0x59]
bokhoa = []
taokey(khoa, bokhoa)

for i in range(16):
      print("khoa ", i, ":")
      print("Trai: ", hex(bokhoa[i].left[0]),hex(bokhoa[i].left[1]), hex(bokhoa[i].left[2]), hex(bokhoa[i].left[3]))
      print("Phai: ", hex(bokhoa[i].right[0]),hex(bokhoa[i].right[1]), hex(bokhoa[i].right[2]), hex(bokhoa[i].right[3]))
      print("Khoa con: ", hex(bokhoa[i].keyround[0]), hex(bokhoa[i].keyround[1]), hex(bokhoa[i].keyround[2]),
                              hex(bokhoa[i].keyround[3]), hex(bokhoa[i].keyround[4]), hex(bokhoa[i].keyround[5]))
      print("-------")

