import unittest
def pode_dirigir(idade):
    return idade >= 18 if True else False


class Dirigir(unittest.TestCase):
    def test_pode_dirigir(self):
        result = pode_dirigir(20)
        self.assertEqual(result,True)
    def test_nao_pode_dirigir(self):
        result = pode_dirigir(16)
        self.assertEqual(result,False)


if __name__ == "__main__":
    unittest.main()
