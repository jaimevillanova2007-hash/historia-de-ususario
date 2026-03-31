from servicios import *
from archivos import * 
import os 

ruta_name = input("Ingresa el nombre del archivo")
ruta = os.path.join(os.path.dirname(__file__), ruta_name)
#ruta = os.path.join(os.path.dirname(__file__), "inventario.csv")

# PROGRAMA PRINCIPAL
#nombre = input("\nIngrese su nombre: ")
opcion = total= recibo = 0
detalle = "" 
inventario = []

while opcion != 9: 

    print("\n1 - Agregar producto")
    print("2 - Mostrar inventario")
    print("3 - Calcular estadistica")
    print("4 - Buscar producto")
    print("5 - Actualizar producto")
    print("6 - Eliminar producto")
    print("7 - Guardar CSV")
    print("8 - Cargar CSV")
    print("9 - Salir")

    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    if opcion==1:
          nombre_producto, precio = agregar_producto()
          cantidad = pedir_cantidad()     
          # Guardar múltiples productos
          producto_existente = buscar_producto(inventario, nombre_producto)

          if producto_existente:
            # Si ya existe → sumamos cantidad
            producto_existente["cantidad"] += cantidad
            producto_existente["precio"] = precio  # opcional actualizar precio
            print("Producto actualizado (se sumó la cantidad)")
          else:
            # Si no existe → lo agregamos
            inventario.append({
                  "nombre": nombre_producto,
                  "precio": precio,
                  "cantidad": cantidad
            })
            print("Producto agregado correctamente")
        
    elif opcion == 2:
            mostrar_inventario(inventario)

    elif opcion == 3:
            calcular_estadisticas(inventario)
    elif opcion == 4:
          nombre_producto = input("Escriba nombre del producto:  ")
          buscar_producto(inventario, nombre_producto)

    elif opcion == 5:
          nombre_producto = input("Escriba nombre del producto:  ")
          nuevo_precio = float(input("ingrese nuevo precio:  "))
          nueva_cantidad = int(input("Ingrese nueva cantidad"))
          actualizar_producto(inventario, nombre_producto, nuevo_precio, nueva_cantidad)

    elif opcion == 6: 
           nombre_producto = input("Escriba nombre del producto:  ")
           eliminar_producto(inventario, nombre_producto)
    elif opcion == 7:
          guardar_csv(inventario, ruta)
    elif opcion == 8:
            cargar = input("¿Desea cargar el inventario desde el CSV? Esto sobrescribirá el inventario actual. (s/n): ").lower()
            if cargar == 's':
                  inventario = cargar_csv(ruta, inventario, True)
            else:
                  cargar_csv(ruta, inventario, False)
    elif opcion == 9:
            break
    else:
         print("Opción incorrecta")

for i in inventario:
      total = i ["precio"] * i["cantidad"]
      detalle += (f"{i['nombre']} x {i['cantidad']} = ${total}\n")
      recibo += total


# RECIBO FINAL
print("\n========= RECIBO DE COMPRA =========")
#print(f"Cliente: {nombre}\n")
print(detalle)
print(f"TOTAL A PAGAR:   ${recibo:.2f}")
print("\n¡Gracias por su compra!")
# El código simula la gestión de un inventario donde el usuario puede ingresar su nombre,
# el nombre del producto, su precio y la cantidad.

# Automáticamente, el sistema calcula el valor total teniendo en cuenta
# el precio ingresado y la cantidad de cada producto.

# El código se compone de varias funciones y un programa principal.
# Las funciones utilizadas son: agregar_producto(), pedir_cantidad(),
# mostrar_inventario() y calcular_estadisticas().

# La función agregar_producto() se encarga de solicitar el nombre y el precio del producto.
# La función pedir_cantidad() se encarga de solicitar la cantidad del producto.
# La función mostrar_inventario() muestra todos los productos registrados con su precio y cantidad.
# La función calcular_estadisticas() calcula el valor total del inventario y la cantidad total de productos.

# En el código principal se solicita el nombre del usuario.
# Luego se muestra un menú donde puede agregar productos, ver el inventario,
# calcular estadísticas o salir del programa.

# Cada vez que se agrega un producto, se calcula su costo según el precio y la cantidad.
# El sistema guarda todos los productos en una lista llamada inventario.

# Finalmente, al salir del programa, se imprime un resumen con el total a pagar.

