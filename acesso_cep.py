import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep).strip()
        cep = cep.replace("-", "")
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido')

    def __str__(self):
        return self.formatacao_cep()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formatacao_cep(self):
        return "{} - {}".format(self.cep[:4], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json() #traz um dicionario, se fosse text seria uma string
        return(
            dados['bairro'],
            dados['complemento'],
            dados['localidade'],
            dados['uf'],
            dados['ddd'],
            dados['cep']
        )

