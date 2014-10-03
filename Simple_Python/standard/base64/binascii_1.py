import binascii

data="hello world"
print binascii.crc32(data)
print binascii.b2a_hex(data)
print binascii.hexlify(data)
