#Leer 2 frases y guardarlas en un archivo
frase1 = input("Dime una frase: ")
frase2 = input("Dime otra frase: ")
mi_ruta = 'C:\\Users\\labc205\\Documents\\Semana12\\'
nota = open("archivo.txt", "w")
nota.write(frase1)
nota.write("\n")
nota.write(frase2)
nota.close