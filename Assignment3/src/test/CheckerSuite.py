import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = "class a extends b {}"
        expect = "Undeclared Class: b"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_2(self):
        input = "class a {}"
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))
