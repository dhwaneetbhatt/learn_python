from pattern_matching.glob_base import Match, Null
from pattern_matching.glob_any import Any
from pattern_matching.glob_lit import Lit
from pattern_matching.glob_either import Either
from pattern_matching.glob_not import Not
from pattern_matching.glob_charset import Charset

class Parser:
    def parse(self, tokens: list[list[str]]) -> Match:
        if not tokens:
            return Null()

        front, back = tokens[0], tokens[1:]
        if front[0] == "Any":
            handler = self._parse_Any
        elif front[0] == "EitherStart":
            handler = self._parse_EitherStart
        elif front[0] == "CharsetStart":
            handler = self._parse_CharsetStart
        elif front[0] == "Lit":
            handler = self._parse_Lit
        else:
            raise NotImplementedError(f"Unexpected front token {front[0]}")

        return handler(front[1:], back)

    def _parse_Any(self, rest: list[str], back: list[list[str]]) -> Any:
        return Any(self.parse(back))

    def _parse_Lit(self, rest: list[str], back: list[list[str]]) -> Lit:
        return Lit(rest[0], self.parse(back))

    def _parse_EitherStart(self, rest: list[str], back: list[list[str]]) -> Either:
        children = list[Match]()
        while back and (back[0][0] == "Lit"):
            children.append(Lit(back[0][1]))
            back = back[1:]

        if not children:
            raise ValueError("empty Either")

        if back[0][0] != "EitherEnd":
            raise ValueError("badly formatted Either")

        return Either(children, self.parse(back[1:]))

    def _parse_CharsetStart(self, rest: list[str], back: list[list[str]]) -> Charset:
        if back[0][0] == "Charset":
            if back[1][0] != "CharsetEnd":
                raise ValueError("badly formatted Charset")

            return Charset(back[0][1], self.parse(back[2:]))
        elif back[0][0] == "Not":
            return Not(self._parse_CharsetStart(rest, back[1:]))
