import csv
import os

# Archivo y campos
ARCHIVO = 'inventario.csv'
CAMPOS = ['nombre', 'precio', 'cantidad']


# -------------------------
# INICIALIZAR ARCHIVO
# -------------------------
def inicializar_archivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=CAMPOS)
            writer.writeheader()


# -------------------------
# CREAR PRODUCTO
# -------------------------
def crear_producto(datos):
    inicializar_archivo()
    with open(ARCHIVO, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writerow(datos)


# -------------------------
# LEER PRODUCTOS
# -------------------------
def leer_productos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, mode='r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


# -------------------------
# ACTUALIZAR PRODUCTO
# -------------------------
def actualizar_producto(nombre_buscado, nuevos_datos):
    filas = leer_productos()
    actualizado = False

    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()

        for fila in filas:
            if fila['nombre'].lower() == nombre_buscado.lower():
                writer.writerow(nuevos_datos)
                actualizado = True
            else:
                writer.writerow(fila)

    return actualizado


# -------------------------
# ELIMINAR PRODUCTO
# -------------------------
def eliminar_producto(nombre_buscado):
    filas = leer_productos()

    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()

        for fila in filas:
            if fila['nombre'].lower() != nombre_buscado.lower():
                writer.writerow(fila)


# -------------------------
# ESTADÍSTICAS
# -------------------------
def calcular_estadisticas():
    productos = leer_productos()

    if len(productos) == 0:
        print("Inventario vacío")
        return

    unidades = sum(int(p['cantidad']) for p in productos)
    valor_total = sum(float(p['precio']) * int(p['cantidad']) for p in productos)

    mas_caro = max(productos, key=lambda p: float(p['precio']))
    mayor_stock = max(productos, key=lambda p: int(p['cantidad']))

    print("\n--- ESTADÍSTICAS ---")
    print("Unidades totales:", unidades)
    print("Valor total:", valor_total)
    print("Más caro:", mas_caro['nombre'], mas_caro['precio'])
    print("Mayor stock:", mayor_stock['nombre'], mayor_stock['cantidad'])


# -------------------------
# MENÚ (SIN while True)
# -------------------------
ejecutando = True

while ejecutando:

    print("\n--- INVENTARIO CSV ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Estadísticas")
    print("6. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        try:
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            if precio < 0 or cantidad < 0:
                print("Valores inválidos")
            else:
                crear_producto({
                    'nombre': nombre,
                    'precio': precio,
                    'cantidad': cantidad
                })
        except:
            print("Error en datos")

    elif opcion == "2":
        productos = leer_productos()
        if len(productos) == 0:
            print("Inventario vacío")
        else:
            for p in productos:
                print(p)

    elif opcion == "3":
        nombre = input("Producto a actualizar: ")
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))

            actualizado = actualizar_producto(nombre, {
                'nombre': nombre,
                'precio': nuevo_precio,
                'cantidad': nueva_cantidad
            })

            if actualizado:
                print("Actualizado")
            else:
                print("No encontrado")
        except:
            print("Error")

    elif opcion == "4":
        nombre = input("Producto a eliminar: ")
        eliminar_producto(nombre)
        print("Proceso completado")

    elif opcion == "5":
        calcular_estadisticas()

    elif opcion == "6":
        ejecutando = False
        print("Fin del programa")

    else:
        print("Opción inválida")