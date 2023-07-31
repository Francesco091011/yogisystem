# A branch from YogiSystemHub

import os

def sygcmd(command):
	win = ('nt', 'dos')
	if command == "syg pyfunc version":
		if os.name in win:
			os.system("python --version")
		else:
			os.system("python3 --version")
	elif command == "syg version":
		print("YogiSystem 1.0.0")
	elif command == "borra" or command == "cancella" or command == "clear" or command== "borrado":
		if os.name in win:
			os.system("cls")
		else:
			os.system("clear")
	elif command == "syg pyfunc python" or command == "syg pyfunc python3":
		if  os.name in win:
			os.system("python")
		else:
			os.system("python3")
	elif command == "syg pyfunc pip install library":
		library = input("""
Qué librería desea descargar desde pip?
YogiSystem Python Pip $ """)
		try:
			os.system(f"pip install {library}")
		except:
			if os.name == "Linux":
				os.system("sudo apt install python3-pip")
			else:
				return "Lamentamos el error de no estar disponible pip"
	elif command == "syg pyfunc pip uninstall library":
		library = input("""
Qué librería desea desinstalar desde pip?
YogiSystem Python Pip $ """)
		os.system(f"pip uninstall {library}")
			

#comando = input("YogiSystem Python $ ")
#sygcmd(comando)
