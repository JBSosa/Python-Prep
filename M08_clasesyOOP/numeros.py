class listaNumero:
    def __init__(self,lista):
        self.lista=lista
    def es_primo(self):
        for i in self.lista:
            divisor=1
            primo=True
            while divisor<=i:
                if i<=1:
                    primo=False
                    break
                if i%divisor==0 and divisor!=1 and divisor!=i:
                    primo=False
                    break
                divisor+=1
            if primo==True:
                print("El número {} es primo.".format(i))
            else:
                print("El número {} no es primo.".format(i))
    def celsius_farenheit_kelvin(self,origen,destino):
        lista=self.lista
        for i in lista:
            resultado=0
            if origen==destino:
                resultado=i
            elif origen=="C" and destino=="F":
                resultado=float((i*(9/5))+32)
            elif origen=="C" and destino=="K":
                resultado=float(i+273.15)
            elif origen=="F":
                resultado=float(i-32/1.8)
                if destino=="K":
                    resultado+=273.15
            elif origen=="K":
                resultado=lista[i]-273.15
                if destino=="F":
                    resultado=(resultado*(9/5))+32
            print("{} grado {} es igual a {} grados {}".format(i,origen,resultado,destino))
    def factorial(self):
        lista=self.lista
        for i in lista:
            inicial=i
            if i==1:
                print('El factorial de 1 es 1')
            elif i>=0 and type(i)==int:
                factor=i-1
                while factor >=1:
                    i=i*factor
                    factor-=1
                print('El factorial de {} es {}'.format(inicial,i))
            elif type(i)==float:
                i="inválido"
                print('No se admiten números no enteros.')
            elif i<0:
                i="inválido"
                print('No se aceptan números negativos')
            
    def mas_repetido(self):
        lista=self.lista
        posicion=0
        elemento_mas_repetido=None
        while posicion < len(lista):
            if lista.count(lista[posicion])>lista.count(lista[posicion-1]) and posicion>0:
                elemento_mas_repetido=lista[posicion]
            posicion+=1
        if type(self.lista)==list and elemento_mas_repetido!=None:
                print('El elemento más repetido de la lista es {}'.format(elemento_mas_repetido))
        elif type(self.lista)!=list:
            print('El objeto no es una lista.')
        else:
            print('No hay elementos repetidos.')