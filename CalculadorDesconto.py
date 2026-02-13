import unittest
def calcular_desconto(valor,percentual):
    limite = 50
    if percentual > limite:
        percentual = limite
    return valor - (valor*percentual/100)


class CalcularDesconto(unittest.TestCase):
    def test_descontoComum(self):
        resultado = calcular_desconto(100,10)
        self.assertEqual(resultado,90)
    def test_limiteSeguraca(self):
        resultado = calcular_desconto(500,70)
        self.assertEqual(resultado,250)
    def test_produtoZero(self):
        resultado = calcular_desconto(0,30)
        self.assertEqual(resultado,0)


if __name__ == "__main__":
    unittest.main()
