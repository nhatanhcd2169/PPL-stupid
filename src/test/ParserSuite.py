import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = """class ABC {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_2(self):
        input = """class ABC extends {}"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,202))
    
    def test_3(self):
        input = """class { } """
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_4(self):
        input = """class ABC } """
        expect = "Error on line 1 col 10: }"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_5(self):
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
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_6(self):
        input = """
            class Shape 
            {
                float length,width;
                float getArea() {}
                Shape(float length,width) 
                {
                    this.length := length;
                    this.width := width;
                }
            }
            class Rectangle extends Shape {
                float getArea()
                {
                    return this.length*this.width;
                }
            }
            class Triangle extends Shape 
            {
                float getArea()
                {
                    return this.length*this.width / 2;
                }
            }
            class Example2 
            {
                void main()
                {
                    Shape s;
                    s := new Rectangle(3,4);
                    io.writeFloatLn(s.getArea());
                    s := new Triangle(3,4);
                    io.writeFloatLn(s.getArea());
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_7(self):
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_8(self):
        input = """ int b, c, d; """
        expect = "Error on line 1 col 1: int"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_9(self):
        input = """ class Kori 
        {
            static int kori = 0;
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_10(self):
        input = """void main()"""
        expect = "Error on line 1 col 0: void"
        self.assertTrue(TestParser.test(input,expect,210))
    
    def test_11(self):
        input = """class Kori {
            class Noooooo {}
        }"""
        expect = "Error on line 2 col 12: class"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_12(self):
        input = """class Math {
            float calc(float a, b; int c) {
                return a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_13(self):
        input = """float calc() {class ABC {}}"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_14(self):
        input = """class ABC {
            string ABC, abc;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_15(self):
        input = """class ABC {
            float abc;
            ABC abc;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
    def test_16(self):
        input = """class ABC extends ABC {{"""
        expect = "Error on line 1 col 23: {"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_17(self):
        input = """class ABC {
            int[5] a = {12, 2, "abc"};
            void main() {
                int[5] a;
                a[0] := 5; 
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_18(self):
        input = """class ABC {
            int [3]a = {5, 6, true};
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_19(self):
        input = """class ABC {
            float b;
            boolean x = true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_20(self):
        input = r"""
                    class Example1 {
                        int factorial(int n){
                            if n == 0 then return 1; else return n * this.factorial(n - 1);
                        }
                        void main(){
                            int x;
                            x := io.readInt();
                            io.writeIntLn(this.factorial(x));
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_21(self):
        input = r"""
                    class test {
                        static void main() {
                            int a;
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_22(self):
        input = r"""
                    class test {
                        void main() {
                        float a,b,c;
                        }
                    }
                """
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_23(self):
        input = r"""
                    class test {
                        int[-5] a;
                    }
                """
        expect = r"Error on line 3 col 28: -"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_24(self):
        input = r"""
                    class test {
                        int foo() {
                            a [(1 + 2 * 3 - 4 / 5 && 6 || 7)*(1+2+3)-(4+5*6/abc && !(123))] := a[(((-5)))];
                        }
                    }
                """
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_25(self):
        input = r"""
                    class test {
                        int foo() {
                        a := b[3] := foo(3)[5] := 5;
                        }
                    }
                """
        expect = r"Error on line 4 col 34: :="
        self.assertTrue(TestParser.test(input,expect,225))
    def test_26(self):
        input = r"""
                    class test {
                        break;
                    }
                """
        expect = r"Error on line 3 col 24: break"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_27(self):
        input = r"""
                    class test {
                        int main () {
                        }
                    }
                """
        expect = r"successful"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_28(self):
        input = r"""
                    class test {
                        int foo(){
                        a = 1;
                        }
                    }
                """
        expect = r"Error on line 4 col 26: ="
        self.assertTrue(TestParser.test(input,expect,228))
    def test_29(self):
        input = """class ABC"""
        expect = "Error on line 1 col 9: <EOF>"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_30(self):
        input = """class ABC extend ABC {}"""
        expect = "Error on line 1 col 10: extend"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_31(self):
        input = """class ABC extends ABC extends DEF{}"""
        expect = "Error on line 1 col 22: extends"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_32(self):
        input = """class ABC extends ABC {
            class ABC extends ABC {
                class ABC extends ABC {
                }
            }
        }"""
        expect = "Error on line 2 col 12: class"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_33(self):
        input = """io.writeLn();"""
        expect = "Error on line 1 col 0: io"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_34(self):
        input = """<EOF>"""
        expect = "Error on line 1 col 0: <"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_35(self):
        input = """class PPL {
            # this is not a joke, this is madness
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_36(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_37(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main()
        }"""
        expect = "Error on line 5 col 8: }"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_38(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main(){
                string con = lecturer ^ " - ";
            }"""
        expect = "Error on line 5 col 27: ="
        self.assertTrue(TestParser.test(input,expect,238))
    def test_39(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main(){
                string con;
                # := lecturer ^ " - ";
            }"""
        expect = "Error on line 7 col 13: <EOF>"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_40(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main(){
                string con;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_41(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main(){
                string con;
                con := lecturer ^ " - ";
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_42(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main(){
                string con;
                con := lecturer ^ " - ";
                con := con ^ PPL;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_43(self):
        input = """class PPL {
            string PPL = "Principles of Programming Languages";
            string lecturer = "Dr. Nguyen Hua Phung";
            void main(){
                string con;
                con := lecturer ^ " - " ^ PPL;
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_44(self):
        input = """class KORI {
            string[7] = 5;
        }
        """
        expect = "Error on line 2 col 22: ="
        self.assertTrue(TestParser.test(input,expect,244))
    def test_45(self):
        input = """class KORI {
            string[7] int = 5;
        }
        """
        expect = "Error on line 2 col 22: int"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_46(self):
        input = """class KORI {
            string[7] intel = 5;
        }
        """
        expect = "Error on line 2 col 30: 5"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_47(self):
        input = """class KORI {
            string[7] intel = {5};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_48(self):
        input = """class KORI {
            string[7], intel = {5};
        }
        """
        expect = "Error on line 2 col 21: ,"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_49(self):
        input = """class KORI {
            string[7] intel, idkcb = {5};
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_50(self):
        input = """class KORI {
            string[7] intel, idkcb = {5}, {6};
        }
        """
        expect = "Error on line 2 col 42: {"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_51(self):
        input = """class KORI {
            string[7] intel; idkcb = {5}, {6};
        }
        """ 
        expect = "Error on line 2 col 35: ="
        self.assertTrue(TestParser.test(input,expect,251))
    def test_52(self):
        input = """class KORI {
            string[7] intel; idkcb := {5}, {6};
        }
        """ 
        expect = "Error on line 2 col 35: :="
        self.assertTrue(TestParser.test(input,expect,252))
    def test_53(self):
        input = """class Kori {
            string b; int c; float d; fowrgoifg t;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_54(self):
        input = """class test {
                    int foo() {
                        for i := 1 to 10+5-4*e+x do break;
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_55(self):
        input = """class ABC {if (i love you) then ok;}"""
        expect = "Error on line 1 col 11: if"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_56(self):
        input = """class ABC {
            void main() {
                if (i love you)
            }
        }"""
        expect = "Error on line 3 col 22: love"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_57(self):
        input = """class ABC {
            void main() {
                if ("i love you")
            }
        }"""
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_58(self):
        input = """class ABC {
            void main() {
                if ("i love you") then "what";
            }
        }"""
        expect = "Error on line 3 col 39: what"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_59(self):
        input = """class ABC {
            void main() {
                if ("i love you") then {
                    print(what);
                }
            }
        }"""
        expect = "Error on line 4 col 25: ("
        self.assertTrue(TestParser.test(input,expect,259))
    def test_60(self):
        input = """class ABC {
            void main() {
                if ("i love you") then {
                    this.print(what);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_61(self):
        input = """class ABC {
            void main() {
                if ("i love you") then {
                    this.print(what, a[5]);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_62(self):
        input = """class ABC {
            void main() {
                if ("i love you") then {
                    this.print(what, a[5], new ABC);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_63(self):
        input = """class ABC {
            void main() {
                if ("i love you") then {
                    print.this.that();
                }
            }
        }"""
        expect = "Error on line 4 col 26: this"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_64(self):
        input = """class test {
            int foo() {
                for i := 1 to 5e2 do fibonacci()
            }
        }
        """ 
        expect = "Error on line 3 col 46: ("
        self.assertTrue(TestParser.test(input,expect,264))
    def test_65(self):
        input = """class test {
            int foo() {
                for i := 1 to 5e2 do this.fibonacci()
            }
        }
        """ 
        expect = "Error on line 4 col 12: }"
        self.assertTrue(TestParser.test(input,expect,265))
    def test_66(self):
        input = """class test {
            int foo() {
                for i := 1 to 5e2 do this.fibonacci();
            }
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_67(self):
        input = """class test {
            int foo() {
                for i := 1 to 5e2 do this.fibonacci();
                int foo2() {
                    return 1;
                }
            }
        }
        """ 
        expect = "Error on line 4 col 16: int"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_68(self):
        input = """
            class test {
                int[6] := {1};
            }
            """
        expect = "Error on line 3 col 23: :="
        self.assertTrue(TestParser.test(input,expect,268))
    def test_69(self):
        input = """class ABC # extends {}
        {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_70(self):
        input = """class ABC extends # ABC {}"""
        expect = "Error on line 1 col 26: <EOF>"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_71(self):
        input = """class ABC /* extends ABC {}
        {string terrorist = "ho" */
        {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
    def test_72(self):
        input = """/* /* */"""
        expect = "Error on line 1 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,272))    
    def test_73(self):
        input = """class test {
            int foo() {
                this.aPI := 3.14;
                value := x.foo(5);
                l[3] := value * 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))    
    def test_74(self):
        input = """
            class test {
                void foo(int a,b;float c) {
                string _str_,o,c;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))    
    def test_75(self):
        input = """
            class test {
                void foo(floata,b,c) {
                string _str_,o,c;
                }
            }
            """
        expect = "Error on line 3 col 31: ,"
        self.assertTrue(TestParser.test(input,expect,275))    
    def test_76(self):
        input = """
            class test {
                void foo(int a,b;c) {
                string _str_,o,c;
                }
            }
            """
        expect = "Error on line 3 col 34: )"
        self.assertTrue(TestParser.test(input,expect,276))    
    def test_77(self):
        input = """class test {
	int foo(){
    a := b / 2 * n / 4 && 5 % g || 2 * 9 / 4 % 2;
	}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))    
    def test_78(self):
        input = """class test {
            int main() {
                a[b+c/d*e.f] = new Obj;
            }
        }"""
        expect = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.test(input,expect,278))    
    def test_79(self):
        input = """class test {
            int main() {
                a[b+c/d*e.f] := new Obj;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))    
    def test_80(self):
        input = """class test {
            int main() {
                new Obj := [b+c/d*e.f];
            }
        }"""
        expect = "Error on line 3 col 16: new"
        self.assertTrue(TestParser.test(input,expect,280))    
    def test_81(self):
        input = """class test {
            int main() {
                +a := 5;
            }
        }"""
        expect = "Error on line 3 col 16: +"
        self.assertTrue(TestParser.test(input,expect,281))    
    def test_82(self):
        input = """class test {
            int main() {
                a := +a;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))    
    def test_83(self):
        input = """class test {
            static final static final string abc;
        }"""
        expect = "Error on line 2 col 25: static"
        self.assertTrue(TestParser.test(input,expect,283))    
    def test_84(self):
        input = """class test {
            static static string abc;
        }"""
        expect = "Error on line 2 col 19: static"
        self.assertTrue(TestParser.test(input,expect,284))    
    def test_85(self):
        input = """class test {
            string final = "final";
        }"""
        expect = "Error on line 2 col 19: final"
        self.assertTrue(TestParser.test(input,expect,285))    
    def test_86(self):
        input = """class test {
            finaL string = "final";
        }"""
        expect = "Error on line 2 col 18: string"
        self.assertTrue(TestParser.test(input,expect,286))    
    def test_87(self):
        input = """class final {
            PPL ass_1;
        }"""
        expect = "Error on line 1 col 6: final"
        self.assertTrue(TestParser.test(input,expect,287))    
    def test_88(self):
        input = """class Final {
            PPL ass_1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))    
    def test_89(self):
        input = """class static {
            PPL ass_1;
        }"""
        expect = "Error on line 1 col 6: static"
        self.assertTrue(TestParser.test(input,expect,289))    
    def test_90(self):
        input = """class PPL {
            int main() {
                static integer;
            }
        }"""
        expect = "Error on line 3 col 16: static"
        self.assertTrue(TestParser.test(input,expect,290))    
    def test_91(self):
        input = """class PPL {
            int 12e = 23;
        }"""
        expect = "Error on line 2 col 16: 12"
        self.assertTrue(TestParser.test(input,expect,291))    
    def test_92(self):
        input = """class PPL {
            int __e__ = "string";
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))    
    def test_93(self):
        input = """
            class Shape {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                float length,width;
                static int getNumOfShape() {
                    return numOfShape;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))    
    def test_94(self):
        input = """clasS ABC extends abc {}"""
        expect = "Error on line 1 col 0: clasS"
        self.assertTrue(TestParser.test(input,expect,294))    
    def test_95(self):
        input = """/* This is the biggest comment i've ever made */ """
        expect = "Error on line 1 col 49: <EOF>"
        self.assertTrue(TestParser.test(input,expect,295))    
    def test_96(self):
        input = """class abc extends static {}"""
        expect = "Error on line 1 col 18: static"
        self.assertTrue(TestParser.test(input,expect,296))    
    def test_97(self):
        input = """class test {
            static final test char;
            final static int[] arr;
        }"""
        expect = "Error on line 3 col 29: ]"
        self.assertTrue(TestParser.test(input,expect,297))    
    def test_98(self):
        input = """class test {
            static final Shape char;
            final static int["abc"] arr;
        }"""
        expect = "Error on line 3 col 29: abc"
        self.assertTrue(TestParser.test(input,expect,298))    
    def test_99(self):
        input = """class test {
            static final Shape char;
            final static int arr[5];
        }"""
        expect = "Error on line 3 col 32: ["
        self.assertTrue(TestParser.test(input,expect,299))    
    def test_100(self):
        input = """ 
        class Point 
        {
            int x, y;
            static float length(Point a, Point b) 
            {
                return Math.sqrt(Math.sqr(a.x - b.x) - (a.y - b.y));
            }
        }
        class Triangle 
        {
            Point point1, point2, point3;
            float edge1, edge2, edge3;
            Triangle(Point p1, Point p2, Point p3) 
            {
                this.point1 := p1;
                this.point2 := p2;
                this.point3 := p3;
                this.edge1 := Point.length(p1, p2);
                this.edge2 := Point.length(p2, p3);
                this.edge3 := Point.length(p3, p1);
            }
            float circumference() 
            {
                return (this.edge1 + this.edge2 + this.edge3) / 2;
            }
            float area() 
            {
                float p;
                p := this.circumference();
                return Math.sqrt(p * (p - this.edge1) * (p - this.edge2) * (p - this.edge3));
            }
        } 
        class Program
        {
            void main() 
            {
                Point p1, p2, p3;
                Triangle abc;
                float area;
                p1 := new Point(0, 0);
                p2 := new Point(0, 1);
                p3 := new Point(1, 0);
                abc := new Triangle(p1, p2, p3);
                area := abc.area();
                io.writeLn("Area of triangle: ", area);
            }
        } 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

    # def test_(self):
    #     input = """"""
    #     expect = ""
    #     self.assertTrue(TestParser.test(input,expect,300))