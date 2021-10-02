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
        buf.write("\u0285\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\3\2")
        buf.write("\6\2\u009a\n\2\r\2\16\2\u009b\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\5\3\u00a4\n\3\3\3\3\3\7\3\u00a8\n\3\f\3\16\3\u00ab\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\5\4\u00b2\n\4\3\5\3\5\5\5\u00b6")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00bd\n\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6\u00c6\n\6\f\6\16\6\u00c9\13\6\3\6\3\6")
        buf.write("\3\7\5\7\u00ce\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00d7")
        buf.write("\n\7\f\7\16\7\u00da\13\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5")
        buf.write("\t\u00e3\n\t\3\n\3\n\5\n\u00e7\n\n\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f6\n\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\7\16\u00ff\n\16\f\16\16\16\u0102")
        buf.write("\13\16\3\17\3\17\3\17\5\17\u0107\n\17\3\20\3\20\5\20\u010b")
        buf.write("\n\20\3\21\3\21\3\21\5\21\u0110\n\21\3\21\3\21\3\21\3")
        buf.write("\22\5\22\u0116\n\22\3\22\3\22\3\22\3\22\5\22\u011c\n\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u0124\n\23\f\23\16")
        buf.write("\23\u0127\13\23\3\24\3\24\5\24\u012b\n\24\3\25\3\25\3")
        buf.write("\25\3\25\7\25\u0131\n\25\f\25\16\25\u0134\13\25\3\26\3")
        buf.write("\26\3\26\7\26\u0139\n\26\f\26\16\26\u013c\13\26\3\27\3")
        buf.write("\27\3\27\5\27\u0141\n\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u015a\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u0162\n\37\3 \3 \7 \u0166")
        buf.write("\n \f \16 \u0169\13 \3 \7 \u016c\n \f \16 \u016f\13 \3")
        buf.write(" \3 \3!\3!\3!\5!\u0176\n!\3\"\3\"\3\"\3\"\7\"\u017c\n")
        buf.write("\"\f\"\16\"\u017f\13\"\3\"\3\"\3#\3#\3$\3$\3$\3$\7$\u0189")
        buf.write("\n$\f$\16$\u018c\13$\3$\3$\3%\3%\3&\3&\3&\3&\3&\3&\3&")
        buf.write("\7&\u0199\n&\f&\16&\u019c\13&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\5(\u01a8\n(\3)\3)\3)\3)\3*\3*\5*\u01b0\n*")
        buf.write("\3+\3+\3,\3,\5,\u01b6\n,\3-\3-\3-\3-\3-\5-\u01bd\n-\3")
        buf.write("-\3-\3-\5-\u01c2\n-\5-\u01c4\n-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u01cf\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\5\65\u01ea\n\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\5\66\u01f1\n\66\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u01fa\n\67\f\67\16\67\u01fd\13\67\38\3")
        buf.write("8\38\38\38\38\38\78\u0206\n8\f8\168\u0209\138\39\39\3")
        buf.write("9\39\39\39\39\79\u0212\n9\f9\169\u0215\139\3:\3:\3:\3")
        buf.write(":\3:\3:\7:\u021d\n:\f:\16:\u0220\13:\3;\3;\3;\5;\u0225")
        buf.write("\n;\3<\3<\3<\3<\5<\u022b\n<\3=\3=\3=\3=\3=\7=\u0232\n")
        buf.write("=\f=\16=\u0235\13=\3>\3>\3>\3>\3>\3>\7>\u023d\n>\f>\16")
        buf.write(">\u0240\13>\3?\3?\3?\3?\3?\5?\u0247\n?\3@\3@\3@\3@\3@")
        buf.write("\3@\3@\3@\5@\u0251\n@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("F\3F\3F\3F\3G\3G\3G\3H\3H\5H\u0266\nH\3H\3H\3I\3I\3I\7")
        buf.write("I\u026d\nI\fI\16I\u0270\13I\3J\3J\3K\3K\3K\3K\5K\u0278")
        buf.write("\nK\3L\3L\3L\3L\7L\u027e\nL\fL\16L\u0281\13L\3L\3L\3L")
        buf.write("\2\blnprxzM\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz")
        buf.write("|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090")
        buf.write("\u0092\u0094\u0096\2\f\3\2\17\22\4\2\5\5??\3\2\16\22\3")
        buf.write("\2\24\25\3\2)*\3\2+.\3\2 !\3\2%&\4\2#$\'(\3\2\t\n\2\u0285")
        buf.write("\2\u0099\3\2\2\2\4\u009f\3\2\2\2\6\u00b1\3\2\2\2\b\u00b5")
        buf.write("\3\2\2\2\n\u00bc\3\2\2\2\f\u00cd\3\2\2\2\16\u00dd\3\2")
        buf.write("\2\2\20\u00e2\3\2\2\2\22\u00e6\3\2\2\2\24\u00e8\3\2\2")
        buf.write("\2\26\u00ea\3\2\2\2\30\u00f5\3\2\2\2\32\u00fb\3\2\2\2")
        buf.write("\34\u0103\3\2\2\2\36\u010a\3\2\2\2 \u010c\3\2\2\2\"\u0115")
        buf.write("\3\2\2\2$\u0120\3\2\2\2&\u012a\3\2\2\2(\u012c\3\2\2\2")
        buf.write("*\u0135\3\2\2\2,\u0140\3\2\2\2.\u0142\3\2\2\2\60\u0144")
        buf.write("\3\2\2\2\62\u0146\3\2\2\2\64\u014b\3\2\2\2\66\u014e\3")
        buf.write("\2\2\28\u0150\3\2\2\2:\u0159\3\2\2\2<\u0161\3\2\2\2>\u0163")
        buf.write("\3\2\2\2@\u0175\3\2\2\2B\u0177\3\2\2\2D\u0182\3\2\2\2")
        buf.write("F\u0184\3\2\2\2H\u018f\3\2\2\2J\u0191\3\2\2\2L\u019f\3")
        buf.write("\2\2\2N\u01a7\3\2\2\2P\u01a9\3\2\2\2R\u01af\3\2\2\2T\u01b1")
        buf.write("\3\2\2\2V\u01b5\3\2\2\2X\u01b7\3\2\2\2Z\u01c5\3\2\2\2")
        buf.write("\\\u01d0\3\2\2\2^\u01d5\3\2\2\2`\u01d8\3\2\2\2b\u01db")
        buf.write("\3\2\2\2d\u01de\3\2\2\2f\u01e2\3\2\2\2h\u01e9\3\2\2\2")
        buf.write("j\u01f0\3\2\2\2l\u01f2\3\2\2\2n\u01fe\3\2\2\2p\u020a\3")
        buf.write("\2\2\2r\u0216\3\2\2\2t\u0224\3\2\2\2v\u022a\3\2\2\2x\u022c")
        buf.write("\3\2\2\2z\u0236\3\2\2\2|\u0246\3\2\2\2~\u0250\3\2\2\2")
        buf.write("\u0080\u0252\3\2\2\2\u0082\u0254\3\2\2\2\u0084\u0256\3")
        buf.write("\2\2\2\u0086\u0258\3\2\2\2\u0088\u025a\3\2\2\2\u008a\u025c")
        buf.write("\3\2\2\2\u008c\u0260\3\2\2\2\u008e\u0263\3\2\2\2\u0090")
        buf.write("\u0269\3\2\2\2\u0092\u0271\3\2\2\2\u0094\u0277\3\2\2\2")
        buf.write("\u0096\u0279\3\2\2\2\u0098\u009a\5\4\3\2\u0099\u0098\3")
        buf.write("\2\2\2\u009a\u009b\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\7\2\2\3\u009e")
        buf.write("\3\3\2\2\2\u009f\u00a0\7\31\2\2\u00a0\u00a3\7?\2\2\u00a1")
        buf.write("\u00a2\7\32\2\2\u00a2\u00a4\7?\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a9\7")
        buf.write("\61\2\2\u00a6\u00a8\5\6\4\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7")
        buf.write("\62\2\2\u00ad\5\3\2\2\2\u00ae\u00b2\5\b\5\2\u00af\u00b2")
        buf.write("\5\30\r\2\u00b0\u00b2\5\36\20\2\u00b1\u00ae\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\7\3\2\2\2\u00b3")
        buf.write("\u00b6\5\n\6\2\u00b4\u00b6\5\f\7\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b4\3\2\2\2\u00b6\t\3\2\2\2\u00b7\u00bd\7\36")
        buf.write("\2\2\u00b8\u00b9\7\36\2\2\u00b9\u00bd\7\37\2\2\u00ba\u00bb")
        buf.write("\7\37\2\2\u00bb\u00bd\7\36\2\2\u00bc\u00b7\3\2\2\2\u00bc")
        buf.write("\u00b8\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be\3\2\2\2")
        buf.write("\u00be\u00bf\5\22\n\2\u00bf\u00c0\7?\2\2\u00c0\u00c1\5")
        buf.write("\16\b\2\u00c1\u00c7\3\2\2\2\u00c2\u00c3\78\2\2\u00c3\u00c4")
        buf.write("\7?\2\2\u00c4\u00c6\5\16\b\2\u00c5\u00c2\3\2\2\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2")
        buf.write("\u00c8\u00ca\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca\u00cb\7")
        buf.write(":\2\2\u00cb\13\3\2\2\2\u00cc\u00ce\7\37\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d0\5\22\n\2\u00d0\u00d1\7?\2\2\u00d1\u00d2\5\20\t")
        buf.write("\2\u00d2\u00d8\3\2\2\2\u00d3\u00d4\78\2\2\u00d4\u00d5")
        buf.write("\7?\2\2\u00d5\u00d7\5\20\t\2\u00d6\u00d3\3\2\2\2\u00d7")
        buf.write("\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\7")
        buf.write(":\2\2\u00dc\r\3\2\2\2\u00dd\u00de\7\6\2\2\u00de\u00df")
        buf.write("\5h\65\2\u00df\17\3\2\2\2\u00e0\u00e1\7\6\2\2\u00e1\u00e3")
        buf.write("\5h\65\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\21\3\2\2\2\u00e4\u00e7\5\26\f\2\u00e5\u00e7\5\24\13\2")
        buf.write("\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\23\3\2")
        buf.write("\2\2\u00e8\u00e9\t\2\2\2\u00e9\25\3\2\2\2\u00ea\u00eb")
        buf.write("\5\24\13\2\u00eb\u00ec\7\65\2\2\u00ec\u00ed\7<\2\2\u00ed")
        buf.write("\u00ee\7\66\2\2\u00ee\27\3\2\2\2\u00ef\u00f6\7\36\2\2")
        buf.write("\u00f0\u00f6\7\37\2\2\u00f1\u00f2\7\36\2\2\u00f2\u00f6")
        buf.write("\7\37\2\2\u00f3\u00f4\7\37\2\2\u00f4\u00f6\7\36\2\2\u00f5")
        buf.write("\u00ef\3\2\2\2\u00f5\u00f0\3\2\2\2\u00f5\u00f1\3\2\2\2")
        buf.write("\u00f5\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\3")
        buf.write("\2\2\2\u00f7\u00f8\5f\64\2\u00f8\u00f9\5\32\16\2\u00f9")
        buf.write("\u00fa\7:\2\2\u00fa\31\3\2\2\2\u00fb\u0100\5\34\17\2\u00fc")
        buf.write("\u00fd\78\2\2\u00fd\u00ff\5\34\17\2\u00fe\u00fc\3\2\2")
        buf.write("\2\u00ff\u0102\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\33\3\2\2\2\u0102\u0100\3\2\2\2\u0103\u0106")
        buf.write("\5T+\2\u0104\u0105\7\6\2\2\u0105\u0107\5T+\2\u0106\u0104")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\35\3\2\2\2\u0108\u010b")
        buf.write("\5 \21\2\u0109\u010b\5\"\22\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u0109\3\2\2\2\u010b\37\3\2\2\2\u010c\u010d\7?\2\2\u010d")
        buf.write("\u010f\7\63\2\2\u010e\u0110\5$\23\2\u010f\u010e\3\2\2")
        buf.write("\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112")
        buf.write("\7\64\2\2\u0112\u0113\5> \2\u0113!\3\2\2\2\u0114\u0116")
        buf.write("\7\37\2\2\u0115\u0114\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("\u0117\3\2\2\2\u0117\u0118\58\35\2\u0118\u0119\t\3\2\2")
        buf.write("\u0119\u011b\7\63\2\2\u011a\u011c\5$\23\2\u011b\u011a")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u011e\7\64\2\2\u011e\u011f\5> \2\u011f#\3\2\2\2\u0120")
        buf.write("\u0125\5&\24\2\u0121\u0122\7:\2\2\u0122\u0124\5&\24\2")
        buf.write("\u0123\u0121\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126%\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u012b\5(\25\2\u0129\u012b\5*\26\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u0129\3\2\2\2\u012b\'\3\2\2\2\u012c")
        buf.write("\u012d\5,\27\2\u012d\u0132\5\66\34\2\u012e\u012f\78\2")
        buf.write("\2\u012f\u0131\5\66\34\2\u0130\u012e\3\2\2\2\u0131\u0134")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write(")\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u013a\5\64\33\2\u0136")
        buf.write("\u0137\78\2\2\u0137\u0139\5\64\33\2\u0138\u0136\3\2\2")
        buf.write("\2\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b")
        buf.write("\3\2\2\2\u013b+\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u0141")
        buf.write("\5\60\31\2\u013e\u0141\5\62\32\2\u013f\u0141\5.\30\2\u0140")
        buf.write("\u013d\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2")
        buf.write("\u0141-\3\2\2\2\u0142\u0143\5f\64\2\u0143/\3\2\2\2\u0144")
        buf.write("\u0145\5\22\n\2\u0145\61\3\2\2\2\u0146\u0147\5\60\31\2")
        buf.write("\u0147\u0148\7\65\2\2\u0148\u0149\7<\2\2\u0149\u014a\7")
        buf.write("\66\2\2\u014a\63\3\2\2\2\u014b\u014c\5,\27\2\u014c\u014d")
        buf.write("\5\66\34\2\u014d\65\3\2\2\2\u014e\u014f\7?\2\2\u014f\67")
        buf.write("\3\2\2\2\u0150\u0151\t\4\2\2\u01519\3\2\2\2\u0152\u015a")
        buf.write("\5L\'\2\u0153\u015a\5X-\2\u0154\u015a\5Z.\2\u0155\u015a")
        buf.write("\5`\61\2\u0156\u015a\5b\62\2\u0157\u015a\5\\/\2\u0158")
        buf.write("\u015a\5d\63\2\u0159\u0152\3\2\2\2\u0159\u0153\3\2\2\2")
        buf.write("\u0159\u0154\3\2\2\2\u0159\u0155\3\2\2\2\u0159\u0156\3")
        buf.write("\2\2\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a;")
        buf.write("\3\2\2\2\u015b\u0162\5L\'\2\u015c\u0162\5X-\2\u015d\u0162")
        buf.write("\5Z.\2\u015e\u0162\5`\61\2\u015f\u0162\5b\62\2\u0160\u0162")
        buf.write("\5\\/\2\u0161\u015b\3\2\2\2\u0161\u015c\3\2\2\2\u0161")
        buf.write("\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162=\3\2\2\2\u0163\u0167\7\61\2")
        buf.write("\2\u0164\u0166\5@!\2\u0165\u0164\3\2\2\2\u0166\u0169\3")
        buf.write("\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016d")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\5:\36\2\u016b")
        buf.write("\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u0170\u0171\7\62\2\2\u0171?\3\2\2\2\u0172\u0176")
        buf.write("\5F$\2\u0173\u0176\5J&\2\u0174\u0176\5B\"\2\u0175\u0172")
        buf.write("\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("A\3\2\2\2\u0177\u0178\5f\64\2\u0178\u017d\5D#\2\u0179")
        buf.write("\u017a\78\2\2\u017a\u017c\5D#\2\u017b\u0179\3\2\2\2\u017c")
        buf.write("\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u0180\3\2\2\2\u017f\u017d\3\2\2\2\u0180\u0181\7")
        buf.write(":\2\2\u0181C\3\2\2\2\u0182\u0183\7?\2\2\u0183E\3\2\2\2")
        buf.write("\u0184\u0185\5\22\n\2\u0185\u018a\5H%\2\u0186\u0187\7")
        buf.write("8\2\2\u0187\u0189\5H%\2\u0188\u0186\3\2\2\2\u0189\u018c")
        buf.write("\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018e\7:\2\2")
        buf.write("\u018eG\3\2\2\2\u018f\u0190\7?\2\2\u0190I\3\2\2\2\u0191")
        buf.write("\u0192\5\22\n\2\u0192\u0193\7\65\2\2\u0193\u0194\7<\2")
        buf.write("\2\u0194\u0195\7\66\2\2\u0195\u019a\5H%\2\u0196\u0197")
        buf.write("\78\2\2\u0197\u0199\5H%\2\u0198\u0196\3\2\2\2\u0199\u019c")
        buf.write("\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u019d\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\7:\2\2")
        buf.write("\u019eK\3\2\2\2\u019f\u01a0\5N(\2\u01a0\u01a1\7\7\2\2")
        buf.write("\u01a1\u01a2\5h\65\2\u01a2\u01a3\7:\2\2\u01a3M\3\2\2\2")
        buf.write("\u01a4\u01a8\5^\60\2\u01a5\u01a8\5H%\2\u01a6\u01a8\5P")
        buf.write(")\2\u01a7\u01a4\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8O\3\2\2\2\u01a9\u01aa\5R*\2\u01aa\u01ab")
        buf.write("\7\67\2\2\u01ab\u01ac\5V,\2\u01acQ\3\2\2\2\u01ad\u01b0")
        buf.write("\7\35\2\2\u01ae\u01b0\5T+\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01b0S\3\2\2\2\u01b1\u01b2\7?\2\2\u01b2")
        buf.write("U\3\2\2\2\u01b3\u01b6\5H%\2\u01b4\u01b6\5^\60\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6W\3\2\2\2\u01b7")
        buf.write("\u01b8\7\f\2\2\u01b8\u01b9\5h\65\2\u01b9\u01bc\7\r\2\2")
        buf.write("\u01ba\u01bd\5:\36\2\u01bb\u01bd\5> \2\u01bc\u01ba\3\2")
        buf.write("\2\2\u01bc\u01bb\3\2\2\2\u01bd\u01c3\3\2\2\2\u01be\u01c1")
        buf.write("\7\13\2\2\u01bf\u01c2\5:\36\2\u01c0\u01c2\5> \2\u01c1")
        buf.write("\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c4\3\2\2\2")
        buf.write("\u01c3\u01be\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4Y\3\2\2")
        buf.write("\2\u01c5\u01c6\7\23\2\2\u01c6\u01c7\5H%\2\u01c7\u01c8")
        buf.write("\7\7\2\2\u01c8\u01c9\5h\65\2\u01c9\u01ca\t\5\2\2\u01ca")
        buf.write("\u01cb\5h\65\2\u01cb\u01ce\7\26\2\2\u01cc\u01cf\5:\36")
        buf.write("\2\u01cd\u01cf\5> \2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3")
        buf.write("\2\2\2\u01cf[\3\2\2\2\u01d0\u01d1\5R*\2\u01d1\u01d2\7")
        buf.write("\67\2\2\u01d2\u01d3\5\u008cG\2\u01d3\u01d4\7:\2\2\u01d4")
        buf.write("]\3\2\2\2\u01d5\u01d6\7?\2\2\u01d6\u01d7\5\u008aF\2\u01d7")
        buf.write("_\3\2\2\2\u01d8\u01d9\7\27\2\2\u01d9\u01da\7:\2\2\u01da")
        buf.write("a\3\2\2\2\u01db\u01dc\7\30\2\2\u01dc\u01dd\7:\2\2\u01dd")
        buf.write("c\3\2\2\2\u01de\u01df\7\b\2\2\u01df\u01e0\5h\65\2\u01e0")
        buf.write("\u01e1\7:\2\2\u01e1e\3\2\2\2\u01e2\u01e3\7?\2\2\u01e3")
        buf.write("g\3\2\2\2\u01e4\u01e5\5j\66\2\u01e5\u01e6\5\u0088E\2\u01e6")
        buf.write("\u01e7\5j\66\2\u01e7\u01ea\3\2\2\2\u01e8\u01ea\5j\66\2")
        buf.write("\u01e9\u01e4\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eai\3\2\2")
        buf.write("\2\u01eb\u01ec\5l\67\2\u01ec\u01ed\5\u0086D\2\u01ed\u01ee")
        buf.write("\5l\67\2\u01ee\u01f1\3\2\2\2\u01ef\u01f1\5l\67\2\u01f0")
        buf.write("\u01eb\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1k\3\2\2\2\u01f2")
        buf.write("\u01f3\b\67\1\2\u01f3\u01f4\5n8\2\u01f4\u01fb\3\2\2\2")
        buf.write("\u01f5\u01f6\f\4\2\2\u01f6\u01f7\5\u0084C\2\u01f7\u01f8")
        buf.write("\5n8\2\u01f8\u01fa\3\2\2\2\u01f9\u01f5\3\2\2\2\u01fa\u01fd")
        buf.write("\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("m\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u01ff\b8\1\2\u01ff")
        buf.write("\u0200\5p9\2\u0200\u0207\3\2\2\2\u0201\u0202\f\4\2\2\u0202")
        buf.write("\u0203\5\u0080A\2\u0203\u0204\5p9\2\u0204\u0206\3\2\2")
        buf.write("\2\u0205\u0201\3\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205")
        buf.write("\3\2\2\2\u0207\u0208\3\2\2\2\u0208o\3\2\2\2\u0209\u0207")
        buf.write("\3\2\2\2\u020a\u020b\b9\1\2\u020b\u020c\5r:\2\u020c\u0213")
        buf.write("\3\2\2\2\u020d\u020e\f\4\2\2\u020e\u020f\5\u0082B\2\u020f")
        buf.write("\u0210\5r:\2\u0210\u0212\3\2\2\2\u0211\u020d\3\2\2\2\u0212")
        buf.write("\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2")
        buf.write("\u0214q\3\2\2\2\u0215\u0213\3\2\2\2\u0216\u0217\b:\1\2")
        buf.write("\u0217\u0218\5t;\2\u0218\u021e\3\2\2\2\u0219\u021a\f\4")
        buf.write("\2\2\u021a\u021b\7/\2\2\u021b\u021d\5t;\2\u021c\u0219")
        buf.write("\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021f\3\2\2\2\u021fs\3\2\2\2\u0220\u021e\3\2\2\2\u0221")
        buf.write("\u0222\7\"\2\2\u0222\u0225\5t;\2\u0223\u0225\5v<\2\u0224")
        buf.write("\u0221\3\2\2\2\u0224\u0223\3\2\2\2\u0225u\3\2\2\2\u0226")
        buf.write("\u0227\5\u0080A\2\u0227\u0228\5v<\2\u0228\u022b\3\2\2")
        buf.write("\2\u0229\u022b\5x=\2\u022a\u0226\3\2\2\2\u022a\u0229\3")
        buf.write("\2\2\2\u022bw\3\2\2\2\u022c\u022d\b=\1\2\u022d\u022e\5")
        buf.write("z>\2\u022e\u0233\3\2\2\2\u022f\u0230\f\4\2\2\u0230\u0232")
        buf.write("\5\u008aF\2\u0231\u022f\3\2\2\2\u0232\u0235\3\2\2\2\u0233")
        buf.write("\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234y\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0236\u0237\b>\1\2\u0237\u0238\5|?\2\u0238")
        buf.write("\u023e\3\2\2\2\u0239\u023a\f\4\2\2\u023a\u023b\7\67\2")
        buf.write("\2\u023b\u023d\5|?\2\u023c\u0239\3\2\2\2\u023d\u0240\3")
        buf.write("\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f{")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0241\u0242\7\33\2\2\u0242")
        buf.write("\u0243\5|?\2\u0243\u0244\5\u008eH\2\u0244\u0247\3\2\2")
        buf.write("\2\u0245\u0247\5~@\2\u0246\u0241\3\2\2\2\u0246\u0245\3")
        buf.write("\2\2\2\u0247}\3\2\2\2\u0248\u0249\7\63\2\2\u0249\u024a")
        buf.write("\5h\65\2\u024a\u024b\7\64\2\2\u024b\u0251\3\2\2\2\u024c")
        buf.write("\u0251\5\u0094K\2\u024d\u0251\7?\2\2\u024e\u0251\5\u008c")
        buf.write("G\2\u024f\u0251\7\35\2\2\u0250\u0248\3\2\2\2\u0250\u024c")
        buf.write("\3\2\2\2\u0250\u024d\3\2\2\2\u0250\u024e\3\2\2\2\u0250")
        buf.write("\u024f\3\2\2\2\u0251\177\3\2\2\2\u0252\u0253\t\6\2\2\u0253")
        buf.write("\u0081\3\2\2\2\u0254\u0255\t\7\2\2\u0255\u0083\3\2\2\2")
        buf.write("\u0256\u0257\t\b\2\2\u0257\u0085\3\2\2\2\u0258\u0259\t")
        buf.write("\t\2\2\u0259\u0087\3\2\2\2\u025a\u025b\t\n\2\2\u025b\u0089")
        buf.write("\3\2\2\2\u025c\u025d\7\65\2\2\u025d\u025e\5h\65\2\u025e")
        buf.write("\u025f\7\66\2\2\u025f\u008b\3\2\2\2\u0260\u0261\7?\2\2")
        buf.write("\u0261\u0262\5\u008eH\2\u0262\u008d\3\2\2\2\u0263\u0265")
        buf.write("\7\63\2\2\u0264\u0266\5\u0090I\2\u0265\u0264\3\2\2\2\u0265")
        buf.write("\u0266\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0268\7\64\2")
        buf.write("\2\u0268\u008f\3\2\2\2\u0269\u026e\5h\65\2\u026a\u026b")
        buf.write("\78\2\2\u026b\u026d\5h\65\2\u026c\u026a\3\2\2\2\u026d")
        buf.write("\u0270\3\2\2\2\u026e\u026c\3\2\2\2\u026e\u026f\3\2\2\2")
        buf.write("\u026f\u0091\3\2\2\2\u0270\u026e\3\2\2\2\u0271\u0272\t")
        buf.write("\13\2\2\u0272\u0093\3\2\2\2\u0273\u0278\7<\2\2\u0274\u0278")
        buf.write("\7=\2\2\u0275\u0278\5\u0092J\2\u0276\u0278\7>\2\2\u0277")
        buf.write("\u0273\3\2\2\2\u0277\u0274\3\2\2\2\u0277\u0275\3\2\2\2")
        buf.write("\u0277\u0276\3\2\2\2\u0278\u0095\3\2\2\2\u0279\u027a\7")
        buf.write("\61\2\2\u027a\u027f\5\u0094K\2\u027b\u027c\78\2\2\u027c")
        buf.write("\u027e\5\u0094K\2\u027d\u027b\3\2\2\2\u027e\u0281\3\2")
        buf.write("\2\2\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280\u0282")
        buf.write("\3\2\2\2\u0281\u027f\3\2\2\2\u0282\u0283\7\62\2\2\u0283")
        buf.write("\u0097\3\2\2\28\u009b\u00a3\u00a9\u00b1\u00b5\u00bc\u00c7")
        buf.write("\u00cd\u00d8\u00e2\u00e6\u00f5\u0100\u0106\u010a\u010f")
        buf.write("\u0115\u011b\u0125\u012a\u0132\u013a\u0140\u0159\u0161")
        buf.write("\u0167\u016d\u0175\u017d\u018a\u019a\u01a7\u01af\u01b5")
        buf.write("\u01bc\u01c1\u01c3\u01ce\u01e9\u01f0\u01fb\u0207\u0213")
        buf.write("\u021e\u0224\u022a\u0233\u023e\u0246\u0250\u0265\u026e")
        buf.write("\u0277\u027f")
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
    RULE_paramList = 17
    RULE_params = 18
    RULE_monoParams = 19
    RULE_polyParams = 20
    RULE_paramType = 21
    RULE_classParamType = 22
    RULE_scalarParamType = 23
    RULE_compositeParamType = 24
    RULE_polyParam = 25
    RULE_monoParam = 26
    RULE_returnType = 27
    RULE_stmt = 28
    RULE_constructorStmt = 29
    RULE_blockStmt = 30
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
    RULE_forStmt = 44
    RULE_invokeStmt = 45
    RULE_arrayVar = 46
    RULE_breakStmt = 47
    RULE_continueStmt = 48
    RULE_returnStmt = 49
    RULE_className = 50
    RULE_exp = 51
    RULE_exp1 = 52
    RULE_exp2 = 53
    RULE_exp3 = 54
    RULE_exp4 = 55
    RULE_exp5 = 56
    RULE_exp6 = 57
    RULE_exp7 = 58
    RULE_exp8 = 59
    RULE_exp9 = 60
    RULE_exp10 = 61
    RULE_exp11 = 62
    RULE_adding = 63
    RULE_multiply = 64
    RULE_logical = 65
    RULE_equality = 66
    RULE_relational = 67
    RULE_indexOp = 68
    RULE_methodInvoke = 69
    RULE_listExp = 70
    RULE_arguList = 71
    RULE_bool_literal = 72
    RULE_literal = 73
    RULE_array_literal = 74

    ruleNames =  [ "program", "classDecl", "memDecl", "attributeDecl", "immutableAttrDecl", 
                   "mutableAttrDecl", "immutableAttrAssign", "mutableAttrAssign", 
                   "attributeType", "scalarType", "compositeType", "objectDecl", 
                   "objList", "objInit", "methodDecl", "constructorDecl", 
                   "normalMethodDecl", "paramList", "params", "monoParams", 
                   "polyParams", "paramType", "classParamType", "scalarParamType", 
                   "compositeParamType", "polyParam", "monoParam", "returnType", 
                   "stmt", "constructorStmt", "blockStmt", "varDecl", "objectVars", 
                   "objectVar", "scalarVars", "scalarVar", "arrayVars", 
                   "assignStmt", "lhs", "attrAccess", "instanceName", "objName", 
                   "attrName", "ifStmt", "forStmt", "invokeStmt", "arrayVar", 
                   "breakStmt", "continueStmt", "returnStmt", "className", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "exp9", "exp10", "exp11", "adding", "multiply", 
                   "logical", "equality", "relational", "indexOp", "methodInvoke", 
                   "listExp", "arguList", "bool_literal", "literal", "array_literal" ]

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
            self.state = 151 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 150
                self.classDecl()
                self.state = 153 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 155
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
            self.state = 157
            self.match(BKOOLParser.CLASS)
            self.state = 158
            self.match(BKOOLParser.ID)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 159
                self.match(BKOOLParser.EXTENDS)
                self.state = 160
                self.match(BKOOLParser.ID)


            self.state = 163
            self.match(BKOOLParser.LP)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.VOID) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FINAL) | (1 << BKOOLParser.STATIC) | (1 << BKOOLParser.ID))) != 0):
                self.state = 164
                self.memDecl()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.attributeDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.objectDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
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
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.immutableAttrDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 181
                self.match(BKOOLParser.FINAL)
                pass

            elif la_ == 2:
                self.state = 182
                self.match(BKOOLParser.FINAL)
                self.state = 183
                self.match(BKOOLParser.STATIC)
                pass

            elif la_ == 3:
                self.state = 184
                self.match(BKOOLParser.STATIC)
                self.state = 185
                self.match(BKOOLParser.FINAL)
                pass


            self.state = 188
            self.attributeType()

            self.state = 189
            self.match(BKOOLParser.ID)
            self.state = 190
            self.immutableAttrAssign()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 192
                self.match(BKOOLParser.COMMA)

                self.state = 193
                self.match(BKOOLParser.ID)
                self.state = 194
                self.immutableAttrAssign()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
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
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 202
                self.match(BKOOLParser.STATIC)


            self.state = 205
            self.attributeType()

            self.state = 206
            self.match(BKOOLParser.ID)
            self.state = 207
            self.mutableAttrAssign()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 209
                self.match(BKOOLParser.COMMA)

                self.state = 210
                self.match(BKOOLParser.ID)
                self.state = 211
                self.mutableAttrAssign()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
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
            self.state = 219
            self.match(BKOOLParser.EQUAL_SIGN)
            self.state = 220
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
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 222
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 223
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.compositeType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
            self.state = 230
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
            self.state = 232
            self.scalarType()
            self.state = 233
            self.match(BKOOLParser.LSB)
            self.state = 234
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 235
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
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(BKOOLParser.FINAL)

            elif la_ == 2:
                self.state = 238
                self.match(BKOOLParser.STATIC)

            elif la_ == 3:
                self.state = 239
                self.match(BKOOLParser.FINAL)
                self.state = 240
                self.match(BKOOLParser.STATIC)

            elif la_ == 4:
                self.state = 241
                self.match(BKOOLParser.STATIC)
                self.state = 242
                self.match(BKOOLParser.FINAL)


            self.state = 245
            self.className()
            self.state = 246
            self.objList()
            self.state = 247
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
            self.state = 249
            self.objInit()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 250
                self.match(BKOOLParser.COMMA)
                self.state = 251
                self.objInit()
                self.state = 256
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
            self.state = 257
            self.objName()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EQUAL_SIGN:
                self.state = 258
                self.match(BKOOLParser.EQUAL_SIGN)
                self.state = 259
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
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.constructorDecl()
                pass
            elif token in [BKOOLParser.VOID, BKOOLParser.INT, BKOOLParser.FLOAT, BKOOLParser.STRING, BKOOLParser.BOOLEAN, BKOOLParser.STATIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.normalMethodDecl()
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

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


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
            self.state = 266
            self.match(BKOOLParser.ID)
            self.state = 267
            self.match(BKOOLParser.LB)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 268
                self.paramList()


            self.state = 271
            self.match(BKOOLParser.RB)
            self.state = 272
            self.blockStmt()
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

        def returnType(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnTypeContext,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockStmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockStmtContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def MAIN(self):
            return self.getToken(BKOOLParser.MAIN, 0)

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
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 274
                self.match(BKOOLParser.STATIC)


            self.state = 277
            self.returnType()
            self.state = 278
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.MAIN or _la==BKOOLParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 279
            self.match(BKOOLParser.LB)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.ID))) != 0):
                self.state = 280
                self.paramList()


            self.state = 283
            self.match(BKOOLParser.RB)
            self.state = 284
            self.blockStmt()
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
        self.enterRule(localctx, 34, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.params()
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.S_COLON:
                self.state = 287
                self.match(BKOOLParser.S_COLON)
                self.state = 288
                self.params()
                self.state = 293
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
        self.enterRule(localctx, 36, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 294
                self.monoParams()
                pass

            elif la_ == 2:
                self.state = 295
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
        self.enterRule(localctx, 38, self.RULE_monoParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.paramType()
            self.state = 299
            self.monoParam()
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 300
                self.match(BKOOLParser.COMMA)
                self.state = 301
                self.monoParam()
                self.state = 306
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
        self.enterRule(localctx, 40, self.RULE_polyParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.polyParam()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 308
                self.match(BKOOLParser.COMMA)
                self.state = 309
                self.polyParam()
                self.state = 314
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

        def scalarParamType(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarParamTypeContext,0)


        def compositeParamType(self):
            return self.getTypedRuleContext(BKOOLParser.CompositeParamTypeContext,0)


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
        self.enterRule(localctx, 42, self.RULE_paramType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 315
                self.scalarParamType()
                pass

            elif la_ == 2:
                self.state = 316
                self.compositeParamType()
                pass

            elif la_ == 3:
                self.state = 317
                self.classParamType()
                pass


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
        self.enterRule(localctx, 44, self.RULE_classParamType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.className()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarParamTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributeType(self):
            return self.getTypedRuleContext(BKOOLParser.AttributeTypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_scalarParamType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarParamType" ):
                return visitor.visitScalarParamType(self)
            else:
                return visitor.visitChildren(self)




    def scalarParamType(self):

        localctx = BKOOLParser.ScalarParamTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_scalarParamType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.attributeType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeParamTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarParamType(self):
            return self.getTypedRuleContext(BKOOLParser.ScalarParamTypeContext,0)


        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(BKOOLParser.INTEGER_LITERAL, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_compositeParamType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeParamType" ):
                return visitor.visitCompositeParamType(self)
            else:
                return visitor.visitChildren(self)




    def compositeParamType(self):

        localctx = BKOOLParser.CompositeParamTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_compositeParamType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.scalarParamType()
            self.state = 325
            self.match(BKOOLParser.LSB)
            self.state = 326
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 327
            self.match(BKOOLParser.RSB)
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
        self.enterRule(localctx, 50, self.RULE_polyParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.paramType()
            self.state = 330
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
        self.enterRule(localctx, 52, self.RULE_monoParam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
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

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

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
        self.enterRule(localctx, 54, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.VOID) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.BOOLEAN))) != 0)):
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
        self.enterRule(localctx, 56, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 336
                self.assignStmt()
                pass

            elif la_ == 2:
                self.state = 337
                self.ifStmt()
                pass

            elif la_ == 3:
                self.state = 338
                self.forStmt()
                pass

            elif la_ == 4:
                self.state = 339
                self.breakStmt()
                pass

            elif la_ == 5:
                self.state = 340
                self.continueStmt()
                pass

            elif la_ == 6:
                self.state = 341
                self.invokeStmt()
                pass

            elif la_ == 7:
                self.state = 342
                self.returnStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorStmtContext(ParserRuleContext):
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
            return BKOOLParser.RULE_constructorStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructorStmt" ):
                return visitor.visitConstructorStmt(self)
            else:
                return visitor.visitChildren(self)




    def constructorStmt(self):

        localctx = BKOOLParser.ConstructorStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_constructorStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 345
                self.assignStmt()
                pass

            elif la_ == 2:
                self.state = 346
                self.ifStmt()
                pass

            elif la_ == 3:
                self.state = 347
                self.forStmt()
                pass

            elif la_ == 4:
                self.state = 348
                self.breakStmt()
                pass

            elif la_ == 5:
                self.state = 349
                self.continueStmt()
                pass

            elif la_ == 6:
                self.state = 350
                self.invokeStmt()
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
        self.enterRule(localctx, 60, self.RULE_blockStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BKOOLParser.LP)
            self.state = 357
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 354
                    self.varDecl() 
                self.state = 359
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 371
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 368
                self.scalarVars()
                pass

            elif la_ == 2:
                self.state = 369
                self.arrayVars()
                pass

            elif la_ == 3:
                self.state = 370
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
            self.state = 373
            self.className()
            self.state = 374
            self.objectVar()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 375
                self.match(BKOOLParser.COMMA)
                self.state = 376
                self.objectVar()
                self.state = 381
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 382
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
            self.state = 384
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
            self.state = 386
            self.attributeType()
            self.state = 387
            self.scalarVar()
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 388
                self.match(BKOOLParser.COMMA)
                self.state = 389
                self.scalarVar()
                self.state = 394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 395
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
            self.state = 397
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
            self.state = 399
            self.attributeType()
            self.state = 400
            self.match(BKOOLParser.LSB)
            self.state = 401
            self.match(BKOOLParser.INTEGER_LITERAL)
            self.state = 402
            self.match(BKOOLParser.RSB)
            self.state = 403
            self.scalarVar()
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 404
                self.match(BKOOLParser.COMMA)
                self.state = 405
                self.scalarVar()
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
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
            self.state = 413
            self.lhs()
            self.state = 414
            self.match(BKOOLParser.ASSIGN)
            self.state = 415
            self.exp()
            self.state = 416
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
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 418
                self.arrayVar()
                pass

            elif la_ == 2:
                self.state = 419
                self.scalarVar()
                pass

            elif la_ == 3:
                self.state = 420
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
            self.state = 423
            self.instanceName()
            self.state = 424
            self.match(BKOOLParser.DOT)
            self.state = 425
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
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.THIS]:
                self.state = 427
                self.match(BKOOLParser.THIS)
                pass
            elif token in [BKOOLParser.ID]:
                self.state = 428
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
            self.state = 431
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
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 433
                self.scalarVar()
                pass

            elif la_ == 2:
                self.state = 434
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
            self.state = 437
            self.match(BKOOLParser.IF)
            self.state = 438
            self.exp()
            self.state = 439
            self.match(BKOOLParser.THEN)
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                self.state = 440
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 441
                self.blockStmt()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 449
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 444
                self.match(BKOOLParser.ELSE)
                self.state = 447
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                    self.state = 445
                    self.stmt()
                    pass
                elif token in [BKOOLParser.LP]:
                    self.state = 446
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
        self.enterRule(localctx, 88, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(BKOOLParser.FOR)
            self.state = 452
            self.scalarVar()
            self.state = 453
            self.match(BKOOLParser.ASSIGN)
            self.state = 454
            self.exp()
            self.state = 455
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 456
            self.exp()
            self.state = 457
            self.match(BKOOLParser.DO)
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.RETURN, BKOOLParser.IF, BKOOLParser.FOR, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.THIS, BKOOLParser.ID]:
                self.state = 458
                self.stmt()
                pass
            elif token in [BKOOLParser.LP]:
                self.state = 459
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
        self.enterRule(localctx, 90, self.RULE_invokeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.instanceName()
            self.state = 463
            self.match(BKOOLParser.DOT)
            self.state = 464
            self.methodInvoke()
            self.state = 465
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
        self.enterRule(localctx, 92, self.RULE_arrayVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(BKOOLParser.ID)
            self.state = 468
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
        self.enterRule(localctx, 94, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(BKOOLParser.BREAK)
            self.state = 471
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
        self.enterRule(localctx, 96, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self.match(BKOOLParser.CONTINUE)
            self.state = 474
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
        self.enterRule(localctx, 98, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(BKOOLParser.RETURN)
            self.state = 477
            self.exp()
            self.state = 478
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
        self.enterRule(localctx, 100, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
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
        self.enterRule(localctx, 102, self.RULE_exp)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 482
                self.exp1()
                self.state = 483
                self.relational()
                self.state = 484
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
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
        self.enterRule(localctx, 104, self.RULE_exp1)
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.exp2(0)
                self.state = 490
                self.equality()
                self.state = 491
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 505
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 499
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 500
                    self.logical()
                    self.state = 501
                    self.exp3(0) 
                self.state = 507
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 517
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 511
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 512
                    self.adding()
                    self.state = 513
                    self.exp4(0) 
                self.state = 519
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_exp4, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 529
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 523
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 524
                    self.multiply()
                    self.state = 525
                    self.exp5(0) 
                self.state = 531
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 540
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 535
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 536
                    self.match(BKOOLParser.CONCATENATE)
                    self.state = 537
                    self.exp6() 
                self.state = 542
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 114, self.RULE_exp6)
        try:
            self.state = 546
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.match(BKOOLParser.NOT)
                self.state = 544
                self.exp6()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.PLUS, BKOOLParser.MINUS, BKOOLParser.LB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
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
        self.enterRule(localctx, 116, self.RULE_exp7)
        try:
            self.state = 552
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.PLUS, BKOOLParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.adding()
                self.state = 549
                self.exp7()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 551
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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 555
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 557
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 558
                    self.indexOp() 
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

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
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 565
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 572
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 567
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 568
                    self.match(BKOOLParser.DOT)
                    self.state = 569
                    self.exp10() 
                self.state = 574
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        self.enterRule(localctx, 122, self.RULE_exp10)
        try:
            self.state = 580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 575
                self.match(BKOOLParser.NEW)
                self.state = 576
                self.exp10()
                self.state = 577
                self.listExp()
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE, BKOOLParser.THIS, BKOOLParser.LB, BKOOLParser.INTEGER_LITERAL, BKOOLParser.FLOAT_LITERAL, BKOOLParser.STRING_LITERAL, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
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
        self.enterRule(localctx, 124, self.RULE_exp11)
        try:
            self.state = 590
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.match(BKOOLParser.LB)
                self.state = 583
                self.exp()
                self.state = 584
                self.match(BKOOLParser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 587
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 588
                self.methodInvoke()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 589
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
        self.enterRule(localctx, 126, self.RULE_adding)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
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
        self.enterRule(localctx, 128, self.RULE_multiply)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
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
        self.enterRule(localctx, 130, self.RULE_logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
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
        self.enterRule(localctx, 132, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 598
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
        self.enterRule(localctx, 134, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
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
        self.enterRule(localctx, 136, self.RULE_indexOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(BKOOLParser.LSB)
            self.state = 603
            self.exp()
            self.state = 604
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
        self.enterRule(localctx, 138, self.RULE_methodInvoke)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(BKOOLParser.ID)
            self.state = 607
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
        self.enterRule(localctx, 140, self.RULE_listExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.match(BKOOLParser.LB)
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.TRUE) | (1 << BKOOLParser.FALSE) | (1 << BKOOLParser.NEW) | (1 << BKOOLParser.THIS) | (1 << BKOOLParser.NOT) | (1 << BKOOLParser.PLUS) | (1 << BKOOLParser.MINUS) | (1 << BKOOLParser.LB) | (1 << BKOOLParser.INTEGER_LITERAL) | (1 << BKOOLParser.FLOAT_LITERAL) | (1 << BKOOLParser.STRING_LITERAL) | (1 << BKOOLParser.ID))) != 0):
                self.state = 610
                self.arguList()


            self.state = 613
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
        self.enterRule(localctx, 142, self.RULE_arguList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.exp()
            self.state = 620
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 616
                self.match(BKOOLParser.COMMA)
                self.state = 617
                self.exp()
                self.state = 622
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
        self.enterRule(localctx, 144, self.RULE_bool_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 623
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
        self.enterRule(localctx, 146, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTEGER_LITERAL]:
                self.state = 625
                self.match(BKOOLParser.INTEGER_LITERAL)
                pass
            elif token in [BKOOLParser.FLOAT_LITERAL]:
                self.state = 626
                self.match(BKOOLParser.FLOAT_LITERAL)
                pass
            elif token in [BKOOLParser.TRUE, BKOOLParser.FALSE]:
                self.state = 627
                self.bool_literal()
                pass
            elif token in [BKOOLParser.STRING_LITERAL]:
                self.state = 628
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
        self.enterRule(localctx, 148, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 631
            self.match(BKOOLParser.LP)
            self.state = 632
            self.literal()
            self.state = 637
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 633
                self.match(BKOOLParser.COMMA)
                self.state = 634
                self.literal()
                self.state = 639
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 640
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
        self._predicates[53] = self.exp2_sempred
        self._predicates[54] = self.exp3_sempred
        self._predicates[55] = self.exp4_sempred
        self._predicates[56] = self.exp5_sempred
        self._predicates[59] = self.exp8_sempred
        self._predicates[60] = self.exp9_sempred
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
         




