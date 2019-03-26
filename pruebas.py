import sys
import unittest
import adn as adn

class prueba(unittest.TestCase):
    def test_obtener_complemento(self):
        self.assertEqual(adn.obtener_complemento('A'), 'T')
        self.assertEqual(adn.obtener_complemento('T'), 'A')
        self.assertEqual(adn.obtener_complemento('C'), 'G')
        self.assertEqual(adn.obtener_complemento('G'), 'C')
        with self.assertRaises(TypeError):
            adn.obtener_complemento('f')

    def test_generar_cadena_complementaria(self):
        self.assertEqual(adn.generar_cadena_complementaria('GATA'), 'CTAT')
        self.assertEqual(adn.generar_cadena_complementaria('CTGT'), 'GACA')
        with self.assertRaises(TypeError):
            adn.generar_cadena_complementaria('GCTH')


    def test_calcular_correspondencia(self):
        self.assertEqual(adn.calcular_correspondencia('GATA', 'CATA'), 0.75)
        self.assertEqual(adn.calcular_correspondencia('TCT', 'GAT'), 0.3333333333333333)
        with self.assertRaises(TypeError):
            adn.calcular_correspondencia('ABCD', 'FGHI')

    def test_corresponden(self):
        self.assertEqual(adn.calcular_correspondencia('GATA', 'CATA'), 0.75)
        self.assertEqual(adn.calcular_correspondencia('TCT', 'GAT'), 0.3333333333333333)
        with self.assertRaises(TypeError):
            adn.calcular_correspondencia('ABCD', 'FGHI')