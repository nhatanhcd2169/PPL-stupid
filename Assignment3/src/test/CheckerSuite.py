import unittest
from TestUtils import TestChecker
from AST import *

from main.bkool.utils.AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_2(self):
        input = "class a {} class a {}"
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_3(self):
        input = """
        class Ex
        {
            int my1Var;
            static float my1Var;
        }"""
        expect = "Redeclared Attribute: my1Var"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_4(self):
        input = """
        class Ex
        {
            final int x = 10.0;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),IntType,FloatLit(10.0))"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_5(self):
        input = """
        class Ex
        {
            void foo()
            {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_6(self):
        input = """
        class Ex
        {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_7(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(
                            Instance(),
                            VarDecl(
                                Id("x"),
                                ArrayType(3, IntType()),
                                ArrayLiteral(
                                    [IntLiteral(2), FloatLiteral(1.2), NullLiteral()]
                                ),
                            ),
                        )
                    ],
                )
            ]
        )
        expect = "Illegal Array Literal: [IntLit(2),FloatLit(1.2),NullLiteral()]"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_8(self):
        input = """
        class a {}
        class b extends a {}
        class a {}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_9(self):
        input = """
        class ABC
        {
            int x;
            float y;
            static string z;
        }
        class XYZ extends ABC
        {
            float x;
            int y;
            final int[3] z = {1,2,3};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(3)]"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_10(self):
        input = """
        class ABC
        {
            int[3] a = {1,2,3};
            final int[3] b = {1,2,3e6};
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),FloatLit(3000000.0)]"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_11(self):
        input = """
        class ABC
        {
            final float[3] a = {1,2,4};
        }
        """
        expect = "Illegal Constant Expression: [IntLit(1),IntLit(2),IntLit(4)]"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_12(self):
        input = """
        class ABC {
            int test() {
                for i := 0 to 5 do {
                    for j := 0 to 5 do {
                        break;
                    }
                    break;
                }
                break;
            }
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_13(self):
        input = """
        class ABC {
            final float x = 1 + 2.2;
            final float y = 1 + 2;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),FloatType,BinaryOp(+,IntLit(1),IntLit(2)))"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_14(self):
        input = """
        class ABC {
            static int x = 5;
        }
        class XYZ extends ABC {
            float x = 7.7;
            int x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_15(self):
        input = """
        class X
        {
            float x = 5 + 2 + 4.4 + 6 + 7;
            final int y = 1 + a;
        }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_16(self):
        input = """
        class X
        {
            final int x;
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_17(self):
        input = """
        class X
        {
            int[5] x = {1,2,3,4,5};
            float x = 7.7;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input, expect, 416))

    
    def test_18(self):
        input = Program(
            [
                ClassDecl(
                    Id("Ex"),
                    [
                        AttributeDecl(Static(), VarDecl(Id("a"), IntType())),
                        AttributeDecl(
                            Instance(),
                            ConstDecl(
                                Id("x"), IntType(), FieldAccess(Id("Ex"), Id("a"))
                            ),
                        ),
                    ],
                )
            ]
        )
        expect = "Illegal Constant Expression: FieldAccess(Id(Ex),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_19(self):
        input = """
        class Test 
        {
            int x;
            int y;
            int z;
            final int u = 5;
            final int v = 5 + u;
            void run(int x, int y, float z) {
                continue;
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_20(self):
        input = """
        class ABC {
            void count(int a, int b, A a) {}
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 419))
    
    def test_21(self):
        input = """
        class A {
            int x = 5;
        }
        class B extends A {
            int x = 6;
            int y = 7;
        }
        class C extends B {
            int z = 8;
            final float u = 10 + e; 
        }
        """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 420))   
        
    def test_22(self):
        input = """
        class ABC {
            int x = 5;
            final int y = 7;
            final static int z = 9;
        }
        class XYZ extends ABC {
            int x = 6 + y;
        }
        class U extends XYZ {
            final int x = x;
        }
        """
        expect = "Illegal Constant Expression: Id(x)"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_23(self):
        input = """
        class A 
        {
            int x = 5;
            static int u = 10;
        }
        class B
        {
            A y = new A();
            float z1 = y.x +5.5;
            float z2 = y.x + 5;
            final float u = A.u + 10;
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(+,FieldAccess(Id(A),Id(u)),IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 422))
