from glob_base import Match

class Charset(Match):
    def __init__(self, set: str, rest: Match = None):
        super().__init__(rest)
        self.set = set

    def _match(self, text: str, start=0) -> int | None:
        if text[start:start+1] not in self.set:
            return None
        return self.rest._match(text, start+1)
