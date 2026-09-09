from __future__ import annotations

from .models import GraphEdge, GraphNeighborhood


def get_neighborhood(node_id: str, limit: int = 12) -> GraphNeighborhood:
    from .repository import load_dataset, node_index

    dataset = load_dataset()
    index = node_index()
    center = index[node_id]
    selected_edges: list[GraphEdge] = []
    selected_node_ids = {node_id}

    for edge in dataset.edges:
        if edge.source == node_id or edge.target == node_id:
            selected_edges.append(edge)
            selected_node_ids.add(edge.source)
            selected_node_ids.add(edge.target)
        if len(selected_edges) >= limit:
            break

    nodes = [index[selected_id] for selected_id in selected_node_ids]
    return GraphNeighborhood(center=center, nodes=nodes, edges=selected_edges)
