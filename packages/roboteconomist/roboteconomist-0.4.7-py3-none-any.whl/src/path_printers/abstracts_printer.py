
from typing import List

from networkx import DiGraph, shortest_path
from rich.console import Console


class AbstractsPrinter(object):
    '''
    Prints the abstracts in the causal path from source to target
    '''

    def __init__(self, G: DiGraph) -> None:
        self.G = G

    def print_path(self, path: List[str], context: int = 100) -> None:

        all_but_last_vertex: List[str] = path[0:-1]
        last_vertex: str = path[-1]

        console = Console()

        print("")
        print(f"[*] start of report")

        causal_chain = " affects ".join(path[0:2])
        causal_chain = causal_chain + " which affects ".join(path[1:]).replace(path[1], "")
        print(f"There is evidence that {causal_chain}")

        for path_step, vertex in enumerate(all_but_last_vertex):
            print("")
            u: str = vertex
            v: str = path[path_step + 1]
            data = self.G.get_edge_data(u, v)
            print(f"{data['filename']} says that {u} affects {v}:")

            snippet: str = data["snippet"]
            console.print(snippet, style='italic')


        print("")
        print(f"[*] end of report")