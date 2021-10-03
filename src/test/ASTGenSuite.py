import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """class kori {}"""
        expect = str(Program([ClassDecl(Id("kori"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_2(self):
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
    
    def test_3(self):
        """More complex program"""
        input = """
        class kori extends phuong {
            int phuongggggg;
            float[5] uwu;
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
        expect = str("hehe")
        self.assertTrue(TestAST.test(input,expect,302))
        
    def test_4(self):
        input = """class a extends b {
                int s = new Shape(a, !b, 12, 25, -2.12314 \ c % 789138712841 + 5, false, "kori  phuonggggggg" ^ "hola", id, (this.pos[14/2+5*7] + 1 / 5));
            }"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,303))
        
    def test_5(self):
        input = """class a extends b {
                    final int c = daaaaaa != 5;
                    int cacbu;
                    void kori() 
                    {
                        b := this.suck(tits.leftTit, tit.rightTit);
                    }
                    void main() {
                        for x := 1 downto -1 do
                        {
                            x := x + 5;
                        }
                    }
            }"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,304))
        
    def test_6(self):
        input = """class a extends b {
                    int c = this.ok().not_ok.very_ok().wtf.nah.mam_tom / 2 \ 5;
            }"""
        expect = ""
        self.assertTrue(TestAST.test(input,expect,305))
        
    def test_7(self):
        input = """class a extends b {
                    static int a, b = 5, c = 66, d, e, f = 77, g = 8;
                    final static int a = 1, b = 2, c = 3;
            }"""
        expect = """Program([ClassDecl(Id(a),Id(b),[AttributeDecl(Static,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id(b),IntType,IntLit(5))),AttributeDecl(Static,VarDecl(Id(c),IntType,IntLit(66))),AttributeDecl(Static,VarDecl(Id(d),IntType)),AttributeDecl(Static,VarDecl(Id(e),IntType)),AttributeDecl(Static,VarDecl(Id(f),IntType,IntLit(77))),AttributeDecl(Static,VarDecl(Id(g),IntType,IntLit(8))),AttributeDecl(Static,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id(c),IntType,IntLit(3)))])])"""
        self.assertTrue(TestAST.test(input,expect,306))