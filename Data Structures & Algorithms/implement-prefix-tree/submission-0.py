class PrefixTree:

    def __init__(self):
        self.seen = set()

    def insert(self, word: str) -> None:
        self.seen.add(word)

    def search(self, word: str) -> bool:
        if word in self.seen:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.seen:
            if prefix in word:
                return True
        return False
        