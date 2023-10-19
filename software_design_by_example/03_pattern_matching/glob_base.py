from __future__ import annotations

class Match:
    def __init__(self, rest: Match):
        self.rest = rest if rest is not None else Null()

    def __eq__(self, other: Match):
        return (
            other is not None
            and self.__class__ == other.__class__
            and self.rest == other.rest
        )

    def match(self, text: str) -> bool:
        result = self._match(text, 0)
        return result == len(text)

    def _match(self, text: str, start: int) -> int | None:
        raise NotImplementedError

class Null(Match):
    def __init__(self):
        self.rest = None

    def _match(self, text: str, start=0) -> int:
        return start
