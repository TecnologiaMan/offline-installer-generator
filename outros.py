import os
from colorama import Fore
def hex2bin(c):
	if '0' <= c <= '9':
		return ord(c) - ord('0')
	if 'a' <= c <= 'f':
		return ord(c) - ord('a') + 10
	if 'A' <= c <= 'F':
		return ord(c) - ord('A') + 10
	return -1

def hexstr2binstr(hexstr):
	len_hexstr = len(hexstr)
	binstr = bytearray(len_hexstr // 2)
	for i in range(0, len_hexstr, 2):
		binstr[i//2] = hex2bin(hexstr[i]) * 16 + hex2bin(hexstr[i+1])
	return bytes(binstr)

def leitor():
	print()
	
def stringinstall():
	caminho_atual = os.getcwd()

	nome = str(input("[nome]# "))

	concatenado = caminho_atual + f"/{nome}"

	hex_input = str(input("[hex]# "))
	if os.path.isfile(hex_input):
		with open(hex_input, "r") as fileHEX:
			ler = fileHEX.read()
			bin1 = hexstr2binstr(ler)
			with open(nome, "wb") as file:
				file.write(bin1)

			print(f"{Fore.GREEN}Concluido..{Fore.RESET} arquivo localizado em {Fore.RED}{concatenado}{Fore.RESET}")
	else:
		bin1 = hexstr2binstr(hex_input);
		with open(nome, "wb") as file:
			file.write(bin1)
		
		print(f"{Fore.GREEN}Concluido..{Fore.RESET} arquivo localizado em {Fore.RED}{concatenado}{Fore.RESET}")





	