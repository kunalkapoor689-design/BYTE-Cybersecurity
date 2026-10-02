import struct, zlib
b = bytearray(open('fixed2.png','rb').read())

b[0x14:0x18] = struct.pack('>I', 850)                    # new height
b[0x1d:0x21] = struct.pack('>I', zlib.crc32(bytes(b[0x0c:0x1d])))  # new CRC

open('fixed3.png','wb').write(b)
