from .model import Event
from typing import List
from collections import defaultdict


forward_edges = defaultdict(list)
backward_edges = defaultdict(list)
visited = {}

def handle(events: List[Event], edge: List[str] = ["", "", ""], node: str = None):
    filtered_events = []
    sub, oper, obj = edge

    bfs_queue = []
    max_time = 0

    for event in events:
        forward_edges[event.subject].append(event)
        backward_edges[event.object].append(event)

        if node:
            if node in event.subject or node in event.object:
                bfs_queue.append(event)
                visited[event]=True
                max_time = max(max_time, event.start_time if event.start_time else 0, event.end_time if event.end_time else 0)
                
        elif (not sub or sub in event.subject) and (not oper or oper in event.operation) and (not obj or obj in event.object):
            bfs_queue.append(event)
            visited[event]=True
            max_time = max(max_time, event.start_time if event.start_time else 0, event.end_time if event.end_time else 0)
    
    while bfs_queue:
        event = bfs_queue.pop(0)
        filtered_events.append(event)

        outgoing_max_time = 0
        for neig in forward_edges[event.subject]:
            if neig.start_time:
                outgoing_max_time = max(outgoing_max_time, neig.start_time)
            if neig.end_time:
                outgoing_max_time = max(outgoing_max_time, neig.end_time)

        for neig in backward_edges[event.subject]:
            if (neig not in visited) and (not neig.start_time or neig.start_time <= min(max_time, outgoing_max_time)):
                bfs_queue.append(neig)
                visited[neig] = True
    
    return filtered_events