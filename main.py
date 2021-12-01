# -*- coding: utf-8 -*-

captura_inicial = []

captura_final = []

Ciudad = [] 

def Validar_Ciudad(linea):
    Texto = '' ; contador = 0 
    for i in linea:
        if i.isalpha()==True:
            Texto = Texto + i
        if i == " ":
            Texto = Texto + " ";
        if i.isnumeric()==True:
            if Texto!=" ":
                contador = contador + 1; 
                print(contador," . ",Texto)
                Texto = " ";

def Validar_Numero_Final(numero):
    completo = ''
    for i in numero:
        if i==',' or i==';':
            captura_final.append(completo)
            completo=''
        else:
            completo +=i


def Crear():
    archivo = open("inicial.txt","w")
    archivo.close()

def Escribir():
    try:
        archivo = open("inicial.txt")
        print("escribe un texto")
        cadena = input()
        archivo.write(cadena+'\n')
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")

def Leer():
    try:
        contador = 0;    
        archivo = open("set1.txt","r")
        for linea in archivo:
            Validar_Ciudad(linea)
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")

def Leer_1():
    try:    
        archivo = open("final.txt")
        linea = archivo.readline()
        while(linea):
            Validar_Numero_Final(linea)
            linea = archivo.readline()
        archivo.close()
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")


if __name__ == "__main__":
    Leer()
    #print('ESTAS SON LAS CIUDADES : ',Ciudad)
    
    
    
    
    #Leer_1()
