class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.liga = None


# Estimado usuario de la clase nodo.
# None al parecer es el equivalente a null en Java o C
# se puede comparar si el campo de liga es null usando la expresion
# <lista>.liga is None
# aunque eso es lo recomendable, tambien puede compararlo usando
# <lista>.liga == None
