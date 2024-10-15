from chempy import Substance
import random

class GeneradorCoordenadas:
    @staticmethod
    def generar_coordenadas(elementos):
        coordenadas = []
        for elemento in elementos:
            x = random.uniform(-10, 10)
            y = random.uniform(-10, 10)
            z = random.uniform(-10, 10)
            coordenadas.append((elemento, x, y, z))
        return coordenadas


    @staticmethod
    def mostrar_molecula(elementos):
        """
        Muestra la composición de la molécula con los elementos seleccionados.
        """
        return [Substance.from_formula(e).unicode_name for e in elementos]
