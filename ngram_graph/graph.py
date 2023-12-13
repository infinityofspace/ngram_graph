from collections import deque
from typing import List, Dict

import dgl


class NGramGraph:
    nodes = Dict[str, "Node"]

    def __init__(self) -> None:
        self.nodes = {}

    def add_node(self, text: str, prev_text: str) -> None:
        """
        Add a node to the graph and connect it to the previous text node.

        :param text: text of the node
        :param prev_text: text of the previous node
        """
        prev_node = self.nodes.get(prev_text)
        text_node = self.nodes.get(text)
        if text_node:
            if prev_node:
                text_node.add_neighbor(prev_node)
                prev_node.add_neighbor(text_node)
        else:
            node_id = self.__len__()

            if prev_node:
                new_node = Node(node_id, text, [prev_node])
                prev_node.add_neighbor(new_node)
            else:
                new_node = Node(node_id, text, [])

            self.nodes[text] = new_node

    def __len__(self):
        return len(self.nodes)

    def __str__(self):
        return "\n\n".join([str(n) for n in self.nodes.values()])

    def as_dgl_graph(self):
        """
        Get the graph as a DGL graph.

        :return: DGL graph
        """

        egdes_from = []
        edges_to = []

        for node in self.nodes.values():
            for n in node.neighbors:
                egdes_from.append(node.id)
                edges_to.append(n.id)

        return dgl.graph((egdes_from, edges_to)), [n.text for n in self.nodes.values()]


class Node:
    id: int
    text: str
    neighbors: List["Node"]

    def __init__(self, id, text, neighbors) -> None:
        self.id = id
        self.text = text
        self.neighbors = neighbors

    def add_neighbor(self, node) -> None:
        """
        Add a neighbor to the node.

        :param node: node to add as a neighbor
        """
        self.neighbors.append(node)

    def __str__(self):
        return f"{self.id}: '{self.text}'\nneighbors:\n\t" \
            + "\n\t".join([f"{n.id}: '{n.text}'" for n in self.neighbors])


def text_to_graph(text: List[str], n: int = 2) -> NGramGraph:
    """
    Convert a text to a n-gram graph.

    :param text: list of words
    :param n: n-gram size

    :return: n-gram graph object
    """
    graph = NGramGraph()

    last_n_words = deque()
    for i in range(len(text) - n + 1):
        w = text[i: i + n]
        if len(last_n_words) == n:
            prev_text = " ".join(last_n_words)
        else:
            prev_text = ""
        graph.add_node(" ".join(w), prev_text)

        if len(last_n_words) == n:
            last_n_words.popleft()
        last_n_words.append(w[0])

    return graph
