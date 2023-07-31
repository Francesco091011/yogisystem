def triangulo(num):
    return num**num

def cuadrado(num):
    num_copy = num
    result = num
    while num_copy > 0:
        result = triangulo(result)
        num_copy-=1
    return result

def pentagono(num):
    num_copy_1=num
    result1 = num
    while num_copy_1>0:
        result1 = cuadrado(result1)
        num_copy_1-=1
    return result1
    
def suma(a, b):
	return a+b




def division(a,b):
	return a/b


def domanda1():
	a = int(input("Escribe el numero para su triangulo $ "))
	print(triangulo(a))
def domanda2():
	b = int(input("Escribe el numero para su cuadrado $ "))
	print(cuadrado(b))
def domanda3():
	c = int(input("Escribe el numero para su pentagono $ "))
	print(pentagono(c))
def domanda4():
	c = int(input("Escribe el numero a para la suma $ "))
	d = int(input("Escribe el numero b para la suma $ "))
	print(suma(c, d))
def domanda5():
	def resta(a,b):
		return a-b
	e = float(input("Escribe el numero a para la resta $ "))
	f = float(input("Escribe el numero b para la resta $ "))
	print(resta(e, f))
def domanda6():
	def multiplicacion(a,b):
		return a*b
	g = int(input("Escribe el numero a para la multiplicación $ "))
	h = int(input("Escribe el numero b para la multiplicación $ "))
	print(multiplicacion(g,h))
def domanda7():
	i = int(input("Escribe el numero a para la división $ "))
	j = int(input("Escribe el numero b para la división $ "))
	print(division(i,j))
