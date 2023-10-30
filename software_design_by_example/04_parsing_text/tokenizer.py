import string

CHARS = set(string.ascii_letters + string.digits)

class Tokenizer:
    def __init__(self) -> None:
        self._setup()

    def _setup(self) -> None:
        self.result = []
        self.current = ""

    def _add(self, thing: str) -> None:
        if thing == "CharsetEnd":
            self.result.append(["Charset", self.current])
            self.current = ""

        if len(self.current) > 0:
            self.result.append(["Lit", self.current])
            self.current = ""

        if thing is not None:
            self.result.append([thing])

    def tok(self, text: str) -> list[list[str]]:
        self._setup()
        for ch in text:
            if ch == "*":
                self._add("Any")
            elif ch == "{":
                self._add("EitherStart")
            elif ch == ",":
                self._add(None)
            elif ch == "}":
                self._add("EitherEnd")
            elif ch == "[":
                self._add("CharsetStart")
            elif ch == "]":
                self._add("CharsetEnd")
            elif ch == "!":
                self._add("Not")
            elif ch in CHARS:
                self.current += ch
            else:
                raise NotImplementedError(f"Unexpected character {ch}")
        self._add(None)
        return self.result
