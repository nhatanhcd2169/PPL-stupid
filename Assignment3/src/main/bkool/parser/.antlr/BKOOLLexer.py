# Generated from d:\Code\GitHub\PPL-iachay\Assignment3\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\7\2\u0094\n\2")
        buf.write("\f\2\16\2\u0097\13\2\3\2\5\2\u009a\n\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\7\3\u00a2\n\3\f\3\16\3\u00a5\13\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\6:\u0178\n:\r:\16")
        buf.write(":\u0179\3:\3:\3;\6;\u017f\n;\r;\16;\u0180\3<\6<\u0184")
        buf.write("\n<\r<\16<\u0185\3<\3<\3<\3<\3<\5<\u018d\n<\3=\3=\7=\u0191")
        buf.write("\n=\f=\16=\u0194\13=\3=\3=\3=\3>\3>\5>\u019b\n>\3>\6>")
        buf.write("\u019e\n>\r>\16>\u019f\3?\3?\5?\u01a4\n?\3@\3@\7@\u01a8")
        buf.write("\n@\f@\16@\u01ab\13@\3A\3A\3B\3B\5B\u01b1\nB\3C\3C\3C")
        buf.write("\3D\3D\3D\5D\u01b9\nD\3E\3E\7E\u01bd\nE\fE\16E\u01c0\13")
        buf.write("E\3F\3F\7F\u01c4\nF\fF\16F\u01c7\13F\3F\3F\3F\5F\u01cc")
        buf.write("\nF\3F\3F\3G\3G\7G\u01d2\nG\fG\16G\u01d5\13G\3G\3G\3G")
        buf.write("\3H\3H\3H\4\u0095\u00a3\2I\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u<w=y>{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089?\u008b@\u008dA\u008fB\3\2\r\3")
        buf.write("\3\f\f\5\2\13\f\16\17\"\"\3\2$$\4\2GGgg\3\2\62;\6\2\f")
        buf.write("\f\17\17$$^^\t\2$$^^ddhhppttvv\3\2^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\4\2\f\f\17\17\2\u01e7\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3")
        buf.write("\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2")
        buf.write("\5\u009d\3\2\2\2\7\u00ab\3\2\2\2\t\u00b0\3\2\2\2\13\u00b2")
        buf.write("\3\2\2\2\r\u00b5\3\2\2\2\17\u00bc\3\2\2\2\21\u00c1\3\2")
        buf.write("\2\2\23\u00c7\3\2\2\2\25\u00cc\3\2\2\2\27\u00cf\3\2\2")
        buf.write("\2\31\u00d4\3\2\2\2\33\u00d9\3\2\2\2\35\u00dd\3\2\2\2")
        buf.write("\37\u00e3\3\2\2\2!\u00ea\3\2\2\2#\u00f2\3\2\2\2%\u00f6")
        buf.write("\3\2\2\2\'\u00f9\3\2\2\2)\u0100\3\2\2\2+\u0103\3\2\2\2")
        buf.write("-\u0109\3\2\2\2/\u0112\3\2\2\2\61\u0118\3\2\2\2\63\u0120")
        buf.write("\3\2\2\2\65\u0124\3\2\2\2\67\u0128\3\2\2\29\u012d\3\2")
        buf.write("\2\2;\u0133\3\2\2\2=\u013a\3\2\2\2?\u013d\3\2\2\2A\u0140")
        buf.write("\3\2\2\2C\u0142\3\2\2\2E\u0144\3\2\2\2G\u0146\3\2\2\2")
        buf.write("I\u0149\3\2\2\2K\u014c\3\2\2\2M\u014f\3\2\2\2O\u0152\3")
        buf.write("\2\2\2Q\u0154\3\2\2\2S\u0156\3\2\2\2U\u0158\3\2\2\2W\u015a")
        buf.write("\3\2\2\2Y\u015c\3\2\2\2[\u015e\3\2\2\2]\u0160\3\2\2\2")
        buf.write("_\u0162\3\2\2\2a\u0164\3\2\2\2c\u0166\3\2\2\2e\u0168\3")
        buf.write("\2\2\2g\u016a\3\2\2\2i\u016c\3\2\2\2k\u016e\3\2\2\2m\u0170")
        buf.write("\3\2\2\2o\u0172\3\2\2\2q\u0174\3\2\2\2s\u0177\3\2\2\2")
        buf.write("u\u017e\3\2\2\2w\u0183\3\2\2\2y\u018e\3\2\2\2{\u0198\3")
        buf.write("\2\2\2}\u01a3\3\2\2\2\177\u01a5\3\2\2\2\u0081\u01ac\3")
        buf.write("\2\2\2\u0083\u01b0\3\2\2\2\u0085\u01b2\3\2\2\2\u0087\u01b8")
        buf.write("\3\2\2\2\u0089\u01ba\3\2\2\2\u008b\u01c1\3\2\2\2\u008d")
        buf.write("\u01cf\3\2\2\2\u008f\u01d9\3\2\2\2\u0091\u0095\7%\2\2")
        buf.write("\u0092\u0094\13\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096")
        buf.write("\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u009a\t\2\2\2")
        buf.write("\u0099\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\b")
        buf.write("\2\2\2\u009c\4\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f")
        buf.write("\7,\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\13\2\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\7,\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\b\3\2\2\u00aa\6\3\2\2\2\u00ab\u00ac")
        buf.write("\7o\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\b\3\2\2\2\u00b0\u00b1\7?\2\2\u00b1\n\3\2")
        buf.write("\2\2\u00b2\u00b3\7<\2\2\u00b3\u00b4\7?\2\2\u00b4\f\3\2")
        buf.write("\2\2\u00b5\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7w\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\16\3\2\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0\7g\2\2\u00c0\20")
        buf.write("\3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6\22")
        buf.write("\3\2\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7u\2\2\u00ca\u00cb\7g\2\2\u00cb\24\3\2\2\2\u00cc\u00cd")
        buf.write("\7k\2\2\u00cd\u00ce\7h\2\2\u00ce\26\3\2\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7j\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3")
        buf.write("\7p\2\2\u00d3\30\3\2\2\2\u00d4\u00d5\7x\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7f\2\2\u00d8\32")
        buf.write("\3\2\2\2\u00d9\u00da\7k\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7v\2\2\u00dc\34\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\36\3\2\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8")
        buf.write("\7p\2\2\u00e8\u00e9\7i\2\2\u00e9 \3\2\2\2\u00ea\u00eb")
        buf.write("\7d\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\"\3\2\2\2\u00f2\u00f3\7h\2\2\u00f3\u00f4")
        buf.write("\7q\2\2\u00f4\u00f5\7t\2\2\u00f5$\3\2\2\2\u00f6\u00f7")
        buf.write("\7v\2\2\u00f7\u00f8\7q\2\2\u00f8&\3\2\2\2\u00f9\u00fa")
        buf.write("\7f\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7y\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7q\2\2\u00ff(\3")
        buf.write("\2\2\2\u0100\u0101\7f\2\2\u0101\u0102\7q\2\2\u0102*\3")
        buf.write("\2\2\2\u0103\u0104\7d\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7c\2\2\u0107\u0108\7m\2\2\u0108,\3")
        buf.write("\2\2\2\u0109\u010a\7e\2\2\u010a\u010b\7q\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7v\2\2\u010d\u010e\7k\2\2\u010e\u010f")
        buf.write("\7p\2\2\u010f\u0110\7w\2\2\u0110\u0111\7g\2\2\u0111.\3")
        buf.write("\2\2\2\u0112\u0113\7e\2\2\u0113\u0114\7n\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115\u0116\7u\2\2\u0116\u0117\7u\2\2\u0117\60")
        buf.write("\3\2\2\2\u0118\u0119\7g\2\2\u0119\u011a\7z\2\2\u011a\u011b")
        buf.write("\7v\2\2\u011b\u011c\7g\2\2\u011c\u011d\7p\2\2\u011d\u011e")
        buf.write("\7f\2\2\u011e\u011f\7u\2\2\u011f\62\3\2\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121\u0122\7g\2\2\u0122\u0123\7y\2\2\u0123\64")
        buf.write("\3\2\2\2\u0124\u0125\7p\2\2\u0125\u0126\7k\2\2\u0126\u0127")
        buf.write("\7n\2\2\u0127\66\3\2\2\2\u0128\u0129\7v\2\2\u0129\u012a")
        buf.write("\7j\2\2\u012a\u012b\7k\2\2\u012b\u012c\7u\2\2\u012c8\3")
        buf.write("\2\2\2\u012d\u012e\7h\2\2\u012e\u012f\7k\2\2\u012f\u0130")
        buf.write("\7p\2\2\u0130\u0131\7c\2\2\u0131\u0132\7n\2\2\u0132:\3")
        buf.write("\2\2\2\u0133\u0134\7u\2\2\u0134\u0135\7v\2\2\u0135\u0136")
        buf.write("\7c\2\2\u0136\u0137\7v\2\2\u0137\u0138\7k\2\2\u0138\u0139")
        buf.write("\7e\2\2\u0139<\3\2\2\2\u013a\u013b\7(\2\2\u013b\u013c")
        buf.write("\7(\2\2\u013c>\3\2\2\2\u013d\u013e\7~\2\2\u013e\u013f")
        buf.write("\7~\2\2\u013f@\3\2\2\2\u0140\u0141\7#\2\2\u0141B\3\2\2")
        buf.write("\2\u0142\u0143\7>\2\2\u0143D\3\2\2\2\u0144\u0145\7@\2")
        buf.write("\2\u0145F\3\2\2\2\u0146\u0147\7?\2\2\u0147\u0148\7?\2")
        buf.write("\2\u0148H\3\2\2\2\u0149\u014a\7#\2\2\u014a\u014b\7?\2")
        buf.write("\2\u014bJ\3\2\2\2\u014c\u014d\7>\2\2\u014d\u014e\7?\2")
        buf.write("\2\u014eL\3\2\2\2\u014f\u0150\7@\2\2\u0150\u0151\7?\2")
        buf.write("\2\u0151N\3\2\2\2\u0152\u0153\7-\2\2\u0153P\3\2\2\2\u0154")
        buf.write("\u0155\7/\2\2\u0155R\3\2\2\2\u0156\u0157\7,\2\2\u0157")
        buf.write("T\3\2\2\2\u0158\u0159\7\'\2\2\u0159V\3\2\2\2\u015a\u015b")
        buf.write("\7^\2\2\u015bX\3\2\2\2\u015c\u015d\7\61\2\2\u015dZ\3\2")
        buf.write("\2\2\u015e\u015f\7`\2\2\u015f\\\3\2\2\2\u0160\u0161\5")
        buf.write("\63\32\2\u0161^\3\2\2\2\u0162\u0163\7}\2\2\u0163`\3\2")
        buf.write("\2\2\u0164\u0165\7\177\2\2\u0165b\3\2\2\2\u0166\u0167")
        buf.write("\7*\2\2\u0167d\3\2\2\2\u0168\u0169\7+\2\2\u0169f\3\2\2")
        buf.write("\2\u016a\u016b\7]\2\2\u016bh\3\2\2\2\u016c\u016d\7_\2")
        buf.write("\2\u016dj\3\2\2\2\u016e\u016f\7\60\2\2\u016fl\3\2\2\2")
        buf.write("\u0170\u0171\7.\2\2\u0171n\3\2\2\2\u0172\u0173\7<\2\2")
        buf.write("\u0173p\3\2\2\2\u0174\u0175\7=\2\2\u0175r\3\2\2\2\u0176")
        buf.write("\u0178\t\3\2\2\u0177\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017b\3")
        buf.write("\2\2\2\u017b\u017c\b:\2\2\u017ct\3\2\2\2\u017d\u017f\5")
        buf.write("\u0081A\2\u017e\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181v\3\2\2\2\u0182")
        buf.write("\u0184\5\u0081A\2\u0183\u0182\3\2\2\2\u0184\u0185\3\2")
        buf.write("\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u018c")
        buf.write("\3\2\2\2\u0187\u018d\5\177@\2\u0188\u018d\5{>\2\u0189")
        buf.write("\u018a\5\177@\2\u018a\u018b\5{>\2\u018b\u018d\3\2\2\2")
        buf.write("\u018c\u0187\3\2\2\2\u018c\u0188\3\2\2\2\u018c\u0189\3")
        buf.write("\2\2\2\u018dx\3\2\2\2\u018e\u0192\t\4\2\2\u018f\u0191")
        buf.write("\5\u0083B\2\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0195\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0195\u0196\t\4\2\2\u0196\u0197\b")
        buf.write("=\3\2\u0197z\3\2\2\2\u0198\u019a\t\5\2\2\u0199\u019b\5")
        buf.write("}?\2\u019a\u0199\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d")
        buf.write("\3\2\2\2\u019c\u019e\5\u0081A\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0|\3\2\2\2\u01a1\u01a4\5O(\2\u01a2\u01a4\5Q)\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a3\u01a2\3\2\2\2\u01a4~\3\2\2\2\u01a5")
        buf.write("\u01a9\5k\66\2\u01a6\u01a8\5\u0081A\2\u01a7\u01a6\3\2")
        buf.write("\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa")
        buf.write("\3\2\2\2\u01aa\u0080\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac")
        buf.write("\u01ad\t\6\2\2\u01ad\u0082\3\2\2\2\u01ae\u01b1\5\u0085")
        buf.write("C\2\u01af\u01b1\n\7\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u0084\3\2\2\2\u01b2\u01b3\7^\2\2\u01b3")
        buf.write("\u01b4\t\b\2\2\u01b4\u0086\3\2\2\2\u01b5\u01b6\7^\2\2")
        buf.write("\u01b6\u01b9\n\b\2\2\u01b7\u01b9\n\t\2\2\u01b8\u01b5\3")
        buf.write("\2\2\2\u01b8\u01b7\3\2\2\2\u01b9\u0088\3\2\2\2\u01ba\u01be")
        buf.write("\t\n\2\2\u01bb\u01bd\t\13\2\2\u01bc\u01bb\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u008a\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c5\t")
        buf.write("\4\2\2\u01c2\u01c4\5\u0083B\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01cb\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01cc\t")
        buf.write("\f\2\2\u01c9\u01cc\n\4\2\2\u01ca\u01cc\7\2\2\3\u01cb\u01c8")
        buf.write("\3\2\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01ce\bF\4\2\u01ce\u008c\3\2\2\2")
        buf.write("\u01cf\u01d3\t\4\2\2\u01d0\u01d2\5\u0083B\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d6\u01d7\5\u0087D\2\u01d7\u01d8\bG\5\2\u01d8\u008e")
        buf.write("\3\2\2\2\u01d9\u01da\13\2\2\2\u01da\u01db\bH\6\2\u01db")
        buf.write("\u0090\3\2\2\2\25\2\u0095\u0099\u00a3\u0179\u0180\u0185")
        buf.write("\u018c\u0192\u019a\u019f\u01a3\u01a9\u01b0\u01b8\u01be")
        buf.write("\u01c5\u01cb\u01d3\7\b\2\2\3=\2\3F\3\3G\4\3H\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LINECOMMENT = 1
    BLOCKCOMMENT = 2
    MAIN = 3
    EQUAL_SIGN = 4
    ASSIGN = 5
    RETURN = 6
    TRUE = 7
    FALSE = 8
    ELSE = 9
    IF = 10
    THEN = 11
    VOID = 12
    INT = 13
    FLOAT = 14
    STRING = 15
    BOOLEAN = 16
    FOR = 17
    TO = 18
    DOWNTO = 19
    DO = 20
    BREAK = 21
    CONTINUE = 22
    CLASS = 23
    EXTENDS = 24
    NEW = 25
    NIL = 26
    THIS = 27
    FINAL = 28
    STATIC = 29
    AND = 30
    OR = 31
    NOT = 32
    LESS = 33
    GREATER = 34
    EQUAL = 35
    NOT_EQUAL = 36
    LESS_EQUAL = 37
    GREATER_EQUAL = 38
    PLUS = 39
    MINUS = 40
    MULTIPLY = 41
    MODULUS = 42
    I_DIVIDE = 43
    F_DIVIDE = 44
    CONCATENATE = 45
    OBJECT_NEW = 46
    LP = 47
    RP = 48
    LB = 49
    RB = 50
    LSB = 51
    RSB = 52
    DOT = 53
    COMMA = 54
    COLON = 55
    S_COLON = 56
    WS = 57
    INTEGER_LITERAL = 58
    FLOAT_LITERAL = 59
    STRING_LITERAL = 60
    ID = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'='", "':='", "'return'", "'true'", "'false'", "'else'", 
            "'if'", "'then'", "'void'", "'int'", "'float'", "'string'", 
            "'boolean'", "'for'", "'to'", "'downto'", "'do'", "'break'", 
            "'continue'", "'class'", "'extends'", "'new'", "'nil'", "'this'", 
            "'final'", "'static'", "'&&'", "'||'", "'!'", "'<'", "'>'", 
            "'=='", "'!='", "'<='", "'>='", "'+'", "'-'", "'*'", "'%'", 
            "'\\'", "'/'", "'^'", "'{'", "'}'", "'('", "')'", "'['", "']'", 
            "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "LINECOMMENT", "BLOCKCOMMENT", "MAIN", "EQUAL_SIGN", "ASSIGN", 
            "RETURN", "TRUE", "FALSE", "ELSE", "IF", "THEN", "VOID", "INT", 
            "FLOAT", "STRING", "BOOLEAN", "FOR", "TO", "DOWNTO", "DO", "BREAK", 
            "CONTINUE", "CLASS", "EXTENDS", "NEW", "NIL", "THIS", "FINAL", 
            "STATIC", "AND", "OR", "NOT", "LESS", "GREATER", "EQUAL", "NOT_EQUAL", 
            "LESS_EQUAL", "GREATER_EQUAL", "PLUS", "MINUS", "MULTIPLY", 
            "MODULUS", "I_DIVIDE", "F_DIVIDE", "CONCATENATE", "OBJECT_NEW", 
            "LP", "RP", "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "COLON", 
            "S_COLON", "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
            "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "LINECOMMENT", "BLOCKCOMMENT", "MAIN", "EQUAL_SIGN", "ASSIGN", 
                  "RETURN", "TRUE", "FALSE", "ELSE", "IF", "THEN", "VOID", 
                  "INT", "FLOAT", "STRING", "BOOLEAN", "FOR", "TO", "DOWNTO", 
                  "DO", "BREAK", "CONTINUE", "CLASS", "EXTENDS", "NEW", 
                  "NIL", "THIS", "FINAL", "STATIC", "AND", "OR", "NOT", 
                  "LESS", "GREATER", "EQUAL", "NOT_EQUAL", "LESS_EQUAL", 
                  "GREATER_EQUAL", "PLUS", "MINUS", "MULTIPLY", "MODULUS", 
                  "I_DIVIDE", "F_DIVIDE", "CONCATENATE", "OBJECT_NEW", "LP", 
                  "RP", "LB", "RB", "LSB", "RSB", "DOT", "COMMA", "COLON", 
                  "S_COLON", "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                  "EXPONENT", "SIGN", "DECIMAL", "DIGIT", "STR_CHAR", "ESC_SEQ", 
                  "ILL_ESCAPE", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRING_LITERAL_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	output = str(self.text)
            	err = ['\u000a', '\r', EOFError]
            	if (output[-1] in err):
            		raise UncloseString(output[1:-1])
            	else:
            		raise UncloseString(output[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])	

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            	
            	raise ErrorToken(self.text)

     


