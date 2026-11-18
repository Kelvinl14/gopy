from antlr4 import CommonTokenStream
from antlr4.Token import CommonToken, Token
from antlr4.ListTokenSource import ListTokenSource

from gopy.lexer_gopy import Lexer, construir_regras
from gopy.gen.GopyParser import GopyParser
from semantic_visitor import SemanticVisitor


def converter_tokens(tokens_lexer):
    """
    Converte os tokens do lexer Python
    para o formato CommonToken do ANTLR.
    """

    tokens_antlr = []

    for token in tokens_lexer:
        # Obtém o identificador numérico do token no ANTLR.
        tipo_antlr = getattr(GopyParser, token.tipo, None)

        if tipo_antlr is None:
            raise ValueError(
                f"Token não reconhecido pelo ANTLR: {token.tipo}"
            )

        novo_token = CommonToken(
            type=tipo_antlr,
            channel=Token.DEFAULT_CHANNEL
        )

        novo_token.text = token.valor
        novo_token.line = token.linha
        novo_token.column = token.coluna - 1

        tokens_antlr.append(novo_token)

    return tokens_antlr


def analisar(codigo):
    lexer = Lexer(codigo, construir_regras())
    tokens_python = lexer.tokenizar()

    tokens_antlr = converter_tokens(tokens_python)

    token_source = ListTokenSource(tokens_antlr)

    token_stream = CommonTokenStream(token_source)

    parser = GopyParser(token_stream)

    arvore = parser.program()

    if parser.getNumberOfSyntaxErrors() == 0:
        semantic = SemanticVisitor()
        semantic.visit(arvore)
        semantic.exibir_resultado()

        print("Programa sintaticamente válido!")
        print(arvore.toStringTree(recog=parser))
    else:
        print("Foram encontrados erros sintáticos.")


if __name__ == "__main__":
    with open("codigo.gopy", "r", encoding="utf-8") as arquivo:
        codigo = arquivo.read()

    analisar(codigo)
