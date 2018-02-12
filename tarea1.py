
def OrdenarDato(ListaDatos):

	CantidadDatos = len(ListaDatos)

	for i in range(CantidadDatos):
		for j in range(CantidadDatos - 1):
			if ListaDatos[j] > ListaDatos[j+1]:
				tmp = ListaDatos[j + 1]
				ListaDatos[j + 1] = ListaDatos [j]
				ListaDatos[j] = tmp

def extraerMediana(listaDatos):
	
	CantidadDatos = len(listaDatos)

	if CantidadDatos % 2 == 0:
		medio_1 = int(CantidadDatos / 2) - 1
		medio_2 = (int(CantidadDatos / 2))

		medio = (listaDatos[medio_1] + listaDatos[medio_2]) / 2
		print("la mediana es: " + str(medio))

	else:
		medio = (int(CantidadDatos / 2)) + 1
		print("la mediana es: " + str(medio))

def ExtraerModa(ListaDatos):

	maximo = 0
	posicion = 0

	for i in range(len(ListaDatos)):
		tmp = ListaDatos[i]
		contador = 0
		for j in range(len(ListaDatos)):
			if tmp == ListaDatos[j]:
				contador += 1
		if maximo < contador:
			posicion = i
			maximo = contador

	print("la moda es: " + str(ListaDatos[posicion]))
	print("el numero de veces que se repitio es: " + str(maximo))

def extraerMedia(ListaDatos):

	suma = 0
	for i in ListaDatos:
		suma += i
	promedio = suma / len(ListaDatos)
	return promedio

def extraerMediaM(ListaDatos):
	promedio = extraerMedia(ListaDatos)
	print("El promedio es: "+ str(promedio))

def ExtraerVarianza(ListaDatos):

	promedio = extraerMedia(ListaDatos)
	NumeroDatos = len(ListaDatos)
	acumulador = 0

	for i in ListaDatos:
		formula = ((i - promedio) ** 2) / (NumeroDatos - 1)
		acumulador += formula

	print("la varianza es: " + str(acumulador))

def ExtraerCovarianza(ListaDatos_1, ListaDatos_2):

	promedio_1 = extraerMedia(ListaDatos_1)
	promedio_2 = extraerMedia(ListaDatos_2)
	acumulador = 0

	if len(ListaDatos_1) == len(ListaDatos_2):
		for i in range(len(ListaDatos_1)):
			formula = (ListaDatos_1[i] - promedio_1)*(ListaDatos_2[i] * promedio_2)
			acumulador += formula

		covarianza = acumulador / (len(ListaDatos_1) - 1)
		print("la covarianza es: "+ str(covarianza))

	else:
		print("las listas deben tener la misma cantidad de datos")	




if __name__ == '__main__':

	listaDatos=[]

	NumeroDatos = (int) (input("ingresar el numero de datos de la lista: "))

	for i in range (NumeroDatos):
		Dato = input("ingresar datos: ")
		listaDatos.append(int(Dato))
		print(listaDatos)

	OrdenarDato(listaDatos)
	print(listaDatos)
	extraerMediana(listaDatos)
	ExtraerModa(listaDatos)
	extraerMediaM(listaDatos)
	ExtraerVarianza(listaDatos)
	ExtraerCovarianza([1,2,3],[1,2,3])