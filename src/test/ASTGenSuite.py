import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class kori {} """
        input = """class kori {}"""
        expect = str(Program([ClassDecl(Id("kori"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class kori extends phuong {
            kori() {}
            int count(int a; float b; string c, d, e) {}
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
        expect = """Program([ClassDecl(Id(kori),Id(phuong),[])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """
        class kori extends phuong {
            int phuongggggg;
            float[5] uwu;
            final float x = 7;
            static float y;
            final static float x = 4 * 5 + 7 / 3 * a[5], y = 3;
            static final int x = 123, y = 5;
        }
        class phuong extends kori {}        
        """
        expect = str("hehe")
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_4(self):
        input = """"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,303))
   