from Transform import TransformNFAtoDFA
from type import determine_type

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

print("Automaton type:", determine_type(variant))

Q = variant['Q']
Sigma = variant["Sigma"]
F = variant["F"]
delta = variant["delta"]
sol = TransformNFAtoDFA(Q, Sigma, F, delta)
sol.nfa.print_transition_dict()
print()
dfa = sol.nfa_to_dfa()
dfa.print_transition_dict()
