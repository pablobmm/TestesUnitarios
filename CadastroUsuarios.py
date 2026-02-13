import unittest
def cadastrar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha muito curta")
    return True


class CadastrarUsuarios(unittest.TestCase):
    def test_senha_correta(self):
        resultado = cadastrar_senha("cachorro567")
        self.assertTrue(resultado)
    def test_senha_curta(self):
        with self.assertRaises(ValueError):
            cadastrar_senha("123")
    


if __name__ == "__main__":
    unittest.main()
