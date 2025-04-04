import unittest
from futbol import Equipo

class TestEquipoSinRandom(unittest.TestCase):

    def setUp(self):
        self.equipo1 = Equipo("Leones", 8, 5)
        self.equipo2 = Equipo("Tiburones", 6, 7)
        self.equipo3 = Equipo("Águilas", 7, 7)

    def test_gana_equipo_que_llama_jugar_contra(self):
        resultado = self.equipo1.jugar_contra(self.equipo2)
        self.assertEqual(resultado, "Leones gana contra Tiburones")

    def test_gana_otro_equipo(self):
        resultado = self.equipo2.jugar_contra(self.equipo1)
        self.assertEqual(resultado, "Tiburones gana contra Leones")

    def test_empate(self):
        resultado = self.equipo3.jugar_contra(self.equipo3)
        self.assertEqual(resultado, "Empate")

if __name__ == '__main__':
    unittest.main()