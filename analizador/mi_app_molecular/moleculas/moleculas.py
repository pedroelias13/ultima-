# moleculas.py
# Autor: pedro elias aponte
# Descripción: Este módulo maneja la representación y análisis de moléculas usando ChemPy.

from chempy import Substance


class Molecula:
    """
    Clase que representa una molécula basada en su fórmula química.

    Atributos:
    -----------
    formula : str
        Fórmula química de la molécula (por ejemplo, 'H2O' para agua).
    """

    def __init__(self, formula: str):
        """
        Constructor para inicializar una molécula con su fórmula.

        Parámetros:
        ------------
        formula : str
            La fórmula química de la molécula.
        """
        self.formula = formula
        self.substance = Substance.from_formula(formula)

    def obtener_masa_molar(self) -> float:
        """
        Calcula la masa molar de la molécula.

        Retorna:
        --------
        float: Masa molar en g/mol.
        """
        return self.substance.molar_mass()

    def obtener_composicion(self) -> dict:
        """
        Retorna la composición atómica de la molécula.

        Retorna:
        --------
        dict: Un diccionario con los elementos y sus proporciones.
        """
        return self.substance.composition
