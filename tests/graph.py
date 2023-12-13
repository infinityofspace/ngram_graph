import unittest

from ngram_graph.graph import text_to_graph


class TestGraph(unittest.TestCase):

    def test_text_to_graph_n2(self):
        text = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        graph = text_to_graph(text, n=2)

        for i in range(len(text) - 1):
            node = graph.nodes[f"{i} {i + 1}"]
            self.assertEqual(node.text, f"{i} {i + 1}")

        self.assertEqual(9, len(graph.nodes))

        self.assertEqual(1, len(graph.nodes["0 1"].neighbors))
        self.assertEqual("2 3", graph.nodes["0 1"].neighbors[0].text)
        self.assertEqual(1, len(graph.nodes["1 2"].neighbors))
        self.assertEqual("3 4", graph.nodes["1 2"].neighbors[0].text)
        self.assertEqual(2, len(graph.nodes["2 3"].neighbors))
        self.assertEqual("0 1", graph.nodes["2 3"].neighbors[0].text)
        self.assertEqual("4 5", graph.nodes["2 3"].neighbors[1].text)
        self.assertEqual(2, len(graph.nodes["3 4"].neighbors))
        self.assertEqual("1 2", graph.nodes["3 4"].neighbors[0].text)
        self.assertEqual("5 6", graph.nodes["3 4"].neighbors[1].text)
        self.assertEqual(2, len(graph.nodes["4 5"].neighbors))
        self.assertEqual("2 3", graph.nodes["4 5"].neighbors[0].text)
        self.assertEqual("6 7", graph.nodes["4 5"].neighbors[1].text)
        self.assertEqual(2, len(graph.nodes["5 6"].neighbors))
        self.assertEqual("3 4", graph.nodes["5 6"].neighbors[0].text)
        self.assertEqual("7 8", graph.nodes["5 6"].neighbors[1].text)
        self.assertEqual(2, len(graph.nodes["6 7"].neighbors))
        self.assertEqual("4 5", graph.nodes["6 7"].neighbors[0].text)
        self.assertEqual("8 9", graph.nodes["6 7"].neighbors[1].text)
        self.assertEqual(1, len(graph.nodes["7 8"].neighbors))
        self.assertEqual("5 6", graph.nodes["7 8"].neighbors[0].text)
        self.assertEqual(1, len(graph.nodes["8 9"].neighbors))
        self.assertEqual("6 7", graph.nodes["8 9"].neighbors[0].text)

    def test_text_to_graph_n3(self):
        text = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        graph = text_to_graph(text, n=3)

        for i in range(len(text) - 2):
            node = graph.nodes[f"{i} {i + 1} {i + 2}"]
            self.assertEqual(node.text, f"{i} {i + 1} {i + 2}")

        self.assertEqual(8, len(graph.nodes))

        self.assertEqual(1, len(graph.nodes["0 1 2"].neighbors))
        self.assertEqual("3 4 5", graph.nodes["0 1 2"].neighbors[0].text)
        self.assertEqual(1, len(graph.nodes["1 2 3"].neighbors))
        self.assertEqual("4 5 6", graph.nodes["1 2 3"].neighbors[0].text)
        self.assertEqual(1, len(graph.nodes["2 3 4"].neighbors))
        self.assertEqual("5 6 7", graph.nodes["2 3 4"].neighbors[0].text)
        self.assertEqual(2, len(graph.nodes["3 4 5"].neighbors))
        self.assertEqual("0 1 2", graph.nodes["3 4 5"].neighbors[0].text)
        self.assertEqual("6 7 8", graph.nodes["3 4 5"].neighbors[1].text)
        self.assertEqual(2, len(graph.nodes["4 5 6"].neighbors))
        self.assertEqual("1 2 3", graph.nodes["4 5 6"].neighbors[0].text)
        self.assertEqual("7 8 9", graph.nodes["4 5 6"].neighbors[1].text)
        self.assertEqual(1, len(graph.nodes["5 6 7"].neighbors))
        self.assertEqual("2 3 4", graph.nodes["5 6 7"].neighbors[0].text)
        self.assertEqual(1, len(graph.nodes["6 7 8"].neighbors))
        self.assertEqual("3 4 5", graph.nodes["6 7 8"].neighbors[0].text)
        self.assertEqual(1, len(graph.nodes["7 8 9"].neighbors))
        self.assertEqual("4 5 6", graph.nodes["7 8 9"].neighbors[0].text)


if __name__ == "__main__":
    unittest.main()
