# Ejercicio propuesto con listas (1)

ventas = []
nombre = input("Introduzca el nombre del ventas: ")
ventas.append(int(input("Venta(L): ")))
ventas.append(int(input("Venta(M): ")))
ventas.append(int(input("Venta(X): ")))
ventas.append(int(input("Venta(J): ")))
ventas.append(int(input("Venta(V): ")))

total = 0
for venta in ventas:
    total += venta

ventas.sort()
max_venta = ventas[len(ventas) - 1]
min_venta = ventas[0]

print("\n")
print("Lista de ventas: ", ventas)
print("Total de ventas: ", total)
print("Mayor venta: ", max_venta)
print("Menor venta: ", min_venta)