import unittest
from tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def test_tok_empty_string(self):
        self.assertEqual(Tokenizer().tok(""), [])

    def test_tok_any_either(self):
        self.assertEqual(
            Tokenizer().tok("*{abc,def}"),
            [
                ["Any"],
                ["EitherStart"],
                ["Lit", "abc"],
                ["Lit", "def"],
                ["EitherEnd"],
            ],
        )

    def test_tok_lit_charset(self):
        self.assertEqual(
            Tokenizer().tok("abc[def]"),
            [
                ["Lit", "abc"],
                ["CharsetStart"],
                ["Charset", "def"],
                ["CharsetEnd"],
            ],
        )

    def test_tok_not(self):
        self.assertEqual(
            Tokenizer().tok("[!def]"),
            [
                ["CharsetStart"],
                ["Not"],
                ["Charset", "def"],
                ["CharsetEnd"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
