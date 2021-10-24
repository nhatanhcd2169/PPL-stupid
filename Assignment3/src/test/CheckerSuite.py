import unittest
from TestUtils import TestChecker
from AST import *


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
        input = Program([ClassDecl(Id("Ex"),[AttributeDecl(Instance(),VarDecl(Id("x"),ArrayType(3,IntType()),ArrayLiteral([IntLiteral(2),FloatLiteral(1.2),NullLiteral()])))])])
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