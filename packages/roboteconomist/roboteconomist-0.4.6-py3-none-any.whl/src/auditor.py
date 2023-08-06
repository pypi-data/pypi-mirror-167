import json
from typing import List

from networkx import DiGraph, dfs_tree, node_link_graph, shortest_path
from networkx.classes.reportviews import OutEdgeView


class Auditor(object):

    def __init__(self, graph_specification: str) -> None:
        self.graph = self._load_graph(graph_specification)

    def _load_graph(self, graph_specification: str) -> DiGraph:
        with open(graph_specification, "r") as inf:
            graph: dict = json.load(inf)
        return node_link_graph(graph)

    def _explore_from_vertex(self,
                             vertex: str,
                             depth_limit: int = 5) -> List[str]:
        subgraph: DiGraph = dfs_tree(self.graph,
                                     vertex,
                                     depth_limit=depth_limit)
        edges: OutEdgeView = subgraph.edges()
        can_reach: List[str] = []
        for edge, edge_info in edges.items():
            u, v = edge  # edge is a tuple ("u", "v"), python type hints don't work with .items?  # type: ignore  # noqa:E501
            can_reach.append(v)
        return can_reach

    def get_shortest_path(self, source: str, target: str) -> list:
        return shortest_path(self.graph,
                             source=source,
                             target=target)

    def _check_valid_query(self,
                           proposed_variable: str,
                           variable_kind: str) -> bool:
        if proposed_variable in set(self.graph.nodes):
            return True
        else:
            # e.g., "cant look for instrument asjelira4a because ... "
            msg = f"The auditor can't look for violations for the {variable_kind} {proposed_variable} because it is not a known variable."  # noqa: E501
            msg = msg + " Try another instrument "
            msg = msg + "(hint: do you need to use semantic similarity?)"
            raise AttributeError(msg)

    def has_iv_violation(self,
                         proposed_instrument: str = "weather",
                         proposed_outcome: str = "research",
                         depth_limit: int = 5) -> bool:

        self._check_valid_query(proposed_variable=proposed_instrument,
                                variable_kind="instrument")
        self._check_valid_query(proposed_variable=proposed_outcome,
                                variable_kind="outcome")

        can_reach: List[str] = self._explore_from_vertex(
            vertex=proposed_instrument, depth_limit=depth_limit
        )

        return proposed_outcome in can_reach