from glob_base import Match

class Either(Match):
    def __init__(self, options, rest=None):
        super().__init__(rest)
        self.options = options

    def _match(self, text, start=0):
        for option in self.options:
            end = option._match(text, start)
            if end is not None:
                end = self.rest._match(text, end)
                if end == len(text):
                    return end
        return None
