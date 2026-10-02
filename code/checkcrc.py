import struct, zlib

d = open('fixed.png','rb').read()
pos, idats = 8, []
while pos + 12 <= len(d):
    ln, t = struct.unpack('>I4s', d[pos:pos+8])
    data = d[pos+8:pos+8+ln]
    crc = struct.unpack('>I', d[pos+8+ln:pos+12+ln])[0]
    ok = zlib.crc32(t + data) == crc
    print(f'{pos:#x} {t!r} len={ln} crc={"ok" if ok else "BAD"}')
    if t == b'IDAT': idats.append(data)
    pos += 12 + ln
    if t == b'IEND': break
print('trailing bytes:', len(d) - pos)

stream = b''.join(idats)
S = 724*3 + 1                      # bytes per row incl. filter byte
o = zlib.decompressobj()
out, outlen_at = bytearray(), []
for i, b in enumerate(stream):
    try:
        out += o.decompress(bytes([b]))
    except zlib.error as e:
        print('zlib error at stream byte', i, '(IDAT #%d)' % (i // 65536 + 1), e)
        break
    outlen_at.append(len(out))

rows = len(out) // S
bad = next((r for r in range(rows) if out[r*S] > 4), None)
print('rows decoded:', rows, '| first row with invalid filter byte:', bad)
if bad is not None:
    s = next(i for i, n in enumerate(outlen_at) if n >= bad*S)
    print('damage is at or shortly before stream byte', s)

    def chunk(t, x):
        return struct.pack('>I', len(x)) + t + x + struct.pack('>I', zlib.crc32(t + x))
    hdr = struct.pack('>IIBBBBB', 724, bad, 8, 2, 0, 0, 0)
    open('partial.png', 'wb').write(
        b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', hdr)
        + chunk(b'IDAT', zlib.compress(bytes(out[:bad*S]))) + chunk(b'IEND', b''))
