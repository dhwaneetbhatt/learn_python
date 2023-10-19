from pattern_matching.glob_base import Match

class Any(Match):
    def __init__(self, rest: Match = None):
        super().__init__(rest)

    def _match(self, text: str, start=0) -> int | None:
        for i in range(start, len(text) + 1):
            end = self.rest._match(text, i)
            if end == len(text):
                return end
        return None
