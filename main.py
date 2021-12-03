#!/usr/bin/env python
# coding=utf-8

Ruta = []

Ciudad = [] 

dato_final = '';

num = ["0","1","2","3","4","5","6","7","8","9"]


dato = []


def Depurar(lista):
    for i in lista:
        if i != "":
            Ciudad.append(i)
            #print('este es el valor de la ciudad : ',i)



def Validar_Ciudad(linea):
    texto = '' ; tipo = ""; nombre_ciudad = []
    for i in range(len(linea)):
        if linea[i].isalpha() == True:
            texto = texto + linea[i]
        if linea[i]==" ":
            for j in range(i,len(linea)):
                if linea[j]!=" ":
                    if num.count(linea[j]) == 0:
                        tipo = "str"
                    else:
                        tipo = "int"
                    break
            if tipo == 'str':
                texto = texto + " ";
            else:
                nombre_ciudad.append(texto)
                texto = ''
    Depurar(nombre_ciudad)
                

def Validar_Ruta(linea):
    ruta = ""
    for i in range(len(linea)):
        if num.count(linea[i]) != 0:
            ruta = ruta + linea[i] ;
        if linea[i] == ',':
            ruta = ruta + ','
            Ruta.append(ruta)
            ruta = '';
    #print('este es el valor de la ruta : ',ruta)
    Ruta.append(ruta)

def Leer():
    try:
        contador = 0;    
        archivo = open("set1.txt","r",encoding="utf-8")
        for linea in archivo:
            dato.append(linea)
    except FileNotFoundError:
        print ("NO EXISTE EL ARCHIVO")

def LLenar_vector():
    Leer()
    for i in range(len(dato)):
        Validar_Ciudad(dato[i])
        Validar_Ruta(dato[i])


if __name__ == "__main__":
    LLenar_vector()
    print('CIUDAD : ',Ciudad)
    print('Ruta : ',Ruta)
