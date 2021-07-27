from validate_docbr import CPF, CNPJ, TituloEleitoral
"""
A classe CPF será chamada quando o documento conter 11 dígitos, 
clsse Titulo Eleitoral quando possuir 12,
classe CNPJ quando possuir 14.
"""

class Documento:

    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        elif len(doc_str) == 14:
            return DocCnpj(doc_str)
        elif len(doc_str) == 12:
            return DocEleitoral(doc_str)
        else:
            raise ValueError("Documento incorreto!!")

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        return self.formatacao()

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)


    def formatacao(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            ValueError('CNPJ inválido')

    def __str__(self):
        return self.formatacao()

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formatacao(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

class DocEleitoral:
    def __init__(self,documento):
        if self.valida(documento):
            self.eleitoral = documento
        else:
            ValueError('Título eleitoral inválido')

    def __str__(self):
        return self.formatacao()

    def valida(self,documento):
        validador = TituloEleitoral()
        return validador.validate(documento)

    def formatacao(self):
        mascara = TituloEleitoral()
        return mascara.mask(self.eleitoral)

