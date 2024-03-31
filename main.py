from colorama import Fore
import os
import time
import sys
import outros

#Criado por TecnologiaMan
VERSION = 0.0
title = """
  _____ ___   ___  _    
 |_   _/ _ \ / _ \| |   
   | || (_) | (_) | |__ 
   |_| \___/ \___/|____|
"""

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

def compilar(executar, caminho, program2, nome, program3):
    if executar == 0:
        #perguntando qual sistema o arquivo deve ser compilado
        winorlinux = str(input("[windows ou linux]# "))

        print("Criando arquivo de execução apos instalação..")
        #criando arquivo
        with open("program.c", "wb") as file:
            bin1 = hexstr2binstr(program2)
            file.write(bin1)
        #lendo
        with open("program.c", "r") as file:
            programa = file.read()
            if 'snprintf(buffer, sizeof(buffer), "")' in programa:
                
                with open("program.c", "w") as file:
                    
                    if winorlinux.lower() == "linux":
                        content = programa.replace('snprintf(buffer, sizeof(buffer), "")', f'snprintf(buffer, sizeof(buffer), "{caminho}")')
                        file.write(content)
                        print(f"{Fore.RED}Coloque a senha de usuario{Fore.RESET}")
                        os.system("echo gcc program.c install.h -o mainINSTALL > compilar.sh && chmod +x compilar.sh");
                        print(f"{Fore.YELLOW}por esse script estar na versão {VERSION} voce tera que dar ./compile.sh manualmente pelo terminal{Fore.RESET}")
                    else:
                        content = programa.replace('snprintf(buffer, sizeof(buffer), "")', f'snprintf(buffer, sizeof(buffer), "start {caminho}")')
                        content2 = content.replace('int main(void)', f'int WinMain(void)')
                        file.write(content)
                        print(f"{Fore.RED}Coloque a senha de usuario{Fore.RESET}")
                        os.system("echo 'x86_64-w64-mingw32-gcc program.c install.h -o InstallMAIN -mwindows && rm install.h && rm program.c && rm compilar.sh' > compilar.sh && chmod +x compilar.sh && ./compilar.sh")
                        print(f"{Fore.YELLOW}por esse script estar na versão {VERSION} voce tera que dar ./compile.sh manualmente pelo terminal{Fore.RESET}")

    else:
        winorlinux = str(input("[windows ou linux]# "))

        print("Criando arquivo de so instalar")
        #criando arquivo
        with open("program.c", "wb") as file:

            bin1 = hexstr2binstr(program3)
            file.write(bin1)
                #lendo
            with open("program.c", "r") as file:

                with open("program.c", "w") as file:  
                    if winorlinux.lower() == "linux":
                                #content = programa.replace('snprintf(buffer, sizeof(buffer), "")', f'snprintf(buffer, sizeof(buffer), "{caminho}")')
                                #file.write(content)
                                #print(f"{Fore.RED}Coloque a senha de usuario{Fore.RESET}")
                        os.system("echo 'gcc program.c install.h -o mainINSTALL && rm install.h && rm program.c && rm compilar.sh' > compilar.sh && chmod +x compilar.sh");
                        print(f"{Fore.YELLOW}por esse script estar na versão {VERSION} voce tera que dar ./compile.sh manualmente pelo terminal{Fore.RESET}")
                    else:
                                #content = programa.replace('snprintf(buffer, sizeof(buffer), "")', f'snprintf(buffer, sizeof(buffer), "start {caminho}")')
                                #content2 = content.replace('int main(void)', f'int WinMain(void)')
                                #file.write(content)
                                #print(f"{Fore.RED}Coloque a senha de usuario{Fore.RESET}")
                        os.system("echo 'x86_64-w64-mingw32-gcc program.c install.h -o InstallMAIN -mwindows && rm install.h && rm program.c && rm compilar.sh' > compilar.sh && chmod +x compilar.sh && ./compilar.sh")
                        print(f"{Fore.YELLOW}por esse script estar na versão {VERSION} voce tera que dar ./compile.sh manualmente pelo terminal{Fore.RESET}")



        


def install():
    #script.c
    program1 = "23696e636c756465203c737464696f2e683e0a23696e636c756465203c7374646c69622e683e0a0a2369666e6465662046494c45535f480a23646566696e652046494c45535f480a0a696e74206865783262696e28636861722063297b0a202020206966202863203e3d202730272026262063203c3d20273927290a202020202020202072657475726e2063202d202730273b0a202020206966202863203e3d202761272026262063203c3d20276627290a202020202020202072657475726e2063202d20276127202b2031303b0a202020206966202863203e3d202741272026262063203c3d20274627290a202020202020202072657475726e2063202d20274127202b2031303b0a2020202072657475726e202d313b0a7d0a0a766f6964206865787374723262696e73747228636f6e737420636861722a206865787374722c20756e7369676e656420636861722a2062696e7374722c20696e74206c656e297b0a20202020666f7228696e742069203d20303b2069203c206c656e3b2069202b3d2032297b0a202020202020202062696e7374725b692f325d203d206865783262696e286865787374725b695d29202a203136202b206865783262696e286865787374725b692b315d293b0a202020207d0a7d0a0a696e7420696e7374616c6c28696e742069297b0a0963686172206275666665725b313032345d3b0a09736e7072696e7466286275666665722c2073697a656f6628627566666572292c202222293b0a0946494c45202a6f70656e203d20666f70656e286275666665722c2022776222293b0a0969662869203d3d2031297b0a090963686172206865785b5d203d2022223b0a0909696e74206c656e203d2073697a656f662868657829202d20313b0a0909756e7369676e656420636861722062696e5b6c656e2f325d3b0a09096865787374723262696e737472286865782c2062696e2c206c656e293b0a09096677726974652862696e2c20312c2073697a656f662862696e292c206f70656e293b0a20202020202020200966636c6f7365286f70656e293b0a097d656c73652069662869203d3d2032297b0a09096368617220686578325b5d203d2022223b0a0909696e74206c656e203d2073697a656f66286865783229202d20313b0a0909756e7369676e656420636861722062696e5b6c656e2f325d3b0a09096865787374723262696e73747228686578322c2062696e2c206c656e293b0a09096677726974652862696e2c20312c2073697a656f662862696e292c206f70656e293b0a20202020202020200966636c6f7365286f70656e293b0a097d0a7d0a0a0a23656e6469660a"
    program2 = "23696e636c756465203c737464696f2e683e0a23696e636c756465203c7374646c69622e683e0a23696e636c7564652022696e7374616c6c2e68220a0a696e74206d61696e28766f6964297b0a0963686172206275666665725b313032345d3b0a090a09736e7072696e7466286275666665722c2073697a656f6628627566666572292c202222293b090a0a09696e7374616c6c2831293b0a090a0946494c45202a6f70656e203d20666f70656e286275666665722c20227222293b0a0a096966286f70656e203d3d204e554c4c297b0a090972657475726e20313b0a097d656c73657b0a090966636c6f7365286f70656e293b0a090969662873797374656d2862756666657229203d3d2030297b0a0909090a09097d090a097d0a090a7d0a0a"
    program3 = "23696e636c756465203c737464696f2e683e0a23696e636c7564652022696e7374616c6c2e68220a0a0a0a696e74206d61696e28766f6964297b0a09696e7374616c6c2831293b0a7d0a"
    #script.c
    
    choice2 = str(input("[file]# "))
    if os.path.exists(choice2):
        print(f"Lendo os bytes do arquivo: {choice2}...")
        #implementando leitor.c aqui
        with open(choice2, "rb") as file:
            dados_bytes = file.read()
            dados_hexadecimais = ''.join(["%02x" % byte for byte in dados_bytes])	
		
            with open("output.txt", "w") as output:
                #salvando os bytes num .txt
                output.write(dados_hexadecimais)


    #criando o arquivo FILES.H
        print(f"Instalado o install.h em {os.getcwd()}")

        with open("install.h", "wb") as filetwo:
            len_hex = len(program1)
            bin1 = hexstr2binstr(program1)
            filetwo.write(bin1)
        #ler o arquivo e procurar o char hex[] = ""
        with open("install.h", "r") as filethree:
            gozar = filethree.read()
            if 'char hex[] = ""' in gozar:
                choice3 = int(input("[executar apos 1- instalação ou 2- não executar?]# "))
                if choice3 == 1:
                    content = gozar.replace('char hex[] = ""', f'char hex[] = "{dados_hexadecimais}"')
                    executar = 0
                elif choice3 == 2:
                    content = gozar.replace('char hex[] = ""', f'char hex[] = "{dados_hexadecimais}"')
                    executar = 1

                choice4 = str(input("[caminho pra instalar o programa..:(Por favor coloque / ao invez de barra inversa )] "))
                if 'snprintf(buffer, sizeof(buffer), "")' in gozar:
                    content = content.replace('snprintf(buffer, sizeof(buffer), "")', f'snprintf(buffer, sizeof(buffer), "{choice4}")')
                with open("install.h", "w") as filefor:
                    filefor.write(content)
                compilar(executar, choice4, program2, choice2, program3)
                





    else:
        print(f"{Fore.RED}Arquivo Não encontrado Forneça o caminho completo ou verifique a pasta aonde esta o programa{Fore.RESET}")
def verification(choice):
    if choice.lower() == "exit":
        sys.exit(0)
    elif choice.lower() == "install":
            install()
    elif choice.lower() == "stringinstall":
        outros.stringinstall()
    else:
        print(f"não foi encontrado o comando: {Fore.RED}{choice}{Fore.RESET}")

if __name__ == "__main__":
    manual = ""
    os.system("clear")
    print(f"{Fore.GREEN}Criado Por: TecnologiaMan\n{Fore.BLUE}Versão: {VERSION} essa versão não contem suporte pra extração .zip{Fore.RESET}")
    time.sleep(1)
    print(f"{Fore.RED}{title}{Fore.RESET}")
    print(f"The TOOL manual was created in {Fore.CYAN}{os.getcwd()}{Fore.RESET}")
    with open("manual.txt", "w") as file:
        print(manual)
        file.write("manual: - 1-'install' this option is the default option of the tool which will simply generate the offline installer for you, follow the instructions after typing\nSorry, the instructions are in Portuguese, but they are easy to understand\n2- 'stringinstall'\nThis option allows you to install a program with binaries in a string or file if the binary is written inside it as if it were text, understand?")

    choice = str(input("\n\n\n[TOOL]# "))
    verification(choice) 

