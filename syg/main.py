# This file was YogiSystemHub

import os
import platform
import time
import sygpyfunc
import mathsyg
import infosyg

def script():
	time.sleep(0)
	print(f"""
__     __         _  _____           _                 
\ \   / /        (_)/ ____|         | |                
 \ \_/ /__   __ _ _| (___  _   _ ___| |_ ___ _ __ ___  
  \   / _ \ / _` | |\___ \| | | / __| __/ _ \ '_ ` _ \ 
   | | (_) | (_| | |____) | |_| \__ \ ||  __/ | | | | |
   |_|\___/ \__, |_|_____/ \__, |___/\__\___|_| |_| |_|
             __/ |          __/ |                      
            |___/          |___/  1.0.0 (default, Jul 5 2023)

Your OS: {platform.system()}
Bienvenidos al YogiSystem Interfance.
Escribe "credits" para los créditos y "help" para la ayuda.""")
	comando = input("YogiSystem $ ")
	if comando == "credits":
		time.sleep(0)
		print("""
Aquí aparecen todos los que aportaron al YogiSystem:

Francesco Eriani H.""")
	elif comando == "help":
		print("""
Aquí está la Ayuda del YogiSystem Offline.
Escribe la letra que indique las preguntas frecuentes. Si no lo encuentra, escribe 0.
		
a) ¿Puedo utilizar YogiSystem con Python simultaneamente?""")
		
		com1 = input("YogiSystem HELP $ ")
		if com1 == "a":
			time.sleep(0)
			print("""
Sí. Para poder funcionarlo, navega en el Terminal hasta donde este la carpeta YogiSystem Folder.
Luego renauda este archivo y escribe ´sygpyfunc´ en la Terminal SYG. Y listo!""")
	elif comando == "sygpyfunc":
		com2 = input("YogiSystem Python $ ")
		time.sleep(0)
		print("")
		sygpyfunc.sygcmd(com2)
	elif comando == "mathsyg":
		com3 = input("YogiSystem Math $ ")
		time.sleep(0)
		print("")
		if com3 == "triangulo":
			mathsyg.domanda1()
		elif com3 == "cuadrado":
			mathsyg.domanda2()
		elif com3 == "pentagono":
			mathsyg.domanda3()
		elif com3 == "suma":
			mathsyg.domanda4()
		elif com3 == "resta":
			mathsyg.domanda5()
		elif com3 == "multiplicación":
			mathsyg.domanda6()
		elif com3 == "división":
			mathsyg.domanda7()
		elif com3 == "multiplicacion" or com3 == "division":
			return f"SyntaxError YogiSystem <{com3}>: Debe escribir con tilde el comando en la última 'o'."
		else:
			print("SyntaxError YogiSystem: No entendimos tu comando.")
			return False
	elif comando == "exit()" or comando == "quit()":
		return "Saliendo de YogiSystem Interface..."
	elif comando == "infosystem":
		print(infosyg.infosystem())
		return True
	elif comando == "infoHuaraz=True":
		print(infosyg.infohuaraz())
		return True
	else:
		print("SyntaxError YogiSystem. Reloading the YogiSystem Interface")
		return False
script()
while not script():
	script()
