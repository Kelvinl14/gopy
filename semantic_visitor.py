from gopy.gen.GopyVisitor import GopyVisitor
from gopy.gen.GopyParser import GopyParser

from tabela_simbolos import TabelaDeSimbolos


class SemanticVisitor(GopyVisitor):

    def __init__(self):
        self.tabela = TabelaDeSimbolos()
        self.erros = []

    def registrar_erro(self, mensagem, ctx):
        linha = ctx.start.line
        self.erros.append(f"Erro semântico na linha {linha}: {mensagem}")

    # Declaração de variável
    def visitVarDecl(self, ctx):

        # Primeiro visita a expressão de inicialização.
        # Assim, uma variável não pode ser usada antes
        # de sua própria declaração.
        self.visitChildren(ctx)

        tipo = ctx.getChild(0).getText()
        nome = ctx.getChild(1).getText()

        if not self.tabela.declarar(nome, tipo):
            self.registrar_erro(
                f"Variável '{nome}' já foi declarada.",
                ctx
            )

    # Atribuição
    def visitAssignment(self, ctx):

        # Analisa primeiro o lado direito da atribuição.
        self.visitChildren(ctx)

        nome = ctx.getChild(0).getText()

        if not self.tabela.existe(nome):
            self.registrar_erro(
                f"Variável '{nome}' utilizada antes da declaração.",
                ctx
            )

    # Expressões
    def visitExpr(self, ctx):

        # Identifica a expressão simples formada apenas por ID.
        # Chamadas de função também possuem ID, mas têm outros filhos.
        identificador = ctx.getToken(GopyParser.ID, 0)

        if identificador is not None and ctx.getChildCount() == 1:
            nome = identificador.getText()

            if not self.tabela.existe(nome):
                self.registrar_erro(
                    f"Variável '{nome}' utilizada antes da declaração.",
                    ctx
                )

        # Continua percorrendo expressões internas.
        return self.visitChildren(ctx)

    # Parâmetros de funções
    def visitParam(self, ctx):

        tipo = ctx.getChild(0).getText()
        nome = ctx.getChild(1).getText()

        if not self.tabela.declarar(nome, tipo):
            self.registrar_erro(
                f"Parâmetro '{nome}' já foi declarado.",
                ctx
            )

    def exibir_resultado(self):

        print("\n--- Análise semântica ---")

        if not self.erros:
            print("Nenhum erro semântico encontrado!")
        else:
            for erro in self.erros:
                print(erro)

        self.tabela.exibir()
