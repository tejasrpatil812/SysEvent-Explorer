from typing import List
from pydot import Dot, Node, Edge

processed_node = {}
GRAPH_FILE = "./data_files/output_raw.dot"
colors = {
    'write': 'red',
    'read': 'steelblue'
}

def handle(data: List, graph_path=None):
    graph = Dot("CSE 545", graph_type="digraph", bgcolor="white")
    for event in data:
        for node in [event.subject, event.object]:
            if node not in processed_node:
                processed_node[node] = True
                graph.add_node(Node(node, shape="circle"))
        
        label = f"{event.operation}[{event.start_time} : {event.end_time}]"
        graph.add_edge(Edge(event.subject, event.object, label=label, color=colors.get(event.operation, 'black')))

    graph.write_raw(graph_path if graph_path else GRAPH_FILE)
