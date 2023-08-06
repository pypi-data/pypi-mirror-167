import os
from pathlib import Path


from networkx import DiGraph
from pkg_resources import resource_filename
from rich import print

from src.auditor import Auditor
from src.path_printers.abstracts_printer import AbstractsPrinter


def get_instrument_from_user() -> str:
    print("")
    print(" Please describe your instrument. For example, you might type: ")  # noqa: E501
    print("-  weather ")
    print("-  election day rain ")
    print("-  draft lottery ")
    print("-  judge fixed effects ")
    return typer.prompt("Please describe your instrument ")


def get_outcome_from_user() -> str:
    print("")
    print(" Please describe your outcome. For example, you might type: ")  # noqa: E501
    print("-  voting ")
    print("-  political participation ")
    print("-  trade volume ")
    print("-  college graduation rates ")
    return typer.prompt("Please describe your outcome ")


def _get_path_to_graph(cached_extractions_directory: str = "dags",
                       library: str = "nber",
                       graph_type: str = ".rulebased.extractions.jsonl.nxdigraph.json") -> Path:  # noqa: E501
    return Path(cached_extractions_directory,
                library + graph_type)


def _check_valid_library(path_to_causal_graph: Path) -> None:
    if not path_to_causal_graph.exists():
        msg = "No causal graph found. The most likely cause is you "
        msg = msg + "selected a library that is not supported. Try "
        msg = msg + "using the library nber or nber_abstracts"
        raise FileNotFoundError(msg)

def iv() -> None:

    import argparse
    import sys
    import json
    msg = "Search for instruments"
    parser = argparse.ArgumentParser(msg)
    parser.add_argument("-i", "--instrument",
                        dest="instrument",
                        type=str)
    parser.add_argument("-o", "--outcome",
                        dest="outcome",
                        type=str)
    parser.add_argument("-library",
                        dest="library", type=str,
                        default="nber_abstracts")
    args = parser.parse_args()

    library: str = args.library
    instrument: str = args.instrument
    outcome: str = args.outcome

    path_to_graph: str = resource_filename(__name__, str(_get_path_to_graph(library=library)))  # noqa: E501

    try:
        _check_valid_library(Path(path_to_graph))
    except FileNotFoundError as e:
        print("[bold red]Error: [/bold red]" + str(e))
        os._exit(1)

    if instrument == "":
        instrument = get_instrument_from_user()
    if outcome == "":
        outcome = get_outcome_from_user()

    print("")
    print(f"- Your instrument is [bold]{instrument}\n")
    print(f"- Your outcome is [bold]{outcome}\n")

    # TODO say number in corpus below
    print(f"[green] Searching the papers from {library}\n")

    auditor = Auditor(graph_specification=path_to_graph)

    try:
        has_violation: bool = auditor.has_iv_violation(proposed_instrument=instrument,  # noqa: E501
                                                       proposed_outcome=outcome)  # noqa: E501

        if has_violation:

            G: DiGraph = auditor._load_graph(path_to_graph)
            printer = AbstractsPrinter(G)

            path: list = auditor.get_shortest_path(source=instrument,
                                                   target=outcome)

            printer.print_path(path)

        else:
            print("[*] No violations found")
    except AttributeError as e:
        print("[bold red] Error:[/bold red]" + str(e))


if __name__ == "__main__":
    iv()
