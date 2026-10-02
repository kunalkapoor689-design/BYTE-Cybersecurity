import struct, zlib
d = open('fixed.png','rb').read()
i = 0x21c89
print(d[i:i+12].hex(' '))        # expect 00 00 00 00 49 45 4e 44 ae 42 60 82
b = d[:i] + d[i+12:]

ln  = struct.unpack('>I', b[0x20039:0x2003d])[0]
crc = struct.unpack('>I', b[0x2003d+4+ln:0x2003d+8+ln])[0]
print('IDAT#3 len', ln, 'crc', 'ok' if zlib.crc32(b[0x2003d:0x2003d+4+ln]) == crc else 'BAD')

open('fixed2.png','wb').write(b)
