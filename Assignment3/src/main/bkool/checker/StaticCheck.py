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
        # Symbol("readInt", MType([], IntType())),
        # Symbol("writeInt", MType([IntType()], VoidType())),
        # Symbol("writeIntLn", MType([IntType()], VoidType())),
        # Symbol("readFloat", MType([], FloatType())),
        # Symbol("writeFloat", MType([FloatType()], VoidType())),
        # Symbol("writeFloatLn", MType([FloatType()], VoidType())),
        # Symbol("readBool", MType([], BoolType())),
        # Symbol("writeBool", MType([BoolType()], VoidType())),
        # Symbol("writeBoolLn", MType([BoolType()], VoidType())),
        # Symbol("readStr", MType([], StringType())),
        # Symbol("writeStr", MType([StringType()], VoidType())),
        # Symbol("writeStrLn", MType([StringType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast

    def getClass(self, obj):
        return obj.__class__.__name__

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        # print("\n\nprogram", ast)
        env = [{"global": c}]
        # print("env:", env)
        for x in ast.decl:
            env += [x.accept(self, env)]

    def lookupVariable(self, name, env):
        # print("finding", name, "in env:", env)
        for index, item in enumerate(env):
            if item:
                if index > 0:
                    if item["name"] == name:
                        return True, item["type"], index
                else:
                    for x in item["global"]:
                        if type(x) is not Symbol and x["name"] == name:
                            return True, x["type"], index
        return False, None, None

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
            return {"type": type, "name": name, "value_type": init, "const": False}
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
            return {"type": type, "name": name, "value_type": init, "const": True}
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
        nameclass = ast.classname.accept(self, c)
        parentclass = ast.parentname.accept(self, c) if ast.parentname else None
        localVar += self.referenceClass(nameclass, parentclass, c)
        attr = []
        for mem in ast.memlist:
            if self.getClass(mem) == "AttributeDecl":
                name = (
                    mem.decl.variable.name
                    if (self.getClass(mem.decl) == "VarDecl")
                    else mem.decl.constant.name
                )
                if name not in attr:
                    if mem.kind.accept(self, c) == "Instance":
                        localVar.append(mem.accept(self, localVar))
                    else:
                        member = mem.accept(self, localVar)
                        localVar[0]["global"].append(member)
                        c[0]["global"] = localVar[0]["global"]
                    attr.append(name)
                else:
                    raise Redeclared(Attribute(), name)
        for mem in ast.memlist:
            if self.getClass(mem) == "MethodDecl":
                mem.accept(self, localVar)
        c.append({"class": nameclass, "local": localVar[1:]})
        
    def visitStatic(self, ast, c):
        return "Static"

    def visitInstance(self, ast, c):
        return "Instance"

    def visitMethodDecl(self, ast, c):
        body = ast.body.accept(self, c)

    def visitAttributeDecl(self, ast, c):
        name = (
            ast.decl.variable.name
            if (self.getClass(ast.decl) == "VarDecl")
            else ast.decl.constant.name
        )
        find = self.lookupVariable(name, c)
        if find[0]:
            # replace at index
            if find[2] > 0:
                c[find[2]]["type"] = find[1]
            else:
                raise Redeclared(Attribute(), name)
        else:
            return ast.decl.accept(self, c)

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
        op = ast.op
        left = ast.left.accept(self, c)
        right = ast.right.accept(self, c)
        hybrid = ["+", "-", "*", "/", "<", "<=", ">", ">="]
        if op in hybrid:
            if left == "float" or right == "float":
                return "float"
            return "int"

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
                forStack.push(stmt)
            if self.getClass(stmt) in ["Continue", "Break"]:
                res = forStack.pop()
                if not res:
                    raise MustInLoop(stmt)
            stmt.accept(self, c)

    def visitIf(self, ast, c):
        pass

    def visitFor(self, ast, c):
        stmt = ast.loop.accept(self, c)

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
