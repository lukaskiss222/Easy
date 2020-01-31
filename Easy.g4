grammar Easy;

//Todo
//Indexovanie do pola pomocou [] a [,]
//od teraz aj nas jazyk podporuje [1,2,3,4] -> vylistovanie prvkou


//main: stmt*;

options {
  output=AST;
}


compileUnit: funcdef*;


NEWLINE: WHITESPACE* ('\r')? '\n' -> skip;


COMMENT:        '#' ~[\r\n]* -> skip;
WHITESPACE: ('\t' | ' ')+ -> skip;

NUMBER: [0-9]+;
CHAR: '\'' . '\'';
STRING: '"'      ('\\' (([ \t]+ ('\r'? '\n')?)|.) | ~[\\\r\n"])*  '"';

POINTER: '*';
DOUBE_DOT: ':';
T_INT: 'int';
T_CHAR: 'char';
T_BOOL: 'bool';
T_STR: 'str';
T_VOID: 'void';
DEL: 'del';
NAME: [a-zA-Z_] [a-zA-Z0-9_]*;
d_type: T_INT | T_CHAR | T_BOOL | T_STR | T_VOID;


a_type: d_type POINTER*;



block: '{' stmt* '}' ;


//test expresion
test:or_test;

or_test: and_test ('||' and_test)*;

and_test: not_test ('&&' not_test)*;

not_test: '!' not_test | comparison;

comparison: expr (comp_op expr)?;

comp_op: '<'|'>'|'=='|'>='|'<='|'!=';


//expresion

expr: arith_expr;

arith_expr: term (('+'| '-') term)*;

term: factor (('*'|'/') factor)*;

factor: ('-')? creator;

access: NAME trailer | default;
default: NAME | NUMBER | CHAR | STRING;

//creator: atom | NAME trailer;
creator: atom | access;



trailer: parameters | listparameters;

atom:
    '(' test ')';


//statements
stmt: s_stmt | c_stmt;
//simple statements

s_stmt: flow_stmt | expr_stmt;

expr_stmt: NAME parameters|  NAME (listparameters| DOUBE_DOT a_type)? '=' test
    | NAME DOUBE_DOT a_type ('(' default ')')? | DEL NAME (listparameters)?;



//compacted statements
//TODO : Mozno zrusit funcdeff??, kvoli tomu aby sa nedal definovat vofunckii
c_stmt: for_stmt | while_stmt | if_stmt | funcdef;

for_stmt: 'for' NAME DOUBE_DOT T_INT 'from' expr 'to' expr 'by' expr block;
while_stmt: 'while' test block;
if_stmt: 'if' test block ('else' block)?;

flow_stmt: return_stmt ;//| break_stmt | continue_stmt ;
//break_stmt: 'break';
//continue_stmt: 'continue'; //TODO continue and break
return_stmt: 'return' (test)?;


//Parsing function
varargslist: NAME DOUBE_DOT a_type (',' NAME DOUBE_DOT a_type)*;

argslist: test (',' test)*;

parameters: '(' (argslist)? ')';
varparameters: '(' (varargslist)? ')';
listparameters: '[' (argslist)? ']';

funcdef: 'def'  NAME DOUBE_DOT d_type varparameters block;

