import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class kori {}"""
        expect = str(Program([ClassDecl(Id("kori"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class kori extends phuong {
            kori() {}
        }"""
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """
        class kori extends phuong {
            int phuongggggg;
            final float x = 7;
            static float y;
            final static float x = 4 * 5 + 7 / 3 * a[5], y = 3;
            static final int x = 123, y = 5;
        }
        class phuong extends kori {}        
        """
        expect = str("hehe")
        self.assertTrue(TestAST.test(input,expect,302))
   