import struct, zlib
d = open('fixed2.png','rb').read()

pos, idat = 8, b''
while pos + 12 <= len(d):
    ln, t = struct.unpack('>I4s', d[pos:pos+8])
    if t == b'IDAT': idat += d[pos+8:pos+8+ln]
    pos += 12 + ln
    if t == b'IEND': break

raw = zlib.decompress(idat)
width = 724
row = 1 + width * 3            # 1 filter byte + 3 bytes per RGB pixel
print(len(raw), len(raw) / row)   # 1847050 -> 850.0
