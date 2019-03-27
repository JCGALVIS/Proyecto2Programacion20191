import sys
import unittest
import adn as adn

class prueba(unittest.TestCase):
    def test_es_cadena_valida(self):
        self.assertEquals(adn.es_cadena_valida('AGATA'),True)
        self.assertEquals(adn.es_cadena_valida('GATA'),True)
        self.assertEquals(adn.es_cadena_valida('CCTT'), True)
        self.assertEquals(adn.es_cadena_valida('ALAT'), False)
        self.assertEquals(adn.es_cadena_valida('ATCB'), False)
        self.assertEquals(adn.es_cadena_valida('OGTAU'), False)

    def test_es_base(self):
        self.assertEquals(adn.es_base('A'), True)
        self.assertEquals(adn.es_base('T'), True)
        self.assertEquals(adn.es_base('C'), True)
        self.assertEquals(adn.es_base('C'), True)
        self.assertEquals(adn.es_base('T'), True)
        self.assertEquals(adn.es_base('a'), True)
        self.assertEquals(adn.es_base('B'), False)
        self.assertEquals(adn.es_base('B'), False)

    def test_es_subcadena(self):
        self.assertEquals(adn.es_subcadena('AGATA','AGA'), True)
        self.assertEquals(adn.es_subcadena('GTAC','TA'), True)
        with self.assertRaises(ValueError):
            adn.es_subcadena('TC', 'TCP')

    def test_reparar_dano(self):
        self.assertEquals(adn.reparar_dano(['I','A','T','A'],'G'),['G', 'A', 'T', 'A'])
        self.assertEquals(adn.reparar_dano(['C', 'A', 'B'], 'C'), ['C', 'A', 'C'])
        with self.assertRaises(ValueError):
            adn.reparar_dano(['G', 'P', 'C', 'G'], 'H'),['C', 'A', 'C']