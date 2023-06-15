import time


class Nodo:
    """Aqui se define la clase nodo, la cual sera la responsable de contener los datos y representar
        cada nodo"""
    def __init__(self, letra=None, izq=None, der=None):
        """Se inicializa la funcion especial __init__ con las variables necesarias"""
        self.letra = letra
        self.izq = izq
        self.der = der

    def __str__(self):
        """Funcion especial para retornar en fromato str cada nodo"""
        return "{}".format(self.letra)


class Arbolbinario:
    """La clase ArbolBinario contendra los metodos necesarios para almacenar y recorrer el arbol binario"""
    def __init__(self, raiz=None):
        self.raiz = raiz

    def append(self, elemento):
        """Aqui se van añadiendo elementos al arbol binario"""
        if self.raiz is None: #Se define el nodo padre o nodo principal
            self.raiz = elemento
        else:# si ya hay un nodo padre, se procede a distribuir a la izquierda y derecha del arbol segun su tamaño
            aux = self.raiz
            padre = None
            while aux is not None:# Se comienza a disytibuir los elemntos por el arbol
                padre = aux
                if elemento.letra >= aux.letra:  # se loxaliza los nodos padre
                    aux = aux.der
                else:
                    aux = aux.izq
            if elemento.letra >= padre.letra: #  se van asignando sus hijos
                padre.der = elemento
            else:
                padre.izq = elemento

    def preorden(self, elemento):
        """recorrido preorden, se utiliza recursividad para proceder a escalar por el arbol
            nodo, izquierdo, derecho"""
        if elemento is not None:
            print(elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)

    def postorden(self, elemento):
        """recorrido postorden, se utiliza recursividad para proceder a escalar por el arbol
            izquierdo, derecho, nodo"""
        if elemento is not None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento)

    def inorden(self, elemento):
        """recorrido inorder, se utiliza recursividad para proceder a escalar por el arbol
            izquierdo, nodo, derecho"""
        if elemento is not None:
            self.inorden(elemento.izq)
            print(elemento)
            self.inorden(elemento.der)

    def getRaiz(self):
        return self.raiz


if __name__ == '__main__':
    """Funcion principal, llamad main donde se carga el menu y se instancian objetos para desarrollar el ejercicio"""
    arbol = Arbolbinario()
    aux1 = True
    while aux1:
        print("+*+*+*+ Menu de arboles binarios *+*+*+*+\n")
        print("1. Agregar elemento")
        print("2. Recorrido inorden")
        print("3. Recorrido preorden")
        print("4. Recorrido postorden")
        print("5. salir")

        opc = int(input("Selecione una opcion :"))
        if opc == 1:
            letra = input("Ingrese letra : ")
            nodo = Nodo(letra)
            arbol.append(nodo)
        elif opc == 2:
            print("Imprimiendo por inorden\n")
            arbol.inorden(arbol.getRaiz())             
        elif opc == 3:
            print("Imprimiendo por postorden\n")
            arbol.postorden(arbol.getRaiz())
        elif opc == 4:
            print("Imprimiendo por preorden\n")
            arbol.preorden(arbol.getRaiz())
        elif opc == 5:
            print("Cerrando programa.....")
            time.sleep(2)
            aux1 = False
        else:
            print("Seleciono una opcion incorrecta.....")
                   
