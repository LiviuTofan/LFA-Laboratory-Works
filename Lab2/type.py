def is_deterministic(variant):
    delta = variant["delta"]
    transitions = {}

    # Construct transition dictionary
    for transition in delta:
        for state, transitions_from_state in transition.items():
            for symbol, next_state in transitions_from_state.items():
                if state not in transitions:
                    transitions[state] = {}
                if symbol not in transitions[state]:
                    transitions[state][symbol] = set()
                transitions[state][symbol].add(next_state)

    # Check for non-determinism
    for state, transitions_from_state in transitions.items():
        for symbol, next_states in transitions_from_state.items():
            if len(next_states) > 1:
                return False
    return True





