#!/usr/bin/env python
# coding=utf-8

Ruta = []

Ciudad = [] 

def Validar_Ciudad(linea):
    Texto = '' ; Ruta = " " 
    for i in linea:
        #SACA LOS DATOS DE LAS CIUDADES
        if i.isalpha()==True:
            Texto = Texto + i
        if i == " ":
            Texto = Texto + " ";
        if i.isnumeric()==True:
            if Texto!=" ":
                Ciudad.append(Texto)
                Texto = " ";



def Validar_Recorrido(linea):
    inicio = 0 ; final = 0 ; ruta = '' ;
    for i in range(len(linea)):
        if linea[i].isnumeric()==True:
            inicio = i
            break
    for i in range(len(linea)):
        if linea[i]=="\n":
            final = i ;
            print('este es el valor final : ',final)
            break
    for j in range(inicio,final):
        ruta = ruta + linea[j] ; 
    Ruta.append(ruta)
    ruta = '';
    




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
        archivo = open("set1.txt","r",encoding="utf-8")
        for linea in archivo:
            Validar_Ciudad(linea)
            Validar_Recorrido(linea)
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
    
   # for i in Ruta:
    #    print('esta es la ruta : ',i)

