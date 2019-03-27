import sys
import unittest
import adn as adn

class prueba(unittest.TestCase):
    def test_obtener_secciones(self):
        self.assertEqual(adn.obtener_secciones('AGATAGA'), 3)
        self.assertEqual(adn.obtener_secciones('GATATACA'), 4)
        self.assertEqual(adn.obtener_secciones('tacaga'), 2)
        with self.assertRaises(TypeError):
            adn.obtener_secciones('GCTI')


    def test_obtener_complementos(self):
        self.assertEqual(adn.obtener_complementos(['GATATACA', 'TATACACA', 'TCTATGTA', 'TAGAGATA','GATA']), ['CTATATGT','ATATGTGT','AGATACAT', 'ATCTCTAT','CTAT'])
        self.assertEqual(adn.obtener_complementos(['tagata', 'cataga', 'gataca']), ['ATCTAT', 'GTATGT', 'CTATGT'])
        with self.assertRaises(TypeError):
            adn.obtener_complementos(['GCTA', 'UTASF'])

    def test_unir_cadena(self):
        self.assertEqual(adn.unir_cadena(['GACA', 'TAC', 'GATA']), 'GACATACGATA')
        self.assertEqual(adn.unir_cadena(['TATA', 'GATAGA', 'TG']), 'TATAGATAGATG')
        with self.assertRaises(TypeError):
            adn.unir_cadena(['FAFSAS', 'UTASF'])

    def test_complementar_cadenas(self):
        self.assertEqual(adn.complementar_cadenas(['GATATA','TATACA','CAGATCA']), ['CTATAT', 'ATATGT', 'GTCTAGT'])
        self.assertEqual(adn.complementar_cadenas(['TATACAGA','TATAGA','TCACAG']), ['ATATGTCT','ATATCT','AGTGTC'])
        with self.assertRaises(TypeError):
            adn.unir_cadena(['AFTAGA','UTASF'])

if __name__ == 'main':

    unittest.main()