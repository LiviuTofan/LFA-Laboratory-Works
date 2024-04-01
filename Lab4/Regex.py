import random

def choose(options: list[str] = None):
    symbol = random.choice(options)
    print(f'Choose {symbol}')
    return symbol


def plus(symbol: str):
    init_symbol = symbol
    result = ""
    last_i = 1
    for i in range(1, random.randint(1, 5)):
        result += symbol
        last_i = i
    print(f'Repeat {init_symbol} {last_i} times')
    return result


def star(symbol: str):
    init_symbol = symbol
    result = ""
    repetitions = random.randint(0, 5)
    for i in range(0, repetitions):
        result += symbol
    print(f'Repeat {init_symbol} {repetitions} times')
    return result


def power(symbol: str, n: int):
    repeated_symbol = ""
    for i in range(0, n-1):
        repeated_symbol += symbol
    print(f'Repeat {symbol} {n} times')
    return repeated_symbol


def const(symbol: str):
    print(f'Constant {symbol}')
    return symbol

def find_chooses(regex):
    stack = []
    for i, char in enumerate(regex):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                matches = []
                start_index = stack.pop()
                substring = regex[start_index + 1:i]
                index = len(substring) + 2
                substring = substring.replace("|", "")
                matches.extend(substring)
    return matches, index

def find_operators(regex):
    num = ""
    result = ""
    i = 0
    while i < len(regex):
        char = regex[i]
        # Find chooses
        if char == "(":
            result += const(num)
            matches, index = find_chooses(regex[i:])
            result += choose(matches)
            i += index  # Increment index to skip over processed characters
            num = ""
            continue
        # Check for constants
        elif char.isalnum():
            num += char
        # Perform * operation
        elif char == "*":
            if num != "":
                result += star(num)
            else:
                result += star(result[-1])
            num = ""
        # Perform + operation
        elif char == "+":
            if num != "":
                result += plus(num)
            else:
                result += plus(result[-1])
            num = ""
        # Perform power operation
        elif char == "^":
            if num != "":
                result += power(num, int(regex[i+1]))
            else:
                result += power(result[-1], int(regex[i + 1]))
            i += 1
            num = ""

        i += 1  # Increment index to move to the next character
    # Perform remaining operations if num is not empty
    if num:
        result += const(num)

    return result

regexes = ["(S|T)(U|V)W*Y+24", "L(M|N)O^3P*Q(2|3)", "L(M|N)O^3P*Q(2|3)"]
for regex in regexes:
    print("------------")
    print("Regex: ", regex)
    print("------------")
    result = find_operators(regex)
    print(result)