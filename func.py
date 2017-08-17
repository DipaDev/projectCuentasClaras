# -*- coding: utf-8 -*-

#Muestra un mensaje de bienvenida para el usuario

def mensajeBienvenida():
	lenghtOfWelcomeMessage = 100
	separatorLine = "+".center(lenghtOfWelcomeMessage,"+")+"\n"
	
	titleString = "cuentas claras".upper() + " v1.0"
	title = titleString.center(len(titleString)+2, " ").center(lenghtOfWelcomeMessage-4,"-").center(lenghtOfWelcomeMessage-2," ").center(lenghtOfWelcomeMessage,"+")+"\n"
	
	
	subtitleString = "basta de papel y calculadora!".title()
	subtitle = subtitleString.center(lenghtOfWelcomeMessage-2," ").center(lenghtOfWelcomeMessage,"+")+"\n"
	
	headerString = "**Coded By DDP**"
	header = headerString.center(len(headerString)+2, " ").ljust(lenghtOfWelcomeMessage-2, " ").center(lenghtOfWelcomeMessage,"+")+"\n"
	
	welcomeMessage = "\n"+separatorLine+title+subtitle+header+separatorLine
	print(welcomeMessage)
	
	
#Pide al usuario que ingrese la cantidad de sueldos que van a cubrir los gastos
def getCantidadAportes():
	cantidadAportes = ""
	conf = ""

	while True:
		inputCantidadAportes = raw_input('Ingrese la cantidad de personas que van a aportar a los gastos (Ej: 1, 2, 4, ...), luego de ingresar el numero presione Enter: ')
		
		try:
			cantidadAportes = int(inputCantidadAportes)
			print("La cantidad ingresada es = " + str(cantidadAportes))
			conf = raw_input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 2
			#conf = input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 3
		except ValueError:
			print("ERROR: '"+inputCantidadAportes+"' NO ES UN VALOR VALIDO"+'\n')			
		

		if conf.lower() in ['s', 'S']:
			break

	return cantidadAportes
	
#Pide al usuario que ingrese el monto neto de cada sueldo
def getSueldosDePantalla(cantidadDeSueldos):
	
	while True:
		sueldos = []
		i = 1
		while i <= cantidadDeSueldos:
			inputSueldoAIngresar = raw_input('Ingrese el importe neto del ' +str(i)+'º sueldo: ')
			try:
				sueldoAIngresar = float(inputSueldoAIngresar)
				sueldos.append(sueldoAIngresar)
				i += 1
			except ValueError:
				print("ERROR: '"+inputSueldoAIngresar+"' NO ES UN VALOR VALIDO"+'\n')		

		print("Los sueldos ingresados son: ")
	
		g = 1
	
		while g <= len(sueldos):
			print(str(g)+"º Sueldo : "+str(sueldos[g-1]))
			g += 1	
	
		#Para Python 2
		conf = raw_input("¿Los sueldos son correctos? (\"S\" = Si, \"N\" = No) ------>  ") 
		#conf = input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 3
				

		if conf.lower() in ['s', 'S']:
			break		

	return sueldos


def obtenerSueldos():
	return getSueldosDePantalla(getCantidadAportes())


#Pide al usuario que ingrese todos los gastos uno por uno
def getGastosPorPantalla():
	gastos = []
	seguirIngresandoGastos = True
	print('A continuacion por favor, ingrese uno por uno los gastos a calcular, luego de ingresar cada uno presione ENTER, para finalizar el ingreso de datos, ingrese como importe \"0\"')
	while seguirIngresandoGastos:
		gasto = float(raw_input('Ingrese el importe del gasto: '))

		if gasto == 0:
			print("Los gastos ingresados son: ")
			g = 1
			while g <= len(gastos):
				print("Gastos "+ str(g)+ " : "+str(gastos[g-1]))
				g += 1
			
			conf = raw_input("¿Los gastos son correctos? (\"S\" = Si, \"N\" = No) ------>  ")
			#conf = input("¿Es correcta? (\"S\" = Si, \"N\" = No) ------>  ") #Para Python 3

			if conf.lower() in ['s', 'S']:
				seguirIngresandoGastos = False

		if seguirIngresandoGastos:		
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
		#print(porcentaje)
	

		if excedenteGastos<0.01:	
			print("El porcentaje a aplicar de ambos sueldos es: %10.2f %%" %(porcentaje))
			print("Del aporte de ambos sueldos sobrarian: $%10.2f " %(sumatoriaDePorcentuales-gastosSumados))
			break

		porcentaje += 0.1


def obtenerSueldosPorcentuales(sueldos, porcentaje):
	sueldosPorcentuales = []
	for x in sueldos:
		sueldoPorcentual = (x/100) * porcentaje
		sueldosPorcentuales.append(sueldoPorcentual)

	return sueldosPorcentuales
