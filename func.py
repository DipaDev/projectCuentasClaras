#Muestra un mensaje de bienvenida para el usuario
def mensajeBienvenida():
	print("""\
		++++++++++++ Bienvenido a CUENTAS CLARAS 1.0 ++++++++++++ 
				**Coded By DDP**
		""")

#Pide al usuario que ingrese la cantidad de sueldos que van a cubrir los gastos
def getCantidadAportes():
	cantidadAportes = int(input('Por Favor Ingrese la cantidad de personas que van a aportar a los gastos (Ej: 1, 2, 4), luego de ingresar el numero presione Enter: '))
	return cantidadAportes

#Pide al usuario que ingrese el monto neto de cada sueldo
def getSueldosDePantalla(cantidadDeSueldos):
	sueldos = []
	i = 1
	while i <= cantidadDeSueldos:
		sueldoAIngresar = float(input('Ingrese el importe neto del ' +str(i)+' sueldo: '))
		sueldos.append(sueldoAIngresar)
		i += 1

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