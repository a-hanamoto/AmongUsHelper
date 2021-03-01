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
        self.assertEquals(len(output), 6)
        self.assertEquals(output[0].type, "MEMBER")
        self.assertEquals(output[0].value, "red")
        self.assertEquals(output[1].type, "COMMA")
        self.assertEquals(output[1].value, ",")
        self.assertEquals(output[2].type, "MEMBER")
        self.assertEquals(output[2].value, "blue")
        self.assertEquals(output[3].type, "TRUST")
        self.assertEquals(output[3].value, "trust")
        self.assertEquals(output[4].type, "MEMBER")
        self.assertEquals(output[4].value, "white")
        self.assertEquals(output[5].type, "SEMI")
        self.assertEquals(output[5].value, ";")

    def test_lexer_2(self):
        input_str = "/doubt"
        lexer.input(input_str)
        output = []
        while True:
            tok = lexer.token()
            if not tok:
                break
            output.append(tok)
        self.assertEquals(len(output), 1)
        self.assertEquals(output[0].type, "DOUBT")
        self.assertEquals(output[0].value, "doubt")
