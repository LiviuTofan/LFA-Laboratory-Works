from Grammar import Grammar
from Automaton import FiniteAutomaton

language = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}

# Create an object of the Grammar class
grammar_instance = Grammar(list(language), ['a', 'b', 'c', 'd'], language, "S")

# Point A, B: Generate 5 valid strings starting with S
generated_strings = grammar_instance.generate_words()

for word in range(len(generated_strings)):
    print("Word", word+1, ":", generated_strings[word])

# Point C: Convert Grammar to FiniteAutomaton
finite_automaton_instance = FiniteAutomaton.grammar_to_DFA(grammar_instance)

print("\nFinite Automaton Details:")
print("States:", finite_automaton_instance.Q)
print("Alphabet:", finite_automaton_instance.Alphabet)
print("Start State:", finite_automaton_instance.q0)
print("Transitions:")
for state, transitions in finite_automaton_instance.delta.items():
    for symbol, result_state in transitions.items():
        print(f"({state}, {symbol}) -> {result_state}")

# Point D: check if the word can be obtained
input_string = "bdaaab"
result = finite_automaton_instance.word_belongs_to_language(input_string)

print(f"\nThe string '{input_string}' belongs to the language: {result}")
