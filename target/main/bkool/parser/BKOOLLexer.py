# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01d0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\7\2\u0088\n\2\f\2\16\2\u008b\13\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\7\3\u0094\n\3\f\3\16\3\u0097\13\3\3\3\5\3")
        buf.write("\u009a\n\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&")
        buf.write("\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\6:")
        buf.write("\u016a\n:\r:\16:\u016b\3:\3:\3;\6;\u0171\n;\r;\16;\u0172")
        buf.write("\3<\6<\u0176\n<\r<\16<\u0177\3<\3<\7<\u017c\n<\f<\16<")
        buf.write("\u017f\13<\3<\3<\5<\u0183\n<\3<\6<\u0186\n<\r<\16<\u0187")
        buf.write("\3<\3<\7<\u018c\n<\f<\16<\u018f\13<\3<\3<\5<\u0193\n<")
        buf.write("\3<\6<\u0196\n<\r<\16<\u0197\5<\u019a\n<\3=\3=\3=\3=\7")
        buf.write("=\u01a0\n=\f=\16=\u01a3\13=\3=\3=\3=\3>\5>\u01a9\n>\3")
        buf.write(">\7>\u01ac\n>\f>\16>\u01af\13>\3?\3?\3?\3@\3@\3@\3@\7")
        buf.write("@\u01b8\n@\f@\16@\u01bb\13@\3@\3@\3@\3@\5@\u01c1\n@\3")
        buf.write("A\3A\3A\3A\7A\u01c7\nA\fA\16A\u01ca\13A\3A\5A\u01cd\n")
        buf.write("A\3A\3A\4\u0089\u0095\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\3\2\16")
        buf.write("\3\3\f\f\5\2\13\f\16\17\"\"\3\2\62;\4\2GGgg\5\2--//~~")
        buf.write("\3\2$$\7\2\f\f\16\17$$))^^\t\2))^^ddhhppttvv\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\3\2^^\4\3\f\f\16\17\2\u01e4\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3")
        buf.write("\2\2\2\5\u0091\3\2\2\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2")
        buf.write("\13\u00a2\3\2\2\2\r\u00a7\3\2\2\2\17\u00ae\3\2\2\2\21")
        buf.write("\u00b3\3\2\2\2\23\u00b9\3\2\2\2\25\u00bf\3\2\2\2\27\u00c7")
        buf.write("\3\2\2\2\31\u00cb\3\2\2\2\33\u00cf\3\2\2\2\35\u00d4\3")
        buf.write("\2\2\2\37\u00da\3\2\2\2!\u00e1\3\2\2\2#\u00e4\3\2\2\2")
        buf.write("%\u00e9\3\2\2\2\'\u00ee\3\2\2\2)\u00f2\3\2\2\2+\u00f8")
        buf.write("\3\2\2\2-\u00ff\3\2\2\2/\u0107\3\2\2\2\61\u010c\3\2\2")
        buf.write("\2\63\u0110\3\2\2\2\65\u0113\3\2\2\2\67\u011a\3\2\2\2")
        buf.write("9\u011d\3\2\2\2;\u0123\3\2\2\2=\u012c\3\2\2\2?\u012f\3")
        buf.write("\2\2\2A\u0132\3\2\2\2C\u0134\3\2\2\2E\u0136\3\2\2\2G\u0138")
        buf.write("\3\2\2\2I\u013b\3\2\2\2K\u013e\3\2\2\2M\u0141\3\2\2\2")
        buf.write("O\u0144\3\2\2\2Q\u0146\3\2\2\2S\u0148\3\2\2\2U\u014a\3")
        buf.write("\2\2\2W\u014c\3\2\2\2Y\u014e\3\2\2\2[\u0150\3\2\2\2]\u0152")
        buf.write("\3\2\2\2_\u0154\3\2\2\2a\u0156\3\2\2\2c\u0158\3\2\2\2")
        buf.write("e\u015a\3\2\2\2g\u015c\3\2\2\2i\u015e\3\2\2\2k\u0160\3")
        buf.write("\2\2\2m\u0162\3\2\2\2o\u0164\3\2\2\2q\u0166\3\2\2\2s\u0169")
        buf.write("\3\2\2\2u\u0170\3\2\2\2w\u0175\3\2\2\2y\u019b\3\2\2\2")
        buf.write("{\u01a8\3\2\2\2}\u01b0\3\2\2\2\177\u01c0\3\2\2\2\u0081")
        buf.write("\u01c2\3\2\2\2\u0083\u0084\7\61\2\2\u0084\u0085\7,\2\2")
        buf.write("\u0085\u0089\3\2\2\2\u0086\u0088\13\2\2\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u008a\3\2\2\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u008c\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008c\u008d\7,\2\2\u008d\u008e\7\61\2\2\u008e\u008f\3")
        buf.write("\2\2\2\u008f\u0090\b\2\2\2\u0090\4\3\2\2\2\u0091\u0095")
        buf.write("\7%\2\2\u0092\u0094\13\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\u0097\3\2\2\2\u0095\u0096\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\t")
        buf.write("\2\2\2\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c")
        buf.write("\b\3\2\2\u009c\6\3\2\2\2\u009d\u009e\7?\2\2\u009e\b\3")
        buf.write("\2\2\2\u009f\u00a0\7<\2\2\u00a0\u00a1\7?\2\2\u00a1\n\3")
        buf.write("\2\2\2\u00a2\u00a3\7o\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5")
        buf.write("\7k\2\2\u00a5\u00a6\7p\2\2\u00a6\f\3\2\2\2\u00a7\u00a8")
        buf.write("\7t\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7w\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7p\2\2\u00ad\16")
        buf.write("\3\2\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1")
        buf.write("\7w\2\2\u00b1\u00b2\7g\2\2\u00b2\20\3\2\2\2\u00b3\u00b4")
        buf.write("\7h\2\2\u00b4\u00b5\7c\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7")
        buf.write("\7u\2\2\u00b7\u00b8\7g\2\2\u00b8\22\3\2\2\2\u00b9\u00ba")
        buf.write("\7e\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7u\2\2\u00bd\u00be\7u\2\2\u00be\24\3\2\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0\u00c1\7z\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7g\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7f\2\2\u00c5\u00c6")
        buf.write("\7u\2\2\u00c6\26\3\2\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00ca\7y\2\2\u00ca\30\3\2\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7n\2\2\u00ce\32")
        buf.write("\3\2\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7j\2\2\u00d1\u00d2")
        buf.write("\7k\2\2\u00d2\u00d3\7u\2\2\u00d3\34\3\2\2\2\u00d4\u00d5")
        buf.write("\7h\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7c\2\2\u00d8\u00d9\7n\2\2\u00d9\36\3\2\2\2\u00da\u00db")
        buf.write("\7u\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7v\2\2\u00de\u00df\7k\2\2\u00df\u00e0\7e\2\2\u00e0 \3")
        buf.write("\2\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7h\2\2\u00e3\"\3")
        buf.write("\2\2\2\u00e4\u00e5\7g\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7")
        buf.write("\7u\2\2\u00e7\u00e8\7g\2\2\u00e8$\3\2\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\u00eb\7j\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed&\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7v\2\2\u00f1(\3\2\2\2\u00f2\u00f3")
        buf.write("\7h\2\2\u00f3\u00f4\7n\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7c\2\2\u00f6\u00f7\7v\2\2\u00f7*\3\2\2\2\u00f8\u00f9")
        buf.write("\7u\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc")
        buf.write("\7k\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe,\3")
        buf.write("\2\2\2\u00ff\u0100\7d\2\2\u0100\u0101\7q\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\u0103\7n\2\2\u0103\u0104\7g\2\2\u0104\u0105")
        buf.write("\7c\2\2\u0105\u0106\7p\2\2\u0106.\3\2\2\2\u0107\u0108")
        buf.write("\7x\2\2\u0108\u0109\7q\2\2\u0109\u010a\7k\2\2\u010a\u010b")
        buf.write("\7f\2\2\u010b\60\3\2\2\2\u010c\u010d\7h\2\2\u010d\u010e")
        buf.write("\7q\2\2\u010e\u010f\7t\2\2\u010f\62\3\2\2\2\u0110\u0111")
        buf.write("\7v\2\2\u0111\u0112\7q\2\2\u0112\64\3\2\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114\u0115\7q\2\2\u0115\u0116\7y\2\2\u0116\u0117")
        buf.write("\7p\2\2\u0117\u0118\7v\2\2\u0118\u0119\7q\2\2\u0119\66")
        buf.write("\3\2\2\2\u011a\u011b\7f\2\2\u011b\u011c\7q\2\2\u011c8")
        buf.write("\3\2\2\2\u011d\u011e\7d\2\2\u011e\u011f\7t\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7c\2\2\u0121\u0122\7m\2\2\u0122:\3")
        buf.write("\2\2\2\u0123\u0124\7e\2\2\u0124\u0125\7q\2\2\u0125\u0126")
        buf.write("\7p\2\2\u0126\u0127\7v\2\2\u0127\u0128\7k\2\2\u0128\u0129")
        buf.write("\7p\2\2\u0129\u012a\7w\2\2\u012a\u012b\7g\2\2\u012b<\3")
        buf.write("\2\2\2\u012c\u012d\7(\2\2\u012d\u012e\7(\2\2\u012e>\3")
        buf.write("\2\2\2\u012f\u0130\7~\2\2\u0130\u0131\7~\2\2\u0131@\3")
        buf.write("\2\2\2\u0132\u0133\7#\2\2\u0133B\3\2\2\2\u0134\u0135\7")
        buf.write(">\2\2\u0135D\3\2\2\2\u0136\u0137\7@\2\2\u0137F\3\2\2\2")
        buf.write("\u0138\u0139\7?\2\2\u0139\u013a\7?\2\2\u013aH\3\2\2\2")
        buf.write("\u013b\u013c\7#\2\2\u013c\u013d\7?\2\2\u013dJ\3\2\2\2")
        buf.write("\u013e\u013f\7>\2\2\u013f\u0140\7?\2\2\u0140L\3\2\2\2")
        buf.write("\u0141\u0142\7@\2\2\u0142\u0143\7?\2\2\u0143N\3\2\2\2")
        buf.write("\u0144\u0145\7-\2\2\u0145P\3\2\2\2\u0146\u0147\7/\2\2")
        buf.write("\u0147R\3\2\2\2\u0148\u0149\7,\2\2\u0149T\3\2\2\2\u014a")
        buf.write("\u014b\7\'\2\2\u014bV\3\2\2\2\u014c\u014d\7^\2\2\u014d")
        buf.write("X\3\2\2\2\u014e\u014f\7\61\2\2\u014fZ\3\2\2\2\u0150\u0151")
        buf.write("\7`\2\2\u0151\\\3\2\2\2\u0152\u0153\5\27\f\2\u0153^\3")
        buf.write("\2\2\2\u0154\u0155\7*\2\2\u0155`\3\2\2\2\u0156\u0157\7")
        buf.write("+\2\2\u0157b\3\2\2\2\u0158\u0159\7]\2\2\u0159d\3\2\2\2")
        buf.write("\u015a\u015b\7_\2\2\u015bf\3\2\2\2\u015c\u015d\7}\2\2")
        buf.write("\u015dh\3\2\2\2\u015e\u015f\7\177\2\2\u015fj\3\2\2\2\u0160")
        buf.write("\u0161\7\60\2\2\u0161l\3\2\2\2\u0162\u0163\7.\2\2\u0163")
        buf.write("n\3\2\2\2\u0164\u0165\7<\2\2\u0165p\3\2\2\2\u0166\u0167")
        buf.write("\7=\2\2\u0167r\3\2\2\2\u0168\u016a\t\3\2\2\u0169\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\b:\2\2")
        buf.write("\u016et\3\2\2\2\u016f\u0171\t\4\2\2\u0170\u016f\3\2\2")
        buf.write("\2\u0171\u0172\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173v\3\2\2\2\u0174\u0176\t\4\2\2\u0175\u0174")
        buf.write("\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0199\3\2\2\2\u0179\u017d\5k\66\2")
        buf.write("\u017a\u017c\t\4\2\2\u017b\u017a\3\2\2\2\u017c\u017f\3")
        buf.write("\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u019a")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0182\t\5\2\2\u0181")
        buf.write("\u0183\t\6\2\2\u0182\u0181\3\2\2\2\u0182\u0183\3\2\2\2")
        buf.write("\u0183\u0185\3\2\2\2\u0184\u0186\t\4\2\2\u0185\u0184\3")
        buf.write("\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u019a\3\2\2\2\u0189\u018d\5k\66\2\u018a")
        buf.write("\u018c\t\4\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0190\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u0190\u0192\t\5\2\2\u0191\u0193")
        buf.write("\t\6\2\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0195\3\2\2\2\u0194\u0196\t\4\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3")
        buf.write("\2\2\2\u0198\u019a\3\2\2\2\u0199\u0179\3\2\2\2\u0199\u0180")
        buf.write("\3\2\2\2\u0199\u0189\3\2\2\2\u019ax\3\2\2\2\u019b\u01a1")
        buf.write("\t\7\2\2\u019c\u01a0\n\b\2\2\u019d\u019e\7^\2\2\u019e")
        buf.write("\u01a0\t\t\2\2\u019f\u019c\3\2\2\2\u019f\u019d\3\2\2\2")
        buf.write("\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5")
        buf.write("\t\7\2\2\u01a5\u01a6\b=\3\2\u01a6z\3\2\2\2\u01a7\u01a9")
        buf.write("\t\n\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ad\3\2\2\2\u01aa")
        buf.write("\u01ac\t\13\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2")
        buf.write("\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae|\3\2")
        buf.write("\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\13\2\2\2\u01b1\u01b2")
        buf.write("\b?\4\2\u01b2~\3\2\2\2\u01b3\u01b9\t\7\2\2\u01b4\u01b8")
        buf.write("\n\b\2\2\u01b5\u01b6\7^\2\2\u01b6\u01b8\t\t\2\2\u01b7")
        buf.write("\u01b4\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01bb\3\2\2\2")
        buf.write("\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bc\3")
        buf.write("\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\7^\2\2\u01bd\u01c1")
        buf.write("\n\t\2\2\u01be\u01bf\n\f\2\2\u01bf\u01c1\b@\5\2\u01c0")
        buf.write("\u01b3\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u0080\3\2\2\2")
        buf.write("\u01c2\u01c8\t\7\2\2\u01c3\u01c7\n\b\2\2\u01c4\u01c5\7")
        buf.write("^\2\2\u01c5\u01c7\t\t\2\2\u01c6\u01c3\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01cb\u01cd\t\r\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01cf\bA\6\2\u01cf\u0082\3\2\2\2\33\2\u0089")
        buf.write("\u0095\u0099\u016b\u0172\u0177\u017d\u0182\u0187\u018d")
        buf.write("\u0192\u0197\u0199\u019f\u01a1\u01a8\u01ab\u01ad\u01b7")
        buf.write("\u01b9\u01c0\u01c6\u01c8\u01cc\7\b\2\2\3=\2\3?\3\3@\4")
        buf.write("\3A\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCKCOMMENT = 1
    LINECOMMENT = 2
    EQUAL_SIGN = 3
    ASSIGN = 4
    MAIN = 5
    RETURN = 6
    TRUE = 7
    FALSE = 8
    CLASS = 9
    EXTENDS = 10
    NEW = 11
    NIL = 12
    THIS = 13
    FINAL = 14
    STATIC = 15
    IF = 16
    ELSE = 17
    THEN = 18
    INT = 19
    FLOAT = 20
    STRING = 21
    BOOLEAN = 22
    VOID = 23
    FOR = 24
    TO = 25
    DOWNTO = 26
    DO = 27
    BREAK = 28
    CONTINUE = 29
    AND = 30
    OR = 31
    NOT = 32
    LT = 33
    GT = 34
    EQ = 35
    NEQ = 36
    LTE = 37
    GTE = 38
    ADD = 39
    MINUS = 40
    MUL = 41
    MOD = 42
    IDIV = 43
    FDIV = 44
    CONCAT = 45
    OBJ_CREA = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    LP = 51
    RP = 52
    DOT = 53
    COMMA = 54
    COLON = 55
    SEMICOLON = 56
    WS = 57
    INT_LIT = 58
    FLOAT_LIT = 59
    STRING_LIT = 60
    ID = 61
    ERROR_CHAR = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':='", "'main'", "'return'", "'true'", "'false'", "'class'", 
            "'extends'", "'new'", "'nil'", "'this'", "'final'", "'static'", 
            "'if'", "'else'", "'then'", "'int'", "'float'", "'string'", 
            "'boolean'", "'void'", "'for'", "'to'", "'downto'", "'do'", 
            "'break'", "'continue'", "'&&'", "'||'", "'!'", "'<'", "'>'", 
            "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", "'*'", "'%'", 
            "'\\'", "'/'", "'^'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCKCOMMENT", "LINECOMMENT", "EQUAL_SIGN", "ASSIGN", "MAIN", 
            "RETURN", "TRUE", "FALSE", "CLASS", "EXTENDS", "NEW", "NIL", 
            "THIS", "FINAL", "STATIC", "IF", "ELSE", "THEN", "INT", "FLOAT", 
            "STRING", "BOOLEAN", "VOID", "FOR", "TO", "DOWNTO", "DO", "BREAK", 
            "CONTINUE", "AND", "OR", "NOT", "LT", "GT", "EQ", "NEQ", "LTE", 
            "GTE", "ADD", "MINUS", "MUL", "MOD", "IDIV", "FDIV", "CONCAT", 
            "OBJ_CREA", "LB", "RB", "LSB", "RSB", "LP", "RP", "DOT", "COMMA", 
            "COLON", "SEMICOLON", "WS", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "BLOCKCOMMENT", "LINECOMMENT", "EQUAL_SIGN", "ASSIGN", 
                  "MAIN", "RETURN", "TRUE", "FALSE", "CLASS", "EXTENDS", 
                  "NEW", "NIL", "THIS", "FINAL", "STATIC", "IF", "ELSE", 
                  "THEN", "INT", "FLOAT", "STRING", "BOOLEAN", "VOID", "FOR", 
                  "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", "AND", "OR", 
                  "NOT", "LT", "GT", "EQ", "NEQ", "LTE", "GTE", "ADD", "MINUS", 
                  "MUL", "MOD", "IDIV", "FDIV", "CONCAT", "OBJ_CREA", "LB", 
                  "RB", "LSB", "RSB", "LP", "RP", "DOT", "COMMA", "COLON", 
                  "SEMICOLON", "WS", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                  "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRING_LIT_action 
            actions[61] = self.ERROR_CHAR_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise IllegalEscape(self.text[1:])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     


