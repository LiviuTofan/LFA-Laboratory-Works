from graphviz import Digraph

def draw_dfa(dfa, filename='dfa_diagram'):
    dfa_graph = Digraph(comment='The DFA')
    def format_state_name(state):
        return ','.join(state) if state else '{}'

    # Add nodes for all states with default shape 'circle'
    for state in dfa["states"]:
        shape = 'doublecircle' if state in dfa["accept_states"] else 'circle'
        label = format_state_name(state)
        dfa_graph.node(label, shape=shape)

    # Add edges for transitions
    for (src_state, input_symbol), dst_state in dfa["transitions"].items():
        src_label = format_state_name(src_state)
        dst_label = format_state_name(dst_state)
        dfa_graph.edge(src_label, dst_label, label=input_symbol)

    # Special handling to denote the start state with an additional invisible edge
    dfa_graph.attr('node', shape='plaintext', style='invisible')
    start_label = format_state_name(dfa["start_state"])
    dfa_graph.node('start', style='invisible')
    dfa_graph.edge('start', start_label, style='dashed')

    dfa_graph.render(filename, view=True, format='png')


