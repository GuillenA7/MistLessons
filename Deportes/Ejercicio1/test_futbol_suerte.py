import unittest
from unittest.mock import patch
from futbol_suerte import Equipo

class TestEquipo(unittest.TestCase):

    def setUp(self):
        self.equipo1 = Equipo("Tigres", 7, 5)
        self.equipo2 = Equipo("América", 6, 6)

    @patch('random.randint', return_value=1)
    def test_equipo1_gana(self, mock_randint):
        resultado = self.equipo1.jugar_contra(self.equipo2)
        self.assertEqual(resultado, "Tigres gana contra América")

    @patch('random.randint', return_value=-2)
    def test_equipo2_gana(self, mock_randint):
        resultado = self.equipo1.jugar_contra(self.equipo2)
        self.assertEqual(resultado, "América gana contra Tigres")

    @patch('random.randint', return_value=-1)
    def test_empate(self, mock_randint):
        resultado = self.equipo1.jugar_contra(self.equipo2)
        self.assertEqual(resultado, "Empate")

if __name__ == '__main__':
    unittest.main()
