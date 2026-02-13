import unittest
def validar_senha_avancada(senha):
    quantidade_carac = len(senha) >= 8
    numero = any(c.isdigit() for c in senha)
    letra_maiuscula = any(c.isupper() for c in senha)
    if quantidade_carac and numero and letra_maiuscula:
        return True
    else: 
        return False

class senha(unittest.TestCase):
    def test_senha_correta(self):
        self.assertTrue(validar_senha_avancada("Senha123"))
    def test_senha_curta(self):
        self.assertFalse(validar_senha_avancada("Curta5"))
    def test_senha_sem_numero(self):
        self.assertFalse(validar_senha_avancada("semNumero"))
    def test_senha_sem_letra_maiuscula(self):
        self.assertFalse(validar_senha_avancada("sem_maiuscula"))


if __name__ == "__main__":
    unittest.main()