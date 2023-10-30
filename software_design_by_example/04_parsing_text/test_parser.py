import unittest
from parser import Parser
from pattern_matching.glob_lit import Lit
from pattern_matching.glob_either import Either
from pattern_matching.glob_not import Not
from pattern_matching.glob_charset import Charset

class TestParser(unittest.TestCase):
    def test_parse_either_two_lit(self):
        self.assertEqual(
            Parser().parse([
                ["EitherStart"],
                ["Lit", "abc"],
                ["Lit", "def"],
                ["EitherEnd"]
            ]),
            Either([Lit("abc"), Lit("def")]),
        )

    def test_parse_charset(self):
        self.assertEqual(
            Parser().parse([
                ["CharsetStart"],
                ["Charset", "abc"],
                ["CharsetEnd"]
            ]),
            Charset("abc"),
        )

    def test_parse_not_charset(self):
        self.assertEqual(
            Parser().parse([
                ["CharsetStart"],
                ["Not"],
                ["Charset", "abc"],
                ["CharsetEnd"]
            ]),
            Not(Charset("abc")),
        )


if __name__ == "__main__":
    unittest.main()
