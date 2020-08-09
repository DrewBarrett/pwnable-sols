from pwn import *
print(p32(0x21DD09EC))
x = 0x21dd09ec//5
y = x+4
print(x)
z = ((p32(x)*4) + p32(y))
p = process(['/home/col/col', z])
p.interactive()
