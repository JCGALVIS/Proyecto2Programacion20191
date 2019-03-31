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
        self.assertEqual(adn.calcular_correspondencia('GATA', 'GATA'), True)
        self.assertEqual(adn.calcular_correspondencia('TCT', 'GAT'), False)
        self.assertEqual(adn.calcular_correspondencia('TCTG', 'GATC'), False)

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
        with self.assertRaises(ValueError):
            adn.es_base('AT')
        with self.assertRaises(ValueError):
            adn.es_base('1')
        with self.assertRaises(ValueError):
            adn.es_base('')

     def test_es_subcadena(self):
        self.assertEquals(adn.es_subcadena('AGATA','AGA'), True)
        self.assertEquals(adn.es_subcadena('GTAC','TA'), True)
        self.assertEquals(adn.es_subcadena('GGCT', 'GCT'), True)
        self.assertEquals(adn.es_subcadena('CCTT', 'CTC'), False)
        with self.assertRaises(ValueError):
            adn.es_subcadena('TC','TCP')
        with self.assertRaises(ValueError):
            adn.es_subcadena('LI', 'KO')
        with self.assertRaises(ValueError):
            adn.es_subcadena('AG','NM')
        self.assertEquals(adn.es_subcadena('ATA', 'ATA'), 'Las cadenas son iguales')

        with self.assertRaises(ValueError):
            adn.es_subcadena('TC', 'TCP')

     def test_reparar_dano(self):
        self.assertEquals(adn.reparar_dano(['I','A','T','A'],'G'),['G', 'A', 'T', 'A'])
        self.assertEquals(adn.reparar_dano(['C', 'A', 'B'], 'C'), ['C', 'A', 'C'])
        self.assertEquals(adn.reparar_dano(['T', 'U', 'A'], 'A'), ['T', 'A', 'A'])
        with self.assertRaises(ValueError):
            adn.reparar_dano(['G', 'P', 'C', 'G'], 'H'),['C', 'A', 'C']

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
