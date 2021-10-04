import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """class kori {}"""
        expect = """Program([ClassDecl(Id(kori),[])])"""
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
        input = """class kori extends phuong {
            kori() {}
            int count(int a; Shape b; string c, d, e) {}
            float[5] getFloatArray() {}
            void main() {
                a := 2;
                a.b.c.d.e := 5;
                for x := 5 to 10 do
                    x := x + 5;
            }
            int okay() {
                a := 2;
                a.b.c.d.e := 5;
                for x := 5 to 10 do
                {
                    break;
                    if a + b == 5 then 
                        a := b;
                    continue;
                    return (x < 5);
                }
            }
        }"""
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[MethodDecl(Id(<init>),Instance,[],VoidType,Block([],[])),MethodDecl(Id(count),Instance,[param(Id(a),IntType),param(Id(b),ClassType(Shape)),param(Id(c),StringType),param(Id(d),StringType),param(Id(e),StringType)],IntType,Block([],[])),MethodDecl(Id(getFloatArray),Instance,[],ArrayType(IntLit(5),FloatType),Block([],[])),MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(Id(a),IntLit(2)),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),Id(e)),IntLit(5)),For(Id(x),IntLit(5),IntLit(10),True,AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])),MethodDecl(Id(okay),Instance,[],IntType,Block([],[AssignStmt(Id(a),IntLit(2)),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),Id(e)),IntLit(5)),For(Id(x),IntLit(5),IntLit(10),True,Block([],[Break,If(BinaryOp(==,BinaryOp(+,Id(a),Id(b)),IntLit(5)),AssignStmt(Id(a),Id(b))),Continue,Return(BinaryOp(<,Id(x),IntLit(5)))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_3(self):
        """More complex program"""
        input = """
        class kori extends phuong {
            int phuongggggg;
            float[5] uwu = {1,2,3,4.5,"concu"};
            final float x = 7;
            static float y;
            final static float x = 4 * 5 + 7 / 3 * a[5], y = 3;
            static final int x = 123, y = 5;
            int abc = !b;
            string x = y ^ "ok";
            int s = new Shape(a, b, 12, 25, 232525223, 2.12314, false, "kori  phuonggggggg");
        }
        class phuong extends kori {}        
        """
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[AttributeDecl(Instance,VarDecl(Id(phuongggggg),IntType)),AttributeDecl(Instance,VarDecl(Id(uwu),ArrayType(IntLit(5),FloatType),[IntLit(1),IntLit(2),IntLit(3),FloatLit(4.5),StringLit(concu)])),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,IntLit(7))),AttributeDecl(Static,VarDecl(Id(y),FloatType)),AttributeDecl(Static,ConstDecl(Id(x),FloatType,BinaryOp(+,BinaryOp(*,IntLit(4),IntLit(5)),BinaryOp(*,BinaryOp(/,IntLit(7),IntLit(3)),ArrayCell(Id(a),IntLit(5)))))),AttributeDecl(Static,ConstDecl(Id(y),FloatType,IntLit(3))),AttributeDecl(Static,ConstDecl(Id(x),IntType,IntLit(123))),AttributeDecl(Static,ConstDecl(Id(y),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(abc),IntType,UnaryOp(!,Id(b)))),AttributeDecl(Instance,VarDecl(Id(x),StringType,BinaryOp(^,Id(y),StringLit(ok)))),AttributeDecl(Instance,VarDecl(Id(s),IntType,NewExpr(Id(Shape),[Id(a),Id(b),IntLit(12),IntLit(25),IntLit(232525223),FloatLit(2.12314),BooleanLit(True),StringLit(kori  phuonggggggg)])))]),ClassDecl(Id(phuong),Id(kori),[])])"""
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_4(self):
        input = """class a extends b {
                Shape s = new Shape(a, !b, 12, 25, -2.12314 \ c % 789138712841 + 5, false, "kori  phuonggggggg" ^ "hola", id, (this.pos[14/2+5*7] + 1 / 5));
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Shape),[Id(a),UnaryOp(!,Id(b)),IntLit(12),IntLit(25),BinaryOp(+,BinaryOp(%,BinaryOp(\,UnaryOp(-,FloatLit(2.12314)),Id(c)),IntLit(789138712841)),IntLit(5)),BooleanLit(True),BinaryOp(^,StringLit(kori  phuonggggggg),StringLit(hola)),Id(id),BinaryOp(+,ArrayCell(FieldAccess(Self(),Id(pos)),BinaryOp(+,BinaryOp(/,IntLit(14),IntLit(2)),BinaryOp(*,IntLit(5),IntLit(7)))),BinaryOp(/,IntLit(1),IntLit(5)))])))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_5(self):
        input = """class a extends b {
                    final int c = daaaaaa != 5;
                    int cacbu;
                    void kori() 
                    {
                        int x;
                        final float x = 1.224;
                        b := this.call(leftRecursive, rightRecursive);
                    }
                    void main() {
                        for x := 1 downto -1 do
                        {
                            x := x + 5;
                        }
                    }
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,Id(daaaaaa),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cacbu),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([VarDecl(Id(x),IntType),ConstDecl(Id(x),FloatType,FloatLit(1.224))],[AssignStmt(Id(b),CallExpr(Self(),Id(call),[Id(leftRecursive),Id(rightRecursive)]))])),MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(x),IntLit(1),UnaryOp(-,IntLit(1)),False,Block([],[AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])]))])])""" 
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_6(self):
        input = """class a extends b {
                    int c = this.ok().not_ok.very_ok().wtf.nah.mam_tom / 2 \ 5;
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(\,BinaryOp(/,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(CallExpr(Self(),Id(ok),[]),Id(not_ok)),Id(very_ok),[]),Id(wtf)),Id(nah)),Id(mam_tom)),IntLit(2)),IntLit(5))))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_7(self):
        input = """class a extends b {
                    static int a, b = 5, c = 66, d, e, f = 77, g = 8;
                    final static int a = 1, b = 2, c = 3;
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Static,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Static,VarDecl(Id(c),IntType,IntLit(66))),AttributeDecl(Static,VarDecl(Id(d),IntType)),AttributeDecl(Static,VarDecl(Id(e),IntType)),AttributeDecl(Static,VarDecl(Id(f),IntType,IntLit(77))),AttributeDecl(Static,VarDecl(Id(g),IntType,IntLit(8))),AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id(c),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test_8(self):
        input = """class a extends b {
                    Shape s;
                    Shape c = new Shape(15);
                    Shape d = c;
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(15)]))),AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(Shape)),Id(c)))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_9(self):
        input = """class a extends b {
                    void main() {
                        this.suck("123");
                    }
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Call(Self(),Id(suck),[StringLit(123)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_10(self):
        input = """class a {
                    void test() {
                        a[3+x.foo(2)] := a[b[2]] +3;
                    }

            }"""
        expect = """Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test_11(self):
        input = """class a {
                    void test() {
                        x.b[2] := x.m()[3];
                    }

            }"""
        expect = """Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),IntLit(2)),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
        
    def test_12(self):
        input = """
            class a {
                int[5] kori(int copy, Phuong isPhuong) {}
            }
        """
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(kori),Instance,[param(Id(copy),IntType),param(Id(isPhuong),ClassType(Phuong))],ArrayType(IntLit(5),IntType),Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,311))
        
    def test_13(self):
        input = """
            class a {
                Shape kori(int ok) {}
            }
        """
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(kori),Instance,[param(Id(ok),IntType)],ClassType(Shape),Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,312))