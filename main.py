# -*- coding: utf-8 -*-
import func


#MAIN

func.mensajeBienvenida()

sueldos = func.obtenerSueldos()
gastos = func.obtenerGastos()
sueldosSumados = sum(sueldos)
gastosSumados = sum(gastos)

if gastosSumados <= sueldosSumados:
	
	func.calculaPorcentaje(sueldos, gastos)

else:
	print("Los sueldos no alcanzan para cubrir todos los gastos!")
	print("El excedente de gastos es: %10.2f" %(gastosSumados - sueldosSumados))

func.exitProgram()


