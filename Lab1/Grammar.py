import random
from Automaton import FiniteAutomaton

class Grammar:
    def __init__(self, _VN: list, _VT: list, _P: dict) -> None:
        self.nonterminals = _VN
        self.terminals = _VT
        self.productions = _P

    def generate_string(self, word="S") -> str:
        while not self.word_is_terminal(word):
            for char in word:
                if not self.char_is_terminal(char):
                    production = self.__pick_replacement(
                        self.productions[char])
                    word = word.replace(char, production, 1)  # Replace only the first occurrence
        return word

    def word_is_terminal(self, word: str) -> bool:
        return all(char in self.terminals for char in word)

    def char_is_terminal(self, char: str) -> bool:
        return char in self.terminals

    def __pick_replacement(self, productions: list) -> str:
        return random.choice(productions)

    def generate_strings(self, num_strings=5) -> list:
        ans = []
        while len(ans) < num_strings:
            word = self.generate_string()
            if word not in ans:
                ans.append(word)
        return ans

    def to_finite_automaton(self) -> FiniteAutomaton:
        Q = self.nonterminals + ["X"]  # Concatenate nonterminals with ["X"]
        Sigma = self.terminals
        q0 = "S"
        F = ["X"]
        delta = {}

        for terminal in self.productions:
            for production in self.productions[terminal]:
                if len(production) > 1:
                    transition = production[0]
                    result_state = production[1]
                    delta.setdefault(terminal, {})[transition] = result_state
                else:
                    transition = production
                    result_state = "X"
                    delta.setdefault(terminal, {})[transition] = result_state

        return FiniteAutomaton(Q, Sigma, q0, F, delta)
