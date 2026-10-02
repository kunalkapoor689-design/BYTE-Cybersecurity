import re, struct, zlib
d = open('fixed.png','rb').read()
marks = [m.start() for m in re.finditer(rb'IDAT|IEND', d)]
for i, a in enumerate(marks):
    field = struct.unpack('>I', d[a-4:a])[0]
    line = f'{a-4:#x} {d[a:a+4].decode()} len_field={field}'
    if i + 1 < len(marks):
        real = marks[i+1] - a - 12          # distance to next type field, minus len/type/crc overhead
        stored = struct.unpack('>I', d[a+4+real:a+8+real])[0]
        ok = zlib.crc32(d[a:a+4+real]) == stored
        line += f' real_len={real} crc_over_real_span={"ok" if ok else "BAD"}'
    print(line)
print('bytes at expected 4th header:', d[0x30045:0x30051].hex(' '))
