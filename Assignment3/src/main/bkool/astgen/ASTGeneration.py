from BKOOLVisitor import BKOOLVisitor
from BKOOLParser import BKOOLParser
from AST import *
from functools import reduce

from main.bkool.utils.AST import *

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
        elif ctx.methodDecl():
            return ctx.methodDecl().accept(self)
    
    def visitAttributeDecl(self, ctx: BKOOLParser.AttributeDeclContext):
        # attributeDecl: immutableAttrDecl | mutableAttrDecl | mutableObjAttrDecl;
        if ctx.immutableAttrDecl():
            return ctx.immutableAttrDecl().accept(self)
        elif ctx.mutableAttrDecl():
            return ctx.mutableAttrDecl().accept(self)
        else:
            return ctx.mutableObjAttrDecl().accept(self)
               
    def visitImmutableAttrDecl(self, ctx: BKOOLParser.ImmutableAttrDeclContext):
        # immutableAttrDecl: (FINAL | FINAL STATIC | STATIC FINAL) attributeType (ID immutableInitialize) (COMMA (ID immutableInitialize))* S_COLON;
        kind = Instance() if (not ctx.STATIC()) else Static()
        type = ctx.attributeType().accept(self)
        def mapImmutable(id, expr):
            return AttributeDecl(kind, ConstDecl(Id(id.getText()), type, expr.accept(self)))
        return list(map(mapImmutable, ctx.ID(), ctx.immutableInitialize()))
    
    def visitMutableAttrDecl(self, ctx: BKOOLParser.MutableAttrDeclContext):
        # mutableAttrDecl: (STATIC)? attributeType (ID mutableInitialize) (COMMA (ID mutableInitialize))* S_COLON;
        kind = Instance() if (not ctx.STATIC()) else Static()
        type = ctx.attributeType().accept(self)
        def mapMutable(id, expr):
            return AttributeDecl(kind, VarDecl(Id(id.getText()), type, expr.accept(self)))
        return list(map(mapMutable, ctx.ID(), ctx.mutableInitialize()))

    def visitMutableObjAttrDecl(self, ctx: BKOOLParser.MutableObjAttrDeclContext):
        # mutableObjAttrDecl:  (STATIC)? ID (LSB INTEGER_LITERAL RSB)? (ID mutableObjInitialize) (COMMA (ID mutableObjInitialize))* S_COLON;
        kind = Instance() if (not ctx.STATIC()) else Static()
        type = ClassType(Id(ctx.ID(0).getText())) 
        if ctx.LSB():
            type = ArrayType(int(ctx.INTEGER_LITERAL().getText()), ClassType(Id(ctx.ID(0).getText())))
        def mapMutable(id, expr):
            return AttributeDecl(kind, VarDecl(Id(id.getText()), type, expr.accept(self)))
        return list(map(mapMutable, ctx.ID()[1:], ctx.mutableObjInitialize()))
    
    def visitMutableInitialize(self, ctx: BKOOLParser.MutableInitializeContext):
        # mutableInitialize: (EQUAL_SIGN exp)?;
        return ctx.exp().accept(self) if ctx.exp() else None
    
    def visitMutableObjInitialize(self, ctx: BKOOLParser.MutableObjInitializeContext):
        # mutableObjInitialize: (EQUAL_SIGN objInit)?;
        return None if (not ctx.EQUAL_SIGN()) else ctx.objInit().accept(self)
    
    def visitObjInit(self, ctx: BKOOLParser.ObjInitContext):
        # objInit: (ID | NEW ID listExp);
        if (ctx.getChildCount() > 1):
            return NewExpr(Id(ctx.ID().getText()), ctx.listExp().accept(self))
        return Id(ctx.ID().getText())
    
    def visitImmutableInitialize(self, ctx: BKOOLParser.ImmutableInitializeContext):
        # immutableInitialize: (EQUAL_SIGN exp)?;
        return ctx.exp().accept(self) if ctx.exp() else None
    
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
        return ArrayType(int(ctx.INTEGER_LITERAL().getText()), ctx.scalarType().accept(self))
    
    def visitMethodDecl(self, ctx: BKOOLParser.MethodDeclContext):
        # methodDecl: constructorDecl | normalMethodDecl | mainMethodDecl;
        if ctx.constructorDecl():
            return ctx.constructorDecl().accept(self)
        elif ctx.normalMethodDecl():
            return ctx.normalMethodDecl().accept(self)
        elif ctx.normalVoidMethodDecl():
            return ctx.normalVoidMethodDecl().accept(self)
        else:
            return ctx.mainMethodDecl().accept(self)

    def visitConstructorDecl(self, ctx: BKOOLParser.ConstructorDeclContext):
        # constructorDecl: ID LB paramList? RB cstrBlockStmt;
        paramList = ctx.paramList().accept(self) if ctx.paramList() else []
        return [MethodDecl(Instance(), Id('"<init>"'), paramList, None, ctx.cstrBlockStmt().accept(self))]
    
    def visitMainMethodDecl(self, ctx:BKOOLParser.MainMethodDeclContext):
        # mainMethodDecl: VOID MAIN LB RB voidBlockStmt;
        return [MethodDecl(Static(), Id("main"), [], VoidType(), ctx.voidBlockStmt().accept(self))]
    
    def visitNormalMethodDecl(self, ctx: BKOOLParser.NormalMethodDeclContext):
        # normalMethodDecl: (STATIC)? (attributeType | className) ID LB paramList? RB blockStmt;
        kind = Static() if ctx.STATIC() else Instance()
        returnType = ctx.attributeType().accept(self) if ctx.attributeType() else ctx.className().accept(self)
        block = ctx.blockStmt().accept(self)
        paramList = ctx.paramList().accept(self) if ctx.paramList() else []
        return [MethodDecl(kind, Id(ctx.ID().getText()), paramList, returnType, block)]
    
    def visitNormalVoidMethodDecl(self, ctx: BKOOLParser.NormalVoidMethodDeclContext):
        # normalVoidMethodDecl: (STATIC)? VOID ID LB paramList? RB voidBlockStmt;
        kind = Static() if ctx.STATIC() else Instance()
        returnType = VoidType()
        block = ctx.voidBlockStmt().accept(self)
        paramList = ctx.paramList().accept(self) if ctx.paramList() else []
        return [MethodDecl(kind, Id(ctx.ID().getText()), paramList, returnType, block)]
    
    def visitParamList(self, ctx: BKOOLParser.ParamListContext):
        # paramList: params (S_COLON params)*;
        return reduce(lambda acc, ele: acc + ele.accept(self), ctx.params()[1:], ctx.params(0).accept(self))
    
    def visitParams(self, ctx: BKOOLParser.ParamsContext):
        # params: (monoParams | polyParams);
        return ctx.monoParams().accept(self) if ctx.monoParams() else ctx.polyParams().accept(self)
    
    def visitMonoParams(self, ctx: BKOOLParser.MonoParamsContext):
        # monoParams: paramType monoParam (COMMA monoParam)*;
        type = ctx.paramType().accept(self)
        def mapMonoParam(param):
            return VarDecl(param.accept(self), type, None)
        return list(map(mapMonoParam, ctx.monoParam()))
    
    def visitPolyParams(self, ctx: BKOOLParser.PolyParamsContext):
        # polyParams: polyParam (COMMA polyParam)*;
        return reduce(lambda acc, ele: acc + ele.accept(self), ctx.polyParam()[1:], ctx.polyParam(0).accept(self))
    
    def visitPolyParam(self, ctx: BKOOLParser.PolyParamContext):
        # polyParam: paramType monoParam;
        return [VarDecl(ctx.monoParam().accept(self), ctx.paramType().accept(self), None)]
        
    def visitMonoParam(self, ctx: BKOOLParser.MonoParamContext):
        # monoParam: ID
        return Id(ctx.ID().getText())
    
    def visitParamType(self, ctx: BKOOLParser.ParamTypeContext):
        # paramType: (attributeType | classParamType);
        return ctx.attributeType().accept(self) if ctx.attributeType() else ctx.classParamType().accept(self)
    
    def visitClassParamType(self, ctx:BKOOLParser.ClassParamTypeContext):
        return ctx.className().accept(self)
    
    # STATEMENTS #######################################################################################
    def visitStmt(self, ctx: BKOOLParser.StmtContext):
        # stmt: (assignStmt | ifStmt | forStmt | breakStmt | continueStmt | invokeStmt | returnStmt | blockStmt);
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
        elif ctx.blockStmt():
            return ctx.blockStmt().accept(self)
        
    def visitStmtWithoutReturn(self, ctx: BKOOLParser.StmtWithoutReturnContext):
        # stmtWithoutReturn: (assignStmt | ifStmtWithoutReturn | forStmtWithoutReturn | breakStmt | continueStmt | invokeStmt | voidBlockStmt) ;
        if ctx.assignStmt():
            return ctx.assignStmt().accept(self)
        elif ctx.ifStmtWithoutReturn():
            return ctx.ifStmtWithoutReturn().accept(self)
        elif ctx.forStmtWithoutReturn():
            return ctx.forStmtWithoutReturn().accept(self)
        elif ctx.breakStmt():
            return ctx.breakStmt().accept(self)
        elif ctx.continueStmt():
            return ctx.continueStmt().accept(self)
        elif ctx.invokeStmt():
            return ctx.invokeStmt().accept(self)
        elif ctx.voidBlockStmt():
            return ctx.voidBlockStmt().accept(self)
           
    def visitBlockStmt(self, ctx: BKOOLParser.BlockStmtContext):
        # blockStmt: LP varDecl* stmt* RP;
        varDecls = reduce(lambda acc, ele: acc + ele.accept(self), ctx.varDecl(), [])
        stmts = reduce(lambda acc, ele: acc + [ele.accept(self)], ctx.stmt(), [])
        return Block(varDecls, stmts)
    
    def visitVoidBlockStmt(self, ctx: BKOOLParser.VoidBlockStmtContext):
        # blockStmt: LP varDecl* stmtWithoutReturn* RP;
        varDecls = reduce(lambda acc, ele: acc + ele.accept(self), ctx.varDecl(), [])
        stmts = reduce(lambda acc, ele: acc + [ele.accept(self)], ctx.stmtWithoutReturn(), [])
        return Block(varDecls, stmts)   
        # Visit a parse tree produced by BKOOLParser#cstrBlock.
        
    def visitCstrBlockStmt(self, ctx:BKOOLParser.CstrBlockStmtContext):
        # cstrBlockStmt: LP cstrVarDecl* stmtWithoutReturn* RP;
        varDecls = reduce(lambda acc, ele: acc + ele.accept(self), ctx.cstrVarDecl(), [])
        stmts = reduce(lambda acc, ele: acc + [ele.accept(self)], ctx.stmtWithoutReturn(), [])
        return Block(varDecls, stmts) 
        
    def visitCstrVarDecl(self, ctx:BKOOLParser.CstrVarDeclContext):
        # cstrVarDecl: (immutableCstrVarDecl | mutableCstrVarDecl | mutableObjCstrVarDecl);
        if ctx.immutableCstrVarDecl():
            return ctx.immutableCstrVarDecl().accept(self)
        elif ctx.mutableCstrVarDecl():
            return ctx.mutableCstrVarDecl().accept(self)
        else:
            return ctx.mutableObjCstrVarDecl().accept(self)


    def visitImmutableCstrVarDecl(self, ctx:BKOOLParser.ImmutableCstrVarDeclContext):
        # immutableCstrVarDecl: FINAL attributeType (ID immutableCstrVarInit) (COMMA (ID immutableCstrVarInit))* S_COLON;
        type = ctx.attributeType().accept(self)
        def mapImmutable(id, expr):
            return ConstDecl(Id(id.getText()), type, expr.accept(self))
        return list(map(mapImmutable, ctx.ID(), ctx.immutableCstrVarInit()))


    def visitMutableCstrVarDecl(self, ctx:BKOOLParser.MutableCstrVarDeclContext):
        # mutableCstrVarDecl: attributeType (ID mutableCstrVarInit) (COMMA (ID mutableCstrVarInit))* S_COLON;
        type = ctx.attributeType().accept(self)
        def mapMutable(id, expr):
            return VarDecl(Id(id.getText()), type, expr.accept(self))
        return list(map(mapMutable, ctx.ID(), ctx.mutableCstrVarInit()))


    def visitMutableObjCstrVarDecl(self, ctx:BKOOLParser.MutableObjCstrVarDeclContext):
        # mutableObjCstrVarDecl: ID (LSB INTEGER_LITERAL RSB)? (ID mutableObjCstrVarInit) (COMMA (ID mutableObjCstrVarInit))* S_COLON;
        type = ClassType(Id(ctx.ID(0).getText()))
        if ctx.LSB():
            type = ArrayType(int(ctx.INTEGER_LITERAL().getText()), ClassType(Id(ctx.ID(0).getText())))
        def mapMutable(id, expr):
            return VarDecl(Id(id.getText()), type, expr.accept(self))
        return list(map(mapMutable, ctx.ID()[1:], ctx.mutableObjCstrVarInit()))
    

    def visitImmutableCstrVarInit(self, ctx:BKOOLParser.ImmutableCstrVarInitContext):
        # immutableCstrVarInit: (EQUAL_SIGN exp);
        return ctx.exp().accept(self)


    def visitMutableCstrVarInit(self, ctx:BKOOLParser.MutableCstrVarInitContext):
        # mutableCstrVarInit: (EQUAL_SIGN exp)?;
        return ctx.exp().accept(self) if ctx.EQUAL_SIGN() else NullLiteral()


    def visitMutableObjCstrVarInit(self, ctx:BKOOLParser.MutableObjCstrVarInitContext):
        # mutableObjCstrVarInit: (EQUAL_SIGN objInit)?;
        return ctx.objInit().accept(self) if ctx.EQUAL_SIGN() else None
    
    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        # varDecl: (immutableVarDecl | mutableVarDecl | mutableObjVarDecl);
        if ctx.immutableVarDecl():
            return ctx.immutableVarDecl().accept(self)
        elif ctx.mutableVarDecl():
            return ctx.mutableVarDecl().accept(self)
        else:
            return ctx.mutableObjVarDecl().accept(self)
    
    def visitImmutableVarDecl(self, ctx:BKOOLParser.ImmutableVarDeclContext):
        # immutableVarDecl: FINAL attributeType (ID immutableInitialize) (COMMA (ID immutableInitialize))* S_COLON;
        type = ctx.attributeType().accept(self)
        def mapImmutable(id, expr):
            return ConstDecl(Id(id.getText()), type, expr.accept(self))
        return list(map(mapImmutable, ctx.ID(), ctx.immutableInitialize()))

    def visitMutableVarDecl(self, ctx:BKOOLParser.MutableVarDeclContext):
        # mutableVarDecl: attributeType (ID mutableInitialize) (COMMA (ID mutableInitialize))* S_COLON;
        type = ctx.attributeType().accept(self)
        def mapMutable(id, expr):
            return VarDecl(Id(id.getText()), type, expr.accept(self))
        return list(map(mapMutable, ctx.ID(), ctx.mutableInitialize()))

    def visitMutableObjVarDecl(self, ctx:BKOOLParser.MutableObjVarDeclContext):
        # mutableObjVarDecl: ID (LSB INTEGER_LITERAL RSB)? (ID mutableObjInitialize) (COMMA (ID mutableObjInitialize))* S_COLON;
        type = ClassType(Id(ctx.ID(0).getText()))
        if ctx.LSB():
            type = ArrayType(int(ctx.INTEGER_LITERAL().getText()), ClassType(Id(ctx.ID(0).getText())))
        def mapMutable(id, expr):
            return VarDecl(Id(id.getText()), type, expr.accept(self))
        return list(map(mapMutable, ctx.ID()[1:], ctx.mutableObjInitialize()))

    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        # assignStmt: lhs ASSIGN exp S_COLON;
        return Assign(ctx.lhs().accept(self), ctx.exp().accept(self))
    
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        #lhs: ID | (ID | THIS) DOT (ID (LSB exp RSB)?) | ID LSB exp RSB;
        if ctx.getChildCount() == 1:
            return Id(ctx.ID(0).getText())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.ID(0).getText()), ctx.exp().accept(self))
        else:
            if ctx.getChildCount() == 3:
                return FieldAccess(Id(ctx.getChild(0).getText()) if ctx.ID() else SelfLiteral(),Id(ctx.getChild(2).getText()))
            else:
                return FieldAccess(Id(ctx.getChild(0).getText()) if ctx.ID() else SelfLiteral(), ArrayCell(Id(ctx.getChild(2).getText()), ctx.exp().accept(self)))
    
    def visitInvokeStmt(self, ctx: BKOOLParser.InvokeStmtContext):
        # invokeStmt: exp DOT ID listExp S_COLON;
        return CallStmt(ctx.exp().accept(self), Id(ctx.ID().getText()), ctx.listExp().accept(self))
    
    def visitIfStmt(self, ctx: BKOOLParser.IfStmtContext):
        # ifStmt: IF exp THEN stmt (ELSE stmt)?; 
        return If(ctx.exp().accept(self), ctx.stmt(0).accept(self), ctx.stmt(1).accept(self) if ctx.stmt(1) else None)
    
    def visitIfStmtWithoutReturn(self, ctx:BKOOLParser.IfStmtWithoutReturnContext):
        # ifStmtWithoutReturn: IF exp THEN stmtWithoutReturn (ELSE stmtWithoutReturn)?;
        return If(ctx.exp().accept(self), ctx.stmtWithoutReturn(0).accept(self), ctx.stmtWithoutReturn(1).accept(self) if ctx.stmtWithoutReturn(1) else None)
    
    def visitForStmt(self, ctx: BKOOLParser.ForStmtContext):
        # forStmt: FOR scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmt;
        return For(ctx.scalarVar().accept(self), ctx.exp(0).accept(self), ctx.exp(1).accept(self), True if ctx.TO() else False, ctx.stmt().accept(self))

    def visitForStmtWithoutReturn(self, ctx:BKOOLParser.ForStmtWithoutReturnContext):
        # forStmtWithoutReturn: FOR scalarVar ASSIGN exp (TO | DOWNTO) exp DO stmtWithoutReturn;
        return For(ctx.scalarVar().accept(self), ctx.exp(0).accept(self), ctx.exp(1).accept(self), True if ctx.TO() else False, ctx.stmtWithoutReturn().accept(self))
    
    def visitScalarVar(self, ctx: BKOOLParser.ScalarVarContext):
        # scalarVar: ID
        return Id(ctx.ID().getText())
    
    def visitContinueStmt(self, ctx: BKOOLParser.ContinueStmtContext):
        # continueStmt: CONTINUE S_COLON;
        return Continue()
    
    def visitBreakStmt(self, ctx: BKOOLParser.BreakStmtContext):
        # breakStmt: BREAK S_COLON;
        return Break()
    
    def visitReturnStmt(self, ctx: BKOOLParser.ReturnStmtContext):
        # returnStmt: RETURN exp S_COLON;
        return Return(ctx.exp().accept(self))   
    
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
        # exp9: exp9 DOT exp10 listExp? | exp10;
        if not ctx.DOT():
            return ctx.exp10().accept(self)
        else:
            if not ctx.listExp():
                return FieldAccess(ctx.exp9().accept(self), ctx.exp10().accept(self))
            return CallExpr(ctx.exp9().accept(self), ctx.exp10().accept(self), ctx.listExp().accept(self))
        
    def visitExp10(self, ctx: BKOOLParser.Exp10Context):
        # exp10: NEW exp10 listExp | exp11;
        if not ctx.NEW():
            return ctx.exp11().accept(self)
        return NewExpr(ctx.exp10().accept(self), ctx.listExp().accept(self))
    
    def visitExp11(self, ctx: BKOOLParser.Exp11Context):
        # exp11: LB exp RB| literal | ID | methodInvoke | THIS | array_literal;
        if ctx.exp():
            return ctx.exp().accept(self)
        elif ctx.literal():
            return ctx.literal().accept(self)
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.methodInvoke():
            return ctx.methodInvoke().accept(self)
        elif ctx.THIS():
            return SelfLiteral()
        elif ctx.array_literal():
            return ctx.array_literal().accept(self)
        
    def visitMethodInvoke(self, ctx: BKOOLParser.MethodInvokeContext):
        # methodInvoke: ID listExp;
        return ctx.ID().getText() + ctx.listExp().accept(self)
    
    def visitListExp(self, ctx: BKOOLParser.ListExpContext):
        # listExp: (LB arguList? RB);
        return ctx.arguList().accept(self) if ctx.arguList() else []
    
    def visitArguList(self, ctx: BKOOLParser.ArguListContext):
        # arguList: exp (COMMA exp)*;
        return reduce(lambda acc, ele: acc + [ele.accept(self)], ctx.exp()[1:], [ctx.exp(0).accept(self)])
    
    def visitLiteral(self, ctx: BKOOLParser.LiteralContext):
        # literal:	(INTEGER_LITERAL|FLOAT_LITERAL|bool_literal|STRING_LITERAL);
        if ctx.INTEGER_LITERAL():
            return IntLiteral(int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.bool_literal():
            return ctx.bool_literal().accept(self)
        else:
            return StringLiteral(ctx.STRING_LITERAL().getText())
    def visitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        value = reduce(lambda acc, ele: acc + [ele.accept(self)], ctx.literal()[1:], [ctx.literal(0).accept(self)])
        return ArrayLiteral(value)
        
    def visitBool_literal(self, ctx: BKOOLParser.Bool_literalContext):
        value = ctx.TRUE().getText() if ctx.TRUE() else ctx.FALSE().getText()
        return BooleanLiteral(bool(value))
    
    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return ClassType(Id(ctx.ID().getText()))