import re
import enum
from graphviz import Digraph

class TokenType(enum.Enum):
    WHITESPACE = 1
    COMMENT = 2
    IDENTIFIER = 3
    KEYWORD = 4
    STRING = 5
    NUMBER = 6
    OPERATOR = 7
    BRACE_OPEN = 8
    BRACE_CLOSE = 9
    PAREN_OPEN = 10
    PAREN_CLOSE = 11
    SEMICOLON = 12
    COMMA = 13
    COLON = 14

def lexer(code):
    tokens = []
    while code:
        code = code.strip()
        match_found = False
        for token_type, token_regex in TOKENS:
            regex = re.compile(token_regex)
            match = regex.match(code)
            if match:
                value = match.group(0).strip()
                if token_type != TokenType.WHITESPACE and token_type != TokenType.COMMENT:
                    tokens.append((token_type, value))
                code = code[match.end():]
                match_found = True
                break
        if not match_found:
            raise SyntaxError(f'Unknown code: {code}')
    return tokens

class ASTNode:
    def __init__(self, type, children=None, value=None):
        self.type = type
        self.value = value
        self.children = children if children is not None else []

    def __repr__(self):
        type_name = self.type.name if isinstance(self.type, enum.Enum) else self.type
        return f"{type_name}({self.value}, {self.children})"

def parse(tokens):
    root = ASTNode(TokenType.KEYWORD, value="ROOT")
    current_node = root

    i = 0
    while i < len(tokens):
        token_type, value = tokens[i]
        if token_type == TokenType.KEYWORD or token_type == TokenType.IDENTIFIER:
            current_node = ASTNode(token_type, value=value)
            root.children.append(current_node)
        elif token_type == TokenType.STRING or token_type == TokenType.NUMBER:
            value_node = ASTNode(token_type, value=value)
            current_node.children.append(value_node)
        i += 1

    return root

def add_nodes_edges(tree, graph=None):
    if graph is None:
        graph = Digraph()
        graph.node(name=str(id(tree)), label=f'{tree.type.name}({tree.value})')

    for child in tree.children:
        child_label = f'{child.type.name}({child.value})' if child.value else child.type.name
        graph.node(name=str(id(child)), label=child_label)
        graph.edge(str(id(tree)), str(id(child)))
        graph = add_nodes_edges(child, graph)

    return graph

TOKENS = [
    (TokenType.WHITESPACE, r'\s+'),
    (TokenType.COMMENT, r'#[^\n]*'),
    (TokenType.KEYWORD, r'\b(?:if|else|elif|for|while|def|class|return|import|from|as|True|False|None)\b'),
    (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
    (TokenType.STRING, r'\'(?:\\.|[^\'])*\'|"(?:\\.|[^"])*"'),
    (TokenType.NUMBER, r'\b\d+(?:\.\d+)?\b'),
    (TokenType.OPERATOR, r'\+|-|\*|/|==|!=|<=|>=|<|>'),
    (TokenType.COLON, r':'),
    (TokenType.BRACE_OPEN, r'\{'),
    (TokenType.BRACE_CLOSE, r'\}'),
    (TokenType.PAREN_OPEN, r'\('),
    (TokenType.PAREN_CLOSE, r'\)'),
    (TokenType.SEMICOLON, r';'),
    (TokenType.COMMA, r','),
]


source_code = """
# This is a Python code snippet
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""

tokens = lexer(source_code)
ast = parse(tokens)
graph = add_nodes_edges(ast)
graph.render('ast_python', view=True)
