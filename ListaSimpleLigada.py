from Nodo import Nodo
import math

# !!! Nombres de los métodos modificados
# para que sean más amigables con la idea
# de trabajar una Cola
# Si buscas la lista original ve a la actividad 8


class Lista:
    def __init__(self):
        self.iniLista = None

    ###
    #   Métodos de inserción
    ###

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)

        if self.iniLista is None:
            self.iniLista = nuevo_nodo
        else:
            nuevo_nodo.liga = self.iniLista
            self.iniLista = nuevo_nodo

    def push(self, dato):

        nuevo_nodo = Nodo(dato)
        if self.iniLista is None:
            self.iniLista = nuevo_nodo
        else:
            aux = self.iniLista
            while aux.liga is not None:
                aux = aux.liga
            aux.liga = nuevo_nodo

    def insertar_orden_ascendente(self, dato):
        # Caso: Lista vacía
        if self.iniLista is None:
            self.iniLista = Nodo(dato)
            return

        # Caso: El mayor dato es el inicio de la lista
        if self.iniLista.dato > dato:
            nuevo = Nodo(dato)
            nuevo.liga = self.iniLista
            self.iniLista = nuevo
            return

        # Recorrer la lista hasta encontrar
        # un valor mayor al dato

        for actual in self:

            if actual.liga is None:
                actual.liga = Nodo(dato)
                return

            siguiente = actual.liga

            if siguiente.dato > dato:
                nuevo = Nodo(dato)
                nuevo.liga = siguiente
                actual.liga = nuevo

                return

    # { Precondicion: Posicion >= 0 }
    # Si un elemento ya existe en la posición indicada, se desplazan
    # todos los elementos a partir de él, una posición más.
    # En los casos NO exitosos regresa un false.
    # e.g: La posición no existe en el arreglo
    def insertar_en_posicion(self, posicion, dato):

        # Caso: Lista vacía
        if self.iniLista is None:
            return False

        # Caso: Posición es cero
        if posicion == 0:
            nuevo = Nodo(dato)
            nuevo.liga = self.iniLista
            self.iniLista = nuevo
            return True

        aux = self.iniLista
        anterior = aux

        # Recorrer la lista hasta llegar al elemento
        for i in range(0, posicion):

            anterior = aux
            aux = aux.liga
            # Si este caso se da, es porque la posicion no existe en el arreglo
            if aux is None:
                return False

        nuevo = Nodo(dato)
        anterior.liga = nuevo
        nuevo.liga = aux

        return True

    ###
    #   Métodos para borrar
    ###

    def pop(self):

        if self.iniLista is None:
            return False

        aux = self.iniLista

        if aux.liga is None:
            self.iniLista = None
        else:
            self.iniLista = aux.liga

        return aux.dato

    def borrar_al_final(self):

        if self.iniLista is None:
            return False

        aux = self.iniLista

        if aux.liga is None:
            self.iniLista = None
        else:
            ant = aux
            while aux.liga is not None:
                ant = aux
                aux = aux.liga
            ant.liga = None
        return aux.dato

    # { Precondicion: Posicion >= 0 }
    # Si la posicion no existe en la lista regresa False
    def borrar_en_posicion(self, posicion):

        # Caso: Lista vacía
        if self.iniLista is None:
            return False

        # Caso: Borrar primer elemento
        if posicion == 0:
            self.iniLista = self.iniLista.liga
            return True

        aux = self.iniLista
        ant = aux

        for i in range(0, posicion):
            ant = aux
            aux = aux.liga
            # Si este caso se da, es porque la posicion no existe en el arreglo
            if aux is None:
                return False

        ant.liga = aux.liga
        return True

    def esta_vacia(self):
        return self.iniLista is None

    ###
    #   Métodos para trabajar Grafos
    ###

    # Comprueba la existencia de un valor buscado
    # en los nodos de la lista
    def existe_elemento(self, buscado):
        if self.iniLista is None:
            return False
        else:
            aux = self.iniLista
            while aux is not None:
                if aux.dato == buscado:
                    return True
                aux = aux.liga
            return False

    # Recuperar una lista con todos los valores
    # de los elementos de la lista
    def enlistar(self):
        nodo_actual = self.iniLista
        if nodo_actual is None:
            return list()
        else:
            adyacencias = list()
            while nodo_actual is not None:
                adyacencias.append(nodo_actual.dato)
                nodo_actual = nodo_actual.liga
            return adyacencias

    ###
    # Métodos para hacer iterable la lista simplemente ligada
    ###

    def __iter__(self):
        return _IteratorList(self.iniLista)


class _IteratorList(object):

    def __init__(self, ini_lista):
        self.actual = ini_lista

    def __next__(self):

        if self.actual is None:
            raise StopIteration()

        nodo = self.actual
        self.actual = self.actual.liga
        return nodo
