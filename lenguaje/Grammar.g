grammar Grammar;
program : (statement NEWLINE)* EOF ;

statement:assing | print | if_statement | for_statement;
/*Definimos la asignacion*/
assing : ID '=' expr;

/*Definimos la impresion*/
print : 'print' '(' expr ')';

/*Definimos el if*/
if_statement : 'if' '('expr')' block;

/*Definimos el for*/
for_statement : 'for' '('assign';'expr';'assign')' block;

/*Definimos block*/
block : '{' (statement NEWLINE)* '}';

/*Definimos expr*/
expr : expr op = ('*' | '/') expr
    | expr op = ('+' | '-') expr
    | expr op = ('>' | '<' | '>=' | '<=') expr
    | expr op = ('==' | '!=') expr
    | NUM
    | ID
    | '(' expr ')'
    ;

/*Definimoslos elementos*/
ID : [a-zA-Z][a-zA-Z_0-9]*;
NUM : [0-9]+;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;
SEMI:';';