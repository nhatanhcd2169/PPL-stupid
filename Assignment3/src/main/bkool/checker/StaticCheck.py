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


class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
    def length(self):
        return len(self.stack)
    def top(self):
        return self.stack[-1]
    def push(self, x):
        self.x = x
        self.stack.append(x)
    def pop(self):
        try:
            self.stack.pop()
            return True
        except IndexError:
            return False

class StaticChecker(BaseVisitor, Stack):

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

    def getClass(self, obj):
        return obj.__class__.__name__

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        env = [c]
        for x in ast.decl:
            env += [x.accept(self, env)]

    def lookupVariable(self, name, env):
        for index, item in enumerate(env):
            if item:
                if index > 0:
                    if item["name"] == name:
                        return True, item["type"]
                else:
                    for x in item:
                        if isinstance(x, dict) and x == name:
                            return True, x["type"]
        return False, None

    def checkType(self, type, init):
        if init == type:
            return True, "Literal"
        else:
            if init not in ["int", "float", "string", "boolean"]:
                return False, "Id_Or_Op"
        return False, "Literal"

    def visitVarDecl(self, ast, c):
        name = ast.variable.accept(self, c)
        type = ast.varType.accept(self, c)
        init = ast.varInit.accept(self, c) if ast.varInit else None
        if not self.lookupVariable(name, c)[0]:
            return {"type": type, "name": name}
        else:
            raise Redeclared(Variable(), name)

    def visitConstDecl(self, ast, c):
        name = ast.constant.accept(self, c)
        type = ast.constType.accept(self, c)
        init = ast.value.accept(self, c)
        if not self.checkType(type, init)[0]:
            if self.checkType(type, init)[1] == "Literal":
                raise TypeMismatchInConstant(ast)
            else:
                raise IllegalConstantExpression(ast.value)
        if not self.lookupVariable(name, c)[0]:
            return {"type": type, "name": name}
        else:
            raise Redeclared(Constant(), name)

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
        localVar = [c[0]]
        name = ast.classname.accept(self, c)
        parent = ast.parentname.accept(self, c) if ast.parentname else None
        localVar += self.referenceClass(name, parent, c)
        for mem in ast.memlist:
            if self.getClass(mem)== "AttributeDecl":
                localVar.append(mem.accept(self, localVar))
        for mem in ast.memlist:
            if self.getClass(mem) == "MethodDecl":
                mem.accept(self, localVar)
        c.append({"class": name, "local": localVar[1:]})

    def visitStatic(self, ast, c):
        return "static"

    def visitInstance(self, ast, c):
        return "instance"

    def visitMethodDecl(self, ast, c):
        # print("ENV of method", ast.name.accept(self, c), c[1:])
        body = ast.body.accept(self, c)
        print(body)

    def visitAttributeDecl(self, ast, c):
        kind = ast.kind.accept(self, c)
        # if (kind == "instance"):
        name = (
            ast.decl.variable.name
            if (self.getClass(ast.decl) == "VarDecl")
            else ast.decl.constant.name
        )
        if self.lookupVariable(name, c)[0]:
            raise Redeclared(Attribute(), name)
        else:
            decl = ast.decl.accept(self, c)
            return decl

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
        forStack = Stack()
        for decl in ast.decl:
            decl.accept(self, c)
        for stmt in ast.stmt:
            if self.getClass(stmt) == "For":
                forStack.push()
            if self.getClass(stmt) in ["Continue", "Break"]:
                res = forStack.pop()
                if not res:
                    raise MustInLoop(stmt)
            stmt.accept(self, c)

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
        return "int"

    def visitFloatLiteral(self, ast, c):
        return "float"

    def visitBooleanLiteral(self, ast, c):
        return "bool"

    def visitStringLiteral(self, ast, c):
        return "string"

    def visitNullLiteral(self, ast, c):
        return "null"

    def visitSelfLiteral(self, ast, c):
        return "self"

    def checkTypeArrayLiteral(self, arr, env):
        list = [x.accept(self, env) for x in arr]
        res = all(map(lambda x: x == list[0], list))
        return res, list[0]

    def visitArrayLiteral(self, ast, c):
        res = self.checkTypeArrayLiteral(ast.value, c)
        if not res[0]:
            raise IllegalArrayLiteral(ast)
        return res[1]
