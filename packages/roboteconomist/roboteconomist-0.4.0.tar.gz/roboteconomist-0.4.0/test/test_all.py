import unittest

from networkx import DiGraph

from src.auditor import Auditor
from src.graph_builders.extractions_to_networkx import Extractions2NetworkXConverter
from src.path_printers.abstracts_printer import AbstractsPrinter


class TestMethods(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_test_one(self) -> None:
        self.assertTrue(1 < 2)

    def test_extractions_2_networkx_has_filenames(self) -> None:
        corpus = "nber_abstracts"
        extractions: str = f"data/{corpus}/extractions/rulebased.extractions.jsonl"
        graph_builder = Extractions2NetworkXConverter(extractions_file=extractions,  # noqa: E501
                                                      output_directory=f"data/{corpus}/graphs/")  # noqa: E501
        G: DiGraph = graph_builder._build_graph()

        for edge in G.edges.data():
            x, y, data = edge
            self.assertTrue("filename" in data)

    def test_graph_has_filenames(self) -> None:

        corpus = "nber_abstracts"
        extractions: str = f"data/{corpus}/extractions/rulebased.extractions.jsonl"
        graph_builder = Extractions2NetworkXConverter(extractions_file=extractions,  # noqa: E501
                                                      output_directory=f"data/{corpus}/graphs/",  # noqa: E501
                                                      verbose=False)
        graph_builder.build_and_serialize()

        path_to_graph: str = "data/nber_abstracts/graphs/rulebased.extractions.jsonl.nxdigraph.json"
        auditor = Auditor(graph_specification=path_to_graph)
        G: DiGraph = auditor._load_graph(path_to_graph)

        for edge in G.edges.data():
            x, y, data = edge
            self.assertTrue("filename" in data)

    def test_abstracts_printer(self) -> None:

        path_to_graph: str = "data/nber_abstracts/graphs/rulebased.extractions.jsonl.nxdigraph.json"
        auditor = Auditor(graph_specification=path_to_graph)
        G: DiGraph = auditor._load_graph(path_to_graph)
        printer = AbstractsPrinter(G)

        path: list = auditor.get_shortest_path(source='income',
                                               target='education')

        printer.print_path(path)

if __name__ == '__main__':
    unittest.main()
