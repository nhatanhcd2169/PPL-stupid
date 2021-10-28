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

    """ENTRY"""
    """
    Class
    {
        "class": classname,
        "statics": {"attrs": [], "methods": []},
        "locals": {"attrs": [], "methods": []},
        inherit: []
    }
    Attribute
    {
        "type": type,
        "name": name,
        "value_type": value_type,
        "const": True
    }
    Methods
    {
        "return_type": type,
        "name": name,
        "param": [VarDecl],
        "body": List[VarDecl + Statement]
    }
    """

    def check(self):
        return self.ast.accept(self, StaticChecker.global_envi)

    def getClass(self, obj):
        return obj.__class__.__name__

    def lookupClass(self, name, env):
        for (index, item) in enumerate(env):
            if item["class"] == name:
                return [True, item, index]
        return [False, None, None]

    def lookupVariable(self, name, env, child, parent=None):
        for class_i, class_item in enumerate(env[:-1]):
            if class_item["class"] == child:
                for statics_i, statics_item in enumerate(
                    class_item["statics"]["attrs"]
                ):
                    if statics_item["name"] == name:
                        return [True, statics_item, "static", class_item["class"]]
                for locals_i, locals_item in enumerate(class_item["locals"]["attrs"]):
                    if locals_item["name"] == name:
                        return [True, locals_item, "local", class_item["class"]]
        if parent != None:
            stack = parent
            while len(stack) > 0:
                for class_i, class_item in enumerate(env[:-1]):
                    if class_item["class"] == stack[-1]:
                        for statics_i, statics_item in enumerate(
                            class_item["statics"]["attrs"]
                        ):
                            if statics_item["name"] == name:
                                return [
                                    True,
                                    statics_item,
                                    "static",
                                    class_item["class"],
                                    "inherited",
                                ]
                        for locals_i, locals_item in enumerate(
                            class_item["locals"]["attrs"]
                        ):
                            if locals_item["name"] == name:
                                return [
                                    True,
                                    locals_item,
                                    "local",
                                    class_item["class"],
                                    "inherited",
                                ]
                stack.pop()
        return [False, None, None]

    def visitProgram(self, ast, c):
        env = [{"class": "io", "statics": {"attrs": [], "methods": c}}]
        for x in ast.decl:
            env += [x.accept(self, env)]

    def visitVarDecl(self, ast, c):
        name = ast.variable.accept(self, c)
        type = ast.varType.accept(self, c)
        init = ast.varInit.accept(self, c) if ast.varInit else [None, True]
        """Không biết có thiếu gì ở đây không"""
        return {"type": type, "name": name, "value_type": init[0], "const": False}

    def visitConstDecl(self, ast, c):
        """mmmm idk"""
        name = ast.constant.accept(self, c)
        type = ast.constType.accept(self, c)
        if self.getClass(ast.value) == "Id":
            lookup = self.lookupVariable(
                ast.value.accept(self, c), c, c[-1]["current"], c[-1]["inherit"]
            )
            if lookup[0]:
                if not lookup[1]["const"]:
                    raise IllegalConstantExpression(ast.value)
            else:
                # raise Undeclared(Identifier(), ast.value.accept(self, c)) # idk why?
                raise IllegalConstantExpression(ast.value)
        init = ast.value.accept(self, c) if ast.value else [None, True]
        if init[0] == None or (len(init) == 3 and init[2] == None):
            raise IllegalConstantExpression(ast.value)
        else:
            if init[0] in ["int", "bool", "float", "string"]:
                if not init[1]:
                    raise IllegalConstantExpression(ast.value)
                else:
                    if init[0] != type:
                        raise TypeMismatchInConstant(ast)
            else:
                raise TypeMismatchInConstant(ast)
        return {"type": type, "name": name, "value_type": init[0], "const": True}

    def visitClassDecl(self, ast, c):
        classname = ast.classname.accept(self, c)
        parentname = ast.parentname.accept(self, c) if ast.parentname else ""
        if self.lookupClass(classname, c)[0]:
            raise Redeclared(Class(), classname)
        local = {
            "class": classname,
            "statics": {"attrs": [], "methods": []},
            "locals": {"attrs": [], "methods": []},
            "inherit": [],
        }
        if parentname != "":
            lookupClass = self.lookupClass(parentname, c)
            if not lookupClass[0]:
                raise Undeclared(Class(), parentname)
            else:
                local["inherit"] = lookupClass[1]["inherit"]
        attr = []
        for mem in ast.memlist:
            if self.getClass(mem) == "AttributeDecl":
                name = (
                    mem.decl.variable.name
                    if (self.getClass(mem.decl) == "VarDecl")
                    else mem.decl.constant.name
                )
                if name not in attr:
                    obj = (
                        c
                        + [local]
                        + [
                            {
                                "current": classname,
                                "inherit": local["inherit"]
                                + ([parentname] if parentname else []),
                            }
                        ]
                    )
                    if mem.kind.accept(self, local) == "Instance":
                        member = mem.accept(self, obj)
                        local["locals"]["attrs"].append(member)
                    else:
                        member = mem.accept(self, obj)
                        local["statics"]["attrs"].append(member)
                else:
                    raise Redeclared(Attribute(), name)
            else:
                """không biết có thiếu gì ở đây không?"""
                name = mem.name.accept(self, c)
                if name not in attr:
                    obj = (
                        c
                        + [local]
                        + [
                            {
                                "current": classname,
                                "inherit": local["inherit"]
                                + ([parentname] if parentname else []),
                            }
                        ]
                    )
                    if mem.kind.accept(self, local) == "Instance":
                        member = mem.accept(self, obj)
                        local["locals"]["methods"].append(member)
                    else:
                        member = mem.accept(self, obj)
                        local["statics"]["methods"].append(member)
                else:
                    raise Redeclared(Method(), name)
            attr.append(name)
        if parentname:
            local["inherit"].append(parentname)
        return local

    def visitStatic(self, ast, c):
        return "Static"

    def visitInstance(self, ast, c):
        return "Instance"

    def visitMethodDecl(self, ast, c):
        params = []
        if len(ast.param) > 0:
            for param in ast.param:
                name = param.variable.name
                names = [x["name"] for x in params]
                if name not in names:
                    member = param.accept(self, c)
                else:
                    raise Redeclared(Parameter(), name)
                params.append(member)
        """kiểm tra params xong, còn phần body và add nguyên cụm lên environment trong class"""
        ast.body.accept(self, c)

    def visitAttributeDecl(self, ast, c):
        current = c[-1]["current"]
        inherit = c[-1]["inherit"]
        name = (
            ast.decl.variable.name
            if (self.getClass(ast.decl) == "VarDecl")
            else ast.decl.constant.name
        )
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
        return {"array": ast.eleType.accept(self, c)}

    def visitClassType(self, ast, c):
        return {"class": ast.classname.name}

    def visitBinaryOp(self, ast, c):
        primitive = [
            "IntLiteral",
            "FloatLiteral",
            "BoolLiteral",
            "StringLiteral",
        ]
        ops = ["BinaryOp", "UnaryOp"]
        isStatic = True
        left = self.getClass(ast.left)
        right = self.getClass(ast.right)
        checkId = {"left": "", "right": ""}
        op = ast.op
        if left not in primitive + ops or right not in primitive + ops:
            if left == "Id":
                res = self.lookupVariable(
                    ast.left.accept(self, c), c, c[-1]["current"], c[-1]["inherit"]
                )
                checkId["left"] = res
                if res[0]:
                    if res[2] > 0:
                        if not c[res[2]]["const"]:
                            isStatic = False
                    else:
                        if not c[0][res[3]]["const"]:
                            isStatic = False
                else:
                    raise Undeclared(Identifier(), ast.left.accept(self, c))
            if right == "Id":
                res = self.lookupVariable(
                    ast.right.accept(self, c), c, c[-1]["current"], c[-1]["inherit"]
                )
                checkId["right"] = res
                if res[0]:
                    if res[2] > 0:
                        if not c[res[2]]["const"]:
                            isStatic = False
                    else:
                        if not c[0][res[3]]["const"]:
                            isStatic = False
                else:
                    raise Undeclared(Identifier(), ast.right.accept(self, c))
        left = (
            ast.left.accept(self, c)
            if checkId["left"] == ""
            else [
                checkId["left"][1]["type"]
                if not isinstance(checkId["left"][1]["type"], dict)
                else checkId["left"][1]["type"]["class"]
                if "class" in checkId["left"][1]["type"]
                else checkId["left"][1]["type"]["array"],
                checkId["left"][1]["const"],
            ]
        )
        right = (
            ast.right.accept(self, c)
            if checkId["right"] == ""
            else [
                checkId["right"][1]["type"]
                if not isinstance(checkId["right"][1]["type"], dict)
                else checkId["right"][1]["type"]["class"]
                if "class" in checkId["right"][1]["type"]
                else checkId["right"][1]["type"]["array"],
                checkId["right"][1]["const"],
            ]
        )
        if op in ["&&", "||"] and left[0] in ["bool"] and right[0] in ["bool"]:
            return ["bool", isStatic]
        elif (
            op in ["==", "!="]
            and left[0] in ["bool", "int"]
            and right[0] in ["bool", "int"]
        ):
            return ["bool", isStatic]
        elif (
            op in ["+", "-", "*", "<", "<=", ">", ">="]
            and left[0] in ["float", "int"]
            and right[0] in ["float", "int"]
        ):
            if left[0] == "int" and right[0] == "int":
                return ["int", isStatic]
            else:
                return ["float", isStatic]
        elif (
            op in ["/"] and left[0] in ["float", "int"] and right[0] in ["float", "int"]
        ):
            return ["float", isStatic]
        elif op in ["\\", "%"] and left[0] == "int" and right[0] == "int":
            return ["int", isStatic]
        elif op in ["^"] and left[0] == "string" and right[0] == "string":
            return ["string", isStatic]
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast, c):
        pass

    def visitCallExpr(self, ast, c):
        pass

    def visitNewExpr(self, ast, c):
        pass

    def visitId(self, ast, c):
        """không biết nên thêm 1 field để nó nhận biết đây là từ Id mà ra không ?"""
        return ast.name

    def visitArrayCell(self, ast, c):
        pass

    def visitFieldAccess(self, ast, c):
        findField = self.lookupVariable(
            ast.fieldname.accept(self, c), c, c[-1]["current"], c[-1]["inherit"]
        )
        if findField[2] == "static":
            if self.getClass(ast.obj) == "Id":
                classname = ast.obj.accept(self, c)
                if classname == findField[3]:
                    return [findField[1]["type"], True, findField[1]["value_type"]]
                else:
                    raise Undeclared(Class(), classname)
            else:
                raise IllegalMemberAccess(ast)
        """còn trường hợp access Instance field"""
        # else:
        #     findObj = self.lookupVariable(
        #         ast.obj.accept(self, c), c, c[-1]["current"], c[-1]["inherit"]
        #     )
        #     if self.getClass(ast.obj) == "Id":
        #         # x.o
        #         objname = ast.obj.accept(self, c)
        #         if not ("class" in findObj[1]["type"]):
        #             raise TypeMismatchInExpression(ast)
        #         else:
        #             if findObj[3] == c[-1]["current"]: # same level
        #                 raise

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
        return

    def visitBreak(self, ast, c):
        return

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

    def visitArrayLiteral(self, ast, c):
        list = [x.accept(self, c) for x in ast.value]
        res = all(map(lambda x: x[0] == list[0][0] and x[1] == True, list))
        if not res:
            raise IllegalArrayLiteral(ast)
        return [list[0][0], False]
