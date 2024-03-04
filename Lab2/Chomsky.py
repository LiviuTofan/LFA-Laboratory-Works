class Grammar:
    def __init__(self, productions):
        self.P = productions

    def classify_grammar(self):
        if self.is_regular():
            return "Type 3 (Regular)"
        elif self.is_context_free():
            return "Type 2 (Context-Free)"
        elif self.is_context_sensitive():
            return "Type 1 (Context-Sensitive)"
        else:
            return "Type 0 (Unrestricted)"

    def is_regular(self):
        for lhs, productions in self.P.items():
            if len(lhs) > 1:
                return False
            for production in productions:
                if len(production) == 1 and production.islower():  # Terminal symbol
                    continue
                elif len(production) == 2 and production[0].islower() and production[1].isupper():
                    continue
                elif len(production) == 2 and production[1].islower() and production[0].isupper():
                    continue
                else:
                    return False
        return True

    def is_context_free(self):
        for lhs, productions in self.P.items():
            if len(lhs) != 1 or not lhs.isupper():
                return False
        return True

    def is_context_sensitive(self):
        s_on_right = False
        for left, productions in self.P.items():
            if 'S' in left:
                s_on_right = True
            for production in productions:
                # Check for S -> epsilon
                if left == 'S' and production == '' and not s_on_right:
                    continue
                if len(left) > len(production):
                    return False
        return True
