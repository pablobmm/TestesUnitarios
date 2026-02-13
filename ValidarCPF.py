import unittest
def validar_formato_cpf(cpf):
    if not isinstance(cpf,str):
        return False
    
    qtde_caracteres = len(cpf) == 11
    digitos_numericos = cpf.isdigit() 
    
    if qtde_caracteres and digitos_numericos:
       return True
    else:
       return False

class cpf(unittest.TestCase):
    def test_cpf_sucesso(self):
        self.assertTrue(validar_formato_cpf("12345678901"))
    def test_cpf_falha_caracter(self):
        self.assertFalse(validar_formato_cpf("123TYFFG"))
    def test_cpf_tamanho_curto(self):
        self.assertFalse(validar_formato_cpf("1333"))
    def test_cpf_tamanho_longo(self):
        self.assertFalse(validar_formato_cpf("242342342343242"))
    def test_cpf_tipo(self):
        self.assertFalse(validar_formato_cpf(2133213))

if __name__ == "__main__":
    unittest.main()