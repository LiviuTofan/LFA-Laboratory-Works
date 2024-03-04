from type import is_deterministic
from Chomsky import Grammar
from Transform import fa_to_regular_grammar, ndfa_to_dfa
from draw import draw_dfa

# Language from previous laboratory, to determine type
language = {
    'S': ['bS', 'dA'],
    'A': ['aA', 'dB', 'b'],
    'B': ['cB', 'a']
}



grammar = Grammar(language)
print("Grammar is:", grammar.classify_grammar())  # Output: Type 2 (Context-Free)



variant = {"Q": ["q0", "q1", "q2"],
           "Sigma": ["a", "b"],
           "F": ["q2"],
           "delta":
               [
                   {"q0": {"b": "q0"}},
                   {"q0": {"b": "q1"}},
                   {"q1": {"b": "q2"}},
                   {"q0": {"a": "q0"}},
                   {"q2": {"a": "q2"}},
                   {"q1": {"a": "q1"}}
               ]
           }

print("Is the given FA deterministic:", is_deterministic(variant))
print("Regular Grammar:")
print("-------------")
regular_grammar = fa_to_regular_grammar(variant)
for state, rules in regular_grammar.items():
    print(f"{state}: {rules}")

dfa = ndfa_to_dfa(variant)
# Test the function with the given DFA
def print_dfa(dfa):
    print("Input Symbols:", dfa["input_symbols"])
    print("Start State:", list(dfa["start_state"])[0])
    print("States:", ', '.join([', '.join(list(state)) for state in dfa["states"]]))
    print("Transitions:")
    for transition, next_state in dfa["transitions"].items():
        current_state = list(transition[0])[0]
        symbol = transition[1]
        next_states = ', '.join(list(next_state))
        print(f"{current_state} --({symbol})--> {next_states}")
    print("Accept States:", ', '.join([', '.join(list(state)) for state in dfa["accept_states"]]))

print("-------------")
print("From NDFA to DFA:")
print(print_dfa(dfa))
draw_dfa(dfa, 'dfa_diagram')
