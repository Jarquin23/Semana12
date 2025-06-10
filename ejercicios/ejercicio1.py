import datetime
def escribir_diario():
    """Escribe una entrada en un archivo de diario, incluyendo la fecha y hora actual"""
    entrada = input("Escriba su entrada para el diario: ")
    try:
        with open("diario.txt", "a")as archivo:
            fecha_hora_act = datetime.datetime.now()
            archivo.write(fecha_hora_act.strftime("%Y-%m-%d %H:%M:%S") + "\n")
            archivo.write(entrada + "\n")
        print("Su entrada ha sido guardada en diario.txt")
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")
def mostrar_diario():
    """Muestra el contenido del archivo diario.txt en la consola"""
    try:
        with open("diario.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo diario.txt no existe")
    except Exception as e:
        print(f"ocurrió un error a la hora de leer el archivo: {e}")
if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Escribir en el diario")
        print("2. Mostrar el diario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            escribir_diario()
        elif opcion== "2":
            mostrar_diario()
        elif opcion== "3":
            break
        else:
            print("La opción no es válida, por favor intentelo nuevamente.")