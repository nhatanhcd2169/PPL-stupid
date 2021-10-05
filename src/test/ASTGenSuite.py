import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """class kori {}"""
        expect = """Program([ClassDecl(Id(kori),[])])"""
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
        input = """class kori extends phuong 
        {
            kori() {}
            int count(int a; Shape b; string c, d, e) {}
            float[5] getFloatArray() {}
            void main() 
            {
                a := 2;
                a.b := 5;
                for x := 5 to 10 do
                    x := x + 5;
            }
            int okay() 
            {
                a := 2;
                a.b := 5;
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
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[MethodDecl(Id("<init>"),Instance,[],Block([],[])),MethodDecl(Id(count),Instance,[param(Id(a),IntType),param(Id(b),ClassType(Shape)),param(Id(c),StringType),param(Id(d),StringType),param(Id(e),StringType)],IntType,Block([],[])),MethodDecl(Id(getFloatArray),Instance,[],ArrayType(5,FloatType),Block([],[])),MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(Id(a),IntLit(2)),AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(5)),For(Id(x),IntLit(5),IntLit(10),True,AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])),MethodDecl(Id(okay),Instance,[],IntType,Block([],[AssignStmt(Id(a),IntLit(2)),AssignStmt(FieldAccess(Id(a),Id(b)),IntLit(5)),For(Id(x),IntLit(5),IntLit(10),True,Block([],[Break,If(BinaryOp(==,BinaryOp(+,Id(a),Id(b)),IntLit(5)),AssignStmt(Id(a),Id(b))),Continue,Return(BinaryOp(<,Id(x),IntLit(5)))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_3(self):
        """More complex program"""
        input = """
        class kori extends phuong 
        {
            int phuongggggg;
            float[5] uwu = {1,2,3,4.5,"concu"};
            final float x = 7;
            static float y;
            final static float x = 4 * 5 + 7 / 3 * a[5], y = 3;
            static final int x = 123, y = 5;
            int abc = !b;
            string x = y ^ "ok";
            Shapy s = new Shapy(a, b, 12, 25, 232525223, 2.12314, false, "kori  phuonggggggg");
        }
        class phuong extends kori {}        
        """
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[AttributeDecl(Instance,VarDecl(Id(phuongggggg),IntType)),AttributeDecl(Instance,VarDecl(Id(uwu),ArrayType(5,FloatType),[IntLit(1),IntLit(2),IntLit(3),FloatLit(4.5),StringLit(concu)])),AttributeDecl(Instance,ConstDecl(Id(x),FloatType,IntLit(7))),AttributeDecl(Static,VarDecl(Id(y),FloatType)),AttributeDecl(Static,ConstDecl(Id(x),FloatType,BinaryOp(+,BinaryOp(*,IntLit(4),IntLit(5)),BinaryOp(*,BinaryOp(/,IntLit(7),IntLit(3)),ArrayCell(Id(a),IntLit(5)))))),AttributeDecl(Static,ConstDecl(Id(y),FloatType,IntLit(3))),AttributeDecl(Static,ConstDecl(Id(x),IntType,IntLit(123))),AttributeDecl(Static,ConstDecl(Id(y),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(abc),IntType,UnaryOp(!,Id(b)))),AttributeDecl(Instance,VarDecl(Id(x),StringType,BinaryOp(^,Id(y),StringLit(ok)))),AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shapy)),NewExpr(Id(Shapy),[Id(a),Id(b),IntLit(12),IntLit(25),IntLit(232525223),FloatLit(2.12314),BooleanLit(True),StringLit(kori  phuonggggggg)])))]),ClassDecl(Id(phuong),Id(kori),[])])"""
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_4(self):
        input = """
        class a extends b 
        {
            Shape s = new Shape(a, !b, 12, 25, -2.12314 \ c % 789138712841 + 5, false, "kori  phuonggggggg" ^ "hola", id, (this.pos[14/2+5*7] + 1 / 5));
        }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Shape),[Id(a),UnaryOp(!,Id(b)),IntLit(12),IntLit(25),BinaryOp(+,BinaryOp(%,BinaryOp(\,UnaryOp(-,FloatLit(2.12314)),Id(c)),IntLit(789138712841)),IntLit(5)),BooleanLit(True),BinaryOp(^,StringLit(kori  phuonggggggg),StringLit(hola)),Id(id),BinaryOp(+,ArrayCell(FieldAccess(Self(),Id(pos)),BinaryOp(+,BinaryOp(/,IntLit(14),IntLit(2)),BinaryOp(*,IntLit(5),IntLit(7)))),BinaryOp(/,IntLit(1),IntLit(5)))])))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_5(self):
        input = """
        class a extends b 
        {
            final int c = daaaaaa != 5;
            int cactus;
            void kori() 
            {
                int x;
                final float x = 1.224;
                b := this.call(leftRecursive, rightRecursive);
            }
            void main() 
            {
                for x := 1 downto -1 do
                {
                    x := x + 5;
                }
            }
        }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,Id(daaaaaa),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cactus),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([VarDecl(Id(x),IntType),ConstDecl(Id(x),FloatType,FloatLit(1.224))],[AssignStmt(Id(b),CallExpr(Self(),Id(call),[Id(leftRecursive),Id(rightRecursive)]))])),MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(x),IntLit(1),UnaryOp(-,IntLit(1)),False,Block([],[AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(5)))])])]))])])""" 
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_6(self):
        input = """class a extends b 
        {
            int c = this.ok().not_ok.very_ok().wtf.nah.hehe / 2 \ 5;
        }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(c),IntType,BinaryOp(\,BinaryOp(/,FieldAccess(FieldAccess(FieldAccess(CallExpr(FieldAccess(CallExpr(Self(),Id(ok),[]),Id(not_ok)),Id(very_ok),[]),Id(wtf)),Id(nah)),Id(hehe)),IntLit(2)),IntLit(5))))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_7(self):
        input = """
        class a extends b 
        {
            static int a, b = 5, c = 66, d, e, f = 77, g = 8;
            final static int a = 1, b = 2, c = 3;
        }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Static,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Static,VarDecl(Id(c),IntType,IntLit(66))),AttributeDecl(Static,VarDecl(Id(d),IntType)),AttributeDecl(Static,VarDecl(Id(e),IntType)),AttributeDecl(Static,VarDecl(Id(f),IntType,IntLit(77))),AttributeDecl(Static,VarDecl(Id(g),IntType,IntLit(8))),AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id(c),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
        
    def test_8(self):
        input = """
        class a extends b 
        {
            Shape s;
            Shape c = new Shape(15);
            Shape d = c;
        }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,VarDecl(Id(s),ClassType(Id(Shape)))),AttributeDecl(Instance,VarDecl(Id(c),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(15)]))),AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(Shape)),Id(c)))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
        
    def test_9(self):
        input = """
        class a extends b 
        {
            void main() 
            {
                this.suck("123");
            }
        }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Call(Self(),Id(suck),[StringLit(123)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,308))
        
    def test_10(self):
        input = """
        class a 
        {
            void test() 
            {
                a[3+x.foo(2)] := a[b[2]] +3;
            }
        }"""
        expect = """Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,309))
        
    def test_11(self):
        input = """
        class a 
        {
            void test() 
            {
                x.b[2] := x.m()[3];
            }
        }"""
        expect = """Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(FieldAccess(Id(x),ArrayCell(Id(b),IntLit(2))),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
        
    def test_12(self):
        input = """
            class a 
            {
                int[5] kori(int copy, Phuong isPhuong) {}
            }
        """
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(kori),Instance,[param(Id(copy),IntType),param(Id(isPhuong),ClassType(Phuong))],ArrayType(5,IntType),Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,311))
        
    def test_13(self):
        input = """
            class a 
            {
                Shape kori(int ok) {}
            }
        """
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(kori),Instance,[param(Id(ok),IntType)],ClassType(Shape),Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,312))
        
    def test_14(self):
        input = """
            class a 
            {
                Shape[123141412313123231231321123] s = new Shape();
            }
        """
        expect = "Program([ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(s),ArrayType(123141412313123231231321123,ClassType(Id(Shape))),NewExpr(Id(Shape),[])))])])"
        self.assertTrue(TestAST.test(input,expect,313))   
         
    def test_15(self):
        input = """
            class a 
            {
                void main() 
                {
                    Shape[5] x;
                    Shape y;
                }
            }
        """
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(x),ArrayType(5,ClassType(Id(Shape)))),VarDecl(Id(y),ClassType(Id(Shape)))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,314))   
        
    def test_16(self):
        input = """
        class a 
        {
            int kori(int a, int b) 
            {
                a.b := c;
            }
        }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(kori),Instance,[param(Id(a),IntType),param(Id(b),IntType)],IntType,Block([],[AssignStmt(FieldAccess(Id(a),Id(b)),Id(c))]))])])"
        self.assertTrue(TestAST.test(input,expect,315))
        
    def test_17(self):
        input = """class test 
        {
            void main(){
                for i := 1 to 100 do 
                {
                    io.writeIntLn(i);
                    Intarray[i] := i + 1;
                }
                for x := 5 downto 2 do
                    io.writeIntLn(x);
            }
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(i),IntLit(1),IntLit(100),True,Block([],[Call(Id(io),Id(writeIntLn),[Id(i)]),AssignStmt(ArrayCell(Id(Intarray),Id(i)),BinaryOp(+,Id(i),IntLit(1)))])]),For(Id(x),IntLit(5),IntLit(2),False,Call(Id(io),Id(writeIntLn),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,316))
        
    def test_18(self):
        input = """class test 
        {
            void main()
            {
                if (a > b && "phuong" == "kori") 
                {
                    this.print("a is the biggest of all");
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[If(BinaryOp(>,Id(a),BinaryOp(==,BinaryOp(&&,Id(b),StringLit(phuong)),StringLit(kori))),Block([],[Call(Self(),Id(print),[StringLit(a is the biggest of all)])]))]))])])"
        self.assertTrue(TestAST.test(input,expect,317))
        
    def test_19(self):
        input = """
        class Example1 
        {
            int factorial(int n)
            {
                if n == 0 then return 1; else return n * this.factorial(n - 1);
            }
            void main()
            {
                int x;
                x := io.readInt();
                io.writeIntLn(this.factorial(x));
            }
        }"""
        expect = "Program([ClassDecl(Id(Example1),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Return(IntLit(1)),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))))])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(x),IntType)],[AssignStmt(Id(x),CallExpr(Id(io),Id(readInt),[])),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,318))
        
    def test_20(self):
        input = """
        class test 
        {
            void main()
            {
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(FieldAccess(Id(this),Id(aPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),IntLit(3)),BinaryOp(*,Id(value),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input,expect,319))
        
    def test_21(self):
        input = """
        class test 
        {
            void main()
            {
                if (flag) then
                    io.writeStrLn("Expression is true");
                else
                    io.writeStrLn ("Expression is false");
            }
        }
        """
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[If(Id(flag),Call(Id(io),Id(writeStrLn),[StringLit(Expression is true)]),Call(Id(io),Id(writeStrLn),[StringLit(Expression is false)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,320))
        
    def test_22(self):
        input = """
        class Shape 
        {
            Shape() 
            {
                int width, height;
                float pi = 314e-2;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Shape),[MethodDecl(Id("<init>"),Instance,[],Block([VarDecl(Id(width),IntType,NullLiteral()),VarDecl(Id(height),IntType,NullLiteral()),VarDecl(Id(pi),FloatType,FloatLit(3.14))],[]))])])"""
        self.assertTrue(TestAST.test(input,expect,321))
    
    def test_23(self):
        input = """
        class Shape 
        {
            void main() 
            {
                {
                    {
                        {
                            {
                                evil := bad;
                            }
                        }
                    }
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Block([],[Block([],[Block([],[Block([],[AssignStmt(Id(evil),Id(bad))])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,322))
        
    def test_24(self):
        input = """
        class Shape 
        {
            Shape() 
            {
                int x;
                int y = 10;
                Shape z;
            }
            void main() 
            {
                Shape e = new Shape();
            }
        }
        """
        expect = """Program([ClassDecl(Id(Shape),[MethodDecl(Id("<init>"),Instance,[],Block([VarDecl(Id(x),IntType,NullLiteral()),VarDecl(Id(y),IntType,IntLit(10)),VarDecl(Id(z),ClassType(Id(Shape)))],[])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(e),ClassType(Id(Shape)),NewExpr(Id(Shape),[]))],[]))])])"""
        self.assertTrue(TestAST.test(input,expect,323))
        
    def test_25(self):
        input = """
        class kori extends phuong 
        {
            void main() 
            {
                this.ok("void");
            }
        }"""
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Call(Self(),Id(ok),[StringLit(void)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def test_26(self):
        input = """
        class test 
        {
            int foo()
            {
                a := b / 2 * n / 4 && 5 % g || 2 * 9 / 4 % 2;
            }
        }"""
        expect = """Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(Id(a),BinaryOp(||,BinaryOp(&&,BinaryOp(/,BinaryOp(*,BinaryOp(/,Id(b),IntLit(2)),Id(n)),IntLit(4)),BinaryOp(%,IntLit(5),Id(g))),BinaryOp(%,BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(9)),IntLit(4)),IntLit(2))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,325))
        
    def test_27(self):
        input = """
        class test 
        {
            void main() 
            {
                int[5] Kori = {1,2,3,4,5};
                Kori[5] := 7;
                this.print(Kori, 0, 4);
            }
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(Kori),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)])],[AssignStmt(ArrayCell(Id(Kori),IntLit(5)),IntLit(7)),Call(Self(),Id(print),[Id(Kori),IntLit(0),IntLit(4)])]))])])"
        self.assertTrue(TestAST.test(input,expect,326))

    def test_28(self):
        input = """class test {
            final int x = 5;
            final string a = "1", b = "6";
            final float h = 1, k = 2;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(5))),AttributeDecl(Instance,ConstDecl(Id(a),StringType,StringLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,StringLit(6))),AttributeDecl(Instance,ConstDecl(Id(h),FloatType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(k),FloatType,IntLit(2)))])])"
        self.assertTrue(TestAST.test(input,expect,327))


    def test_29(self):
        input = """class test {
            int x = 5;
            int a, b = 6;
            float h = 1.3, k = 2.4;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(x),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(6))),AttributeDecl(Instance,VarDecl(Id(h),FloatType,FloatLit(1.3))),AttributeDecl(Instance,VarDecl(Id(k),FloatType,FloatLit(2.4)))])])"
        self.assertTrue(TestAST.test(input,expect,328))


    def test_30(self):
        input = """class test {
            int[5] a;
            float[4] x,y;
            }
        """
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(x),ArrayType(4,FloatType))),AttributeDecl(Instance,VarDecl(Id(y),ArrayType(4,FloatType)))])])"
        self.assertTrue(TestAST.test(input,expect,329))
   

    def test_31(self):
        input = """class a extends b {
                    final int c = daaaaaa != 5;
                    int cacbu;
                    void kori() 
                    {
                        b := this.suck;
                    }
            }"""
        expect = "Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(!=,Id(daaaaaa),IntLit(5)))),AttributeDecl(Instance,VarDecl(Id(cacbu),IntType)),MethodDecl(Id(kori),Instance,[],VoidType,Block([],[AssignStmt(Id(b),FieldAccess(Self(),Id(suck)))]))])])"
        self.assertTrue(TestAST.test(input,expect,330))

    
    def test_32(self):
        input = """class a {
                    void main() {}
        
            }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(main),Static,[],VoidType,Block([],[]))])])"
        self.assertTrue(TestAST.test(input,expect,331))
    

    def test_33(self):
        input = """class zzz {
                    zzz() {}
        
            }"""
        expect = 'Program([ClassDecl(Id(zzz),[MethodDecl(Id("<init>"),Instance,[],Block([],[]))])])'
        self.assertTrue(TestAST.test(input,expect,332))


    def test_34(self):
        input = """class a {
                    void test() {
                        a[3+x.foo(2)] := a[b[2]] +3;
                    }
        
            }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,333))

    
    def test_35(self):
        input = """class a {
                    void test() {
                        x.b[2] := x.m()[3];
                    }
        
            }"""
        expect = "Program([ClassDecl(Id(a),[MethodDecl(Id(test),Instance,[],VoidType,Block([],[AssignStmt(FieldAccess(Id(x),ArrayCell(Id(b),IntLit(2))),ArrayCell(CallExpr(Id(x),Id(m),[]),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,334))
    

    def test_36(self):
        input = """class Shape {
                    static final int numOfShape = 0;
                    final int immuAttribute = 0;
                    float length,width;
                    static int getNumOfShape() {
                        return numOfShape;
                    }
                }
                class Rectangle extends Shape {
                    float getArea(){
                    return this.length*this.width;
                }
                }"""
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,335))

    
    def test_37(self):
        input = """class Shape {
                    static final int numOfShape = 0;
                    final int immuAttribute = 0;
                    float length,width;
                    static int getNumOfShape() {
                        return numOfShape;
                    }
                }
                """
        expect = "Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id(numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immuAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(getNumOfShape),Static,[],IntType,Block([],[Return(Id(numOfShape))]))])])"
        self.assertTrue(TestAST.test(input,expect,336))


    def test_38(self):
        input = """class Rectangle extends Shape {
                    float getArea(){
                    return this.length*this.width;
                }"""
        expect = "Program([ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],FloatType,Block([],[Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))])])"
        self.assertTrue(TestAST.test(input,expect,337))
    

    def test_39(self):
        input = """class test {
                        void main(){
                            Shape s;
                            s := new Rectangle(3,4);
                            s := new Triangle(3,4);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)))],[AssignStmt(Id(s),NewExpr(Id(Rectangle),[IntLit(3),IntLit(4)])),AssignStmt(Id(s),NewExpr(Id(Triangle),[IntLit(3),IntLit(4)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,338))


    def test_40(self):
        input = """class test {
                        void main(){
                            Shape s = new Shape(5, 10.000000)
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Shape),[IntLit(5),FloatLit(10.0)]))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,339))


    def test_41(self):
        input = """class test {
                        void main(){
                            Shape s =  new Triangle();
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(s),ClassType(Id(Shape)),NewExpr(Id(Triangle),[]))],[]))])])"
        self.assertTrue(TestAST.test(input,expect,340))


    def test_42(self):
        input = """class test {
                        void main(){
                            this.aPI := 3.14;
                            value := x.foo(5);
                            l[3] := value * 2;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[AssignStmt(FieldAccess(Id(this),Id(aPI)),FloatLit(3.14)),AssignStmt(Id(value),CallExpr(Id(x),Id(foo),[IntLit(5)])),AssignStmt(ArrayCell(Id(l),IntLit(3)),BinaryOp(*,Id(value),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input,expect,341))


    def test_43(self):
        input = """class test {
                        void main(){
                            if flag then
                                io.writeStrLn("Expression is true");
                            else
                                io.writeStrLn ("Expression is false");
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[If(Id(flag),Call(Id(io),Id(writeStrLn),[StringLit(Expression is true)]),Call(Id(io),Id(writeStrLn),[StringLit(Expression is false)]))]))])])"
        self.assertTrue(TestAST.test(input,expect,342))


    def test_44(self):
        input = """class test {
                        void main(){
                            float r,s;
                            int[5] a,b;
                            r:=2.0;
                            s:=r*r*this.myPI;
                            a[0]:= s;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(r),FloatType),VarDecl(Id(s),FloatType),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType))],[AssignStmt(Id(r),FloatLit(2.0)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))]))])])"
        self.assertTrue(TestAST.test(input,expect,343))


    def test_45(self):
        input = """class test {
                        void main(){
                            for i := 1 to 100 do {
                                io.writeIntLn(i);
                                Intarray[i] := i + 1;
                            }
                            for x := 5 downto 2 do
                                io.writeIntLn(x);
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[For(Id(i),IntLit(1),IntLit(100),True,Block([],[Call(Id(io),Id(writeIntLn),[Id(i)]),AssignStmt(ArrayCell(Id(Intarray),Id(i)),BinaryOp(+,Id(i),IntLit(1)))])]),For(Id(x),IntLit(5),IntLit(2),False,Call(Id(io),Id(writeIntLn),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,344))


    def test_46(self):
        input = """class test {
                        void main(){
                            break;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Break]))])])"
        self.assertTrue(TestAST.test(input,expect,345))


    def test_47(self):
        input = """class test {
                        void main(){
                            continue;
                        }
                    }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(main),Static,[],VoidType,Block([],[Continue]))])])"
        self.assertTrue(TestAST.test(input,expect,346))


    def test_48(self):
        input = """class test {
                        int foo(){
                            return abcd;
                        }
                    }
                """
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[Return(Id(abcd))]))])])"
        self.assertTrue(TestAST.test(input,expect,347))


    def test_49(self):
        input = """class Example1 {
                            int factorial(int n){
                            if n == 0 then return 1; else return n * this.factorial(n - 1);
                        }
                        void main(){
                            int x;
                            x := io.readInt();
                            io.writeIntLn(this.factorial(x));
                        }
                    }"""
        expect = "Program([ClassDecl(Id(Example1),[MethodDecl(Id(factorial),Instance,[param(Id(n),IntType)],IntType,Block([],[If(BinaryOp(==,Id(n),IntLit(0)),Return(IntLit(1)),Return(BinaryOp(*,Id(n),CallExpr(Self(),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]))))])),MethodDecl(Id(main),Static,[],VoidType,Block([VarDecl(Id(x),IntType)],[AssignStmt(Id(x),CallExpr(Id(io),Id(readInt),[])),Call(Id(io),Id(writeIntLn),[CallExpr(Self(),Id(factorial),[Id(x)])])]))])])"
        self.assertTrue(TestAST.test(input,expect,348))


    def test_50(self):
        input = """class test {
                    Shape nah;
                    test() {
                        Shape s;
                        int x;
                        float y;
                    }
        
            }"""
        expect = 'Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(nah),ClassType(Id(Shape)))),MethodDecl(Id("<init>"),Instance,[],Block([VarDecl(Id(s),ClassType(Id(Shape))),VarDecl(Id(x),IntType,NullLiteral()),VarDecl(Id(y),FloatType,NullLiteral())],[]))])])'
        self.assertTrue(TestAST.test(input,expect,349)) 


    def test_51(self):
        input = """class test 
        {
            int a, b, c;
            float x, y;
            string z = "abc";
            static boolean d = true;
        }"""
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),AttributeDecl(Instance,VarDecl(Id(x),FloatType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),AttributeDecl(Instance,VarDecl(Id(z),StringType,StringLit(abc))),AttributeDecl(Static,VarDecl(Id(d),BoolType,BooleanLit(True)))])])"
        self.assertTrue(TestAST.test(input,expect,350))


    def test_52(self):
        input = """
        class test 
        {
            void foo() {
                int x;
                float y;
                string[1000] str;
            }
            int x;
            float y;
            string[1000] str;
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],VoidType,Block([VarDecl(Id(x),IntType),VarDecl(Id(y),FloatType),VarDecl(Id(str),ArrayType(1000,StringType))],[])),AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),FloatType)),AttributeDecl(Instance,VarDecl(Id(str),ArrayType(1000,StringType)))])])"
        self.assertTrue(TestAST.test(input,expect,351))


    def test_53(self):
        input = """class test {
            int a;
            float b;
            string z;
            float nml () {
                for i:= traithang to bede do this.hahaha();
                    for i := 4 downto -5 do h := 6;
                return 1;
            }"""
        expect = "Program([ClassDecl(Id(test),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(z),StringType)),MethodDecl(Id(nml),Instance,[],FloatType,Block([],[For(Id(i),Id(traithang),Id(bede),True,Call(Self(),Id(hahaha),[])]),For(Id(i),IntLit(4),UnaryOp(-,IntLit(5)),False,AssignStmt(Id(h),IntLit(6))]),Return(IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input,expect,352))


    def test_54(self):
        input = """class test {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 && -7)*(1+2+3)-(4+5*6/abc && (123))] := a[(((-5)))];
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(&&,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),UnaryOp(-,IntLit(7))),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),IntLit(123)))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input,expect,353))


    def test_55(self):
        input = """class test {
	int foo() {
		a [(1 + 2 * 3 - 4 / 5 && 6 || 7)*(1+2+3)-(4+5*6/abc && !(123))] := a[(((-5)))];
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[AssignStmt(ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,BinaryOp(||,BinaryOp(&&,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))),BinaryOp(/,IntLit(4),IntLit(5))),IntLit(6)),IntLit(7)),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3))),BinaryOp(&&,BinaryOp(+,IntLit(4),BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(6)),Id(abc))),UnaryOp(!,IntLit(123))))),ArrayCell(Id(a),UnaryOp(-,IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input,expect,354))


    def test_56(self):
        input = """class test {
	int foo() {
		for i := 1 to 10+5-4*e+x do break;
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),IntLit(1),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(10),IntLit(5)),BinaryOp(*,IntLit(4),Id(e))),Id(x)),True,Break])]))])])"
        self.assertTrue(TestAST.test(input,expect,355))


    def test_57(self):
        input = """class test {
	int foo() {
		for i := 10+5-4*e+x downto 1 do break;
	}
}"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(10),IntLit(5)),BinaryOp(*,IntLit(4),Id(e))),Id(x)),IntLit(1),False,Break])]))])])"
        self.assertTrue(TestAST.test(input,expect,356))


    def test_58(self):
        input = """
        class test 
        {
            int foo() 
            {
                for i := 1 to 5e2 do i:= i-1;
            }
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([],[For(Id(i),IntLit(1),FloatLit(500.0),True,AssignStmt(Id(i),BinaryOp(-,Id(i),IntLit(1)))])]))])])"
        self.assertTrue(TestAST.test(input,expect,357))
        
    def test_59(self):
        input = """
        class test 
        {
            int foo() 
            {
                int[3] a = {5, 6, true};
            }
        }"""
        expect = "Program([ClassDecl(Id(test),[MethodDecl(Id(foo),Instance,[],IntType,Block([VarDecl(Id(a),ArrayType(3,IntType),[IntLit(5),IntLit(6),BooleanLit(True)])],[]))])])"
        self.assertTrue(TestAST.test(input,expect,358))
        