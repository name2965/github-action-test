import sys
mz = [0x4D, 0x5A, 0x90, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0xFF, 0xFF,0x00,0x00]
enc = [0xDE, 0xC0, 0x1B, 0x8C, 0x8C, 0x93, 0x9E, 0x86, 0x98, 0x97, 0x9A, 0x8C, 0x73, 0x6C,0x9a,0x8b]
res = ''

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()
res_path = 'result'+sys.argv[1]+'.txt'

for i in range(len(mz)):
    res += chr(mz[i] ^ enc[i] ^ 0xff)

print(res)

with open(res_path,'w') as f:
    f.write(res)
