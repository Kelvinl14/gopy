grammar Gopy;
tokens { DEDENT }

// Regra inicial: um programa e uma sequência de comandos
program
    : (statement | NEWLINE)* EOF
    ;

// Um comando pode ser declaração, atribuição,
// estrutura de controle, função ou retorno
statement
    : varDecl
    | assignment
    | ifStmt
    | whileStmt
    | functionDecl
    | returnStmt
    ;

// Declaração de variável
varDecl
    : type ID (ATRIB expr)?
    ;

// Tipos da Gopy
type
    : TP_NUM
    | TP_TEXT
    | TP_BOOL
    ;

// Condicional
ifStmt
    : IF expr DOIS_PONTOS block
      (ELSE DOIS_PONTOS block)?
    ;

// Repetição
whileStmt
    : WHILE expr DOIS_PONTOS block
    ;

// Função
functionDecl
    : FUNCTION type ID PAR_ESQ params? PAR_DIR DOIS_PONTOS block
    ;

block
    : NEWLINE INDENT (statement NEWLINE*)+ DEDENT
    ;

// Parâmetros da função
params
    : param (VIRGULA param)*
    ;

param
    : type ID
    ;

// Retorno de função
returnStmt
    : RETURN expr
    ;

// Atribuição
assignment
    : ID ATRIB expr
    ;

// Expressões
expr
    : expr OP_OR expr
    | expr OP_AND expr
    | expr (OP_EQ | OP_NE) expr
    | expr (OP_LT | OP_GT | OP_LE | OP_GE) expr
    | expr (OP_SOMA | OP_SUB) expr
    | expr (OP_MULT | OP_DIV) expr
    | OP_NOT expr
    | ID PAR_ESQ args? PAR_DIR
    | ID
    | INT
    | REAL
    | STRING
    | TRUE
    | FALSE
    | PAR_ESQ expr PAR_DIR
    ;

// Argumentos de chamada de função
args
    : expr (VIRGULA expr)*
    ;

// ------------------- Lexer -------------------

TP_NUM  : 'num';
TP_TEXT : 'text';
TP_BOOL : 'bool';

// Indentação por TAB e quebras de linha
NEWLINE : '\r'? '\n';
INDENT  : '\t'+;

WS      : [ ]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;

TRUE    : 'true';
FALSE   : 'false';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
FUNCTION: 'function';
RETURN  : 'return';

// Operadores
OP_EQ    : '==';
OP_NE    : '!=';
OP_LE    : '<=';
OP_GE    : '>=';
OP_AND   : '&&';
OP_OR    : '||';
ATRIB    : '=';
OP_LT    : '<';
OP_GT    : '>';
OP_SOMA  : '+';
OP_SUB   : '-';
OP_MULT  : '*';
OP_DIV   : '/';
OP_NOT   : '!';

// Símbolos
PAR_ESQ     : '(';
PAR_DIR     : ')';
VIRGULA     : ',';
DOIS_PONTOS : ':';

INT     : [0-9]+;
REAL    : [0-9]+ '.' [0-9]+;
STRING  : '"' (~["\r\n])* '"';
ID      : [a-zA-Z_][a-zA-Z_0-9]*;