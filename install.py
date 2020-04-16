import os, time, sys


os.system("clear")
print("--------------------")
print("|      Choose      |")
print("|------------------|")
print("| 1. Termux        |")
print("| 2. Unix          |")
print("|                  |")
print("| Choose 1 or 2:   |")
print("--------------------")
numb = int(input("\n"))
if numb == 1:
	os.system("pkg install python")
	os.system("pkg install python3")
	os.system("pkg install python3-pip")
	os.system("pkg install dos2unix")
	os.system("pip3 install requests")
	os.system("pip install sockets")
	os.system("pip3 install colorama")
	os.system("pip install PySocks")
	print("Install complead")
elif numb == 2:
	if os.system(whoami) != 'root':
		print("Run install.py whis root (sudo bash install.sh)")
		sys.exit()
	else:
		os.system("apt install python3 python3-pip dos2unix")
		os.system("pip3 install requests")
		os.system("pip3 install sockets")
		os.system("pip3 install colorama")
		os.system("pip install PySocks")
		os.system("DEAThor")
		
else:
	print("False!")
