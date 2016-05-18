# -*- coding: utf-8 -*-

#Muestra un mensaje de bienvenida para el usuario
def mensajeBienvenida():
	print("\n")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("+ --------------- CUENTAS CLARAS v1.0 ----------------  +")
	print("+            Basta de papel y calculadora!              +")
	print("+ **Coded By DDP**                                      +")
	print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("\n")

#Pide al usuario que ingrese la cantidad de sueldos que van a cubrir los gastos
def getCantidadAportes():
	cantidadAportes = ""

	while True:
		cantidadAportes = int(input('Por Favor Ingrese la cantidad de personas que van a aportar a los gastos (Ej: 1, 2, 4), luego de ingresar el numero presione Enter: '))
		print("La cantidad ingresada es = " + str(cantidadAportes))
		conf = raw_input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 2
		#conf = input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 3

		if conf.lower() in ['s', 'S']:
			break

	return cantidadAportes

#Pide al usuario que ingrese el monto neto de cada sueldo
def getSueldosDePantalla(cantidadDeSueldos):
	

	while True:
		sueldos = []
		i = 1
		while i <= cantidadDeSueldos:
			sueldoAIngresar = float(input('Ingrese el importe neto del ' +str(i)+' sueldo: '))
			sueldos.append(sueldoAIngresar)
			i += 1

		print("Los gastos ingresados son:)
		g = 1
		while g <= sueldos:
			print("Sueldo "+ str(g)+ " : "+str(sueldos[g-1])
		
		conf = raw_input("¿Los sueldos son correctos? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 2
		#conf = input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 3

		if conf.lower() in ['s', 'S']:
			break		

	return sueldos


def obtenerSueldos():
	return getSueldosDePantalla(getCantidadAportes())
	

#Pide al usuario que ingrese todos los gastos uno por uno
def getGastosPorPantalla():
	gastos = []
	print('A continuacion por favor, ingrese uno por uno los gastos a calcular, luego de ingresar cada uno presione ENTER, para finalizar el ingreso de datos, ingrese como importe \"0\"')
	while True:
		gasto = float(input('Ingrese el importe del gasto: '))
		
		if gasto == 0:
			break
		gastos.append(float(gasto))

	return gastos

def obtenerGastos():
	return getGastosPorPantalla()

def calculaPorcentaje(sueldos, gastos):

	gastosSumados = sum(gastos)
	sueldosSumados = sum(sueldos)

	porcentaje = 0.1

	sueldosPorcentuales = []

	while porcentaje <= 100.00:
		
		sumatoriaDePorcentuales = sum(obtenerSueldosPorcentuales(sueldos, porcentaje))

		sueldosPorcentuales = obtenerSueldosPorcentuales(sueldos, porcentaje)
		
		excedenteGastos = gastosSumados-sumatoriaDePorcentuales
		print(porcentaje)
		
		if excedenteGastos<0.01:	
			print("El porcentaje a aplicar de ambos sueldos es: %10.2f " %(porcentaje))
			print("Del aporte de ambos sueldos sobrarian: %10.2f " %(sumatoriaDePorcentuales-gastosSumados))
			break

		porcentaje += 0.1


def obtenerSueldosPorcentuales(sueldos, porcentaje):
	sueldosPorcentuales = []
	for x in sueldos:
		sueldoPorcentual = (x/100) * porcentaje
		sueldosPorcentuales.append(sueldoPorcentual)

	return sueldosPorcentuales


#def mostrarCuantoPoneCadaUno(sueldos, porcentaje):
#	sueldosPorcentuales = []
#	for x in sueldos:
#		sueldoPorcentual = (x/100) * porcentaje
#		sueldosPorcentuales.append(sueldoPorcentual)
#
#	return sueldosPorcentuales