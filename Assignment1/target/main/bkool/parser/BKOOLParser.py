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
        buf.write("\u024e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\3\2")
        buf.write("\6\2\u0088\n\2\r\2\16\2\u0089\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u0092\n\3\3\3\3\3\7\3\u0096\n\3\f\3\16\3\u0099\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\5\4\u00a0\n\4\3\5\3\5\5\5\u00a4")
        buf.write("\n\5\3\5\3\5\5\5\u00a8\n\5\5\5\u00aa\n\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\5\6\u00b1\n\6\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u00b9")
        buf.write("\n\b\f\b\16\b\u00bc\13\b\3\t\3\t\3\t\5\t\u00c1\n\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\7\13\u00cc\n\13\f")
        buf.write("\13\16\13\u00cf\13\13\3\f\3\f\3\f\5\f\u00d4\n\f\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\7\16\u00dd\n\16\f\16\16\16\u00e0")
        buf.write("\13\16\3\17\3\17\3\17\5\17\u00e5\n\17\3\20\3\20\5\20\u00e9")
        buf.write("\n\20\3\21\3\21\3\21\5\21\u00ee\n\21\3\21\3\21\3\21\3")
        buf.write("\22\5\22\u00f4\n\22\3\22\3\22\3\22\3\22\5\22\u00fa\n\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u0102\n\23\f\23\16")
        buf.write("\23\u0105\13\23\3\24\3\24\5\24\u0109\n\24\3\25\3\25\3")
        buf.write("\25\3\25\7\25\u010f\n\25\f\25\16\25\u0112\13\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\7\26\u011a\n\26\f\26\16\26\u011d")
        buf.write("\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0126\n")
        buf.write("\27\3\30\3\30\3\31\3\31\5\31\u012c\n\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\5\32\u0135\n\32\3\33\3\33\7\33\u0139")
        buf.write("\n\33\f\33\16\33\u013c\13\33\3\33\7\33\u013f\n\33\f\33")
        buf.write("\16\33\u0142\13\33\3\33\3\33\3\34\3\34\3\34\5\34\u0149")
        buf.write("\n\34\3\35\3\35\3\35\3\35\7\35\u014f\n\35\f\35\16\35\u0152")
        buf.write("\13\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7")
        buf.write("\36\u015d\n\36\f\36\16\36\u0160\13\36\3\36\3\36\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u0168\n\37\f\37\16\37\u016b\13\37\3")
        buf.write("\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\5!\u0177\n!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\5#\u0181\n#\3#\3#\3#\5#\u0186\n#\5#")
        buf.write("\u0188\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u0193\n$\3%\3")
        buf.write("%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3*\3*")
        buf.write("\5*\u01a7\n*\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\5,\u01b3\n")
        buf.write(",\3-\3-\3-\3-\3-\5-\u01ba\n-\3.\3.\3.\3.\3.\3.\3.\7.\u01c3")
        buf.write("\n.\f.\16.\u01c6\13.\3/\3/\3/\3/\3/\3/\3/\7/\u01cf\n/")
        buf.write("\f/\16/\u01d2\13/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\7")
        buf.write("\60\u01db\n\60\f\60\16\60\u01de\13\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\7\61\u01e6\n\61\f\61\16\61\u01e9\13\61\3")
        buf.write("\62\3\62\3\62\5\62\u01ee\n\62\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01f4\n\63\3\64\3\64\3\64\3\64\3\64\7\64\u01fb\n\64\f")
        buf.write("\64\16\64\u01fe\13\64\3\65\3\65\3\65\3\65\3\65\3\65\7")
        buf.write("\65\u0206\n\65\f\65\16\65\u0209\13\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\5\66\u0210\n\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\5\67\u021a\n\67\38\38\39\39\3:\3:\3;\3;\3<")
        buf.write("\3<\3=\3=\3=\3=\3>\3>\3>\3?\3?\5?\u022f\n?\3?\3?\3@\3")
        buf.write("@\3@\7@\u0236\n@\f@\16@\u0239\13@\3A\3A\3B\3B\3B\3B\5")
        buf.write("B\u0241\nB\3C\3C\3C\3C\7C\u0247\nC\fC\16C\u024a\13C\3")
        buf.write("C\3C\3C\2\bZ\\^`fhD\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln")
        buf.write("prtvxz|~\u0080\u0082\u0084\2\f\4\2\7\7??\3\2\25\30\3\2")
        buf.write("\33\34\4\2\17\17??\4\2#$\'(\3\2%&\3\2 !\3\2)*\3\2+.\3")
        buf.write("\2\t\n\2\u024f\2\u0087\3\2\2\2\4\u008d\3\2\2\2\6\u009f")
        buf.write("\3\2\2\2\b\u00a9\3\2\2\2\n\u00b0\3\2\2\2\f\u00b2\3\2\2")
        buf.write("\2\16\u00b5\3\2\2\2\20\u00bd\3\2\2\2\22\u00c2\3\2\2\2")
        buf.write("\24\u00c8\3\2\2\2\26\u00d0\3\2\2\2\30\u00d5\3\2\2\2\32")
        buf.write("\u00d9\3\2\2\2\34\u00e1\3\2\2\2\36\u00e8\3\2\2\2 \u00ea")
        buf.write("\3\2\2\2\"\u00f3\3\2\2\2$\u00fe\3\2\2\2&\u0108\3\2\2\2")
        buf.write("(\u010a\3\2\2\2*\u0113\3\2\2\2,\u0125\3\2\2\2.\u0127\3")
        buf.write("\2\2\2\60\u012b\3\2\2\2\62\u0134\3\2\2\2\64\u0136\3\2")
        buf.write("\2\2\66\u0148\3\2\2\28\u014a\3\2\2\2:\u0155\3\2\2\2<\u0163")
        buf.write("\3\2\2\2>\u016e\3\2\2\2@\u0176\3\2\2\2B\u0178\3\2\2\2")
        buf.write("D\u017b\3\2\2\2F\u0189\3\2\2\2H\u0194\3\2\2\2J\u0197\3")
        buf.write("\2\2\2L\u019a\3\2\2\2N\u019e\3\2\2\2P\u01a2\3\2\2\2R\u01a6")
        buf.write("\3\2\2\2T\u01a8\3\2\2\2V\u01b2\3\2\2\2X\u01b9\3\2\2\2")
        buf.write("Z\u01bb\3\2\2\2\\\u01c7\3\2\2\2^\u01d3\3\2\2\2`\u01df")
        buf.write("\3\2\2\2b\u01ed\3\2\2\2d\u01f3\3\2\2\2f\u01f5\3\2\2\2")
        buf.write("h\u01ff\3\2\2\2j\u020f\3\2\2\2l\u0219\3\2\2\2n\u021b\3")
        buf.write("\2\2\2p\u021d\3\2\2\2r\u021f\3\2\2\2t\u0221\3\2\2\2v\u0223")
        buf.write("\3\2\2\2x\u0225\3\2\2\2z\u0229\3\2\2\2|\u022c\3\2\2\2")
        buf.write("~\u0232\3\2\2\2\u0080\u023a\3\2\2\2\u0082\u0240\3\2\2")
        buf.write("\2\u0084\u0242\3\2\2\2\u0086\u0088\5\4\3\2\u0087\u0086")
        buf.write("\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087\3\2\2\2\u0089")
        buf.write("\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\7\2\2\3")
        buf.write("\u008c\3\3\2\2\2\u008d\u008e\7\13\2\2\u008e\u0091\7?\2")
        buf.write("\2\u008f\u0090\7\f\2\2\u0090\u0092\7?\2\2\u0091\u008f")
        buf.write("\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2\u0093")
        buf.write("\u0097\7\65\2\2\u0094\u0096\5\6\4\2\u0095\u0094\3\2\2")
        buf.write("\2\u0096\u0099\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a")
        buf.write("\u009b\7\66\2\2\u009b\5\3\2\2\2\u009c\u00a0\5\b\5\2\u009d")
        buf.write("\u00a0\5\30\r\2\u009e\u00a0\5\36\20\2\u009f\u009c\3\2")
        buf.write("\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\7\3")
        buf.write("\2\2\2\u00a1\u00a3\7\20\2\2\u00a2\u00a4\7\21\2\2\u00a3")
        buf.write("\u00a2\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00aa\3\2\2\2")
        buf.write("\u00a5\u00a7\7\21\2\2\u00a6\u00a8\7\20\2\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00aa\3\2\2\2\u00a9")
        buf.write("\u00a1\3\2\2\2\u00a9\u00a5\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ac\5\n\6\2\u00ac\u00ad\7")
        buf.write(":\2\2\u00ad\t\3\2\2\2\u00ae\u00b1\5\f\7\2\u00af\u00b1")
        buf.write("\5\22\n\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\13\3\2\2\2\u00b2\u00b3\5.\30\2\u00b3\u00b4\5\16\b\2\u00b4")
        buf.write("\r\3\2\2\2\u00b5\u00ba\5\20\t\2\u00b6\u00b7\78\2\2\u00b7")
        buf.write("\u00b9\5\20\t\2\u00b8\u00b6\3\2\2\2\u00b9\u00bc\3\2\2")
        buf.write("\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\17\3")
        buf.write("\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00c0\7?\2\2\u00be\u00bf")
        buf.write("\7\5\2\2\u00bf\u00c1\5V,\2\u00c0\u00be\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\21\3\2\2\2\u00c2\u00c3\5.\30\2\u00c3\u00c4")
        buf.write("\7\63\2\2\u00c4\u00c5\7<\2\2\u00c5\u00c6\7\64\2\2\u00c6")
        buf.write("\u00c7\5\24\13\2\u00c7\23\3\2\2\2\u00c8\u00cd\5\26\f\2")
        buf.write("\u00c9\u00ca\78\2\2\u00ca\u00cc\5\26\f\2\u00cb\u00c9\3")
        buf.write("\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce")
        buf.write("\3\2\2\2\u00ce\25\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d3")
        buf.write("\7?\2\2\u00d1\u00d2\7\5\2\2\u00d2\u00d4\5\u0084C\2\u00d3")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\27\3\2\2\2\u00d5")
        buf.write("\u00d6\7?\2\2\u00d6\u00d7\5\32\16\2\u00d7\u00d8\7:\2\2")
        buf.write("\u00d8\31\3\2\2\2\u00d9\u00de\5\34\17\2\u00da\u00db\7")
        buf.write("8\2\2\u00db\u00dd\5\34\17\2\u00dc\u00da\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\33\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\7?\2")
        buf.write("\2\u00e2\u00e3\7\5\2\2\u00e3\u00e5\7:\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\35\3\2\2\2\u00e6\u00e9")
        buf.write("\5 \21\2\u00e7\u00e9\5\"\22\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e7\3\2\2\2\u00e9\37\3\2\2\2\u00ea\u00eb\7?\2\2\u00eb")
        buf.write("\u00ed\7\61\2\2\u00ec\u00ee\5$\23\2\u00ed\u00ec\3\2\2")
        buf.write("\2\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0")
        buf.write("\7\62\2\2\u00f0\u00f1\5\64\33\2\u00f1!\3\2\2\2\u00f2\u00f4")
        buf.write("\7\21\2\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\5\60\31\2\u00f6\u00f7\t\2\2")
        buf.write("\2\u00f7\u00f9\7\61\2\2\u00f8\u00fa\5$\23\2\u00f9\u00f8")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\7\62\2\2\u00fc\u00fd\5\64\33\2\u00fd#\3\2\2\2\u00fe")
        buf.write("\u0103\5&\24\2\u00ff\u0100\7:\2\2\u0100\u0102\5&\24\2")
        buf.write("\u0101\u00ff\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104%\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0106\u0109\5(\25\2\u0107\u0109\5*\26\2\u0108")
        buf.write("\u0106\3\2\2\2\u0108\u0107\3\2\2\2\u0109\'\3\2\2\2\u010a")
        buf.write("\u010b\5,\27\2\u010b\u0110\7?\2\2\u010c\u010d\78\2\2\u010d")
        buf.write("\u010f\7?\2\2\u010e\u010c\3\2\2\2\u010f\u0112\3\2\2\2")
        buf.write("\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111)\3\2\2")
        buf.write("\2\u0112\u0110\3\2\2\2\u0113\u0114\5,\27\2\u0114\u011b")
        buf.write("\7?\2\2\u0115\u0116\78\2\2\u0116\u0117\5,\27\2\u0117\u0118")
        buf.write("\7?\2\2\u0118\u011a\3\2\2\2\u0119\u0115\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c+\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0126\5.\30")
        buf.write("\2\u011f\u0120\5.\30\2\u0120\u0121\7\63\2\2\u0121\u0122")
        buf.write("\7<\2\2\u0122\u0123\7\64\2\2\u0123\u0126\3\2\2\2\u0124")
        buf.write("\u0126\7?\2\2\u0125\u011e\3\2\2\2\u0125\u011f\3\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126-\3\2\2\2\u0127\u0128\t\3\2")
        buf.write("\2\u0128/\3\2\2\2\u0129\u012c\5.\30\2\u012a\u012c\7\31")
        buf.write("\2\2\u012b\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c\61")
        buf.write("\3\2\2\2\u012d\u0135\5> \2\u012e\u0135\5D#\2\u012f\u0135")
        buf.write("\5F$\2\u0130\u0135\5H%\2\u0131\u0135\5J&\2\u0132\u0135")
        buf.write("\5T+\2\u0133\u0135\5L\'\2\u0134\u012d\3\2\2\2\u0134\u012e")
        buf.write("\3\2\2\2\u0134\u012f\3\2\2\2\u0134\u0130\3\2\2\2\u0134")
        buf.write("\u0131\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0133\3\2\2\2")
        buf.write("\u0135\63\3\2\2\2\u0136\u013a\7\65\2\2\u0137\u0139\5\66")
        buf.write("\34\2\u0138\u0137\3\2\2\2\u0139\u013c\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0140\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013d\u013f\5\62\32\2\u013e\u013d\3\2\2")
        buf.write("\2\u013f\u0142\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143")
        buf.write("\u0144\7\66\2\2\u0144\65\3\2\2\2\u0145\u0149\58\35\2\u0146")
        buf.write("\u0149\5:\36\2\u0147\u0149\5<\37\2\u0148\u0145\3\2\2\2")
        buf.write("\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149\67\3\2")
        buf.write("\2\2\u014a\u014b\5.\30\2\u014b\u0150\7?\2\2\u014c\u014d")
        buf.write("\78\2\2\u014d\u014f\7?\2\2\u014e\u014c\3\2\2\2\u014f\u0152")
        buf.write("\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write("\u0153\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7:\2\2")
        buf.write("\u01549\3\2\2\2\u0155\u0156\5.\30\2\u0156\u0157\7\63\2")
        buf.write("\2\u0157\u0158\7<\2\2\u0158\u0159\7\64\2\2\u0159\u015e")
        buf.write("\7?\2\2\u015a\u015b\78\2\2\u015b\u015d\7?\2\2\u015c\u015a")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u015e\3\2\2\2")
        buf.write("\u0161\u0162\7:\2\2\u0162;\3\2\2\2\u0163\u0164\7?\2\2")
        buf.write("\u0164\u0169\7?\2\2\u0165\u0166\78\2\2\u0166\u0168\7?")
        buf.write("\2\2\u0167\u0165\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016d\7:\2\2\u016d=\3\2\2\2\u016e")
        buf.write("\u016f\5@!\2\u016f\u0170\7\6\2\2\u0170\u0171\5V,\2\u0171")
        buf.write("\u0172\7:\2\2\u0172?\3\2\2\2\u0173\u0177\5B\"\2\u0174")
        buf.write("\u0177\7?\2\2\u0175\u0177\5N(\2\u0176\u0173\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177A\3\2\2\2\u0178")
        buf.write("\u0179\7?\2\2\u0179\u017a\5x=\2\u017aC\3\2\2\2\u017b\u017c")
        buf.write("\7\22\2\2\u017c\u017d\5V,\2\u017d\u0180\7\24\2\2\u017e")
        buf.write("\u0181\5\62\32\2\u017f\u0181\5\64\33\2\u0180\u017e\3\2")
        buf.write("\2\2\u0180\u017f\3\2\2\2\u0181\u0187\3\2\2\2\u0182\u0185")
        buf.write("\7\23\2\2\u0183\u0186\5\62\32\2\u0184\u0186\5\64\33\2")
        buf.write("\u0185\u0183\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0188\3")
        buf.write("\2\2\2\u0187\u0182\3\2\2\2\u0187\u0188\3\2\2\2\u0188E")
        buf.write("\3\2\2\2\u0189\u018a\7\32\2\2\u018a\u018b\7?\2\2\u018b")
        buf.write("\u018c\7\6\2\2\u018c\u018d\5V,\2\u018d\u018e\t\4\2\2\u018e")
        buf.write("\u018f\5V,\2\u018f\u0192\7\35\2\2\u0190\u0193\5\62\32")
        buf.write("\2\u0191\u0193\5\64\33\2\u0192\u0190\3\2\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0193G\3\2\2\2\u0194\u0195\7\36\2\2\u0195\u0196")
        buf.write("\7:\2\2\u0196I\3\2\2\2\u0197\u0198\7\37\2\2\u0198\u0199")
        buf.write("\7:\2\2\u0199K\3\2\2\2\u019a\u019b\7\b\2\2\u019b\u019c")
        buf.write("\5V,\2\u019c\u019d\7:\2\2\u019dM\3\2\2\2\u019e\u019f\5")
        buf.write("P)\2\u019f\u01a0\7\67\2\2\u01a0\u01a1\5R*\2\u01a1O\3\2")
        buf.write("\2\2\u01a2\u01a3\t\5\2\2\u01a3Q\3\2\2\2\u01a4\u01a7\7")
        buf.write("?\2\2\u01a5\u01a7\5B\"\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7S\3\2\2\2\u01a8\u01a9\5P)\2\u01a9\u01aa")
        buf.write("\7\67\2\2\u01aa\u01ab\5z>\2\u01ab\u01ac\7:\2\2\u01acU")
        buf.write("\3\2\2\2\u01ad\u01ae\5X-\2\u01ae\u01af\5n8\2\u01af\u01b0")
        buf.write("\5X-\2\u01b0\u01b3\3\2\2\2\u01b1\u01b3\5X-\2\u01b2\u01ad")
        buf.write("\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b3W\3\2\2\2\u01b4\u01b5")
        buf.write("\5Z.\2\u01b5\u01b6\5p9\2\u01b6\u01b7\5Z.\2\u01b7\u01ba")
        buf.write("\3\2\2\2\u01b8\u01ba\5Z.\2\u01b9\u01b4\3\2\2\2\u01b9\u01b8")
        buf.write("\3\2\2\2\u01baY\3\2\2\2\u01bb\u01bc\b.\1\2\u01bc\u01bd")
        buf.write("\5\\/\2\u01bd\u01c4\3\2\2\2\u01be\u01bf\f\4\2\2\u01bf")
        buf.write("\u01c0\5r:\2\u01c0\u01c1\5\\/\2\u01c1\u01c3\3\2\2\2\u01c2")
        buf.write("\u01be\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2")
        buf.write("\u01c4\u01c5\3\2\2\2\u01c5[\3\2\2\2\u01c6\u01c4\3\2\2")
        buf.write("\2\u01c7\u01c8\b/\1\2\u01c8\u01c9\5^\60\2\u01c9\u01d0")
        buf.write("\3\2\2\2\u01ca\u01cb\f\4\2\2\u01cb\u01cc\5t;\2\u01cc\u01cd")
        buf.write("\5^\60\2\u01cd\u01cf\3\2\2\2\u01ce\u01ca\3\2\2\2\u01cf")
        buf.write("\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2")
        buf.write("\u01d1]\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\b\60\1")
        buf.write("\2\u01d4\u01d5\5`\61\2\u01d5\u01dc\3\2\2\2\u01d6\u01d7")
        buf.write("\f\4\2\2\u01d7\u01d8\5v<\2\u01d8\u01d9\5`\61\2\u01d9\u01db")
        buf.write("\3\2\2\2\u01da\u01d6\3\2\2\2\u01db\u01de\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd_\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e0\b\61\1\2\u01e0\u01e1\5b\62")
        buf.write("\2\u01e1\u01e7\3\2\2\2\u01e2\u01e3\f\4\2\2\u01e3\u01e4")
        buf.write("\7/\2\2\u01e4\u01e6\5b\62\2\u01e5\u01e2\3\2\2\2\u01e6")
        buf.write("\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8a\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb\7\"\2")
        buf.write("\2\u01eb\u01ee\5b\62\2\u01ec\u01ee\5d\63\2\u01ed\u01ea")
        buf.write("\3\2\2\2\u01ed\u01ec\3\2\2\2\u01eec\3\2\2\2\u01ef\u01f0")
        buf.write("\5t;\2\u01f0\u01f1\5d\63\2\u01f1\u01f4\3\2\2\2\u01f2\u01f4")
        buf.write("\5f\64\2\u01f3\u01ef\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4")
        buf.write("e\3\2\2\2\u01f5\u01f6\b\64\1\2\u01f6\u01f7\5h\65\2\u01f7")
        buf.write("\u01fc\3\2\2\2\u01f8\u01f9\f\4\2\2\u01f9\u01fb\5x=\2\u01fa")
        buf.write("\u01f8\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fdg\3\2\2\2\u01fe\u01fc\3\2\2")
        buf.write("\2\u01ff\u0200\b\65\1\2\u0200\u0201\5j\66\2\u0201\u0207")
        buf.write("\3\2\2\2\u0202\u0203\f\4\2\2\u0203\u0204\7\67\2\2\u0204")
        buf.write("\u0206\5j\66\2\u0205\u0202\3\2\2\2\u0206\u0209\3\2\2\2")
        buf.write("\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208i\3\2\2")
        buf.write("\2\u0209\u0207\3\2\2\2\u020a\u020b\7\r\2\2\u020b\u020c")
        buf.write("\5j\66\2\u020c\u020d\5|?\2\u020d\u0210\3\2\2\2\u020e\u0210")
        buf.write("\5l\67\2\u020f\u020a\3\2\2\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("k\3\2\2\2\u0211\u0212\7\61\2\2\u0212\u0213\5V,\2\u0213")
        buf.write("\u0214\7\62\2\2\u0214\u021a\3\2\2\2\u0215\u021a\5\u0082")
        buf.write("B\2\u0216\u021a\7?\2\2\u0217\u021a\5z>\2\u0218\u021a\7")
        buf.write("\17\2\2\u0219\u0211\3\2\2\2\u0219\u0215\3\2\2\2\u0219")
        buf.write("\u0216\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u0218\3\2\2\2")
        buf.write("\u021am\3\2\2\2\u021b\u021c\t\6\2\2\u021co\3\2\2\2\u021d")
        buf.write("\u021e\t\7\2\2\u021eq\3\2\2\2\u021f\u0220\t\b\2\2\u0220")
        buf.write("s\3\2\2\2\u0221\u0222\t\t\2\2\u0222u\3\2\2\2\u0223\u0224")
        buf.write("\t\n\2\2\u0224w\3\2\2\2\u0225\u0226\7\63\2\2\u0226\u0227")
        buf.write("\5V,\2\u0227\u0228\7\64\2\2\u0228y\3\2\2\2\u0229\u022a")
        buf.write("\7?\2\2\u022a\u022b\5|?\2\u022b{\3\2\2\2\u022c\u022e\7")
        buf.write("\61\2\2\u022d\u022f\5~@\2\u022e\u022d\3\2\2\2\u022e\u022f")
        buf.write("\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0231\7\62\2\2\u0231")
        buf.write("}\3\2\2\2\u0232\u0237\5V,\2\u0233\u0234\78\2\2\u0234\u0236")
        buf.write("\5V,\2\u0235\u0233\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235")
        buf.write("\3\2\2\2\u0237\u0238\3\2\2\2\u0238\177\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u023a\u023b\t\13\2\2\u023b\u0081\3\2\2\2\u023c")
        buf.write("\u0241\7<\2\2\u023d\u0241\7=\2\2\u023e\u0241\5\u0080A")
        buf.write("\2\u023f\u0241\7>\2\2\u0240\u023c\3\2\2\2\u0240\u023d")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u023f\3\2\2\2\u0241")
        buf.write("\u0083\3\2\2\2\u0242\u0243\7\65\2\2\u0243\u0248\5\u0082")
        buf.write("B\2\u0244\u0245\78\2\2\u0245\u0247\5\u0082B\2\u0246\u0244")
        buf.write("\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248")
        buf.write("\u0249\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024b\u024c\7\66\2\2\u024c\u0085\3\2\2\2\67\u0089\u0091")
        buf.write("\u0097\u009f\u00a3\u00a7\u00a9\u00b0\u00ba\u00c0\u00cd")
        buf.write("\u00d3\u00de\u00e4\u00e8\u00ed\u00f3\u00f9\u0103\u0108")
        buf.write("\u0110\u011b\u0125\u012b\u0134\u013a\u0140\u0148\u0150")
        buf.write("\u015e\u0169\u0176\u0180\u0185\u0187\u0192\u01a6\u01b2")
        buf.write("\u01b9\u01c4\u01d0\u01dc\u01e7\u01ed\u01f3\u01fc\u0207")
        buf.write("\u020f\u0219\u022e\u0237\u0240\u0248")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'='", "':='", 
                     "'main'", "'return'", "'true'", "'false'", "'class'", 
                     "'extends'", "'new'", "'nil'", "'this'", "'final'", 
                     "'static'", "'if'", "'else'", "'then'", "'int'", "'float'", 
                     "'string'", "'boolean'", "'void'", "'for'", "'to'", 
                     "'downto'", "'do'", "'break'", "'continue'", "'&&'", 
                     "'||'", "'!'", "'<'", "'>'", "'=='", "'!='", "'<='", 
                     "'>='", "'+'", "'-'", "'*'", "'%'", "'\\'", "'/'", 
                     "'^'", "<INVALID>", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "BLOCKCOMMENT", "LINECOMMENT", "EQUAL_SIGN", 
                      "ASSIGN", "MAIN", "RETURN", "TRUE", "FALSE", "CLASS", 
                      "EXTENDS", "NEW", "NIL", "THIS", "FINAL", "STATIC", 
                      "IF", "ELSE", "THEN", "INT", "FLOAT", "STRING", "BOOLEAN", 
                      "VOID", "FOR", "TO", "DOWNTO", "DO", "BREAK", "CONTINUE", 
                      "AND", "OR", "NOT", "LT", "GT", "EQ", "NEQ", "LTE", 
                      "GTE", "ADD", "MINUS", "MUL", "MOD", "IDIV", "FDIV", 
                      "CONCAT", "OBJ_CREA", "LB", "RB", "LSB", "RSB", "LP", 
                      "RP", "DOT", "COMMA", "COLON", "SEMICOLON", "WS", 
                      "INT_LIT", "FLOAT_LIT", "STRING_LIT", "ID", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_class_body = 2
    RULE_atb_decl = 3
    RULE_atb_init = 4
    RULE_var_decls = 5
    RULE_decl_list = 6
    RULE_var_decl = 7
    RULE_array_decls = 8
    RULE_array_list = 9
    RULE_array_decl = 10
    RULE_obj_decls = 11
    RULE_obj_list = 12
    RULE_obj_decl = 13
    RULE_method_decls = 14
    RULE_constructor_decl = 15
    RULE_method_decl = 16
    RULE_param_list = 17
    RULE_params = 18
    RULE_one_params = 19
    RULE_many_params = 20
    RULE_param_type = 21
    RULE_var_type = 22
    RULE_return_type = 23
    RULE_stmt = 24
    RULE_block_stmt = 25
    RULE_stmt_decl = 26
    RULE_variables = 27
    RULE_array_variables = 28
    RULE_object_variables = 29
    RULE_assign_stmt = 30
    RULE_lhs = 31
    RULE_array_var = 32
    RULE_if_stmt = 33
    RULE_for_stmt = 34
    RULE_break_stmt = 35
    RULE_continue_stmt = 36
    RULE_return_stmt = 37
    RULE_atb_access = 38
    RULE_instance_name = 39
    RULE_attr_name = 40
    RULE_invoke_stmt = 41
    RULE_exp = 42
    RULE_exp1 = 43
    RULE_exp2 = 44
    RULE_exp3 = 45
    RULE_exp4 = 46
    RULE_exp5 = 47
    RULE_exp6 = 48
    RULE_exp7 = 49
    RULE_exp8 = 50
    RULE_exp9 = 51
    RULE_exp10 = 52
    RULE_exp11 = 53
    RULE_relation = 54
    RULE_comparision = 55
    RULE_logic = 56
    RULE_add_minus = 57
    RULE_mul_mod_div = 58
    RULE_index_op = 59
    RULE_method_invo = 60
    RULE_listExp = 61
    RULE_arguList = 62
    RULE_bool_lit = 63
    RULE_literal = 64
    RULE_array_lit = 65

    ruleNames =  [ "program", "class_decl", "class_body", "atb_decl", "atb_init", 
                   "var_decls", "decl_list", "var_decl", "array_decls", 
                   "array_list", "array_decl", "obj_decls", "obj_list", 
                   "obj_decl", "method_decls", "constructor_decl", "method_decl", 
                   "param_list", "params", "one_params", "many_params", 
                   "param_type", "var_type", "return_type", "stmt", "block_stmt", 
                   "stmt_decl", "variables", "array_variables", "object_variables", 
                   "assign_stmt", "lhs", "array_var", "if_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "atb_access", 
                   "instance_name", "attr_name", "invoke_stmt", "exp", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "exp9", "exp10", "exp11", "relation", "comparision", 
                   "logic", "add_minus", "mul_mod_div", "index_op", "method_invo", 
                   "listExp", "arguList", "bool_lit", "literal", "array_lit" ]

    EOF = Token.EOF
    BLOCKCOMMENT=1
    LINECOMMENT=2
    EQUAL_SIGN=3
    ASSIGN=4
    MAIN=5
    RETURN=6
    TRUE=7
    FALSE=8
    CLASS=9
    EXTENDS=10
    NEW=11
    NIL=12
    THIS=13
    FINAL=14
    STATIC=15
    IF=16
    ELSE=17
    THEN=18
    INT=19
    FLOAT=20
    STRING=21
    BOOLEAN=22
    VOID=23
    FOR=24
    TO=25
    DOWNTO=26
    DO=27
    BREAK=28
    CONTINUE=29
    AND=30
    OR=31
    NOT=32
    LT=33
    GT=34
    EQ=35
    NEQ=36
    LTE=37
    GTE=38
    ADD=39
    MINUS=40
    MUL=41
    MOD=42
    IDIV=43
    FDIV=44
    CONCAT=45
    OBJ_CREA=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    LP=51
    RP=52
    DOT=53
    COMMA=54
    COLON=55
    SEMICOLON=56
    WS=57
    INT_LIT=58
    FLOAT_LIT=59
    STRING_LIT=60
    ID=61
    ERROR_CHAR=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64

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

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_declContext,i)


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
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.class_decl()
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 137
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
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

        def class_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_bodyContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_bodyContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = BKOOLParser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(BKOOLParser.CLASS)
            self.state = 140
            self.match(BKOOLParser.ID)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 141
                self.match(BKOOLParser.EXTENDS)
                self.state = 142
                self.match(BKOOLParser.ID)


            self.state = 145
            self.match(BKOOLParser.LP)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.VOID) | (1 << BKOOLParser.ID))) != 0):
                self.state = 146
                self.class_body()
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atb_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Atb_declContext,0)


        def obj_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_declsContext,0)


        def method_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_class_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_body" ):
                return visitor.visitClass_body(self)
            else:
                return visitor.visitChildren(self)




    def class_body(self):

        localctx = BKOOLParser.Class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_body)
        try:
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.atb_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.obj_decls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.method_decls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atb_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atb_init(self):
            return self.getTypedRuleContext(BKOOLParser.Atb_initContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_atb_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtb_decl" ):
                return visitor.visitAtb_decl(self)
            else:
                return visitor.visitChildren(self)




    def atb_decl(self):

        localctx = BKOOLParser.Atb_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atb_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.FINAL]:
                self.state = 159
                self.match(BKOOLParser.FINAL)
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 160
                    self.match(BKOOLParser.STATIC)


                pass
            elif token in [BKOOLParser.STATIC]:
                self.state = 163
                self.match(BKOOLParser.STATIC)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 164
                    self.match(BKOOLParser.FINAL)


                pass
            elif token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN]:
                pass
            else:
                pass
            self.state = 169
            self.atb_init()
            self.state = 170
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atb_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Var_declsContext,0)


        def array_decls(self):
            return self.getTypedRuleContext(BKOOLParser.Array_declsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_atb_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtb_init" ):
                return visitor.visitAtb_init(self)
            else:
                return visitor.visitChildren(self)




    def atb_init(self):

        localctx = BKOOLParser.Atb_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atb_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 172
                self.var_decls()
                pass

            elif la_ == 2:
                self.state = 173
                self.array_decls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(BKOOLParser.Decl_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decls" ):
                return visitor.visitVar_decls(self)
            else:
                return visitor.visitChildren(self)




    def var_decls(self):

        localctx = BKOOLParser.Var_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.var_type()
            self.state = 177
            self.decl_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Var_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = BKOOLParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.var_decl()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 180
                self.match(BKOOLParser.COMMA)
                self.state = 181
                self.var_decl()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = BKOOLParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKOOLParser.ID)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 188
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 189
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKOOLParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decls" ):
                return visitor.visitArray_decls(self)
            else:
                return visitor.visitChildren(self)




    def array_decls(self):

        localctx = BKOOLParser.Array_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.var_type()
            self.state = 193
            self.match(BKOOLParser.LSB)
            self.state = 194
            self.match(BKOOLParser.INT_LIT)
            self.state = 195
            self.match(BKOOLParser.RSB)
            self.state = 196
            self.array_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Array_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Array_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKOOLParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.array_decl()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 199
                self.match(BKOOLParser.COMMA)
                self.state = 200
                self.array_decl()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def array_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Array_litContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = BKOOLParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(BKOOLParser.ID)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 207
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 208
                self.array_lit()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def obj_list(self):
            return self.getTypedRuleContext(BKOOLParser.Obj_listContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_decls" ):
                return visitor.visitObj_decls(self)
            else:
                return visitor.visitChildren(self)




    def obj_decls(self):

        localctx = BKOOLParser.Obj_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_obj_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(BKOOLParser.ID)
            self.state = 212
            self.obj_list()
            self.state = 213
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def obj_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Obj_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Obj_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_list" ):
                return visitor.visitObj_list(self)
            else:
                return visitor.visitChildren(self)




    def obj_list(self):

        localctx = BKOOLParser.Obj_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_obj_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.obj_decl()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 216
                self.match(BKOOLParser.COMMA)
                self.state = 217
                self.obj_decl()
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def EQUAL_SIGN(self):
            return self.getToken(BKOOLParser.EQUAL_SIGN, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_obj_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_decl" ):
                return visitor.visitObj_decl(self)
            else:
                return visitor.visitChildren(self)




    def obj_decl(self):

        localctx = BKOOLParser.Obj_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_obj_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BKOOLParser.ID)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 224
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 225
                self.match(BKOOLParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constructor_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Constructor_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Method_declContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decls" ):
                return visitor.visitMethod_decls(self)
            else:
                return visitor.visitChildren(self)




    def method_decls(self):

        localctx = BKOOLParser.Method_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_method_decls)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.constructor_decl()
                pass
            elif token in [BKOOLParser.STATIC, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN, BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.method_decl()
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


    class Constructor_declContext(ParserRuleContext):
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

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_decl" ):
                return visitor.visitConstructor_decl(self)
            else:
                return visitor.visitChildren(self)




    def constructor_decl(self):

        localctx = BKOOLParser.Constructor_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructor_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(BKOOLParser.ID)
            self.state = 233
            self.match(BKOOLParser.LB)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 234
                self.param_list()


            self.state = 237
            self.match(BKOOLParser.RB)
            self.state = 238
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_type(self):
            return self.getTypedRuleContext(BKOOLParser.Return_typeContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def MAIN(self):
            return self.getToken(BKOOLParser.MAIN, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = BKOOLParser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 240
                self.match(BKOOLParser.STATIC)


            self.state = 243
            self.return_type()
            self.state = 244
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.MAIN or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 245
            self.match(BKOOLParser.LB)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 246
                self.param_list()


            self.state = 249
            self.match(BKOOLParser.RB)
            self.state = 250
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamsContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMICOLON)
            else:
                return self.getToken(BKOOLParser.SEMICOLON, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.params()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.SEMICOLON:
                self.state = 253
                self.match(BKOOLParser.SEMICOLON)
                self.state = 254
                self.params()
                self.state = 259
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

        def one_params(self):
            return self.getTypedRuleContext(BKOOLParser.One_paramsContext,0)


        def many_params(self):
            return self.getTypedRuleContext(BKOOLParser.Many_paramsContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = BKOOLParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 260
                self.one_params()
                pass

            elif la_ == 2:
                self.state = 261
                self.many_params()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_type(self):
            return self.getTypedRuleContext(BKOOLParser.Param_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_one_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_params" ):
                return visitor.visitOne_params(self)
            else:
                return visitor.visitChildren(self)




    def one_params(self):

        localctx = BKOOLParser.One_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_one_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.param_type()
            self.state = 265
            self.match(BKOOLParser.ID)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 266
                self.match(BKOOLParser.COMMA)
                self.state = 267
                self.match(BKOOLParser.ID)
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Param_typeContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Param_typeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_many_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_params" ):
                return visitor.visitMany_params(self)
            else:
                return visitor.visitChildren(self)




    def many_params(self):

        localctx = BKOOLParser.Many_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_many_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.param_type()
            self.state = 274
            self.match(BKOOLParser.ID)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 275
                self.match(BKOOLParser.COMMA)
                self.state = 276
                self.param_type()
                self.state = 277
                self.match(BKOOLParser.ID)
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_type" ):
                return visitor.visitParam_type(self)
            else:
                return visitor.visitChildren(self)




    def param_type(self):

        localctx = BKOOLParser.Param_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 284
                self.var_type()
                pass

            elif la_ == 2:
                self.state = 285
                self.var_type()
                self.state = 286
                self.match(BKOOLParser.LSB)
                self.state = 287
                self.match(BKOOLParser.INT_LIT)
                self.state = 288
                self.match(BKOOLParser.RSB)
                pass

            elif la_ == 3:
                self.state = 290
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
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
            return BKOOLParser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = BKOOLParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
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


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = BKOOLParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_return_type)
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.var_type()
                pass
            elif token in [BKOOLParser.VOID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
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

        def assign_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Continue_stmtContext,0)


        def invoke_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Invoke_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 299
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.state = 300
                self.if_stmt()
                pass

            elif la_ == 3:
                self.state = 301
                self.for_stmt()
                pass

            elif la_ == 4:
                self.state = 302
                self.break_stmt()
                pass

            elif la_ == 5:
                self.state = 303
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.state = 304
                self.invoke_stmt()
                pass

            elif la_ == 7:
                self.state = 305
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def stmt_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Stmt_declContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Stmt_declContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = BKOOLParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(BKOOLParser.LP)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 309
                    self.stmt_decl() 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.RETURN) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.IF) | (1 << BKOOLParser.FOR) | (1 << BKOOLParser.BREAK) | (1 << BKOOLParser.CONTINUE) | (1 << BKOOLParser.ID))) != 0):
                self.state = 315
                self.stmt()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 321
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(BKOOLParser.VariablesContext,0)


        def array_variables(self):
            return self.getTypedRuleContext(BKOOLParser.Array_variablesContext,0)


        def object_variables(self):
            return self.getTypedRuleContext(BKOOLParser.Object_variablesContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_decl" ):
                return visitor.visitStmt_decl(self)
            else:
                return visitor.visitChildren(self)




    def stmt_decl(self):

        localctx = BKOOLParser.Stmt_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 323
                self.variables()
                pass

            elif la_ == 2:
                self.state = 324
                self.array_variables()
                pass

            elif la_ == 3:
                self.state = 325
                self.object_variables()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariables" ):
                return visitor.visitVariables(self)
            else:
                return visitor.visitChildren(self)




    def variables(self):

        localctx = BKOOLParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.var_type()
            self.state = 329
            self.match(BKOOLParser.ID)
            self.state = 334
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 330
                self.match(BKOOLParser.COMMA)
                self.state = 331
                self.match(BKOOLParser.ID)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 337
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_variablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(BKOOLParser.Var_typeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_variables" ):
                return visitor.visitArray_variables(self)
            else:
                return visitor.visitChildren(self)




    def array_variables(self):

        localctx = BKOOLParser.Array_variablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_array_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.var_type()
            self.state = 340
            self.match(BKOOLParser.LSB)
            self.state = 341
            self.match(BKOOLParser.INT_LIT)
            self.state = 342
            self.match(BKOOLParser.RSB)
            self.state = 343
            self.match(BKOOLParser.ID)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 344
                self.match(BKOOLParser.COMMA)
                self.state = 345
                self.match(BKOOLParser.ID)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 351
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_variablesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_object_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_variables" ):
                return visitor.visitObject_variables(self)
            else:
                return visitor.visitChildren(self)




    def object_variables(self):

        localctx = BKOOLParser.Object_variablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_object_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BKOOLParser.ID)
            self.state = 354
            self.match(BKOOLParser.ID)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 355
                self.match(BKOOLParser.COMMA)
                self.state = 356
                self.match(BKOOLParser.ID)
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 362
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
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


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKOOLParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.lhs()
            self.state = 365
            self.match(BKOOLParser.ASSIGN)
            self.state = 366
            self.exp()
            self.state = 367
            self.match(BKOOLParser.SEMICOLON)
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

        def array_var(self):
            return self.getTypedRuleContext(BKOOLParser.Array_varContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def atb_access(self):
            return self.getTypedRuleContext(BKOOLParser.Atb_accessContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = BKOOLParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 369
                self.array_var()
                pass

            elif la_ == 2:
                self.state = 370
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 3:
                self.state = 371
                self.atb_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def index_op(self):
            return self.getTypedRuleContext(BKOOLParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_array_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_var" ):
                return visitor.visitArray_var(self)
            else:
                return visitor.visitChildren(self)




    def array_var(self):

        localctx = BKOOLParser.Array_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(BKOOLParser.ID)
            self.state = 375
            self.index_op()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
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


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKOOLParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(BKOOLParser.IF)
            self.state = 378
            self.exp()
            self.state = 379
            self.match(BKOOLParser.THEN)
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.ID]:
                self.state = 380
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 381
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 384
                self.match(BKOOLParser.ELSE)
                self.state = 387
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.ID]:
                    self.state = 385
                    self.stmt()
                    pass
                elif token in [BKOOLParser.LP]:
                    self.state = 386
                    self.block_stmt()
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


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

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


        def block_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKOOLParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(BKOOLParser.FOR)
            self.state = 392
            self.match(BKOOLParser.ID)
            self.state = 393
            self.match(BKOOLParser.ASSIGN)
            self.state = 394
            self.exp()
            self.state = 395
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 396
            self.exp()
            self.state = 397
            self.match(BKOOLParser.DO)
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.ID]:
                self.state = 398
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 399
                self.block_stmt()
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


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKOOLParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(BKOOLParser.BREAK)
            self.state = 403
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKOOLParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(BKOOLParser.CONTINUE)
            self.state = 406
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(BKOOLParser.RETURN)
            self.state = 409
            self.exp()
            self.state = 410
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atb_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_name(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_nameContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def attr_name(self):
            return self.getTypedRuleContext(BKOOLParser.Attr_nameContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_atb_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtb_access" ):
                return visitor.visitAtb_access(self)
            else:
                return visitor.visitChildren(self)




    def atb_access(self):

        localctx = BKOOLParser.Atb_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_atb_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.instance_name()
            self.state = 413
            self.match(BKOOLParser.DOT)
            self.state = 414
            self.attr_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_instance_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_name" ):
                return visitor.visitInstance_name(self)
            else:
                return visitor.visitChildren(self)




    def instance_name(self):

        localctx = BKOOLParser.Instance_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_instance_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.THIS or _la==BKOOLParser.ID):
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


    class Attr_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def array_var(self):
            return self.getTypedRuleContext(BKOOLParser.Array_varContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attr_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_name" ):
                return visitor.visitAttr_name(self)
            else:
                return visitor.visitChildren(self)




    def attr_name(self):

        localctx = BKOOLParser.Attr_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_attr_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 418
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.state = 419
                self.array_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invoke_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_name(self):
            return self.getTypedRuleContext(BKOOLParser.Instance_nameContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_invoke_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvoke_stmt" ):
                return visitor.visitInvoke_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invoke_stmt(self):

        localctx = BKOOLParser.Invoke_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_invoke_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.instance_name()
            self.state = 423
            self.match(BKOOLParser.DOT)
            self.state = 424
            self.method_invo()
            self.state = 425
            self.match(BKOOLParser.SEMICOLON)
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


        def relation(self):
            return self.getTypedRuleContext(BKOOLParser.RelationContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_exp)
        try:
            self.state = 432
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.exp1()
                self.state = 428
                self.relation()
                self.state = 429
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
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


        def comparision(self):
            return self.getTypedRuleContext(BKOOLParser.ComparisionContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp1)
        try:
            self.state = 439
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.exp2(0)
                self.state = 435
                self.comparision()
                self.state = 436
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 438
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


        def logic(self):
            return self.getTypedRuleContext(BKOOLParser.LogicContext,0)


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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 444
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 445
                    self.logic()
                    self.state = 446
                    self.exp3(0) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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


        def add_minus(self):
            return self.getTypedRuleContext(BKOOLParser.Add_minusContext,0)


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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    self.add_minus()
                    self.state = 458
                    self.exp4(0) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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


        def mul_mod_div(self):
            return self.getTypedRuleContext(BKOOLParser.Mul_mod_divContext,0)


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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 474
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 468
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 469
                    self.mul_mod_div()
                    self.state = 470
                    self.exp5(0) 
                self.state = 476
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

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
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 480
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 481
                    self.match(BKOOLParser.CONCAT)
                    self.state = 482
                    self.exp6() 
                self.state = 487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        self.enterRule(localctx, 96, self.RULE_exp6)
        try:
            self.state = 491
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.match(BKOOLParser.NOT)
                self.state = 489
                self.exp6()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.MINUS, BKOOLParser.LB, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
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

        def add_minus(self):
            return self.getTypedRuleContext(BKOOLParser.Add_minusContext,0)


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
        self.enterRule(localctx, 98, self.RULE_exp7)
        try:
            self.state = 497
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.add_minus()
                self.state = 494
                self.exp7()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 496
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


        def index_op(self):
            return self.getTypedRuleContext(BKOOLParser.Index_opContext,0)


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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 506
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 502
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 503
                    self.index_op() 
                self.state = 508
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 510
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 517
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 512
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 513
                    self.match(BKOOLParser.DOT)
                    self.state = 514
                    self.exp10() 
                self.state = 519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        self.enterRule(localctx, 104, self.RULE_exp10)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.match(BKOOLParser.NEW)
                self.state = 521
                self.exp10()
                self.state = 522
                self.listExp()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INT_LIT, BKOOLParser.FLOAT_LIT, BKOOLParser.STRING_LIT, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
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

        def method_invo(self):
            return self.getTypedRuleContext(BKOOLParser.Method_invoContext,0)


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
        self.enterRule(localctx, 106, self.RULE_exp11)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(BKOOLParser.LB)
                self.state = 528
                self.exp()
                self.state = 529
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                self.method_invo()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 534
                self.match(BKOOLParser.THIS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(BKOOLParser.LT, 0)

        def GT(self):
            return self.getToken(BKOOLParser.GT, 0)

        def LTE(self):
            return self.getToken(BKOOLParser.LTE, 0)

        def GTE(self):
            return self.getToken(BKOOLParser.GTE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_relation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = BKOOLParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LT) | (1 << BKOOLParser.GT) | (1 << BKOOLParser.LTE) | (1 << BKOOLParser.GTE))) != 0)):
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


    class ComparisionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_comparision

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparision" ):
                return visitor.visitComparision(self)
            else:
                return visitor.visitChildren(self)




    def comparision(self):

        localctx = BKOOLParser.ComparisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_comparision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.EQ or _la==BKOOLParser.NEQ):
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


    class LogicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_logic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic" ):
                return visitor.visitLogic(self)
            else:
                return visitor.visitChildren(self)




    def logic(self):

        localctx = BKOOLParser.LogicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_logic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
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


    class Add_minusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def MINUS(self):
            return self.getToken(BKOOLParser.MINUS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_add_minus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd_minus" ):
                return visitor.visitAdd_minus(self)
            else:
                return visitor.visitChildren(self)




    def add_minus(self):

        localctx = BKOOLParser.Add_minusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_add_minus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.ADD or _la==BKOOLParser.MINUS):
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


    class Mul_mod_divContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mul_mod_div

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul_mod_div" ):
                return visitor.visitMul_mod_div(self)
            else:
                return visitor.visitChildren(self)




    def mul_mod_div(self):

        localctx = BKOOLParser.Mul_mod_divContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_mul_mod_div)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.MOD) | (1 << BKOOLParser.IDIV) | (1 << BKOOLParser.FDIV))) != 0)):
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


    class Index_opContext(ParserRuleContext):
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
            return BKOOLParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = BKOOLParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(BKOOLParser.LSB)
            self.state = 548
            self.exp()
            self.state = 549
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def listExp(self):
            return self.getTypedRuleContext(BKOOLParser.ListExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_method_invo

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invo" ):
                return visitor.visitMethod_invo(self)
            else:
                return visitor.visitChildren(self)




    def method_invo(self):

        localctx = BKOOLParser.Method_invoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_method_invo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 551
            self.match(BKOOLParser.ID)
            self.state = 552
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
        self.enterRule(localctx, 122, self.RULE_listExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.match(BKOOLParser.LB)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.ADD) | (1 << BKOOLParser.MINUS) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INT_LIT) | (1 << BKOOLParser.FLOAT_LIT) | (1 << BKOOLParser.STRING_LIT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 555
                self.arguList()


            self.state = 558
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
        self.enterRule(localctx, 124, self.RULE_arguList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self.exp()
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 561
                self.match(BKOOLParser.COMMA)
                self.state = 562
                self.exp()
                self.state = 567
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKOOLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKOOLParser.FALSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_bool_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)




    def bool_lit(self):

        localctx = BKOOLParser.Bool_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_bool_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
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

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def bool_lit(self):
            return self.getTypedRuleContext(BKOOLParser.Bool_litContext,0)


        def STRING_LIT(self):
            return self.getToken(BKOOLParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKOOLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INT_LIT]:
                self.state = 570
                self.match(BKOOLParser.INT_LIT)
                pass
            elif token in [BKOOLParser.FLOAT_LIT]:
                self.state = 571
                self.match(BKOOLParser.FLOAT_LIT)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 572
                self.bool_lit()
                pass
            elif token in [BKOOLParser.STRING_LIT]:
                self.state = 573
                self.match(BKOOLParser.STRING_LIT)
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


    class Array_litContext(ParserRuleContext):
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
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_array_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(BKOOLParser.LP)
            self.state = 577
            self.literal()
            self.state = 582
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 578
                self.match(BKOOLParser.COMMA)
                self.state = 579
                self.literal()
                self.state = 584
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 585
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
        self._predicates[44] = self.exp2_sempred
        self._predicates[45] = self.exp3_sempred
        self._predicates[46] = self.exp4_sempred
        self._predicates[47] = self.exp5_sempred
        self._predicates[50] = self.exp8_sempred
        self._predicates[51] = self.exp9_sempred
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
         




