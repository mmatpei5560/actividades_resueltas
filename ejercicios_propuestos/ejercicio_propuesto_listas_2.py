# Ejercicio propuesto con listas (2)

lista_empleados = []
nombre = input("Introduzca el nombre del comercial: ")
while (nombre != ""):
    comercial_actual = []
    comercial_actual.append(nombre)
    comercial_actual.append(int(input("Venta(L): ")))
    comercial_actual.append(int(input("Venta(M): ")))
    comercial_actual.append(int(input("Venta(X): ")))
    comercial_actual.append(int(input("Venta(J): ")))
    comercial_actual.append(int(input("Venta(V): ")))
    lista_empleados.append(comercial_actual)
    nombre = input("\nIntroduzca el nombre del comercial: ")

print("\n","-"*40,"\nINFORMACIÓN DE DEPURACIÓN: lista_empleados = ", lista_empleados,"\n","-"*40,"\n")

num_items = int(input("Introduzca el número de items de interés: "))
print("Los empleados que vendieron ", num_items, " items fueron:")
for empleado in lista_empleados:
    if num_items in empleado:
        nombre_empleado = empleado[0]
        print("- ", nombre_empleado)

        
