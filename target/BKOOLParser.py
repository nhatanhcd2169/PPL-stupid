# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u02aa\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\3\2\6\2\u009c\n\2\r\2\16\2\u009d\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3\u00a6\n\3\3\3\3\3\7\3\u00aa\n\3\f\3\16\3\u00ad")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\5\4\u00b4\n\4\3\5\3\5\5\5\u00b8")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00bf\n\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6\u00c8\n\6\f\6\16\6\u00cb\13\6\3\6\3\6")
        buf.write("\3\7\5\7\u00d0\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00d9")
        buf.write("\n\7\f\7\16\7\u00dc\13\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5")
        buf.write("\t\u00e5\n\t\3\n\3\n\5\n\u00e9\n\n\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f8\n\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\7\16\u0101\n\16\f\16\16\16\u0104")
        buf.write("\13\16\3\17\3\17\3\17\5\17\u0109\n\17\3\20\3\20\3\20\5")
        buf.write("\20\u010e\n\20\3\21\3\21\3\21\5\21\u0113\n\21\3\21\3\21")
        buf.write("\3\21\3\22\5\22\u0119\n\22\3\22\3\22\5\22\u011d\n\22\3")
        buf.write("\22\3\22\3\22\5\22\u0122\n\22\3\22\3\22\3\22\5\22\u0127")
        buf.write("\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\7\24")
        buf.write("\u0132\n\24\f\24\16\24\u0135\13\24\3\25\3\25\5\25\u0139")
        buf.write("\n\25\3\26\3\26\3\26\3\26\7\26\u013f\n\26\f\26\16\26\u0142")
        buf.write("\13\26\3\27\3\27\3\27\7\27\u0147\n\27\f\27\16\27\u014a")
        buf.write("\13\27\3\30\3\30\5\30\u014e\n\30\3\31\3\31\3\32\3\32\3")
        buf.write("\32\3\33\3\33\3\34\3\34\5\34\u0159\n\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u0162\n\35\3\36\3\36\7\36\u0166")
        buf.write("\n\36\f\36\16\36\u0169\13\36\3\36\7\36\u016c\n\36\f\36")
        buf.write("\16\36\u016f\13\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0179\n\37\3 \3 \7 \u017d\n \f \16 \u0180\13")
        buf.write(" \3 \7 \u0183\n \f \16 \u0186\13 \3 \3 \3!\3!\3!\5!\u018d")
        buf.write("\n!\3\"\3\"\3\"\3\"\7\"\u0193\n\"\f\"\16\"\u0196\13\"")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3$\3$\7$\u01a0\n$\f$\16$\u01a3\13")
        buf.write("$\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&\7&\u01b0\n&\f&\16&")
        buf.write("\u01b3\13&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\5(\u01bf")
        buf.write("\n(\3)\3)\3)\3)\3*\3*\5*\u01c7\n*\3+\3+\3,\3,\5,\u01cd")
        buf.write("\n,\3-\3-\3-\3-\3-\5-\u01d4\n-\3-\3-\3-\5-\u01d9\n-\5")
        buf.write("-\u01db\n-\3.\3.\3.\3.\3.\5.\u01e2\n.\3.\3.\3.\5.\u01e7")
        buf.write("\n.\5.\u01e9\n.\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01f4\n")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u020f\n\66\3\67\3\67\3\67\3")
        buf.write("\67\3\67\5\67\u0216\n\67\38\38\38\38\38\38\38\78\u021f")
        buf.write("\n8\f8\168\u0222\138\39\39\39\39\39\39\39\79\u022b\n9")
        buf.write("\f9\169\u022e\139\3:\3:\3:\3:\3:\3:\3:\7:\u0237\n:\f:")
        buf.write("\16:\u023a\13:\3;\3;\3;\3;\3;\3;\7;\u0242\n;\f;\16;\u0245")
        buf.write("\13;\3<\3<\3<\5<\u024a\n<\3=\3=\3=\3=\5=\u0250\n=\3>\3")
        buf.write(">\3>\3>\3>\7>\u0257\n>\f>\16>\u025a\13>\3?\3?\3?\3?\3")
        buf.write("?\3?\7?\u0262\n?\f?\16?\u0265\13?\3@\3@\3@\3@\3@\5@\u026c")
        buf.write("\n@\3A\3A\3A\3A\3A\3A\3A\3A\5A\u0276\nA\3B\3B\3C\3C\3")
        buf.write("D\3D\3E\3E\3F\3F\3G\3G\3G\3G\3H\3H\3H\3I\3I\5I\u028b\n")
        buf.write("I\3I\3I\3J\3J\3J\7J\u0292\nJ\fJ\16J\u0295\13J\3K\3K\3")
        buf.write("L\3L\3L\3L\5L\u029d\nL\3M\3M\3M\3M\7M\u02a3\nM\fM\16M")
        buf.write("\u02a6\13M\3M\3M\3M\2\bnprtz|N\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\2\n\3\2\17")
        buf.write("\22\3\2\24\25\3\2)*\3\2+.\3\2 !\3\2%&\4\2#$\'(\3\2\t\n")
        buf.write("\2\u02b1\2\u009b\3\2\2\2\4\u00a1\3\2\2\2\6\u00b3\3\2\2")
        buf.write("\2\b\u00b7\3\2\2\2\n\u00be\3\2\2\2\f\u00cf\3\2\2\2\16")
        buf.write("\u00df\3\2\2\2\20\u00e4\3\2\2\2\22\u00e8\3\2\2\2\24\u00ea")
        buf.write("\3\2\2\2\26\u00ec\3\2\2\2\30\u00f7\3\2\2\2\32\u00fd\3")
        buf.write("\2\2\2\34\u0105\3\2\2\2\36\u010d\3\2\2\2 \u010f\3\2\2")
        buf.write("\2\"\u0118\3\2\2\2$\u0128\3\2\2\2&\u012e\3\2\2\2(\u0138")
        buf.write("\3\2\2\2*\u013a\3\2\2\2,\u0143\3\2\2\2.\u014d\3\2\2\2")
        buf.write("\60\u014f\3\2\2\2\62\u0151\3\2\2\2\64\u0154\3\2\2\2\66")
        buf.write("\u0158\3\2\2\28\u0161\3\2\2\2:\u0163\3\2\2\2<\u0178\3")
        buf.write("\2\2\2>\u017a\3\2\2\2@\u018c\3\2\2\2B\u018e\3\2\2\2D\u0199")
        buf.write("\3\2\2\2F\u019b\3\2\2\2H\u01a6\3\2\2\2J\u01a8\3\2\2\2")
        buf.write("L\u01b6\3\2\2\2N\u01be\3\2\2\2P\u01c0\3\2\2\2R\u01c6\3")
        buf.write("\2\2\2T\u01c8\3\2\2\2V\u01cc\3\2\2\2X\u01ce\3\2\2\2Z\u01dc")
        buf.write("\3\2\2\2\\\u01ea\3\2\2\2^\u01f5\3\2\2\2`\u01fa\3\2\2\2")
        buf.write("b\u01fd\3\2\2\2d\u0200\3\2\2\2f\u0203\3\2\2\2h\u0207\3")
        buf.write("\2\2\2j\u020e\3\2\2\2l\u0215\3\2\2\2n\u0217\3\2\2\2p\u0223")
        buf.write("\3\2\2\2r\u022f\3\2\2\2t\u023b\3\2\2\2v\u0249\3\2\2\2")
        buf.write("x\u024f\3\2\2\2z\u0251\3\2\2\2|\u025b\3\2\2\2~\u026b\3")
        buf.write("\2\2\2\u0080\u0275\3\2\2\2\u0082\u0277\3\2\2\2\u0084\u0279")
        buf.write("\3\2\2\2\u0086\u027b\3\2\2\2\u0088\u027d\3\2\2\2\u008a")
        buf.write("\u027f\3\2\2\2\u008c\u0281\3\2\2\2\u008e\u0285\3\2\2\2")
        buf.write("\u0090\u0288\3\2\2\2\u0092\u028e\3\2\2\2\u0094\u0296\3")
        buf.write("\2\2\2\u0096\u029c\3\2\2\2\u0098\u029e\3\2\2\2\u009a\u009c")
        buf.write("\5\4\3\2\u009b\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u00a0\7\2\2\3\u00a0\3\3\2\2\2\u00a1\u00a2\7\31")
        buf.write("\2\2\u00a2\u00a5\7?\2\2\u00a3\u00a4\7\32\2\2\u00a4\u00a6")
        buf.write("\7?\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a7\3\2\2\2\u00a7\u00ab\7\61\2\2\u00a8\u00aa\5\6\4")
        buf.write("\2\u00a9\u00a8\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ae\u00af\7\62\2\2\u00af\5\3\2\2\2\u00b0")
        buf.write("\u00b4\5\b\5\2\u00b1\u00b4\5\30\r\2\u00b2\u00b4\5\36\20")
        buf.write("\2\u00b3\u00b0\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\7\3\2\2\2\u00b5\u00b8\5\n\6\2\u00b6\u00b8")
        buf.write("\5\f\7\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8")
        buf.write("\t\3\2\2\2\u00b9\u00bf\7\36\2\2\u00ba\u00bb\7\36\2\2\u00bb")
        buf.write("\u00bf\7\37\2\2\u00bc\u00bd\7\37\2\2\u00bd\u00bf\7\36")
        buf.write("\2\2\u00be\u00b9\3\2\2\2\u00be\u00ba\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1\5\22\n\2\u00c1")
        buf.write("\u00c2\7?\2\2\u00c2\u00c3\5\16\b\2\u00c3\u00c9\3\2\2\2")
        buf.write("\u00c4\u00c5\78\2\2\u00c5\u00c6\7?\2\2\u00c6\u00c8\5\16")
        buf.write("\b\2\u00c7\u00c4\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00cd\7:\2\2\u00cd\13\3\2\2\2\u00ce")
        buf.write("\u00d0\7\37\2\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2")
        buf.write("\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\5\22\n\2\u00d2\u00d3")
        buf.write("\7?\2\2\u00d3\u00d4\5\20\t\2\u00d4\u00da\3\2\2\2\u00d5")
        buf.write("\u00d6\78\2\2\u00d6\u00d7\7?\2\2\u00d7\u00d9\5\20\t\2")
        buf.write("\u00d8\u00d5\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00de\7:\2\2\u00de\r\3\2\2\2\u00df\u00e0")
        buf.write("\7\6\2\2\u00e0\u00e1\5j\66\2\u00e1\17\3\2\2\2\u00e2\u00e3")
        buf.write("\7\6\2\2\u00e3\u00e5\5j\66\2\u00e4\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\21\3\2\2\2\u00e6\u00e9\5\26\f\2\u00e7")
        buf.write("\u00e9\5\24\13\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2")
        buf.write("\2\u00e9\23\3\2\2\2\u00ea\u00eb\t\2\2\2\u00eb\25\3\2\2")
        buf.write("\2\u00ec\u00ed\5\24\13\2\u00ed\u00ee\7\65\2\2\u00ee\u00ef")
        buf.write("\7<\2\2\u00ef\u00f0\7\66\2\2\u00f0\27\3\2\2\2\u00f1\u00f8")
        buf.write("\7\36\2\2\u00f2\u00f8\7\37\2\2\u00f3\u00f4\7\36\2\2\u00f4")
        buf.write("\u00f8\7\37\2\2\u00f5\u00f6\7\37\2\2\u00f6\u00f8\7\36")
        buf.write("\2\2\u00f7\u00f1\3\2\2\2\u00f7\u00f2\3\2\2\2\u00f7\u00f3")
        buf.write("\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fa\5h\65\2\u00fa\u00fb\5\32\16")
        buf.write("\2\u00fb\u00fc\7:\2\2\u00fc\31\3\2\2\2\u00fd\u0102\5\34")
        buf.write("\17\2\u00fe\u00ff\78\2\2\u00ff\u0101\5\34\17\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0101\u0104\3\2\2\2\u0102\u0100\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\33\3\2\2\2\u0104\u0102\3\2\2\2\u0105")
        buf.write("\u0108\5T+\2\u0106\u0107\7\6\2\2\u0107\u0109\5T+\2\u0108")
        buf.write("\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\35\3\2\2\2\u010a")
        buf.write("\u010e\5 \21\2\u010b\u010e\5\"\22\2\u010c\u010e\5$\23")
        buf.write("\2\u010d\u010a\3\2\2\2\u010d\u010b\3\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\37\3\2\2\2\u010f\u0110\7?\2\2\u0110\u0112")
        buf.write("\7\63\2\2\u0111\u0113\5&\24\2\u0112\u0111\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\7\64\2")
        buf.write("\2\u0115\u0116\5> \2\u0116!\3\2\2\2\u0117\u0119\7\37\2")
        buf.write("\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011c")
        buf.write("\3\2\2\2\u011a\u011d\5\22\n\2\u011b\u011d\7\16\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2")
        buf.write("\u011e\u011f\7?\2\2\u011f\u0121\7\63\2\2\u0120\u0122\5")
        buf.write("&\24\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0123")
        buf.write("\3\2\2\2\u0123\u0126\7\64\2\2\u0124\u0127\5:\36\2\u0125")
        buf.write("\u0127\5> \2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127")
        buf.write("#\3\2\2\2\u0128\u0129\7\16\2\2\u0129\u012a\7\5\2\2\u012a")
        buf.write("\u012b\7\63\2\2\u012b\u012c\7\64\2\2\u012c\u012d\5> \2")
        buf.write("\u012d%\3\2\2\2\u012e\u0133\5(\25\2\u012f\u0130\7:\2\2")
        buf.write("\u0130\u0132\5(\25\2\u0131\u012f\3\2\2\2\u0132\u0135\3")
        buf.write("\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\'")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0136\u0139\5*\26\2\u0137")
        buf.write("\u0139\5,\27\2\u0138\u0136\3\2\2\2\u0138\u0137\3\2\2\2")
        buf.write("\u0139)\3\2\2\2\u013a\u013b\5.\30\2\u013b\u0140\5\64\33")
        buf.write("\2\u013c\u013d\78\2\2\u013d\u013f\5\64\33\2\u013e\u013c")
        buf.write("\3\2\2\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u0141\3\2\2\2\u0141+\3\2\2\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u0148\5\62\32\2\u0144\u0145\78\2\2\u0145\u0147\5\62\32")
        buf.write("\2\u0146\u0144\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149-\3\2\2\2\u014a\u0148")
        buf.write("\3\2\2\2\u014b\u014e\5\22\n\2\u014c\u014e\5\60\31\2\u014d")
        buf.write("\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014e/\3\2\2\2\u014f")
        buf.write("\u0150\5h\65\2\u0150\61\3\2\2\2\u0151\u0152\5.\30\2\u0152")
        buf.write("\u0153\5\64\33\2\u0153\63\3\2\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("\65\3\2\2\2\u0156\u0159\5\22\n\2\u0157\u0159\7\16\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2\2\u0159\67\3\2")
        buf.write("\2\2\u015a\u0162\5L\'\2\u015b\u0162\5X-\2\u015c\u0162")
        buf.write("\5\\/\2\u015d\u0162\5b\62\2\u015e\u0162\5d\63\2\u015f")
        buf.write("\u0162\5^\60\2\u0160\u0162\5f\64\2\u0161\u015a\3\2\2\2")
        buf.write("\u0161\u015b\3\2\2\2\u0161\u015c\3\2\2\2\u0161\u015d\3")
        buf.write("\2\2\2\u0161\u015e\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u01629\3\2\2\2\u0163\u0167\7\61\2\2\u0164\u0166")
        buf.write("\5@!\2\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016d\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u016a\u016c\58\35\2\u016b\u016a\3\2\2\2")
        buf.write("\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3")
        buf.write("\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3\2\2\2\u0170\u0171")
        buf.write("\7\62\2\2\u0171;\3\2\2\2\u0172\u0179\5L\'\2\u0173\u0179")
        buf.write("\5X-\2\u0174\u0179\5\\/\2\u0175\u0179\5b\62\2\u0176\u0179")
        buf.write("\5d\63\2\u0177\u0179\5^\60\2\u0178\u0172\3\2\2\2\u0178")
        buf.write("\u0173\3\2\2\2\u0178\u0174\3\2\2\2\u0178\u0175\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179=\3\2\2")
        buf.write("\2\u017a\u017e\7\61\2\2\u017b\u017d\5@!\2\u017c\u017b")
        buf.write("\3\2\2\2\u017d\u0180\3\2\2\2\u017e\u017c\3\2\2\2\u017e")
        buf.write("\u017f\3\2\2\2\u017f\u0184\3\2\2\2\u0180\u017e\3\2\2\2")
        buf.write("\u0181\u0183\5<\37\2\u0182\u0181\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0187")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\7\62\2\2\u0188")
        buf.write("?\3\2\2\2\u0189\u018d\5F$\2\u018a\u018d\5J&\2\u018b\u018d")
        buf.write("\5B\"\2\u018c\u0189\3\2\2\2\u018c\u018a\3\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018dA\3\2\2\2\u018e\u018f\5h\65\2\u018f")
        buf.write("\u0194\5D#\2\u0190\u0191\78\2\2\u0191\u0193\5D#\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0197\u0198\7:\2\2\u0198C\3\2\2\2\u0199\u019a\7")
        buf.write("?\2\2\u019aE\3\2\2\2\u019b\u019c\5\22\n\2\u019c\u01a1")
        buf.write("\5H%\2\u019d\u019e\78\2\2\u019e\u01a0\5H%\2\u019f\u019d")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a4\u01a5\7:\2\2\u01a5G\3\2\2\2\u01a6\u01a7\7?\2\2")
        buf.write("\u01a7I\3\2\2\2\u01a8\u01a9\5\22\n\2\u01a9\u01aa\7\65")
        buf.write("\2\2\u01aa\u01ab\7<\2\2\u01ab\u01ac\7\66\2\2\u01ac\u01b1")
        buf.write("\5H%\2\u01ad\u01ae\78\2\2\u01ae\u01b0\5H%\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b4\3\2\2\2\u01b3\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b5\7:\2\2\u01b5K\3\2\2\2\u01b6\u01b7\5N(\2\u01b7")
        buf.write("\u01b8\7\7\2\2\u01b8\u01b9\5j\66\2\u01b9\u01ba\7:\2\2")
        buf.write("\u01baM\3\2\2\2\u01bb\u01bf\5`\61\2\u01bc\u01bf\5H%\2")
        buf.write("\u01bd\u01bf\5P)\2\u01be\u01bb\3\2\2\2\u01be\u01bc\3\2")
        buf.write("\2\2\u01be\u01bd\3\2\2\2\u01bfO\3\2\2\2\u01c0\u01c1\5")
        buf.write("R*\2\u01c1\u01c2\7\67\2\2\u01c2\u01c3\5V,\2\u01c3Q\3\2")
        buf.write("\2\2\u01c4\u01c7\7\35\2\2\u01c5\u01c7\5T+\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7S\3\2\2\2\u01c8\u01c9")
        buf.write("\7?\2\2\u01c9U\3\2\2\2\u01ca\u01cd\5H%\2\u01cb\u01cd\5")
        buf.write("`\61\2\u01cc\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cdW")
        buf.write("\3\2\2\2\u01ce\u01cf\7\f\2\2\u01cf\u01d0\5j\66\2\u01d0")
        buf.write("\u01d3\7\r\2\2\u01d1\u01d4\58\35\2\u01d2\u01d4\5:\36\2")
        buf.write("\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01da\3")
        buf.write("\2\2\2\u01d5\u01d8\7\13\2\2\u01d6\u01d9\58\35\2\u01d7")
        buf.write("\u01d9\5:\36\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7\3\2\2\2")
        buf.write("\u01d9\u01db\3\2\2\2\u01da\u01d5\3\2\2\2\u01da\u01db\3")
        buf.write("\2\2\2\u01dbY\3\2\2\2\u01dc\u01dd\7\f\2\2\u01dd\u01de")
        buf.write("\5j\66\2\u01de\u01e1\7\r\2\2\u01df\u01e2\58\35\2\u01e0")
        buf.write("\u01e2\5:\36\2\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2")
        buf.write("\u01e2\u01e8\3\2\2\2\u01e3\u01e6\7\13\2\2\u01e4\u01e7")
        buf.write("\58\35\2\u01e5\u01e7\5:\36\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e3\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9[\3\2\2\2\u01ea\u01eb\7\23\2")
        buf.write("\2\u01eb\u01ec\5H%\2\u01ec\u01ed\7\7\2\2\u01ed\u01ee\5")
        buf.write("j\66\2\u01ee\u01ef\t\3\2\2\u01ef\u01f0\5j\66\2\u01f0\u01f3")
        buf.write("\7\26\2\2\u01f1\u01f4\58\35\2\u01f2\u01f4\5:\36\2\u01f3")
        buf.write("\u01f1\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4]\3\2\2\2\u01f5")
        buf.write("\u01f6\5R*\2\u01f6\u01f7\7\67\2\2\u01f7\u01f8\5\u008e")
        buf.write("H\2\u01f8\u01f9\7:\2\2\u01f9_\3\2\2\2\u01fa\u01fb\7?\2")
        buf.write("\2\u01fb\u01fc\5\u008cG\2\u01fca\3\2\2\2\u01fd\u01fe\7")
        buf.write("\27\2\2\u01fe\u01ff\7:\2\2\u01ffc\3\2\2\2\u0200\u0201")
        buf.write("\7\30\2\2\u0201\u0202\7:\2\2\u0202e\3\2\2\2\u0203\u0204")
        buf.write("\7\b\2\2\u0204\u0205\5j\66\2\u0205\u0206\7:\2\2\u0206")
        buf.write("g\3\2\2\2\u0207\u0208\7?\2\2\u0208i\3\2\2\2\u0209\u020a")
        buf.write("\5l\67\2\u020a\u020b\5\u008aF\2\u020b\u020c\5l\67\2\u020c")
        buf.write("\u020f\3\2\2\2\u020d\u020f\5l\67\2\u020e\u0209\3\2\2\2")
        buf.write("\u020e\u020d\3\2\2\2\u020fk\3\2\2\2\u0210\u0211\5n8\2")
        buf.write("\u0211\u0212\5\u0088E\2\u0212\u0213\5n8\2\u0213\u0216")
        buf.write("\3\2\2\2\u0214\u0216\5n8\2\u0215\u0210\3\2\2\2\u0215\u0214")
        buf.write("\3\2\2\2\u0216m\3\2\2\2\u0217\u0218\b8\1\2\u0218\u0219")
        buf.write("\5p9\2\u0219\u0220\3\2\2\2\u021a\u021b\f\4\2\2\u021b\u021c")
        buf.write("\5\u0086D\2\u021c\u021d\5p9\2\u021d\u021f\3\2\2\2\u021e")
        buf.write("\u021a\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u0221\3\2\2\2\u0221o\3\2\2\2\u0222\u0220\3\2\2")
        buf.write("\2\u0223\u0224\b9\1\2\u0224\u0225\5r:\2\u0225\u022c\3")
        buf.write("\2\2\2\u0226\u0227\f\4\2\2\u0227\u0228\5\u0082B\2\u0228")
        buf.write("\u0229\5r:\2\u0229\u022b\3\2\2\2\u022a\u0226\3\2\2\2\u022b")
        buf.write("\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022dq\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0230\b:\1\2")
        buf.write("\u0230\u0231\5t;\2\u0231\u0238\3\2\2\2\u0232\u0233\f\4")
        buf.write("\2\2\u0233\u0234\5\u0084C\2\u0234\u0235\5t;\2\u0235\u0237")
        buf.write("\3\2\2\2\u0236\u0232\3\2\2\2\u0237\u023a\3\2\2\2\u0238")
        buf.write("\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239s\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023b\u023c\b;\1\2\u023c\u023d\5v<\2\u023d")
        buf.write("\u0243\3\2\2\2\u023e\u023f\f\4\2\2\u023f\u0240\7/\2\2")
        buf.write("\u0240\u0242\5v<\2\u0241\u023e\3\2\2\2\u0242\u0245\3\2")
        buf.write("\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244u\3")
        buf.write("\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\7\"\2\2\u0247\u024a")
        buf.write("\5v<\2\u0248\u024a\5x=\2\u0249\u0246\3\2\2\2\u0249\u0248")
        buf.write("\3\2\2\2\u024aw\3\2\2\2\u024b\u024c\5\u0082B\2\u024c\u024d")
        buf.write("\5x=\2\u024d\u0250\3\2\2\2\u024e\u0250\5z>\2\u024f\u024b")
        buf.write("\3\2\2\2\u024f\u024e\3\2\2\2\u0250y\3\2\2\2\u0251\u0252")
        buf.write("\b>\1\2\u0252\u0253\5|?\2\u0253\u0258\3\2\2\2\u0254\u0255")
        buf.write("\f\4\2\2\u0255\u0257\5\u008cG\2\u0256\u0254\3\2\2\2\u0257")
        buf.write("\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2")
        buf.write("\u0259{\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\b?\1\2")
        buf.write("\u025c\u025d\5~@\2\u025d\u0263\3\2\2\2\u025e\u025f\f\4")
        buf.write("\2\2\u025f\u0260\7\67\2\2\u0260\u0262\5~@\2\u0261\u025e")
        buf.write("\3\2\2\2\u0262\u0265\3\2\2\2\u0263\u0261\3\2\2\2\u0263")
        buf.write("\u0264\3\2\2\2\u0264}\3\2\2\2\u0265\u0263\3\2\2\2\u0266")
        buf.write("\u0267\7\33\2\2\u0267\u0268\5~@\2\u0268\u0269\5\u0090")
        buf.write("I\2\u0269\u026c\3\2\2\2\u026a\u026c\5\u0080A\2\u026b\u0266")
        buf.write("\3\2\2\2\u026b\u026a\3\2\2\2\u026c\177\3\2\2\2\u026d\u026e")
        buf.write("\7\63\2\2\u026e\u026f\5j\66\2\u026f\u0270\7\64\2\2\u0270")
        buf.write("\u0276\3\2\2\2\u0271\u0276\5\u0096L\2\u0272\u0276\7?\2")
        buf.write("\2\u0273\u0276\5\u008eH\2\u0274\u0276\7\35\2\2\u0275\u026d")
        buf.write("\3\2\2\2\u0275\u0271\3\2\2\2\u0275\u0272\3\2\2\2\u0275")
        buf.write("\u0273\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u0081\3\2\2\2")
        buf.write("\u0277\u0278\t\4\2\2\u0278\u0083\3\2\2\2\u0279\u027a\t")
        buf.write("\5\2\2\u027a\u0085\3\2\2\2\u027b\u027c\t\6\2\2\u027c\u0087")
        buf.write("\3\2\2\2\u027d\u027e\t\7\2\2\u027e\u0089\3\2\2\2\u027f")
        buf.write("\u0280\t\b\2\2\u0280\u008b\3\2\2\2\u0281\u0282\7\65\2")
        buf.write("\2\u0282\u0283\5j\66\2\u0283\u0284\7\66\2\2\u0284\u008d")
        buf.write("\3\2\2\2\u0285\u0286\7?\2\2\u0286\u0287\5\u0090I\2\u0287")
        buf.write("\u008f\3\2\2\2\u0288\u028a\7\63\2\2\u0289\u028b\5\u0092")
        buf.write("J\2\u028a\u0289\3\2\2\2\u028a\u028b\3\2\2\2\u028b\u028c")
        buf.write("\3\2\2\2\u028c\u028d\7\64\2\2\u028d\u0091\3\2\2\2\u028e")
        buf.write("\u0293\5j\66\2\u028f\u0290\78\2\2\u0290\u0292\5j\66\2")
        buf.write("\u0291\u028f\3\2\2\2\u0292\u0295\3\2\2\2\u0293\u0291\3")
        buf.write("\2\2\2\u0293\u0294\3\2\2\2\u0294\u0093\3\2\2\2\u0295\u0293")
        buf.write("\3\2\2\2\u0296\u0297\t\t\2\2\u0297\u0095\3\2\2\2\u0298")
        buf.write("\u029d\7<\2\2\u0299\u029d\7=\2\2\u029a\u029d\5\u0094K")
        buf.write("\2\u029b\u029d\7>\2\2\u029c\u0298\3\2\2\2\u029c\u0299")
        buf.write("\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029b\3\2\2\2\u029d")
        buf.write("\u0097\3\2\2\2\u029e\u029f\7\61\2\2\u029f\u02a4\5\u0096")
        buf.write("L\2\u02a0\u02a1\78\2\2\u02a1\u02a3\5\u0096L\2\u02a2\u02a0")
        buf.write("\3\2\2\2\u02a3\u02a6\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4")
        buf.write("\u02a5\3\2\2\2\u02a5\u02a7\3\2\2\2\u02a6\u02a4\3\2\2\2")
        buf.write("\u02a7\u02a8\7\62\2\2\u02a8\u0099\3\2\2\2@\u009d\u00a5")
        buf.write("\u00ab\u00b3\u00b7\u00be\u00c9\u00cf\u00da\u00e4\u00e8")
        buf.write("\u00f7\u0102\u0108\u010d\u0112\u0118\u011c\u0121\u0126")
        buf.write("\u0133\u0138\u0140\u0148\u014d\u0158\u0161\u0167\u016d")
        buf.write("\u0178\u017e\u0184\u018c\u0194\u01a1\u01b1\u01be\u01c6")
        buf.write("\u01cc\u01d3\u01d8\u01da\u01e1\u01e6\u01e8\u01f3\u020e")
        buf.write("\u0215\u0220\u022c\u0238\u0243\u0249\u024f\u0258\u0263")
        buf.write("\u026b\u0275\u028a\u0293\u029c\u02a4")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'main'", "'='", 
                     "':='", "'return'", "'true'", "'false'", "'else'", 
                     "'if'", "'then'", "'void'", "'int'", "'float'", "'string'", 
                     "'boolean'", "'for'", "'to'", "'downto'", "'do'", "'break'", 
                     "'continue'", "'class'", "'extends'", "'new'", "'nil'", 
                     "'this'", "'final'", "'static'", "'&&'", "'||'", "'!'", 
                     "'<'", "'>'", "'=='", "'!='", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'%'", "'\\'", "'/'", "'^'", "<INVALID>", 
                     "'{'", "'}'", "'('", "')'", "'['", "']'", "'.'", "','", 
                     "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "LINECOMMENT", "BLOCKCOMMENT", "MAIN", 
                      "EQUAL_SIGN", "ASSIGN", "RETURN", "TRUE", "FALSE", 
                      "ELSE", "IF", "THEN", "VOID", "INT", "FLOAT", "STRING", 
                      "BOOLEAN", "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", 
                      "CLASS", "EXTENDS", "NEW", "NIL", "THIS", "FINAL", 
                      "STATIC", "AND", "OR", "NOT", "LESS", "GREATER", "EQUAL", 
                      "NOT_EQUAL", "LESS_EQUAL", "GREATER_EQUAL", "PLUS", 
                      "MINUS", "MULTIPLY", "MODULUS", "I_DIVIDE", "F_DIVIDE", 
                      "CONCATENATE", "OBJECT_NEW", "LP", "RP", "LB", "RB", 
                      "LSB", "RSB", "DOT", "COMMA", "COLON", "S_COLON", 
                      "WS", "INTEGER_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
                      "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_classDecl = 1
    RULE_memDecl = 2
    RULE_attributeDecl = 3
    RULE_immutableAttrDecl = 4
    RULE_mutableAttrDecl = 5
    RULE_immutableAttrAssign = 6
    RULE_mutableAttrAssign = 7
    RULE_attributeType = 8
    RULE_scalarType = 9
    RULE_compositeType = 10
    RULE_objectDecl = 11
    RULE_objList = 12
    RULE_objInit = 13
    RULE_methodDecl = 14
    RULE_constructorDecl = 15
    RULE_normalMethodDecl = 16
    RULE_mainMethodDecl = 17
    RULE_paramList = 18
    RULE_params = 19
    RULE_monoParams = 20
    RULE_polyParams = 21
    RULE_paramType = 22
    RULE_classParamType = 23
    RULE_polyParam = 24
    RULE_monoParam = 25
    RULE_returnType = 26
    RULE_stmt = 27
    RULE_blockStmt = 28
    RULE_stmtWithoutReturn = 29
    RULE_voidBlockStmt = 30
    RULE_varDecl = 31
    RULE_objectVars = 32
    RULE_objectVar = 33
    RULE_scalarVars = 34
    RULE_scalarVar = 35
    RULE_arrayVars = 36
    RULE_assignStmt = 37
    RULE_lhs = 38
    RULE_attrAccess = 39
    RULE_instanceName = 40
    RULE_objName = 41
    RULE_attrName = 42
    RULE_ifStmt = 43
    RULE_ifWithoutReturn = 44
    RULE_forStmt = 45
    RULE_invokeStmt = 46
    RULE_arrayVar = 47
    RULE_breakStmt = 48
    RULE_continueStmt = 49
    RULE_returnStmt = 50
    RULE_className = 51
    RULE_exp = 52
    RULE_exp1 = 53
    RULE_exp2 = 54
    RULE_exp3 = 55
    RULE_exp4 = 56
    RULE_exp5 = 57
    RULE_exp6 = 58
    RULE_exp7 = 59
    RULE_exp8 = 60
    RULE_exp9 = 61
    RULE_exp10 = 62
    RULE_exp11 = 63
    RULE_adding = 64
    RULE_multiply = 65
    RULE_logical = 66
    RULE_equality = 67
    RULE_relational = 68
    RULE_indexOp = 69
    RULE_methodInvoke = 70
    RULE_listExp = 71
    RULE_arguList = 72
    RULE_bool_literal = 73
    RULE_literal = 74
    RULE_array_literal = 75

    ruleNames =  [ "program", "classDecl", "memDecl", "attributeDecl", "immutableAttrDecl", 
                   "mutableAttrDecl", "immutableAttrAssign", "mutableAttrAssign", 
                   "attributeType", "scalarType", "compositeType", "objectDecl", 
                   "objList", "objInit", "methodDecl", "constructorDecl", 
                   "normalMethodDecl", "mainMethodDecl", "paramList", "params", 
                   "monoParams", "polyParams", "paramType", "classParamType", 
                   "polyParam", "monoParam", "returnType", "stmt", "blockStmt", 
                   "stmtWithoutReturn", "voidBlockStmt", "varDecl", "objectVars", 
                   "objectVar", "scalarVars", "scalarVar", "arrayVars", 
                   "assignStmt", "lhs", "attrAccess", "instanceName", "objName", 
                   "attrName", "ifStmt", "ifWithoutReturn", "forStmt", "invokeStmt", 
                   "arrayVar", "breakStmt", "continueStmt", "returnStmt", 
                   "className", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "exp11", "adding", 
                   "multiply", "logical", "equality", "relational", "indexOp", 
                   "methodInvoke", "listExp", "arguList", "bool_literal", 
                   "literal", "array_literal" ]

    EOF = Token.EOF
    LINECOMMENT=1
    BLOCKCOMMENT=2
    MAIN=3
    EQUAL_SIGN=4
    ASSIGN=5
    RETURN=6
    TRUE=7
    FALSE=8
    ELSE=9
    IF=10
    THEN=11
    VOID=12
    INT=13
    FLOAT=14
    STRING=15
    BOOLEAN=16
    FOR=17
    TO=18
    DOWNTO=19
    DO=20
    BREAK=21
    CONTINUE=22
    CLASS=23
    EXTENDS=24
    NEW=25
    NIL=26
    THIS=27
    FINAL=28
    STATIC=29
    AND=30
    OR=31
    NOT=32
    LESS=33
    GREATER=34
    EQUAL=35
    NOT_EQUAL=36
    LESS_EQUAL=37
    GREATER_EQUAL=38
    PLUS=39
    MINUS=40
    MULTIPLY=41
    MODULUS=42
    I_DIVIDE=43
    F_DIVIDE=44
    CONCATENATE=45
    OBJECT_NEW=46
    LP=47
    RP=48
    LB=49
    RB=50
    LSB=51
    RSB=52
    DOT=53
    COMMA=54
    COLON=55
    S_COLON=56
    WS=57
    INTEGER_LITERAL=58
    FLOAT_LITERAL=59
    STRING_LITERAL=60
    ID=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassDeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 152
                self.classDecl()
                self.state = 155 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 157
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def memDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MemDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MemDeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = BKOOLParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BKOOLParser.CLASS)
            self.state = 160
            self.match(BKOOLParser.ID)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 161
                self.match(BKOOLParser.EXTENDS)
                self.state = 162
                self.match(BKOOLParser.ID)


            self.state = 165
            self.match(BKOOLParser.LP)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.VOID) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 166
                self.memDecl()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 172
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeDecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeDeclContext,0)


        def objectDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ObjectDeclContext,0)


        def methodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethodDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemDecl" ):
                return visitor.visitMemDecl(self)
            else:
                return visitor.visitChildren(self)




    def memDecl(self):

        localctx = BKOOLParser.MemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memDecl)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.objectDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.methodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def immutableAttrDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ImmutableAttrDeclContext,0)


        def mutableAttrDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MutableAttrDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeDecl" ):
                return visitor.visitAttributeDecl(self)
            else:
                return visitor.visitChildren(self)




    def attributeDecl(self):

        localctx = BKOOLParser.AttributeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attributeDecl)
        try:
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.immutableAttrDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.mutableAttrDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableAttrDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def immutableAttrAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ImmutableAttrAssignContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ImmutableAttrAssignContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_immutableAttrDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutableAttrDecl" ):
                return visitor.visitImmutableAttrDecl(self)
            else:
                return visitor.visitChildren(self)




    def immutableAttrDecl(self):

        localctx = BKOOLParser.ImmutableAttrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_immutableAttrDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 183
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 184
                self.match(BKOOLParser.FINAL)
                self.state = 185
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.state = 186
                self.match(BKOOLParser.STATIC)
                self.state = 187
                self.match(BKOOLParser.FINAL)
                pass


            self.state = 190
            self.attributeType()

            self.state = 191
            self.match(BKOOLParser.ID)
            self.state = 192
            self.immutableAttrAssign()
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 194
                self.match(BKOOLParser.COMMA)

                self.state = 195
                self.match(BKOOLParser.ID)
                self.state = 196
                self.immutableAttrAssign()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableAttrDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def mutableAttrAssign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MutableAttrAssignContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MutableAttrAssignContext,i)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mutableAttrDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableAttrDecl" ):
                return visitor.visitMutableAttrDecl(self)
            else:
                return visitor.visitChildren(self)




    def mutableAttrDecl(self):

        localctx = BKOOLParser.MutableAttrDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mutableAttrDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 204
                self.match(BKOOLParser.STATIC)


            self.state = 207
            self.attributeType()

            self.state = 208
            self.match(BKOOLParser.ID)
            self.state = 209
            self.mutableAttrAssign()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 211
                self.match(BKOOLParser.COMMA)

                self.state = 212
                self.match(BKOOLParser.ID)
                self.state = 213
                self.mutableAttrAssign()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 219
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImmutableAttrAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_immutableAttrAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImmutableAttrAssign" ):
                return visitor.visitImmutableAttrAssign(self)
            else:
                return visitor.visitChildren(self)




    def immutableAttrAssign(self):

        localctx = BKOOLParser.ImmutableAttrAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_immutableAttrAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 222
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MutableAttrAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mutableAttrAssign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutableAttrAssign" ):
                return visitor.visitMutableAttrAssign(self)
            else:
                return visitor.visitChildren(self)




    def mutableAttrAssign(self):

        localctx = BKOOLParser.MutableAttrAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_mutableAttrAssign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 224
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 225
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compositeType(self):
            return self.getTypedRuleContext(BKOOLParser.CompositeTypeContext,0)


        def scalarType(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attributeType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributeType" ):
                return visitor.visitAttributeType(self)
            else:
                return visitor.visitChildren(self)




    def attributeType(self):

        localctx = BKOOLParser.AttributeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attributeType)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.compositeType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.scalarType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarType" ):
                return visitor.visitScalarType(self)
            else:
                return visitor.visitChildren(self)




    def scalarType(self):

        localctx = BKOOLParser.ScalarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_scalarType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarType(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarTypeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_compositeType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeType" ):
                return visitor.visitCompositeType(self)
            else:
                return visitor.visitChildren(self)




    def compositeType(self):

        localctx = BKOOLParser.CompositeTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_compositeType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.scalarType()
            self.state = 235
            self.match(BKOOLParser.LSB)
            self.state = 236
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 237
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(BKOOLParser.ClassNameContext,0)


        def objList(self):
            return self.getTypedRuleContext(BKOOLParser.ObjListContext,0)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objectDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectDecl" ):
                return visitor.visitObjectDecl(self)
            else:
                return visitor.visitChildren(self)




    def objectDecl(self):

        localctx = BKOOLParser.ObjectDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_objectDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 239
                self.match(BKOOLParser.FINAL)

            elif la_ == 2:
                self.state = 240
                self.match(BKOOLParser.STATIC)

            elif la_ == 3:
                self.state = 241
                self.match(BKOOLParser.FINAL)
                self.state = 242
                self.match(BKOOLParser.STATIC)

            elif la_ == 4:
                self.state = 243
                self.match(BKOOLParser.STATIC)
                self.state = 244
                self.match(BKOOLParser.FINAL)


            self.state = 247
            self.className()
            self.state = 248
            self.objList()
            self.state = 249
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objInit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjInitContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjInitContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjList" ):
                return visitor.visitObjList(self)
            else:
                return visitor.visitChildren(self)




    def objList(self):

        localctx = BKOOLParser.ObjListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_objList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.objInit()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 252
                self.match(BKOOLParser.COMMA)
                self.state = 253
                self.objInit()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjNameContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjNameContext,i)


        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjInit" ):
                return visitor.visitObjInit(self)
            else:
                return visitor.visitChildren(self)




    def objInit(self):

        localctx = BKOOLParser.ObjInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_objInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.objName()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 260
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 261
                self.objName()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructorDecl(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorDeclContext,0)


        def normalMethodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.NormalMethodDeclContext,0)


        def mainMethodDecl(self):
            return self.getTypedRuleContext(BKOOLParser.MainMethodDeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = BKOOLParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_methodDecl)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.constructorDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.normalMethodDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.mainMethodDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def voidBlockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.VoidBlockStmtContext,0)


        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructorDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorDecl" ):
                return visitor.visitConstructorDecl(self)
            else:
                return visitor.visitChildren(self)




    def constructorDecl(self):

        localctx = BKOOLParser.ConstructorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructorDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(BKOOLParser.ID)
            self.state = 270
            self.match(BKOOLParser.LB)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 271
                self.paramList()


            self.state = 274
            self.match(BKOOLParser.RB)
            self.state = 275
            self.voidBlockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalMethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def voidBlockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.VoidBlockStmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def paramList(self):
            return self.getTypedRuleContext(BKOOLParser.ParamListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_normalMethodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalMethodDecl" ):
                return visitor.visitNormalMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def normalMethodDecl(self):

        localctx = BKOOLParser.NormalMethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_normalMethodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 277
                self.match(BKOOLParser.STATIC)


            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN]:
                self.state = 280
                self.attributeType()
                pass
            elif token in [BKOOLParser.VOID]:
                self.state = 281
                self.match(BKOOLParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 284
            self.match(BKOOLParser.ID)
            self.state = 285
            self.match(BKOOLParser.LB)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 286
                self.paramList()


            self.state = 289
            self.match(BKOOLParser.RB)
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 290
                self.blockStmt()
                pass

            elif la_ == 2:
                self.state = 291
                self.voidBlockStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainMethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def MAIN(self):
            return self.getToken(BKOOLParser.MAIN, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def voidBlockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.VoidBlockStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mainMethodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainMethodDecl" ):
                return visitor.visitMainMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def mainMethodDecl(self):

        localctx = BKOOLParser.MainMethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_mainMethodDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BKOOLParser.VOID)
            self.state = 295
            self.match(BKOOLParser.MAIN)
            self.state = 296
            self.match(BKOOLParser.LB)
            self.state = 297
            self.match(BKOOLParser.RB)
            self.state = 298
            self.voidBlockStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamsContext,i)


        def S_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.S_COLON)
            else:
                return self.getToken(BKOOLParser.S_COLON, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = BKOOLParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.params()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.S_COLON:
                self.state = 301
                self.match(BKOOLParser.S_COLON)
                self.state = 302
                self.params()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monoParams(self):
            return self.getTypedRuleContext(BKOOLParser.MonoParamsContext,0)


        def polyParams(self):
            return self.getTypedRuleContext(BKOOLParser.PolyParamsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 308
                self.monoParams()
                pass

            elif la_ == 2:
                self.state = 309
                self.polyParams()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonoParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramType(self):
            return self.getTypedRuleContext(BKOOLParser.ParamTypeContext,0)


        def monoParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.MonoParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.MonoParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_monoParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonoParams" ):
                return visitor.visitMonoParams(self)
            else:
                return visitor.visitChildren(self)




    def monoParams(self):

        localctx = BKOOLParser.MonoParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_monoParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.paramType()
            self.state = 313
            self.monoParam()
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 314
                self.match(BKOOLParser.COMMA)
                self.state = 315
                self.monoParam()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolyParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def polyParam(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.PolyParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.PolyParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_polyParams

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolyParams" ):
                return visitor.visitPolyParams(self)
            else:
                return visitor.visitChildren(self)




    def polyParams(self):

        localctx = BKOOLParser.PolyParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_polyParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.polyParam()
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 322
                self.match(BKOOLParser.COMMA)
                self.state = 323
                self.polyParam()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def classParamType(self):
            return self.getTypedRuleContext(BKOOLParser.ClassParamTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamType" ):
                return visitor.visitParamType(self)
            else:
                return visitor.visitChildren(self)




    def paramType(self):

        localctx = BKOOLParser.ParamTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_paramType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN]:
                self.state = 329
                self.attributeType()
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 330
                self.classParamType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassParamTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(BKOOLParser.ClassNameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_classParamType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassParamType" ):
                return visitor.visitClassParamType(self)
            else:
                return visitor.visitChildren(self)




    def classParamType(self):

        localctx = BKOOLParser.ClassParamTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_classParamType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.className()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolyParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramType(self):
            return self.getTypedRuleContext(BKOOLParser.ParamTypeContext,0)


        def monoParam(self):
            return self.getTypedRuleContext(BKOOLParser.MonoParamContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_polyParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolyParam" ):
                return visitor.visitPolyParam(self)
            else:
                return visitor.visitChildren(self)




    def polyParam(self):

        localctx = BKOOLParser.PolyParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_polyParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.paramType()
            self.state = 336
            self.monoParam()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonoParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_monoParam

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonoParam" ):
                return visitor.visitMonoParam(self)
            else:
                return visitor.visitChildren(self)




    def monoParam(self):

        localctx = BKOOLParser.MonoParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_monoParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnType" ):
                return visitor.visitReturnType(self)
            else:
                return visitor.visitChildren(self)




    def returnType(self):

        localctx = BKOOLParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_returnType)
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.attributeType()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.match(BKOOLParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def invokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvokeStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 344
                self.assignStmt()
                pass

            elif la_ == 2:
                self.state = 345
                self.ifStmt()
                pass

            elif la_ == 3:
                self.state = 346
                self.forStmt()
                pass

            elif la_ == 4:
                self.state = 347
                self.breakStmt()
                pass

            elif la_ == 5:
                self.state = 348
                self.continueStmt()
                pass

            elif la_ == 6:
                self.state = 349
                self.invokeStmt()
                pass

            elif la_ == 7:
                self.state = 350
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_blockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStmt" ):
                return visitor.visitBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def blockStmt(self):

        localctx = BKOOLParser.BlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BKOOLParser.LP)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 354
                    self.varDecl() 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.RETURN) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ID))) != 0):
                self.state = 360
                self.stmt()
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtWithoutReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStmt(self):
            return self.getTypedRuleContext(BKOOLParser.AssignStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinueStmtContext,0)


        def invokeStmt(self):
            return self.getTypedRuleContext(BKOOLParser.InvokeStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtWithoutReturn

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtWithoutReturn" ):
                return visitor.visitStmtWithoutReturn(self)
            else:
                return visitor.visitChildren(self)




    def stmtWithoutReturn(self):

        localctx = BKOOLParser.StmtWithoutReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmtWithoutReturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 368
                self.assignStmt()
                pass

            elif la_ == 2:
                self.state = 369
                self.ifStmt()
                pass

            elif la_ == 3:
                self.state = 370
                self.forStmt()
                pass

            elif la_ == 4:
                self.state = 371
                self.breakStmt()
                pass

            elif la_ == 5:
                self.state = 372
                self.continueStmt()
                pass

            elif la_ == 6:
                self.state = 373
                self.invokeStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidBlockStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarDeclContext,i)


        def stmtWithoutReturn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtWithoutReturnContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtWithoutReturnContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_voidBlockStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVoidBlockStmt" ):
                return visitor.visitVoidBlockStmt(self)
            else:
                return visitor.visitChildren(self)




    def voidBlockStmt(self):

        localctx = BKOOLParser.VoidBlockStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_voidBlockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(BKOOLParser.LP)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 377
                    self.varDecl() 
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.ID))) != 0):
                self.state = 383
                self.stmtWithoutReturn()
                self.state = 388
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 389
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarVars(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarVarsContext,0)


        def arrayVars(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayVarsContext,0)


        def objectVars(self):
            return self.getTypedRuleContext(BKOOLParser.ObjectVarsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = BKOOLParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 391
                self.scalarVars()
                pass

            elif la_ == 2:
                self.state = 392
                self.arrayVars()
                pass

            elif la_ == 3:
                self.state = 393
                self.objectVars()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectVarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(BKOOLParser.ClassNameContext,0)


        def objectVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ObjectVarContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ObjectVarContext,i)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objectVars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectVars" ):
                return visitor.visitObjectVars(self)
            else:
                return visitor.visitChildren(self)




    def objectVars(self):

        localctx = BKOOLParser.ObjectVarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_objectVars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.className()
            self.state = 397
            self.objectVar()
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 398
                self.match(BKOOLParser.COMMA)
                self.state = 399
                self.objectVar()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objectVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectVar" ):
                return visitor.visitObjectVar(self)
            else:
                return visitor.visitChildren(self)




    def objectVar(self):

        localctx = BKOOLParser.ObjectVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_objectVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarVarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def scalarVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ScalarVarContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,i)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarVars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarVars" ):
                return visitor.visitScalarVars(self)
            else:
                return visitor.visitChildren(self)




    def scalarVars(self):

        localctx = BKOOLParser.ScalarVarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_scalarVars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.attributeType()
            self.state = 410
            self.scalarVar()
            self.state = 415
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 411
                self.match(BKOOLParser.COMMA)
                self.state = 412
                self.scalarVar()
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 418
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarVar" ):
                return visitor.visitScalarVar(self)
            else:
                return visitor.visitChildren(self)




    def scalarVar(self):

        localctx = BKOOLParser.ScalarVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_scalarVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayVarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def scalarVar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ScalarVarContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,i)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayVars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayVars" ):
                return visitor.visitArrayVars(self)
            else:
                return visitor.visitChildren(self)




    def arrayVars(self):

        localctx = BKOOLParser.ArrayVarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrayVars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.attributeType()
            self.state = 423
            self.match(BKOOLParser.LSB)
            self.state = 424
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 425
            self.match(BKOOLParser.RSB)
            self.state = 426
            self.scalarVar()
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 427
                self.match(BKOOLParser.COMMA)
                self.state = 428
                self.scalarVar()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 434
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKOOLParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = BKOOLParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.lhs()
            self.state = 437
            self.match(BKOOLParser.ASSIGN)
            self.state = 438
            self.exp()
            self.state = 439
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayVar(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayVarContext,0)


        def scalarVar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,0)


        def attrAccess(self):
            return self.getTypedRuleContext(BKOOLParser.AttrAccessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 441
                self.arrayVar()
                pass

            elif la_ == 2:
                self.state = 442
                self.scalarVar()
                pass

            elif la_ == 3:
                self.state = 443
                self.attrAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceName(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceNameContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def attrName(self):
            return self.getTypedRuleContext(BKOOLParser.AttrNameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrAccess" ):
                return visitor.visitAttrAccess(self)
            else:
                return visitor.visitChildren(self)




    def attrAccess(self):

        localctx = BKOOLParser.AttrAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_attrAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.instanceName()
            self.state = 447
            self.match(BKOOLParser.DOT)
            self.state = 448
            self.attrName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstanceNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def objName(self):
            return self.getTypedRuleContext(BKOOLParser.ObjNameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_instanceName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstanceName" ):
                return visitor.visitInstanceName(self)
            else:
                return visitor.visitChildren(self)




    def instanceName(self):

        localctx = BKOOLParser.InstanceNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_instanceName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.state = 450
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 451
                self.objName()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_objName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjName" ):
                return visitor.visitObjName(self)
            else:
                return visitor.visitChildren(self)




    def objName(self):

        localctx = BKOOLParser.ObjNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_objName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarVar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,0)


        def arrayVar(self):
            return self.getTypedRuleContext(BKOOLParser.ArrayVarContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attrName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrName" ):
                return visitor.visitAttrName(self)
            else:
                return visitor.visitChildren(self)




    def attrName(self):

        localctx = BKOOLParser.AttrNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_attrName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 456
                self.scalarVar()
                pass

            elif la_ == 2:
                self.state = 457
                self.arrayVar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def blockStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.BlockStmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BKOOLParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(BKOOLParser.IF)
            self.state = 461
            self.exp()
            self.state = 462
            self.match(BKOOLParser.THEN)
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                self.state = 463
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 464
                self.blockStmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 467
                self.match(BKOOLParser.ELSE)
                self.state = 470
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                    self.state = 468
                    self.stmt()
                    pass
                elif token in [BKOOLParser.LP]:
                    self.state = 469
                    self.blockStmt()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfWithoutReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def blockStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.BlockStmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifWithoutReturn

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfWithoutReturn" ):
                return visitor.visitIfWithoutReturn(self)
            else:
                return visitor.visitChildren(self)




    def ifWithoutReturn(self):

        localctx = BKOOLParser.IfWithoutReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_ifWithoutReturn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(BKOOLParser.IF)
            self.state = 475
            self.exp()
            self.state = 476
            self.match(BKOOLParser.THEN)
            self.state = 479
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                self.state = 477
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 478
                self.blockStmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ELSE:
                self.state = 481
                self.match(BKOOLParser.ELSE)
                self.state = 484
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                    self.state = 482
                    self.stmt()
                    pass
                elif token in [BKOOLParser.LP]:
                    self.state = 483
                    self.blockStmt()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def scalarVar(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarVarContext,0)


        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BKOOLParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(BKOOLParser.FOR)
            self.state = 489
            self.scalarVar()
            self.state = 490
            self.match(BKOOLParser.ASSIGN)
            self.state = 491
            self.exp()
            self.state = 492
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 493
            self.exp()
            self.state = 494
            self.match(BKOOLParser.DO)
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                self.state = 495
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 496
                self.blockStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InvokeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instanceName(self):
            return self.getTypedRuleContext(BKOOLParser.InstanceNameContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def methodInvoke(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeContext,0)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_invokeStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvokeStmt" ):
                return visitor.visitInvokeStmt(self)
            else:
                return visitor.visitChildren(self)




    def invokeStmt(self):

        localctx = BKOOLParser.InvokeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_invokeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.instanceName()
            self.state = 500
            self.match(BKOOLParser.DOT)
            self.state = 501
            self.methodInvoke()
            self.state = 502
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def indexOp(self):
            return self.getTypedRuleContext(BKOOLParser.IndexOpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_arrayVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayVar" ):
                return visitor.visitArrayVar(self)
            else:
                return visitor.visitChildren(self)




    def arrayVar(self):

        localctx = BKOOLParser.ArrayVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_arrayVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(BKOOLParser.ID)
            self.state = 505
            self.indexOp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = BKOOLParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(BKOOLParser.BREAK)
            self.state = 508
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continueStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BKOOLParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.match(BKOOLParser.CONTINUE)
            self.state = 511
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def S_COLON(self):
            return self.getToken(BKOOLParser.S_COLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = BKOOLParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(BKOOLParser.RETURN)
            self.state = 514
            self.exp()
            self.state = 515
            self.match(BKOOLParser.S_COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_className

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassName" ):
                return visitor.visitClassName(self)
            else:
                return visitor.visitChildren(self)




    def className(self):

        localctx = BKOOLParser.ClassNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def relational(self):
            return self.getTypedRuleContext(BKOOLParser.RelationalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_exp)
        try:
            self.state = 524
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 519
                self.exp1()
                self.state = 520
                self.relational()
                self.state = 521
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 523
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def equality(self):
            return self.getTypedRuleContext(BKOOLParser.EqualityContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_exp1)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.exp2(0)
                self.state = 527
                self.equality()
                self.state = 528
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def logical(self):
            return self.getTypedRuleContext(BKOOLParser.LogicalContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 536
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 537
                    self.logical()
                    self.state = 538
                    self.exp3(0) 
                self.state = 544
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def adding(self):
            return self.getTypedRuleContext(BKOOLParser.AddingContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 554
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 548
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 549
                    self.adding()
                    self.state = 550
                    self.exp4(0) 
                self.state = 556
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def multiply(self):
            return self.getTypedRuleContext(BKOOLParser.MultiplyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 566
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 560
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 561
                    self.multiply()
                    self.state = 562
                    self.exp5(0) 
                self.state = 568
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCATENATE(self):
            return self.getToken(BKOOLParser.CONCATENATE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 577
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 572
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 573
                    self.match(BKOOLParser.CONCATENATE)
                    self.state = 574
                    self.exp6() 
                self.state = 579
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_exp6)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.match(BKOOLParser.NOT)
                self.state = 581
                self.exp6()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.PLUS, BKOOLParser.MINUS, BKOOLParser.LB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding(self):
            return self.getTypedRuleContext(BKOOLParser.AddingContext,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_exp7)
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.PLUS, BKOOLParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 585
                self.adding()
                self.state = 586
                self.exp7()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 588
                self.exp8(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def indexOp(self):
            return self.getTypedRuleContext(BKOOLParser.IndexOpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 598
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,54,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 594
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 595
                    self.indexOp() 
                self.state = 600
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,54,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 609
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 604
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 605
                    self.match(BKOOLParser.DOT)
                    self.state = 606
                    self.exp10() 
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def listExp(self):
            return self.getTypedRuleContext(BKOOLParser.ListExpContext,0)


        def exp11(self):
            return self.getTypedRuleContext(BKOOLParser.Exp11Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_exp10)
        try:
            self.state = 617
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.match(BKOOLParser.NEW)
                self.state = 613
                self.exp10()
                self.state = 614
                self.listExp()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 616
                self.exp11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def literal(self):
            return self.getTypedRuleContext(BKOOLParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def methodInvoke(self):
            return self.getTypedRuleContext(BKOOLParser.MethodInvokeContext,0)


        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp11" ):
                return visitor.visitExp11(self)
            else:
                return visitor.visitChildren(self)




    def exp11(self):

        localctx = BKOOLParser.Exp11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_exp11)
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.match(BKOOLParser.LB)
                self.state = 620
                self.exp()
                self.state = 621
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 623
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 624
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 625
                self.methodInvoke()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 626
                self.match(BKOOLParser.THIS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(BKOOLParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(BKOOLParser.MINUS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_adding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding" ):
                return visitor.visitAdding(self)
            else:
                return visitor.visitChildren(self)




    def adding(self):

        localctx = BKOOLParser.AddingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.PLUS or _la==BKOOLParser.MINUS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLY(self):
            return self.getToken(BKOOLParser.MULTIPLY, 0)

        def MODULUS(self):
            return self.getToken(BKOOLParser.MODULUS, 0)

        def F_DIVIDE(self):
            return self.getToken(BKOOLParser.F_DIVIDE, 0)

        def I_DIVIDE(self):
            return self.getToken(BKOOLParser.I_DIVIDE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_multiply

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)




    def multiply(self):

        localctx = BKOOLParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_multiply)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MULTIPLY) | (1 << BKOOLParser.MODULUS) | (1 << BKOOLParser.I_DIVIDE) | (1 << BKOOLParser.F_DIVIDE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_logical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical" ):
                return visitor.visitLogical(self)
            else:
                return visitor.visitChildren(self)




    def logical(self):

        localctx = BKOOLParser.LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.AND or _la==BKOOLParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(BKOOLParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKOOLParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_equality

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = BKOOLParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 635
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.EQUAL or _la==BKOOLParser.NOT_EQUAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(BKOOLParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(BKOOLParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relational

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = BKOOLParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESS_EQUAL) | (1 << BKOOLParser.GREATER_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_indexOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexOp" ):
                return visitor.visitIndexOp(self)
            else:
                return visitor.visitChildren(self)




    def indexOp(self):

        localctx = BKOOLParser.IndexOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_indexOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.match(BKOOLParser.LSB)
            self.state = 640
            self.exp()
            self.state = 641
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvokeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def listExp(self):
            return self.getTypedRuleContext(BKOOLParser.ListExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_methodInvoke

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvoke" ):
                return visitor.visitMethodInvoke(self)
            else:
                return visitor.visitChildren(self)




    def methodInvoke(self):

        localctx = BKOOLParser.MethodInvokeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_methodInvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(BKOOLParser.ID)
            self.state = 644
            self.listExp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def arguList(self):
            return self.getTypedRuleContext(BKOOLParser.ArguListContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_listExp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListExp" ):
                return visitor.visitListExp(self)
            else:
                return visitor.visitChildren(self)




    def listExp(self):

        localctx = BKOOLParser.ListExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_listExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            self.match(BKOOLParser.LB)
            self.state = 648
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.PLUS) | (1 << BKOOLParser.MINUS) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 647
                self.arguList()


            self.state = 650
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arguList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguList" ):
                return visitor.visitArguList(self)
            else:
                return visitor.visitChildren(self)




    def arguList(self):

        localctx = BKOOLParser.ArguListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_arguList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.exp()
            self.state = 657
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 653
                self.match(BKOOLParser.COMMA)
                self.state = 654
                self.exp()
                self.state = 659
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_literal" ):
                return visitor.visitBool_literal(self)
            else:
                return visitor.visitChildren(self)




    def bool_literal(self):

        localctx = BKOOLParser.Bool_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TRUE or _la==BKOOLParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(BKOOLParser.FLOAT_LITERAL, 0)

        def bool_literal(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_literalContext,0)


        def STRING_LITERAL(self):
            return self.getToken(BKOOLParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LITERAL]:
                self.state = 662
                self.match(BKOOLParser.INTEGER_LITERAL)
                pass
            elif token in [BKOOLParser.FLOAT_LITERAL]:
                self.state = 663
                self.match(BKOOLParser.FLOAT_LITERAL)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 664
                self.bool_literal()
                pass
            elif token in [BKOOLParser.STRING_LITERAL]:
                self.state = 665
                self.match(BKOOLParser.STRING_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralContext,i)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = BKOOLParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(BKOOLParser.LP)
            self.state = 669
            self.literal()
            self.state = 674
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 670
                self.match(BKOOLParser.COMMA)
                self.state = 671
                self.literal()
                self.state = 676
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 677
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[54] = self.exp2_sempred
        self._predicates[55] = self.exp3_sempred
        self._predicates[56] = self.exp4_sempred
        self._predicates[57] = self.exp5_sempred
        self._predicates[60] = self.exp8_sempred
        self._predicates[61] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




