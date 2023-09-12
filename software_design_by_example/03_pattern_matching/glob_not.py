from glob_base import Match

class Not(Match):
    def __init__(self, matcher: Match):
        super().__init__(None)
        self.matcher = matcher

    def _match(self, text: str, start=0) -> int | None:
        end = self.matcher._match(text, start)
        if end is not None:
            return None
        return end
