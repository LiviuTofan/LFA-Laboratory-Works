def fa_to_regular_grammar(variant):
    grammar = {}

    states = variant["Q"]
    transitions = variant["delta"]
    alphabet = variant["Sigma"]

    for state in states:
        rules = []
        for symbol in alphabet:
            for transition in transitions:
                if state in transition and symbol in transition[state]:
                    destination = transition[state][symbol]
                    rules.append(f'{symbol}{destination}')
        grammar[state] = rules

    return grammar


def ndfa_to_dfa(variant):
    dfa = {}

    dfa["input_symbols"] = variant["Sigma"]
    unprocessed_states = [frozenset([variant["Q"][0]])]
    dfa["start_state"] = frozenset([variant["Q"][0]])
    dfa["states"] = set()
    dfa["transitions"] = {}
    dfa["accept_states"] = set()

    while unprocessed_states:
        current_state = unprocessed_states.pop()
        if current_state not in dfa["states"]:
            dfa["states"].add(current_state)
            for input_symbol in dfa["input_symbols"]:
                next_state = frozenset(
                    [s for state in current_state for s in
                     [t[state][input_symbol] for t in variant["delta"] if state in t and input_symbol in t[state]]])
                if next_state:
                    dfa["transitions"][current_state, input_symbol] = next_state
                    unprocessed_states.append(next_state)

    dfa["accept_states"] = {state for state in dfa["states"] if variant["F"][0] in state}

    return dfa