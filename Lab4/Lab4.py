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
    for i in range(0, n):
        repeated_symbol += symbol
    print(f'Repeat {symbol} {n} times')
    return repeated_symbol


def const(symbol: str):
    print(f'Constant {symbol}')
    return symbol


def first_regex():
    "(S|T)(U|V)W*Y+24"
    result = ""
    result += choose(["S", "T"])
    result += choose(["U", "V"])
    result += star("W")
    result += plus("Y")
    result += "24"
    return result


def second_regex():
    "L(M|N)O^3P*Q(2|3)"
    result = ""
    result += const("L")
    result += choose(["M", "N"])
    result += power("O", 3)
    result += star("P")
    result += const("Q")
    result += choose(["2", "3"])
    return result


def third_regex():
    "R*S(T|U|V)W(X|Y|X)^2"
    result = ""
    result += star("R")
    result += const("S")
    result += star(choose(["T", "U", "V"]))
    result += const("W")
    result += power(choose(["X", "Y", "Z"]), 2)
    return result


print("------------")
print("First regex")
print("------------")
print("Generated String:", first_regex())
print("------------")
print("Second regex")
print("------------")
print("Generated String:", second_regex())
print("------------")
print("Third regex")
print("------------")
print("Generated String:", third_regex())