# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classDecl.
    def visitClassDecl(self, ctx:BKOOLParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memDecl.
    def visitMemDecl(self, ctx:BKOOLParser.MemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeDecl.
    def visitAttributeDecl(self, ctx:BKOOLParser.AttributeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableAttrDecl.
    def visitImmutableAttrDecl(self, ctx:BKOOLParser.ImmutableAttrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableAttrDecl.
    def visitMutableAttrDecl(self, ctx:BKOOLParser.MutableAttrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#immutableAttrAssign.
    def visitImmutableAttrAssign(self, ctx:BKOOLParser.ImmutableAttrAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mutableAttrAssign.
    def visitMutableAttrAssign(self, ctx:BKOOLParser.MutableAttrAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributeType.
    def visitAttributeType(self, ctx:BKOOLParser.AttributeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalarType.
    def visitScalarType(self, ctx:BKOOLParser.ScalarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#compositeType.
    def visitCompositeType(self, ctx:BKOOLParser.CompositeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objectDecl.
    def visitObjectDecl(self, ctx:BKOOLParser.ObjectDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objList.
    def visitObjList(self, ctx:BKOOLParser.ObjListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objInit.
    def visitObjInit(self, ctx:BKOOLParser.ObjInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodDecl.
    def visitMethodDecl(self, ctx:BKOOLParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructorDecl.
    def visitConstructorDecl(self, ctx:BKOOLParser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#normalMethodDecl.
    def visitNormalMethodDecl(self, ctx:BKOOLParser.NormalMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mainMethodDecl.
    def visitMainMethodDecl(self, ctx:BKOOLParser.MainMethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramList.
    def visitParamList(self, ctx:BKOOLParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#monoParams.
    def visitMonoParams(self, ctx:BKOOLParser.MonoParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#polyParams.
    def visitPolyParams(self, ctx:BKOOLParser.PolyParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramType.
    def visitParamType(self, ctx:BKOOLParser.ParamTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classParamType.
    def visitClassParamType(self, ctx:BKOOLParser.ClassParamTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#polyParam.
    def visitPolyParam(self, ctx:BKOOLParser.PolyParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#monoParam.
    def visitMonoParam(self, ctx:BKOOLParser.MonoParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnType.
    def visitReturnType(self, ctx:BKOOLParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockStmt.
    def visitBlockStmt(self, ctx:BKOOLParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtWithoutReturn.
    def visitStmtWithoutReturn(self, ctx:BKOOLParser.StmtWithoutReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#voidBlockStmt.
    def visitVoidBlockStmt(self, ctx:BKOOLParser.VoidBlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#varDecl.
    def visitVarDecl(self, ctx:BKOOLParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objectVars.
    def visitObjectVars(self, ctx:BKOOLParser.ObjectVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objectVar.
    def visitObjectVar(self, ctx:BKOOLParser.ObjectVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalarVars.
    def visitScalarVars(self, ctx:BKOOLParser.ScalarVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#scalarVar.
    def visitScalarVar(self, ctx:BKOOLParser.ScalarVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayVars.
    def visitArrayVars(self, ctx:BKOOLParser.ArrayVarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assignStmt.
    def visitAssignStmt(self, ctx:BKOOLParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrAccess.
    def visitAttrAccess(self, ctx:BKOOLParser.AttrAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instanceName.
    def visitInstanceName(self, ctx:BKOOLParser.InstanceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#objName.
    def visitObjName(self, ctx:BKOOLParser.ObjNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attrName.
    def visitAttrName(self, ctx:BKOOLParser.AttrNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmt.
    def visitIfStmt(self, ctx:BKOOLParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifStmtWithoutReturn.
    def visitIfStmtWithoutReturn(self, ctx:BKOOLParser.IfStmtWithoutReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmt.
    def visitForStmt(self, ctx:BKOOLParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forStmtWithoutReturn.
    def visitForStmtWithoutReturn(self, ctx:BKOOLParser.ForStmtWithoutReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invokeStmt.
    def visitInvokeStmt(self, ctx:BKOOLParser.InvokeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arrayVar.
    def visitArrayVar(self, ctx:BKOOLParser.ArrayVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakStmt.
    def visitBreakStmt(self, ctx:BKOOLParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continueStmt.
    def visitContinueStmt(self, ctx:BKOOLParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnStmt.
    def visitReturnStmt(self, ctx:BKOOLParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#className.
    def visitClassName(self, ctx:BKOOLParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp11.
    def visitExp11(self, ctx:BKOOLParser.Exp11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#adding.
    def visitAdding(self, ctx:BKOOLParser.AddingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#multiply.
    def visitMultiply(self, ctx:BKOOLParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#logical.
    def visitLogical(self, ctx:BKOOLParser.LogicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#equality.
    def visitEquality(self, ctx:BKOOLParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#relational.
    def visitRelational(self, ctx:BKOOLParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#indexOp.
    def visitIndexOp(self, ctx:BKOOLParser.IndexOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodInvoke.
    def visitMethodInvoke(self, ctx:BKOOLParser.MethodInvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listExp.
    def visitListExp(self, ctx:BKOOLParser.ListExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arguList.
    def visitArguList(self, ctx:BKOOLParser.ArguListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_literal.
    def visitBool_literal(self, ctx:BKOOLParser.Bool_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_literal.
    def visitArray_literal(self, ctx:BKOOLParser.Array_literalContext):
        return self.visitChildren(ctx)



del BKOOLParser