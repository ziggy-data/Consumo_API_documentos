import re
"""
Essa classe faz validação e formatação de um numero de telefone (nacional ou internacional) com RegEx. 
"""

class TelefoneBr:
    def __init__(self,numero):
        if self.valida_numero(numero):
            self.numero = numero
        else:
            raise ValueError('Numero incorreto')

    def __str__(self):
        return self.formatacao_numero()

    def valida_numero(self,numero):
        padrao =  "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao,numero)
        if resposta:
            return True
        else:
            return False

    def formatacao_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+{} ({}) {}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_formatado