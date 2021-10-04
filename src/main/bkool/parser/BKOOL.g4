// Student ID: 1852236
grammar BKOOL;

@lexer::header {
from lexererr import *

}

options {
	language = Python3;
}

//	program

program: classDecl+ EOF;

////	class

classDecl: CLASS ID (EXTENDS ID)? LP memDecl* RP;
memDecl: attributeDecl | methodDecl;

////////	attribute

// attributeDecl: (FINAL | FINAL STATIC | STATIC | STATIC FINAL)? attributeType (ID attributeAssign) (COMMA (ID attributeAssign))* S_COLON;
// attributeAssign: (EQUAL_SIGN exp)?;

attributeDecl: immutableAttrDecl | mutableAttrDecl | mutableObjAttrDecl;
immutableAttrDecl: (FINAL | FINAL STATIC | STATIC FINAL) attributeType (ID immutableInitialize) (COMMA (ID immutableInitialize))* S_COLON;
mutableAttrDecl: (STATIC)? attributeType (ID mutableInitialize) (COMMA (ID mutableInitialize))* S_COLON;
mutableObjAttrDecl:  (STATIC)? ID (LSB INTEGER_LITERAL RSB)? (ID mutableObjInitialize) (COMMA (ID mutableObjInitialize))* S_COLON;

immutableInitialize: (EQUAL_SIGN exp);
mutableInitialize: (EQUAL_SIGN exp)?;
// mutableObjInitialize: (EQUAL_SIGN exp10)?;
mutableObjInitialize: (EQUAL_SIGN objInit)?;
objInit: (ID | NEW ID listExp);

attributeType: compositeType | scalarType;
scalarType: INT | FLOAT | STRING | BOOLEAN;
compositeType: scalarType LSB INTEGER_LITERAL RSB;

////////	method

methodDecl: constructorDecl | normalMethodDecl | mainMethodDecl | normalVoidMethodDecl;

constructorDecl: ID LB paramList? RB voidBlockStmt;

normalMethodDecl: (STATIC)? (attributeType | className) ID LB paramList? RB blockStmt;

normalVoidMethodDecl: (STATIC)? VOID ID LB paramList? RB voidBlockStmt;

mainMethodDecl: VOID MAIN LB RB voidBlockStmt;

paramList: params (S_COLON params)*;

params: (monoParams | polyParams);

monoParams: paramType monoParam (COMMA monoParam)*;

polyParams: polyParam (COMMA polyParam)*;

paramType: (attributeType | classParamType);

classParamType: className;

polyParam: paramType monoParam;

monoParam: ID;



// attributeType: INT | FLOAT | STRING | BOOLEAN;
returnType: attributeType | VOID;

////	statement

stmt: (assignStmt | ifStmt | forStmt | breakStmt | continueStmt | invokeStmt | returnStmt | blockStmt);
blockStmt: LP varDecl* stmt* RP;
stmtWithoutReturn: (assignStmt | ifStmtWithoutReturn | forStmtWithoutReturn | breakStmt | continueStmt | invokeStmt | voidBlockStmt) ;
voidBlockStmt: LP varDecl* stmtWithoutReturn* RP;

varDecl: (immutableVarDecl | mutableVarDecl | mutableObjVarDecl);

immutableVarDecl: FINAL? attributeType (ID immutableInitialize) (COMMA (ID immutableInitialize))* S_COLON;
mutableVarDecl: attributeType (ID mutableInitialize) (COMMA (ID mutableInitialize))* S_COLON;
mutableObjVarDecl: ID (LSB INTEGER_LITERAL RSB)? (ID mutableObjInitialize) (COMMA (ID mutableObjInitialize))* S_COLON;

scalarVar: ID;

assignStmt: lhs ASSIGN exp S_COLON;

// lhs: (arrayVar | scalarVar | attrAccess);
lhs: exp;

ifStmt: IF exp THEN stmt (ELSE stmt)?;
ifStmtWithoutReturn: IF exp THEN stmtWithoutReturn (ELSE stmtWithoutReturn)?;


forStmt: FOR scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmt;
forStmtWithoutReturn: FOR scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmtWithoutReturn;



invokeStmt: exp DOT ID listExp S_COLON;
arrayVar: ID indexOp;
breakStmt: BREAK S_COLON;
continueStmt: CONTINUE S_COLON;
returnStmt: RETURN exp S_COLON;

className: ID;
////	expressions

exp: exp1 relational exp1 | exp1;
exp1: exp2 equality exp2 | exp2;
exp2: exp2 logical exp3 | exp3;
exp3: exp3 adding exp4 | exp4;
exp4: exp4 multiply exp5 | exp5;
exp5: exp5 CONCATENATE exp6 | exp6;
exp6: NOT exp6 | exp7;
exp7: adding exp7 | exp8;
exp8: exp8 indexOp | exp9;
exp9: exp9 DOT exp10 listExp? | exp10;
exp10: NEW exp10 listExp | exp11;
exp11: LB exp RB| literal | ID | methodInvoke | THIS | array_literal;

adding: PLUS | MINUS;
multiply: MULTIPLY | MODULUS | F_DIVIDE | I_DIVIDE;
logical: AND | OR; 
equality: EQUAL | NOT_EQUAL;
relational: LESS | GREATER | LESS_EQUAL | GREATER_EQUAL;
indexOp: LSB exp RSB;
methodInvoke: ID listExp;
listExp: (LB arguList? RB);
arguList: exp (COMMA exp)*;

////	comment

LINECOMMENT: 	'#' .*? ('\n' | EOF) -> skip;
BLOCKCOMMENT: 	'/*' .*? '*/' -> skip;



////	keyword

////////	special

MAIN: 			'main';
EQUAL_SIGN:		'=';
ASSIGN:			':=';

////////	function

RETURN: 		'return';

////////	boolean

TRUE: 			'true';
FALSE: 			'false';

////////	conditional

ELSE: 			'else';
IF: 			'if';
THEN: 			'then';

////////	type

VOID: 			'void';
INT: 			'int';
FLOAT: 			'float';
STRING: 		'string';
BOOLEAN: 		'boolean';

////////	loop

FOR: 			'for';
TO: 			'to';
DOWNTO: 		'downto';
DO: 			'do';
BREAK: 			'break';
CONTINUE: 		'continue';

////////	class

CLASS: 			'class';
EXTENDS: 		'extends';
NEW: 			'new';
NIL: 			'nil';
THIS: 			'this';
FINAL: 			'final';
STATIC: 		'static';

////	operator
////////	logical

AND: 			'&&';
OR: 			'||';
NOT:			'!'	;

////////	relational

LESS:			'<'	;
GREATER:		'>'	;
EQUAL:			'==';
NOT_EQUAL:		'!=';
LESS_EQUAL:		'<=';
GREATER_EQUAL:	'>=';	

////////	arithmetic

PLUS:			'+'	;
MINUS:			'-'	;
MULTIPLY:		'*'	;	
MODULUS:		'%'	;
I_DIVIDE:		'\\';
F_DIVIDE:		'/'	;

////////	special

CONCATENATE:	'^'	;
OBJECT_NEW:		NEW	;

////	separator

LP:				'{'	;
RP:				'}'	;
LB:				'('	;
RB:				')'	;
LSB:			'['	;
RSB:			']'	;
DOT:			'.'	;
COMMA:			','	;
COLON:			':'	;
S_COLON:		';'	;


WS : 				[ \t\f\r\n]+ -> skip ;
INTEGER_LITERAL:	DIGIT+;
FLOAT_LITERAL:		DIGIT+	(DECIMAL	|	EXPONENT	|	DECIMAL EXPONENT);
bool_literal:		TRUE | FALSE;
STRING_LITERAL:		["] STR_CHAR* ["] {self.text = self.text[1:-1]};
literal:			(INTEGER_LITERAL	|	FLOAT_LITERAL	|	bool_literal	|	STRING_LITERAL);
array_literal:		LP literal (COMMA literal)* RP;

fragment EXPONENT:		[eE] SIGN? DIGIT+;
fragment SIGN: 			(PLUS | MINUS);
fragment DECIMAL:		DOT DIGIT*;
fragment DIGIT: 		[0-9];
fragment STR_CHAR: 		ESC_SEQ		|	~([\r\n\\"]);
fragment ESC_SEQ: 		'\\' [bfrnt"\\];
fragment ILL_ESCAPE: 	'\\' ~([bfrnt"\\]) | ~'\\';

ID: [_a-zA-Z][_a-zA-Z0-9]*;

UNCLOSE_STRING: ["] STR_CHAR* ('\u000a' | '\r' | ~'"' | EOF)
{
	output = str(self.text)
	err = ['\u000a', '\r', EOFError]
	if (output[-1] in err):
		raise UncloseString(output[1:-1])
	else:
		raise UncloseString(output[1:])
};
ILLEGAL_ESCAPE: ["] STR_CHAR* ILL_ESCAPE 
{
	raise IllegalEscape(self.text[1:])	
};
ERROR_CHAR: .
{	
	raise ErrorToken(self.text)
};