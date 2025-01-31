import unittest

from rdfscript.parser import Parser

from rdfscript.core import Value


class ParserLiteralTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def tearDown(self):
        None

    def test_parser_literal_boolean(self):
        forms = self.parser.parse('true false')
        self.assertEqual(forms, [Value(True, None),
                                 Value(False, None)])

    def test_parser_literal_double(self):
        forms = self.parser.parse('0.12345')
        self.assertEqual(forms, [Value(0.12345, None)])

    def test_parser_literal_integer(self):
        forms = self.parser.parse('12345')
        self.assertEqual(forms, [Value(12345, None)])

    def test_parser_literal_negative_integer(self):
        forms = self.parser.parse('-12345')
        self.assertEqual(forms, [Value(-12345, None)])

    def test_parser_literal_string(self):
        script = '"string with whitespace"'
        forms = self.parser.parse(script)
        self.assertEqual(forms, [Value("string with whitespace", None)])
