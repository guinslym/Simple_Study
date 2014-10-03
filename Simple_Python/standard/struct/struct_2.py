import struct
import binascii

s=struct.Struct("I 2s f")
packed_data=binascii.unhexlify("0100000061620000cdcc2c40")
unpacked_data=s.unpack(packed_data)
print "Unacked Value   :",unpacked_data