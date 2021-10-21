"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor, Utils):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        env = []
        for x in ast.decl:
            env += [x.accept(self, env)]

    def visitVarDecl(self, ast, c):
        pass

    def visitConstDecl(self, ast, c):
        pass

    def visitClassDecl(self, ast, c):
        # classname : Id    memlist : List[MemDecl]    parentname : Id = None
        # print(type(ast), type(ast.parentname))
        localVar = []
        name = ast.classname.accept(self, c)
        print(name)
        print(ast.parentname)
        # parent = ast.parentname.accept(self, c) if ast.parentname != None else None
        # if parent != None:
        #     if parent not in c:
        #         raise Undeclared("Class", parent)
        localVar += ["concac"]
        c.append({"class": name, "local": localVar})
        
    def visitStatic(self, ast, c):
        pass

    def visitInstance(self, ast, c):
        pass

    def visitMethodDecl(self, ast, c):
        pass

    def visitAttributeDecl(self, ast, c):
        pass

    def visitIntType(self, ast, c):
        pass

    def visitFloatType(self, ast, c):
        pass

    def visitBoolType(self, ast, c):
        pass

    def visitStringType(self, ast, c):
        pass

    def visitVoidType(self, ast, c):
        pass

    def visitArrayType(self, ast, c):
        pass

    def visitClassType(self, ast, c):
        pass

    def visitBinaryOp(self, ast, c):
        pass

    def visitUnaryOp(self, ast, c):
        pass

    def visitCallExpr(self, ast, c):
        pass

    def visitNewExpr(self, ast, c):
        pass

    def visitId(self, ast, c):
        return ast.name

    def visitArrayCell(self, ast, c):
        pass

    def visitFieldAccess(self, ast, c):
        pass

    def visitBlock(self, ast, c):
        pass

    def visitIf(self, ast, c):
        pass

    def visitFor(self, ast, c):
        pass

    def visitContinue(self, ast, c):
        pass

    def visitBreak(self, ast, c):
        pass

    def visitReturn(self, ast, c):
        pass

    def visitAssign(self, ast, c):
        pass

    def visitCallStmt(self, ast, c):
        pass

    def visitIntLiteral(self, ast, c):
        pass

    def visitFloatLiteral(self, ast, c):
        pass

    def visitBooleanLiteral(self, ast, c):
        pass

    def visitStringLiteral(self, ast, c):
        pass

    def visitNullLiteral(self, ast, c):
        pass

    def visitSelfLiteral(self, ast, c):
        pass

    def visitArrayLiteral(self, ast, c):
        pass
