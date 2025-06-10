nombre_archivo = input("Ingrese el nombre del archivo: ")
mi_ruta = 'C:\\Users\\labc205\\Documents\\Semana12\\'
nombre_archivo = open(mi_ruta + nombre_archivo)
mi_archivo = open(mi_archivo)
try:
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        total_lineas = len(lineas)
        print(f"El archivo '{nombre_archivo}' tiene {total_lineas} línea(s)")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró, verifique el nombre y la ruta")