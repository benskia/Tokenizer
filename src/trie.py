class Trie:

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "\0"

    def __repr__(self) -> str:
        def list_words_r(trie: dict) -> list[str]:
            words = []
            for k, v in trie.items():
                if k != self.end_symbol:
                    pass
            return words

        return ""

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
                current = current[letter]
        if self.end_symbol not in current:
            current[self.end_symbol] = 1
        else:
            current[self.end_symbol] += 1
