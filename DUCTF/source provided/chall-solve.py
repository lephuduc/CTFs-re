encrypted = [0xc4, 0xda, 0xc5, 0xdb, 0xce, 0x80, 0xf8, 0x3e, 0x82, 0xe8, 0xf7, 0x82, 0xef, 0xc0, 0xf3, 0x86, 0x89, 0xf0, 0xc7, 0xf9, 0xf7, 0x92, 0xca, 0x8c, 0xfb, 0xfc, 0xff, 0x89, 0xff, 0x93, 0xd1, 0xd7, 0x84, 0x80, 0x87, 0x9a, 0x9b, 0xd8, 0x97, 0x89, 0x94, 0xa6, 0x89, 0x9d, 0xdd, 0x94, 0x9a, 0xa7, 0xf3, 0xb2]
text = ""
for e in range(len(encrypted)):
    print(chr((encrypted[e]^0x42)-0x42-e),end = "")
    
