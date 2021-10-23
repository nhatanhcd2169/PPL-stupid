"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *

from main.bkool.utils.AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("readInt", MType([], IntType())),
        Symbol("writeInt", MType([IntType()], VoidType())),
        Symbol("writeIntLn", MType([IntType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("writeFloatLn", MType([FloatType()], VoidType())),
        Symbol("readBool", MType([], BoolType())),
        Symbol("writeBool", MType([BoolType()], VoidType())),
        Symbol("writeBoolLn", MType([BoolType()], VoidType())),
        Symbol("readStr", MType([], StringType())),
        Symbol("writeStr", MType([StringType()], VoidType())),
        Symbol("writeStrLn", MType([StringType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        env = [{"global": c}]
        for x in ast.decl:
            env += [x.accept(self, env)]

    def lookupVariable(self, name, env):
        for index, item in enumerate(env):
            if item:
                if index > 0:
                    print("I am iterating classes (class - local)")
                else:
                    print("I am in global scope")
        return False, None

    def visitVarDecl(self, ast, c):
        # print("ENV:", c)
        name = ast.variable.accept(self, c)
        type = ast.varType.accept(self, c)
        init = ast.varInit.accept(self, c) if ast.varInit else None
        # print("VAR:", name, type, init)
        raise Undeclared(Variable(), "Debugging")

    def visitConstDecl(self, ast, c):
        name = ast.constant.accept(self, c)
        type = ast.constType.accept(self, c)
        init = ast.value.accept(self, c)
        # print("CONST:", name, type, init)
        raise Undeclared(Constant(), "Debugging")

    def lookupClass(self, name, env):
        if len(env) > 1:
            for index, item in enumerate(env):
                if index > 0 and item:
                    if item["class"] == name:
                        return True, index
        return False, None

    def referenceClass(self, classname, parentname, env):
        lookupName = self.lookupClass(classname, env)
        lookupParent = self.lookupClass(parentname, env)
        if lookupName[0]:
            raise Redeclared(Class(), classname)
        if parentname != None:
            if not lookupParent[0]:
                raise Undeclared(Class(), parentname)
            else:
                return env[lookupParent[1]]["local"]
        return []

    def visitClassDecl(self, ast, c):
        localVar = [c[0]['global']]
        name = ast.classname.accept(self, c)
        parent = ast.parentname.accept(self, c) if ast.parentname else None
        localVar += self.referenceClass(name, parent, c)
        for mem in ast.memlist:
            mem.accept(self, localVar)
        c.append({"class": name, "local": localVar})

    def visitStatic(self, ast, c):
        pass

    def visitInstance(self, ast, c):
        pass

    def visitMethodDecl(self, ast, c):
        raise Undeclared(Method(), "Debugging")

    def visitAttributeDecl(self, ast, c):
        kind = ast.kind
        decl = ast.decl.accept(self, c)

    def visitIntType(self, ast, c):
        return "int"

    def visitFloatType(self, ast, c):
        return "float"

    def visitBoolType(self, ast, c):
        return "bool"

    def visitStringType(self, ast, c):
        return "string"

    def visitVoidType(self, ast, c):
        return "void"

    def visitArrayType(self, ast, c):
        return "array"

    def visitClassType(self, ast, c):
        return "class"

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
