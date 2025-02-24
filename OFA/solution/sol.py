#!/usr/bin/python3

from Crypto.Util.number import * 
import random
import time 
from pwn import * 


def init(i):
    random.seed(i)




seed_asm = int(time.time())

io = remote('ofa.ctf.ingeniums.club' , 1337 , ssl=True)

io.sendlineafter(b'>' , b'2')

flag = io.recvline().decode().strip()



for i in range(-40 , 40):
    print(i)
    io.sendlineafter(b'>' , b'1')
    init(seed_asm + i )
    nonce = long_to_bytes(random.getrandbits(8*8)).hex()
    io.sendlineafter(b'plaintext(hex) : ' , flag.encode() )
    io.sendlineafter(b'nonce(hex) :' , nonce.encode() )
    out = bytes.fromhex(io.recvline().decode().strip())
    if b'ingehack' in out : 
        print((i , out))
        break 



io.interactive()