import unittest
from ah_lex import lexer


class TestAHLex(unittest.TestCase):
    def test_lexer_1(self):
        input_str = "red, blue trust white;"
        lexer.input(input_str)
        output = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.append(tok)
        self.assertEqual(len(output), 6)
        self.assertEqual(output[0].type, "MEMBER")
        self.assertEqual(output[0].value, "red")
        self.assertEqual(output[1].type, "COMMA")
        self.assertEqual(output[1].value, ",")
        self.assertEqual(output[2].type, "MEMBER")
        self.assertEqual(output[2].value, "blue")
        self.assertEqual(output[3].type, "TRUST")
        self.assertEqual(output[3].value, "trust")
        self.assertEqual(output[4].type, "MEMBER")
        self.assertEqual(output[4].value, "white")
        self.assertEqual(output[5].type, "SEMI")
        self.assertEqual(output[5].value, ";")

    def test_lexer_2(self):
        input_str = "/doubt"
        lexer.input(input_str)
        output = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.append(tok)
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].type, "DOUBT")
        self.assertEqual(output[0].value, "doubt")
