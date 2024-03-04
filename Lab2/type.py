def determine_type(automaton):
    delta = automaton.get("delta", [])

    for transition in delta:
        for state, transitions in transition.items():
            next_states = set(transitions.values())
            if len(next_states) > 1:
                return "NFA"
    return "DFA"