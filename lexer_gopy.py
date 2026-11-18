"""
Lexer da linguagem Gopy 1.0.

Uso:
    python lexer_aluno.py codigo_entrada.txt

O analisador usa AFDs para identificadores, números e lexemas fixos.
A indentação é processada por linha: TABs reais definem os blocos.
"""

from __future__ import annotations
from dataclasses import dataclass
import sys


# =====================================================================
# 1. TOKEN
# =====================================================================

@dataclass
class Token:
    tipo: str
    valor: str
    linha: int
    coluna: int

    def __repr__(self) -> str:
        return f"<{self.tipo}, {self.valor!r}> @ {self.linha}:{self.coluna}"


# =====================================================================
# 2. AFD — tabela de transições
# =====================================================================

class AFD:
    """AFD representado por tabela (estado, símbolo) -> estado."""

    def __init__(self, nome: str):
        self.nome = nome
        self.transicoes: dict[tuple[int, str], int] = {}
        self.finais: set[int] = set()
        self.inicial: int = 0
        self._prox: int = 1

    def novo_estado(self) -> int:
        estado = self._prox
        self._prox += 1
        return estado

    def transicao(self, origem: int, simbolos: str, destino: int) -> None:
        """Registra uma transição para cada caractere fornecido."""
        for simbolo in simbolos:
            self.transicoes[(origem, simbolo)] = destino

    def marcar_final(self, estado: int) -> None:
        """Marca um estado como estado de aceitação."""
        self.finais.add(estado)

    def maior_prefixo(self, texto: str) -> int:
        """Retorna o maior prefixo aceito ou -1 se nenhum for aceito."""
        estado = self.inicial
        ultimo = 0 if estado in self.finais else -1

        for i, caractere in enumerate(texto):
            proximo = self.transicoes.get((estado, caractere))
            if proximo is None:
                break
            estado = proximo
            if estado in self.finais:
                ultimo = i + 1

        return ultimo


# =====================================================================
# 3. CONFIGURAÇÃO DA LINGUAGEM GOPY 1.0
# =====================================================================

LETRAS_ID = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
INICIAIS_ID = LETRAS_ID + "_"
CONTINUACAO_ID = LETRAS_ID + "0123456789_"
DIGITOS = "0123456789"

PALAVRAS_RESERVADAS: dict[str, str] = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "function": "FUNCTION",
    "return": "RETURN",
    "num": "TP_NUM",
    "text": "TP_TEXT",
    "bool": "TP_BOOL",
    "true": "TRUE",
    "false": "FALSE",
}

OPERADORES: dict[str, str] = {
    "==": "OP_EQ",
    "!=": "OP_NE",
    "<=": "OP_LE",
    ">=": "OP_GE",
    "&&": "OP_AND",
    "||": "OP_OR",
    "=": "ATRIB",
    "<": "OP_LT",
    ">": "OP_GT",
    "+": "OP_SOMA",
    "-": "OP_SUB",
    "*": "OP_MULT",
    "/": "OP_DIV",
    "!": "OP_NOT",
}

SIMBOLOS: dict[str, str] = {
    "(": "PAR_ESQ",
    ")": "PAR_DIR",
    ",": "VIRGULA",
    ":": "DOIS_PONTOS",
}

FIXOS: dict[str, str] = {**OPERADORES, **SIMBOLOS}


# =====================================================================
# 4. CONSTRUTORES GENÉRICOS DE AFDs
# =====================================================================

def afd_literal(nome: str, texto: str) -> AFD:
    """Constrói um AFD que reconhece exatamente um lexema."""
    afd = AFD(nome)
    atual = afd.inicial

    for caractere in texto:
        proximo = afd.novo_estado()
        afd.transicao(atual, caractere, proximo)
        atual = proximo

    afd.marcar_final(atual)
    return afd


def afd_conjunto_literais(nome: str, textos: list[str]) -> AFD:
    """Constrói um trie/AFD para um conjunto de lexemas fixos."""
    afd = AFD(nome)

    for texto in textos:
        atual = afd.inicial
        for caractere in texto:
            proximo = afd.transicoes.get((atual, caractere))
            if proximo is None:
                proximo = afd.novo_estado()
                afd.transicao(atual, caractere, proximo)
            atual = proximo
        afd.marcar_final(atual)

    return afd


# =====================================================================
# 5. CONSTRUTORES ESPECÍFICOS — IDENTIFICADORES E NÚMEROS
# =====================================================================

def afd_identificador() -> AFD:
    """Reconhece [a-zA-Z_][a-zA-Z0-9_]*."""
    afd = AFD("ID")
    q1 = afd.novo_estado()
    afd.transicao(afd.inicial, INICIAIS_ID, q1)
    afd.transicao(q1, CONTINUACAO_ID, q1)
    afd.marcar_final(q1)
    return afd


def afd_inteiro() -> AFD:
    """Reconhece inteiros: [0-9]+."""
    afd = AFD("INT")
    q1 = afd.novo_estado()
    afd.transicao(afd.inicial, DIGITOS, q1)
    afd.transicao(q1, DIGITOS, q1)
    afd.marcar_final(q1)
    return afd


def afd_real() -> AFD:
    """Reconhece reais com dígitos antes e depois do ponto decimal."""
    afd = AFD("REAL")
    parte_inteira = afd.novo_estado()
    ponto_decimal = afd.novo_estado()
    parte_fracionaria = afd.novo_estado()

    afd.transicao(afd.inicial, DIGITOS, parte_inteira)
    afd.transicao(parte_inteira, DIGITOS, parte_inteira)
    afd.transicao(parte_inteira, ".", ponto_decimal)
    afd.transicao(ponto_decimal, DIGITOS, parte_fracionaria)
    afd.transicao(parte_fracionaria, DIGITOS, parte_fracionaria)
    afd.marcar_final(parte_fracionaria)
    return afd


# =====================================================================
# 6. LEXER
# =====================================================================

class Lexer:
    def __init__(self, entrada: str, regras: list[tuple[str, AFD]]):
        self.entrada = entrada
        self.regras = regras
        self.pos = 0
        self.linha = 1
        self.coluna = 1

    def _avancar(self, n: int) -> None:
        for _ in range(n):
            if self.pos >= len(self.entrada):
                return
            if self.entrada[self.pos] == "\n":
                self.linha += 1
                self.coluna = 1
            else:
                self.coluna += 1
            self.pos += 1

    def _reclassificar(self, tipo: str, valor: str) -> str:
        """Converte IDs em palavras reservadas e FIXO em token específico."""
        if tipo == "ID" and valor in PALAVRAS_RESERVADAS:
            return PALAVRAS_RESERVADAS[valor]
        if tipo == "FIXO":
            return FIXOS[valor]
        return tipo

    def _tokenizar_conteudo_linha(
        self, conteudo: str, numero_linha: int, coluna_inicial: int
    ) -> list[Token]:
        """Tokeniza o conteúdo de uma linha, sem tratar sua indentação."""
        tokens: list[Token] = []
        i = 0

        while i < len(conteudo):
            caractere = conteudo[i]

            if caractere in " \r":
                i += 1
                continue

            # Comentário de linha: ignora tudo a partir de //.
            if conteudo.startswith("//", i):
                break

            coluna = coluna_inicial + i

            # String entre aspas duplas, com suporte a escapes como \\" e \\\\.
            if caractere == '"':
                inicio = i
                i += 1
                escapado = False
                fechou = False

                while i < len(conteudo):
                    atual = conteudo[i]
                    if escapado:
                        escapado = False
                    elif atual == "\\":
                        escapado = True
                    elif atual == '"':
                        fechou = True
                        i += 1
                        break
                    i += 1

                if not fechou:
                    raise SyntaxError(
                        f"String não terminada em L{numero_linha}:C{coluna}"
                    )

                valor = conteudo[inicio:i]
                tokens.append(Token("STRING", valor, numero_linha, coluna))
                continue

            resto = conteudo[i:]
            melhor_tipo: str | None = None
            melhor_tamanho = 0

            # A regra de maior prefixo garante, por exemplo, que >= prevaleça sobre >.
            for tipo, afd in self.regras:
                tamanho = afd.maior_prefixo(resto)
                if tamanho > melhor_tamanho:
                    melhor_tamanho = tamanho
                    melhor_tipo = tipo

            if melhor_tamanho == 0 or melhor_tipo is None:
                raise SyntaxError(
                    f"Caractere inesperado {caractere!r} "
                    f"em L{numero_linha}:C{coluna}"
                )

            valor = conteudo[i:i + melhor_tamanho]
            tipo_final = self._reclassificar(melhor_tipo, valor)
            tokens.append(Token(tipo_final, valor, numero_linha, coluna))
            i += melhor_tamanho

        return tokens

    def tokenizar(self) -> list[Token]:
        """Tokeniza o programa e produz NEWLINE, INDENT e DEDENT."""
        tokens: list[Token] = []
        pilha_indentacao = [0]
        linhas = self.entrada.splitlines()
        
        for numero_linha, texto_linha in enumerate(linhas, start=1):
            # Contar somente TABs no começo da linha. Espaços no começo
            # de linhas com código são proibidos como indentação.
            prefixo = 0
            while prefixo < len(texto_linha) and texto_linha[prefixo] == "\t":
                prefixo += 1

            restante = texto_linha[prefixo:]

            # Linhas vazias e linhas que contêm apenas comentários não alteram
            # a pilha de indentação nem geram tokens de bloco.
            if not restante.strip() or restante.lstrip().startswith("//"):
                continue

            # Espaços antes do primeiro token são inválidos; a indentação usa TAB.
            if restante.startswith(" "):
                raise IndentationError(
                    f"Use TAB para indentação, não espaços "
                    f"(linha {numero_linha})."
                )

            nivel = prefixo
            if nivel > pilha_indentacao[-1]:
                pilha_indentacao.append(nivel)
                tokens.append(Token("INDENT", "\\t" * (nivel - pilha_indentacao[-2]),
                                    numero_linha, 1))
            elif nivel < pilha_indentacao[-1]:
                while nivel < pilha_indentacao[-1]:
                    pilha_indentacao.pop()
                    tokens.append(Token("DEDENT", "", numero_linha, 1))
                if nivel != pilha_indentacao[-1]:
                    raise IndentationError(
                        f"Nível de indentação inconsistente na linha {numero_linha}."
                    )

            tokens.extend(
                self._tokenizar_conteudo_linha(
                    restante, numero_linha, prefixo + 1
                )
            )
            tokens.append(Token("NEWLINE", "\\n", numero_linha, len(texto_linha) + 1))

        # Fecha todos os blocos abertos no fim do arquivo.
        linha_final = len(linhas) + 1 if linhas else 1
        while len(pilha_indentacao) > 1:
            pilha_indentacao.pop()
            tokens.append(Token("DEDENT", "", linha_final, 1))

        return tokens


# =====================================================================
# 7. CONSTRUÇÃO DAS REGRAS E PROGRAMA PRINCIPAL
# =====================================================================

def construir_regras() -> list[tuple[str, AFD]]:
    """Monta os AFDs usados pelo lexer."""
    return [
        ("ID", afd_identificador()),
        ("REAL", afd_real()),
        ("INT", afd_inteiro()),
        ("FIXO", afd_conjunto_literais("FIXO", sorted(FIXOS, key=lambda s: (-len(s), s)))),
    ]


def main() -> None:
    if len(sys.argv) > 1:
        caminho = sys.argv[1]
        with open(caminho, "r", encoding="utf-8") as arquivo:
            codigo = arquivo.read()
    else:
        print("Uso: python lexer_aluno.py codigo_entrada.txt")
        sys.exit(1)

    tokens = Lexer(codigo, construir_regras()).tokenizar()

    print(f"{'TEXTO':<20} {'TOKEN':<12}")
    print("-" * 32)
    for token in tokens:
        print(f"{token.valor:<20} {token.tipo:<12}")


if __name__ == "__main__":
    main()
