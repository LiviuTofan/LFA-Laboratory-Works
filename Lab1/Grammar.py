import random

class Grammar:
    def __init__(self, _VN: list, _VT: list, _L: dict, _S: str) -> None:
        self.nonterminals = _VN
        self.terminals = _VT
        self.language = _L
        self.start = _S

    def generate_string(self, word=None) -> str:
        current_word = self.start if word is None else word
        while not self.terminal_word(current_word):
            for char in current_word:
                if not self.terminal_char(char):
                    production = self.__replace(self.language[char])
                    current_word = current_word.replace(char, production, 1)  # Replace only the first occurrence
        return current_word

    def terminal_word(self, word: str) -> bool:
        # Check if all char from word are terminals
        return all(char in self.terminals for char in word)

    def terminal_char(self, char: str) -> bool:
        # Check if char is terminal
        return char in self.terminals

    def __replace(self, value: list) -> str:
        # Choose random from values of dictionary of given char
        return random.choice(value)

    def generate_words(self, num_strings=5) -> list:
        ans = []
        while len(ans) < num_strings:
            word = self.generate_string()
            if word not in ans:
                ans.append(word)
        return ans
