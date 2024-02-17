from Grammar import Grammar
from Automaton import FiniteAutomaton

language = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}

# Create an object of the Grammar class
grammar_instance = Grammar(['S', 'A', 'B'], ['a', 'b', 'c', 'd'], language)

# Point A, B: Generate 5 valid strings starting with S
generated_strings = grammar_instance.generate_strings()

print("Generated Strings:")
for word, generated_string in enumerate(generated_strings, start=1):
    print(f"Word {word}: {generated_string}")

# Point C: Convert Grammar to FiniteAutomaton
finite_automaton_instance = grammar_instance.to_finite_automaton()

print("\nFinite Automaton Details:")
print("States:", finite_automaton_instance.Q)
print("Alphabet:", finite_automaton_instance.Sigma)
print("Start State:", finite_automaton_instance.q0)
print("Transitions:")
for state, transitions in finite_automaton_instance.delta.items():
    for symbol, result_state in transitions.items():
        print(f"({state}, {symbol}) -> {result_state}")

# Point D: check if the word can be obtained
input_string = "carnat"
result = finite_automaton_instance.string_belongs_to_language(input_string)
print()
print(f"The string '{input_string}' belongs to the language: {result}")
