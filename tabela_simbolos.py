class TabelaDeSimbolos:
    def __init__(self):
        # HashMap: nome da variável -> tipo
        self.simbolos = {}

    def declarar(self, nome, tipo):
        """Registra uma variável, se ainda não existir."""

        if nome in self.simbolos:
            return False

        self.simbolos[nome] = tipo
        return True

    def existe(self, nome):
        """Verifica se uma variável foi declarada."""
        return nome in self.simbolos

    def obter_tipo(self, nome):
        """Retorna o tipo de uma variável."""
        return self.simbolos.get(nome)

    def exibir(self):
        print("\nTabela de símbolos:")
        for nome, tipo in self.simbolos.items():
            print(f"{nome}: {tipo}")
