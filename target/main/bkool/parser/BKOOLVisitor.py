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


    # Visit a parse tree produced by BKOOLParser#class_decl.
    def visitClass_decl(self, ctx:BKOOLParser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_body.
    def visitClass_body(self, ctx:BKOOLParser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atb_decl.
    def visitAtb_decl(self, ctx:BKOOLParser.Atb_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atb_init.
    def visitAtb_init(self, ctx:BKOOLParser.Atb_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decls.
    def visitVar_decls(self, ctx:BKOOLParser.Var_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#decl_list.
    def visitDecl_list(self, ctx:BKOOLParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_decl.
    def visitVar_decl(self, ctx:BKOOLParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_decls.
    def visitArray_decls(self, ctx:BKOOLParser.Array_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_list.
    def visitArray_list(self, ctx:BKOOLParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_decl.
    def visitArray_decl(self, ctx:BKOOLParser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_decls.
    def visitObj_decls(self, ctx:BKOOLParser.Obj_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_list.
    def visitObj_list(self, ctx:BKOOLParser.Obj_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#obj_decl.
    def visitObj_decl(self, ctx:BKOOLParser.Obj_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decls.
    def visitMethod_decls(self, ctx:BKOOLParser.Method_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor_decl.
    def visitConstructor_decl(self, ctx:BKOOLParser.Constructor_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_decl.
    def visitMethod_decl(self, ctx:BKOOLParser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_list.
    def visitParam_list(self, ctx:BKOOLParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#params.
    def visitParams(self, ctx:BKOOLParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#one_params.
    def visitOne_params(self, ctx:BKOOLParser.One_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#many_params.
    def visitMany_params(self, ctx:BKOOLParser.Many_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param_type.
    def visitParam_type(self, ctx:BKOOLParser.Param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#var_type.
    def visitVar_type(self, ctx:BKOOLParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_type.
    def visitReturn_type(self, ctx:BKOOLParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#block_stmt.
    def visitBlock_stmt(self, ctx:BKOOLParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_decl.
    def visitStmt_decl(self, ctx:BKOOLParser.Stmt_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#variables.
    def visitVariables(self, ctx:BKOOLParser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_variables.
    def visitArray_variables(self, ctx:BKOOLParser.Array_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#object_variables.
    def visitObject_variables(self, ctx:BKOOLParser.Object_variablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#assign_stmt.
    def visitAssign_stmt(self, ctx:BKOOLParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#lhs.
    def visitLhs(self, ctx:BKOOLParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_var.
    def visitArray_var(self, ctx:BKOOLParser.Array_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#if_stmt.
    def visitIf_stmt(self, ctx:BKOOLParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#for_stmt.
    def visitFor_stmt(self, ctx:BKOOLParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#break_stmt.
    def visitBreak_stmt(self, ctx:BKOOLParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continue_stmt.
    def visitContinue_stmt(self, ctx:BKOOLParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKOOLParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#atb_access.
    def visitAtb_access(self, ctx:BKOOLParser.Atb_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#instance_name.
    def visitInstance_name(self, ctx:BKOOLParser.Instance_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attr_name.
    def visitAttr_name(self, ctx:BKOOLParser.Attr_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#invoke_stmt.
    def visitInvoke_stmt(self, ctx:BKOOLParser.Invoke_stmtContext):
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


    # Visit a parse tree produced by BKOOLParser#relation.
    def visitRelation(self, ctx:BKOOLParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#comparision.
    def visitComparision(self, ctx:BKOOLParser.ComparisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#logic.
    def visitLogic(self, ctx:BKOOLParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#add_minus.
    def visitAdd_minus(self, ctx:BKOOLParser.Add_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#mul_mod_div.
    def visitMul_mod_div(self, ctx:BKOOLParser.Mul_mod_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_op.
    def visitIndex_op(self, ctx:BKOOLParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#method_invo.
    def visitMethod_invo(self, ctx:BKOOLParser.Method_invoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#listExp.
    def visitListExp(self, ctx:BKOOLParser.ListExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arguList.
    def visitArguList(self, ctx:BKOOLParser.ArguListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bool_lit.
    def visitBool_lit(self, ctx:BKOOLParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literal.
    def visitLiteral(self, ctx:BKOOLParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit.
    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return self.visitChildren(ctx)



del BKOOLParser