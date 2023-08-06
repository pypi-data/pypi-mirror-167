

from networkx import DiGraph, shortest_path


class VertexPrinter(object):
    '''
    Prints vertexes along shortest path from source to target
    '''
    def print(self, G: DiGraph, v1: str, v2: str) -> None:
        print(shortest_path(G,
                            source=v1,
                            target=v2))