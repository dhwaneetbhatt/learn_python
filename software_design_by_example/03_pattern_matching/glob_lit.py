from pattern_matching.glob_base import Match

class Lit(Match):
    def __init__(self, chars: str, rest: Match = None):
        super().__init__(rest)
        self.chars = chars

    def __eq__(self, other: Match):
        return super().__eq__(other) and self.chars == other.chars

    def _match(self, text: str, start=0) -> int | None:
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)
