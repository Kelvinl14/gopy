# Guia de utilização da Gopy

## 1. Gerar o Parser ANTLR

Execute na pasta do projeto:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o gen Gopy.g4
```

## 2. Executar o Lexer

Para analisar o código e gerar a tabela de tokens:

```bash
python lexer_gopy.py codigo_entrada.txt > tabela_saida.txt
```

O resultado será salvo em `tabela_saida.txt`.

## 3. Executar o Parser

Execute o arquivo de integração:

```bash
python integracao_antlr.py
```

O programa verificará a estrutura sintática do código e exibirá a árvore sintática.

## 4. Executar a análise semântica

Com o `SemanticVisitor` integrado:

```bash
python integracao_antlr.py
```

O programa também verificará:
- Variáveis utilizadas antes da declaração.
- Declarações duplicadas.

## 5. Arquivos principais

- `Gopy.g4`: gramática da linguagem.
- `lexer_gopy.py`: analisador léxico.
- `gen/`: arquivos gerados pelo ANTLR.
- `integracao_antlr.py`: integração entre Lexer e Parser.
- `tabela_simbolos.py`: tabela de símbolos.
- `semantic_visitor.py`: análise semântica.
- `codigo_entrada.txt`: código-fonte para testes.