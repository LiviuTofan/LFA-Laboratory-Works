from Grammar import Grammar

class FiniteAutomaton:
    def __init__(self, grammar: Grammar, _delta: dict) -> None:
        self.Q = grammar.nonterminals + ["X"]
        self.Alphabet = grammar.terminals
        self.q0 = grammar.start
        self.delta = _delta
        self.F = ["X"]

    @classmethod
    def grammar_to_DFA(cls, grammar: Grammar) -> 'FiniteAutomaton':
        delta = {}

        for nonterminal in grammar.language:
            for production in grammar.language[nonterminal]:
                if len(production) > 1:
                    transition = production[0]
                    result_state = production[1]
                    delta.setdefault(nonterminal, {})[transition] = result_state
                else:
                    transition = production
                    result_state = "X"
                    delta.setdefault(nonterminal, {})[transition] = result_state

        return cls(grammar, delta)

    def word_belongs_to_language(self, string: str) -> bool:
        state = self.q0
        for char in string:
            if char not in self.Alphabet:
                return False
            if char in self.delta[state]:
                state = self.delta[state][char]
            else:
                return False
        return state in self.F
