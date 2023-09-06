from glob_base import Match

class Lit(Match):
    def __init__(self, chars: str, rest: Match = None):
        super().__init__(rest)
        self.chars = chars

    def _match(self, text: str, start=0) -> int | None:
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)
