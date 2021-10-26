"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *

# from main.bkool.utils.AST import *


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
        # print("AST:", ast)
        env = [{"global": c}]
        for x in ast.decl:
            env += [x.accept(self, env)]

    def lookupObject(self, name, env):
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

    def lookupVariable(self, name, env):
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
            if isinstance(type, dict):
                if "array" in type and type["array"] == init:
                    return True, "Literal"
                if "class" in type and type["class"] == init:
                    return False, "Id_Or_Op"
            if init not in ["int", "float", "string", "boolean"]:
                return False, "Id_Or_Op"
        return False, "Literal"

    def varCheck(self, ast, c):
        name = ast.variable.accept(self, c)
        type = ast.varType.accept(self, c)
        init = ast.varInit.accept(self, c) if ast.varInit else [None, True]
        check = self.checkType(type, init[0])
        # if not check[0]:
        #     if check[1] == "Literal":
        #         print("deo cung type cua literal")
        #     else:
        #         print("hinh nhu dung cung may type khac luon")
        return {
            "type": type,
            "name": name,
            "value_type": init[0] if init != None else type,
            "const": False,
        }

    def constCheck(self, ast, c):
        name = ast.constant.accept(self, c)
        type = ast.constType.accept(self, c)
        if self.getClass(ast.value) == "Id":
            lookup = self.lookupVariable(ast.value.accept(self, c), c)
            if lookup[0]:
                if not c[lookup[0]["const"]]:
                    raise IllegalConstantExpression(ast.value)
            else:
                raise IllegalConstantExpression(ast.value)
        init = ast.value.accept(self, c) if ast.value else [None, True]
        check = self.checkType(type, init[0])
        if not init[1]:
            raise IllegalConstantExpression(ast.value)
        if not check[0]:
            if check[1] == "Literal":
                raise TypeMismatchInConstant(ast)
            else:
                raise IllegalConstantExpression(ast.value)
        return {"type": type, "name": name, "value_type": init[0], "const": True}

    def visitVarDecl(self, ast, c):
        name = ast.variable.accept(self, c)
        if not self.lookupVariable(name, c)[0]:
            res = self.varCheck(ast, c)
            return res
        else:
            raise Redeclared(Variable(), name)

    def visitConstDecl(self, ast, c):
        name = ast.constant.accept(self, c)
        if not self.lookupVariable(name, c)[0]:
            res = self.constCheck(ast, c)
            return res
        else:
            raise Redeclared(Constant(), name)

    def lookupClass(self, name, env):
        if len(env) > 1:
            for index, item in enumerate(env):
                if index > 0 and item:
                    # print(item)
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
                        member = mem.accept(self, localVar)
                        if member != None:
                            member.update({"class": nameclass})
                            localVar.append(member)
                    else:
                        member = mem.accept(self, localVar)
                        # member.update({"class": nameclass})
                        localVar[0]["global"].append(member)
                        c[0]["global"] = localVar[0]["global"]
                    attr.append(name)
                else:
                    raise Redeclared(Attribute(), name)
        for mem in ast.memlist:
            if self.getClass(mem) == "MethodDecl":
                mem.accept(self, localVar)

        c[0].update({"class": nameclass})
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
            if find[2] > 0:
                if self.getClass(ast.decl) == "ConstDecl":
                    res = self.constCheck(ast.decl, c)
                else:
                    res = self.varCheck(ast.decl, c)
                c[find[2]] = res
            else:
                raise Redeclared(Attribute(), name)
        else:
            res = ast.decl.accept(self, c)
            return res

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
        return {"array": ast.eleType.accept(self, c)}

    def visitClassType(self, ast, c):
        return {"class": ast.classname.name}

    def visitBinaryOp(self, ast, c):
        primitive = [
            "IntLiteral",
            "FloatLiteral",
            "BoolLiteral",
            "StringLiteral",
            "ArrayLiteral",
        ]
        ops = ["BinaryOp", "UnaryOp"]
        hybrid = ["+", "-", "*", "/", "<", "<=", ">", ">="]
        op = ast.op
        isStatic = True
        left = self.getClass(ast.left)
        right = self.getClass(ast.right)
        if left not in primitive + ops or right not in primitive + ops:
            isStatic = False
        left = ast.left.accept(self, c)
        right = ast.right.accept(self, c)
        if op in hybrid:
            if left[0] == "float" or right[0] == "float":
                return ["float", isStatic]
            return ["int", isStatic]

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
        lookupclass = self.lookupClass(ast.obj.accept(self, c), c)
        if lookupclass[0]:
            lookupvar = self.lookupVariable(
                ast.fieldname.accept(self, c), c[lookupclass[1]]
            )
            if lookupvar[0]:
                return lookupvar[1], False
        else:
            lookupobj = self.lookupVariable(
                ast.fieldname.accept(self, c), c[lookupclass[1]]
            )

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
        return ["int", True]

    def visitFloatLiteral(self, ast, c):
        return ["float", True]

    def visitBooleanLiteral(self, ast, c):
        return ["bool", True]

    def visitStringLiteral(self, ast, c):
        return ["string", True]

    def visitNullLiteral(self, ast, c):
        return ["null", True]

    def visitSelfLiteral(self, ast, c):
        return ["self", True]

    def checkTypeArrayLiteral(self, arr, env):
        list = [x.accept(self, env) for x in arr]
        res = all(map(lambda x: x == list[0], list))
        return res, list[0]

    def visitArrayLiteral(self, ast, c):
        res = self.checkTypeArrayLiteral(ast.value, c)
        if not res[0]:
            raise IllegalArrayLiteral(ast)
        return res[1]
