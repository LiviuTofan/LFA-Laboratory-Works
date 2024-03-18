import re

TOKEN_PATTERNS = [
    ('DECIMAL', r'\d+\.\d+'),
    ('INTEGER', r'\d+'),
    ('STRING', r'"[^"]*"|\'[^\']*\''),
    ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),
    ('OPERATOR', r'[\+\-\*/=<>!]=?|&&|\|\|'),
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),
    ('BRACKET', r'[\{\}\(\)\[\]]'),
    ('PUNCTUATION', r'[;:,\.]'),
    ('WHITESPACE', r'\s+'),
    ('UNKNOWN', r'.')
]


class Tokenizer:
    def __init__(self, code_text):
        self.code_text = code_text
        self.tokens = []

    def tokenize(self):
        while self.code_text:
            for token_name, pattern in TOKEN_PATTERNS:
                regex = re.compile(pattern)
                match = regex.match(self.code_text)
                if match:
                    value = match.group(0)
                    if token_name != 'WHITESPACE' and token_name != 'COMMENT':
                        self.tokens.append((token_name, value))
                    self.code_text = self.code_text[len(value):]
                    break
            else:
                raise Exception('TokenizerError: Unknown token')

        return self.tokens


source_code = """
// This is a Python script
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_prev = 0
        fib_curr = 1
        for _ in range(2, n):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

print("Fibonacci sequence:")
for i in range(1, 11):
    print(fibonacci(i), end=" ")
"""

tokenizer = Tokenizer(source_code)
tokenized_result = tokenizer.tokenize()
for result in tokenized_result:
    print(result)
