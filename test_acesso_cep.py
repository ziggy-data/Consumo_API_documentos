from unittest import TestCase
from acesso_cep import BuscaEndereco


class TestBuscaEndereco(TestCase):

    def setUp(self):
        self.leme = BuscaEndereco('22010-070')

    def test_deve_retornar_um_erro_quando_o_cep_for_invalido(self):
        cep_invalido = BuscaEndereco('12345-678')
        self.assertEqual(self.fail, cep_invalido)

    def test_deve_retornar_as_informacoes_do_cep_com_a_saida_de_dados_completa_da_api(self):
        cep = self.leme.acessa_via_cep()
        self.assertEqual(('Leme', '', 'Rio de Janeiro', 'RJ', '21', '22010-070'),cep)

    def test_deve_retornar_um_item_especifico_do_cep(self):
        bairro, complemento, cidade, uf, localidade, cep = self.leme.acessa_via_cep() #TEM QUE FUNCIONAR CADA ITEM DESSA LISTA
        self.assertEqual('Leme', bairro)

    def test_deve_retornar_um_erro_quando_o_cep_nao_ter_oito_digitos(self):
        cep_incorreto = BuscaEndereco('1234567')
        self.assertEqual(ValueError('CEP inválido'), cep_incorreto)








