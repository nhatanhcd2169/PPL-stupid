from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

from main.bkool.utils.AST import ArrayCell, ArrayType, AttributeDecl, Block, ClassDecl, ConstDecl, Instance, IntLiteral, MethodDecl, Static, UnaryOp, VarDecl

class ASTGeneration(BKOOLVisitor):

    def visitProgram(self, ctx: BKOOLParser.ProgramContext):
        # program: classDecl+ EOF;
        return Program(reduce(lambda acc, ele: acc + ele.accept(self), ctx.classDecl(), []))
    
    def visitClassDecl(self, ctx: BKOOLParser.ClassDeclContext):
        # classDecl: CLASS ID (EXTENDS ID)? LP memDecl* RP;
        if ctx.ID(1):
            return [ClassDecl(Id(ctx.ID(0).getText()), reduce(lambda acc, ele: acc + ele.accept(self), ctx.memDecl(), []), Id(ctx.ID(1).getText()))]
        return [ClassDecl(Id(ctx.ID(0).getText()), reduce(lambda acc, ele: acc + ele.accept(self), ctx.memDecl(), []), None)]
      
    def visitMemDecl(self, ctx: BKOOLParser.MemDeclContext):
        # bodyDecl: attributeDecl | objectDecl | methodDecl;
        if ctx.attributeDecl():
            return ctx.attributeDecl().accept(self)
        elif ctx.objectDecl():
            return ctx.objectDecl().accept(self)
        elif ctx.methodDecl():
            return ctx.methodDecl().accept(self)
    
    def visitAttributeDecl(self, ctx: BKOOLParser.AttributeDeclContext):
        # attributeDecl: immutableAttrDecl | mutableAttrDecl;
        return ctx.immutableAttrDecl().accept(self) if ctx.immutableAttrDecl() else ctx.mutableAttrDecl().accept(self)
    
    def visitImmutableAttrDecl(self, ctx: BKOOLParser.ImmutableAttrDeclContext):
        # immutableAttrDecl: (FINAL | FINAL STATIC | STATIC FINAL) attributeType (ID immutableAttrAssign) (COMMA (ID immutableAttrAssign))* S_COLON;
        kind = Instance() if (not ctx.STATIC()) else Static()
        type = ctx.attributeType().accept(self)
        def mapImmutable(id, expr):
            return AttributeDecl(kind, ConstDecl(Id(id.getText()), type, expr.accept(self)))
        return list(map(mapImmutable, ctx.ID(), ctx.immutableAttrAssign()))
    
    def visitMutableAttrDecl(self, ctx: BKOOLParser.MutableAttrDeclContext):
        # mutableAttrDecl: (STATIC)? attributeType (ID mutableAttrAssign) (COMMA (ID mutableAttrAssign))* S_COLON;
        kind = Instance() if (not ctx.STATIC()) else Static()
        type = ctx.attributeType().accept(self)
        def mapMutable(id, expr):
            return AttributeDecl(kind, VarDecl(Id(id.getText()), type, expr.accept(self)))
        return list(map(mapMutable, ctx.ID(), ctx.mutableAttrAssign()))
    
    def visitMutableAttrAssign(self, ctx: BKOOLParser.MutableAttrAssignContext):
        # mutableAttrAssign: (EQUAL_SIGN exp)?;
        return ctx.exp().accept(self) if ctx.exp() else None
    
    
    def visitImmutableAttrAssign(self, ctx: BKOOLParser.ImmutableAttrAssignContext):
        # immutableAttrAssign: (EQUAL_SIGN exp);
        return ctx.exp().accept(self)
    
    def visitAttributeType(self, ctx: BKOOLParser.AttributeTypeContext):
        # attributeType: compositeType | scalarType;
        return ctx.compositeType().accept(self) if ctx.compositeType() else ctx.scalarType().accept(self)
    
    def visitScalarType(self, ctx: BKOOLParser.ScalarTypeContext):
        # scalarType: INT | FLOAT | STRING | BOOLEAN;
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        
    def visitCompositeType(self, ctx: BKOOLParser.CompositeTypeContext):
        # compositeType: scalarType LSB INTEGER_LITERAL RSB; 
        return ArrayType(IntLiteral(int(ctx.INTEGER_LITERAL().getText()), ctx.scalarType().accept(self)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def visitObjectDecl(self, ctx: BKOOLParser.ObjectDeclContext):
        return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def visitMethodDecl(self, ctx: BKOOLParser.MethodDeclContext):
        # methodDecl: constructorDecl | normalMethodDecl;
        if ctx.constructorDecl():
            return ctx.constructorDecl().accept(self)
        return ctx.normalMethodDecl().accept(self)

    
    def visiConstructorDecl(self, ctx: BKOOLParser.ConstructorDeclContext):
        # constructorDecl: ID LB paramList? RB blockStmt;
        paramList = ctx.paramList().accept(self) if ctx.paramList() else []
        return MethodDecl(Instance(), Id("<init>"), paramList, None, ctx.blockStmt().accept(self))
    
    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        # paramList: params (S_COLON params)*;
        return reduce(lambda acc, ele: acc + ele.accept(self), ctx.params()[1:], ctx.params(0).accept(self))
    
    def visitParams(self, ctx: BKOOLParser.ParamsContext):
        return None
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # STATEMENTS #######################################################################################
    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        # stmt: (assignStmt | ifStmt | forStmt | breakStmt | continueStmt | invokeStmt | returnStmt);
        if ctx.assignStmt():
            return ctx.assignStmt().accept(self)
        elif ctx.ifStmt():
            return ctx.ifStmt().accept(self)
        elif ctx.forStmt():
            return ctx.forStmt().accept(self)
        elif ctx.breakStmt():
            return ctx.breakStmt().accept(self)
        elif ctx.continueStmt():
            return ctx.continueStmt().accept(self)
        elif ctx.invokeStmt():
            return ctx.invokeStmt().accept(self)
        elif ctx.returnStmt():
            return ctx.returnStmt().accept(self)
        
        
        
        
        
        
    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):
        # blockStmt: LP varDecl* stmt* RP;
        varDecls = reduce(lambda acc, ele: acc + ele.accept(self), ctx.varDecl(), [])
        stmts = reduce(lambda acc, ele: acc + ele.accept(self), ctx.stmt(), [])
        return Block(varDecls, stmts)
    
    def visitInvokeStmt(self, ctx: BKOOLParser.InvokeStmtContext):
        # invokeStmt: instanceName DOT methodInvoke S_COLON;
        return None
    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext):
        # ifStmt: IF exp THEN (stmt | blockStmt) (ELSE (stmt | blockStmt))?;    
        return None
    
    
    
    
    
    
    
    
    
    
    
    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        # continueStmt: CONTINUE S_COLON;
        return Continue()
    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        # breakStmt: BREAK S_COLON;
        return Break()
    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        # returnStmt: RETURN exp S_COLON;
        return Return(ctx.exp().accept(self))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def visitExp(self, ctx: BKOOLParser.ExpContext):
        return 23115
    
    
    
    # # EXPRESSIONS ######################################################################################
        
    def visitExp(self, ctx: BKOOLParser.ExpContext):
        # exp: exp1 relational exp1 | exp1;
        if ctx.getChildCount() == 1:
            return ctx.exp1(0).accept(self)
        return BinaryOp(ctx.relational().accept(self), ctx.exp1(0).accept(self), ctx.exp1(1).accept(self))
    def visitRelational(self, ctx: BKOOLParser.RelationalContext):
        # relational: LESS | GREATER | LESS_EQUAL | GREATER_EQUAL;
        if ctx.LESS():
            return ctx.LESS().getText()
        elif ctx.GREATER():
            return ctx.GREATER().getText()
        elif ctx.LESS_EQUAL():
            return ctx.LESS_EQUAL().getText()
        elif ctx.GREATER_EQUAL():
            return ctx.GREATER_EQUAL().getText()
    def visitExp1(self, ctx: BKOOLParser.Exp1Context):
        # exp1: exp2 equality exp2 | exp2;
        if ctx.getChildCount() == 1:
            return ctx.exp2(0).accept(self)
        return BinaryOp(ctx.equality().accept(self), ctx.exp2(0).accept(self), ctx.exp2(1).accept(self))
    def visitEquality(self, ctx: BKOOLParser.EqualityContext):
        # equality: EQUAL | NOT_EQUAL;
        return ctx.EQUAL().getText() if ctx.EQUAL() else ctx.NOT_EQUAL().getText()
    def visitExp2(self, ctx: BKOOLParser.Exp2Context):
        # exp2: exp2 logical exp3 | exp3;
        if ctx.getChildCount() == 1:
            return ctx.exp3().accept(self)
        return BinaryOp(ctx.logical().accept(self), ctx.exp2().accept(self), ctx.exp3().accept(self))
    def visitLogical(self, ctx: BKOOLParser.LogicalContext):
        # logical: AND | OR;
        return ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
    def visitExp3(self, ctx: BKOOLParser.Exp3Context): 
        # exp3: exp3 adding exp4 | exp4;
        if ctx.getChildCount() == 1:
            return ctx.exp4().accept(self)
        return BinaryOp(ctx.adding().accept(self), ctx.exp3().accept(self), ctx.exp4().accept(self))
    def visitAdding(self, ctx: BKOOLParser.AddingContext):
        # adding: PLUS | MINUS;
        return ctx.PLUS().getText() if ctx.PLUS() else ctx.MINUS().getText()
    def visitExp4(self, ctx: BKOOLParser.Exp4Context):    
        # exp4: exp4 multiply exp5 | exp5;
        if ctx.getChildCount() == 1:
            return ctx.exp5().accept(self)
        return BinaryOp(ctx.multiply().accept(self), ctx.exp4().accept(self), ctx.exp5().accept(self))
    def visitMultiply(self, ctx: BKOOLParser.MultiplyContext):
        # multiply: MULTIPLY | MODULUS | F_DIVIDE | I_DIVIDE;
        if ctx.MULTIPLY():
            return ctx.MULTIPLY().getText()
        elif ctx.MODULUS():
            return ctx.MODULUS().getText()
        elif ctx.F_DIVIDE():
            return ctx.F_DIVIDE().getText()
        elif ctx.I_DIVIDE():
            return ctx.I_DIVIDE().getText()
    def visitExp5(self, ctx: BKOOLParser.Exp5Context):          
        # exp5: exp5 CONCATENATE exp6 | exp6;
        if ctx.getChildCount() == 1:
            return ctx.exp6().accept(self)
        return BinaryOp(ctx.CONCATENATE().getText(), ctx.exp5().accept(self), ctx.exp6().accept(self))
    def visitExp6(self, ctx: BKOOLParser.Exp6Context):          
        # exp6: NOT exp6 | exp7;
        if ctx.getChildCount() == 1:
            return ctx.exp7().accept(self)
        return UnaryOp(ctx.NOT().getText(), ctx.exp6().accept(self))
    def visitExp7(self, ctx: BKOOLParser.Exp7Context):
        # exp7: adding exp7 | exp8;
        if not ctx.adding():
            return ctx.exp8().accept(self)
        return UnaryOp(ctx.adding().accept(self), ctx.exp7().accept(self))
    
    def visitExp8(self, ctx: BKOOLParser.Exp8Context):
        # exp8: exp8 indexOp | exp9;
        if not ctx.indexOp():
            return ctx.exp9().accept(self)
        return ArrayCell(ctx.exp8().accept(self), ctx.indexOp().accept(self))
    
    def visitIndexOp(self, ctx: BKOOLParser.IndexOpContext):
        # indexOp: LSB exp RSB;
        return ctx.exp().accept(self)
    
    def visitExp9(self, ctx: BKOOLParser.Exp9Context):
        # exp9: exp9 DOT exp10 | exp10;
        if not ctx.DOT():
            return ctx.exp10().accept(self)
        return FieldAccess(ctx.exp9().accept(self), ctx.exp10().accept(self))
    def visitExp10(self, ctx: BKOOLParser.Exp10Context):
        # exp10: NEW exp10 listExp | exp11;
        if not ctx.NEW():
            return ctx.exp11().accept(self)
        return NewExpr(ctx.exp10().accept(self), ctx.listExp().accept(self))
    def visitExp11(self, ctx: BKOOLParser.Exp11Context):
        # exp11: LB exp RB| literal | ID | methodInvoke | THIS;
        if ctx.exp():
            return ctx.exp().accept(self)
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.methodInvoke():
            return ctx.methodInvoke().accept(self)
        elif ctx.THIS():
            return ctx.THIS().getText()
    def visitMethodInvoke(self, ctx: BKOOLParser.MethodInvokeContext):
        # methodInvoke: ID listExp;
        return ctx.ID().getText() + ctx.listExp().accept(self)
    def visitListExp(self, ctx: BKOOLParser.ListExpContext):
        # listExp: (LB arguList? RB);
        if ctx.arguList():
            return ctx.arguList().accept(self) 
    def visitArguList(self, ctx: BKOOLParser.ArguListContext):
        # arguList: exp (COMMA exp)*;
        return reduce(lambda acc, ele: acc + ele.accept(self), ctx.exp()[1:], ctx.exp(0).accept(self))
    
    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        
    






