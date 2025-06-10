try:
    mi_ruta = 'C:\\Users\\labc112\\Documents\\Archivo'
    mi_archivo = open(mi_ruta + "notas.txt", "w")
    texto = input("Dime algo: ")
    mi_archivo.write("texto")
    mi_archivo.close()
except Exception:
    print("ERROR")