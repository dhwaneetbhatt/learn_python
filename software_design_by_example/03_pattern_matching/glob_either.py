from pattern_matching.glob_base import Match

class Either(Match):
    def __init__(self, options: list[Match], rest: Match = None):
        super().__init__(rest)
        self.options = options

    def _match(self, text: str, start=0) -> int | None:
        for option in self.options:
            end = option._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
