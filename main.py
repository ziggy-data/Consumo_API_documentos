from cpf_cnpj_titulo import DocCpf, DocCnpj, DocEleitoral
from telefone import TelefoneBr
import requests
from acesso_cep import BuscaEndereco

leme = BuscaEndereco('	22010-070 ') #espaços extras com proposito
cep = leme.acessa_via_cep()

print(cep)

pontal = BuscaEndereco('	22790877 ') #espaços extras com proposito
bairro, complemento, localidade, uf, ddd, cep = pontal.acessa_via_cep()

print(bairro, complemento, localidade, uf, ddd, cep)

