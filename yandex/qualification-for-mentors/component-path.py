from __future__ import annotations

import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple

# It is possible to implement non-recursive version, but I don't have
# enough time for that
sys.setrecursionlimit(100000)


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


@dataclass
class Vertex:
    label: int
    weight: int
    enter_timestamp: int = 0
    lowest_reachable_timestamp: int = 0
    color: int = -1
    dfs_color: Color = Color.WHITE
    dfs_parent: Optional[Vertex] = None
    adj: List[Vertex] = field(default_factory=list)

    def __repr__(self) -> str:
        return f"Vertex(label={self.label}, weight={self.weight}, enter_timestamp={self.enter_timestamp}, lowest_reachable_timestamp={self.lowest_reachable_timestamp}, color={self.color})"


def dfs(vertex: Vertex, timestamp: int) -> int:
    vertex.dfs_color = Color.GRAY
    vertex.enter_timestamp = timestamp
    vertex.lowest_reachable_timestamp = timestamp
    timestamp += 1

    for next_vertex in vertex.adj:
        if next_vertex.dfs_color == Color.GRAY:
            # back edge
            vertex.lowest_reachable_timestamp = min(
                vertex.lowest_reachable_timestamp, next_vertex.enter_timestamp
            )
        elif next_vertex.dfs_color == Color.WHITE:
            # tree edge

            next_vertex.adj.remove(vertex)
            timestamp = dfs(next_vertex, timestamp)
            next_vertex.adj.append(vertex)

            vertex.lowest_reachable_timestamp = min(
                vertex.lowest_reachable_timestamp,
                next_vertex.lowest_reachable_timestamp,
            )

    vertex.dfs_color = Color.BLACK

    return timestamp


def paint(vertex: Vertex, color: int, max_color: int) -> int:
    vertex.dfs_color = Color.GRAY
    vertex.color = color

    for adj_vertex in vertex.adj:
        # Already processed
        if adj_vertex.dfs_color != Color.WHITE:
            continue

        # Articulation point
        if adj_vertex.lowest_reachable_timestamp > vertex.enter_timestamp:
            max_color = max(max_color, paint(adj_vertex, max_color + 1, max_color + 1))
        else:
            max_color = max(max_color, paint(adj_vertex, color, max_color))

    vertex.dfs_color = Color.BLACK

    return max_color


def biconnect_components(vertices: List[Vertex]) -> None:
    timestamp = 0

    # Set dfs timestamps
    for vertex in vertices:
        if vertex.dfs_color == Color.WHITE:
            timestamp = dfs(vertex, timestamp)

    # Reset dfs colors
    for vertex in vertices:
        vertex.dfs_color = Color.WHITE

    # Paint components
    color = 0
    for vertex in vertices:
        if vertex.color == -1:
            color = paint(vertex, color, color) + 1


def calculate_components_sum(vertices: List[Vertex]) -> List[int]:
    return [v.weight for v in sorted(vertices, key=lambda x: x.weight)]


def build_compressed_graph(vertices: List[Vertex]) -> List[Vertex]:
    colors = len({v.color for v in vertices})
    compressed_vertices = [Vertex(pos, 0) for pos in range(colors)]

    for vertex in vertices:
        compressed_vertices[vertex.color].weight += vertex.weight
        compressed_vertices[vertex.color].color = vertex.color

        for adj_vertex in vertex.adj:
            if vertex.color == adj_vertex.color:
                continue

            compressed_vertices[vertex.color].adj.append(
                compressed_vertices[adj_vertex.color]
            )

    return compressed_vertices


def longest_path(vertices: List[Vertex]) -> int:
    paths: List[int] = [1] * len(vertices)
    for vertex in reversed(sorted(vertices, key=lambda x: x.weight)):
        for adj_vertex in vertex.adj:
            if vertex.weight > adj_vertex.weight:
                paths[adj_vertex.label - 1] = max(
                    paths[adj_vertex.label - 1],
                    paths[vertex.label - 1] + 1,
                )

    return max(paths)


def component_path(vertices: List[Vertex]) -> Tuple[List[int], int]:
    biconnect_components(vertices)
    compressed_vertices = build_compressed_graph(vertices)

    return calculate_components_sum(compressed_vertices), longest_path(
        compressed_vertices
    )


def gen_vertices(
    num_vertices: int, edges: List[Tuple[int, int]], weights: List[int]
) -> List[Vertex]:
    vertices: List[Vertex] = [
        Vertex(pos + 1, weights[pos]) for pos in range(num_vertices)
    ]

    for src, dst in edges:
        vertices[src - 1].adj.append(vertices[dst - 1])
        vertices[dst - 1].adj.append(vertices[src - 1])

    return vertices


def get_vertices_and_edges() -> Tuple[int, int]:
    line = input().rstrip()

    num_vertices_str, num_edges_str = line.split(" ")

    return int(num_vertices_str), int(num_edges_str)


def get_edge() -> Tuple[int, int]:
    line = input().rstrip()

    src_str, dst_str = line.split(" ")

    return int(src_str), int(dst_str)


def get_weights() -> List[int]:
    line = input().rstrip()

    weights_str = line.split(" ")

    return list(map(int, weights_str))


def print_array(array: List[int]) -> None:
    array.append("\n")
    sys.stdout.write(" ".join(map(str, array)))


def main() -> None:
    num_vertices, num_edges = get_vertices_and_edges()

    weights = get_weights()
    edges: List[Tuple[int, int]] = []

    for _ in range(num_edges):
        edges.append(get_edge())

    compressed_weights, longest_compressed_path = component_path(
        gen_vertices(num_vertices, edges, weights)
    )

    print_array(compressed_weights)
    sys.stdout.write(str(longest_compressed_path) + "\n")


if __name__ == "__main__":
    main()


class TestComponentPath:
    def test_case1(self) -> None:
        assert (
            component_path(
                gen_vertices(
                    6,
                    [
                        (1, 2),
                        (2, 3),
                        (1, 3),
                        (3, 5),
                        (5, 6),
                        (5, 6),
                        (3, 4),
                    ],
                    [2, 2, 6, 10, 7, 8],
                )
            )
            == ([10, 10, 15], 2)
        )

    def test_case2(self) -> None:
        assert (
            component_path(
                gen_vertices(
                    7,
                    [
                        (1, 2),
                        (2, 3),
                        (1, 3),
                        (4, 5),
                        (5, 6),
                        (4, 6),
                        (3, 5),
                        (3, 7),
                    ],
                    [2, 2, 2, 4, 4, 4, 3],
                )
            )
            == ([3, 6, 12], 3)
        )

    def test_case3(self) -> None:
        assert (
            component_path(
                gen_vertices(
                    13,
                    [
                        (9, 1),
                        (9, 8),
                        (13, 9),
                        (10, 11),
                        (12, 5),
                        (3, 6),
                        (8, 1),
                        (6, 1),
                        (5, 10),
                        (5, 11),
                    ],
                    [92, 807, 784, 805, 113, 13, 677, 525, 377, 198, 546, 551, 421],
                )
            )
            == ([13, 421, 551, 677, 784, 805, 807, 857, 994], 2)
        )

    def test_case4(self) -> None:
        assert component_path(
            gen_vertices(
                100,
                [
                    (21, 65),
                    (10, 80),
                    (84, 41),
                    (6, 40),
                    (57, 56),
                    (79, 69),
                    (77, 66),
                    (87, 6),
                    (13, 93),
                    (86, 41),
                    (47, 61),
                    (94, 93),
                    (78, 39),
                    (86, 54),
                    (70, 86),
                    (43, 48),
                    (52, 26),
                    (50, 69),
                    (50, 94),
                    (60, 64),
                    (17, 15),
                    (33, 69),
                    (5, 77),
                    (66, 20),
                    (86, 93),
                    (45, 33),
                    (80, 99),
                    (28, 56),
                    (97, 83),
                    (16, 31),
                    (56, 33),
                    (33, 10),
                    (88, 12),
                    (33, 13),
                    (48, 6),
                    (30, 93),
                    (37, 86),
                    (38, 62),
                    (90, 31),
                    (20, 45),
                    (67, 32),
                    (30, 56),
                    (85, 8),
                    (49, 89),
                    (100, 21),
                    (10, 45),
                    (44, 41),
                    (49, 14),
                    (13, 19),
                    (48, 40),
                    (11, 83),
                    (16, 22),
                    (42, 61),
                    (44, 1),
                    (36, 35),
                    (24, 65),
                    (67, 1),
                    (82, 22),
                    (67, 59),
                    (33, 68),
                    (81, 71),
                    (57, 11),
                    (55, 94),
                    (61, 14),
                    (2, 30),
                    (3, 33),
                    (97, 40),
                    (33, 52),
                    (33, 35),
                    (92, 33),
                    (41, 18),
                    (27, 89),
                    (8, 82),
                    (54, 92),
                    (73, 4),
                    (55, 67),
                    (36, 25),
                    (38, 57),
                    (55, 39),
                    (19, 87),
                    (67, 27),
                    (25, 10),
                    (53, 56),
                    (70, 89),
                    (61, 70),
                    (24, 71),
                    (50, 46),
                    (25, 29),
                    (18, 96),
                    (89, 9),
                    (93, 64),
                    (16, 100),
                    (95, 3),
                    (92, 44),
                    (23, 6),
                    (24, 87),
                    (40, 41),
                    (79, 84),
                    (15, 96),
                    (85, 62),
                ],
                [
                    42,
                    32,
                    647,
                    908,
                    443,
                    467,
                    644,
                    226,
                    464,
                    782,
                    325,
                    716,
                    257,
                    59,
                    999,
                    129,
                    95,
                    330,
                    184,
                    996,
                    167,
                    426,
                    544,
                    968,
                    452,
                    983,
                    816,
                    532,
                    704,
                    877,
                    831,
                    50,
                    866,
                    644,
                    783,
                    59,
                    173,
                    515,
                    172,
                    959,
                    79,
                    51,
                    459,
                    501,
                    193,
                    844,
                    42,
                    595,
                    715,
                    750,
                    157,
                    325,
                    764,
                    298,
                    17,
                    292,
                    509,
                    79,
                    913,
                    745,
                    417,
                    774,
                    979,
                    897,
                    817,
                    620,
                    864,
                    512,
                    939,
                    414,
                    769,
                    97,
                    438,
                    313,
                    981,
                    883,
                    934,
                    558,
                    553,
                    134,
                    763,
                    185,
                    332,
                    961,
                    553,
                    972,
                    924,
                    84,
                    719,
                    117,
                    582,
                    411,
                    416,
                    447,
                    131,
                    143,
                    727,
                    173,
                    417,
                    477,
                ],
            )
        ) == (
            [
                32,
                42,
                50,
                51,
                79,
                84,
                95,
                97,
                117,
                131,
                134,
                143,
                157,
                172,
                173,
                173,
                313,
                325,
                330,
                417,
                438,
                443,
                459,
                464,
                512,
                532,
                544,
                558,
                582,
                620,
                644,
                644,
                647,
                704,
                716,
                745,
                763,
                764,
                769,
                831,
                844,
                883,
                897,
                908,
                913,
                934,
                979,
                981,
                983,
                996,
                999,
                25210,
            ],
            3,
        )

    def test_case5(self) -> None:
        assert (
            component_path(
                gen_vertices(
                    13,
                    [
                        (2, 13),
                        (5, 10),
                        (8, 7),
                        (3, 1),
                        (11, 9),
                        (13, 2),
                        (9, 4),
                        (12, 10),
                        (13, 8),
                        (6, 13),
                    ],
                    [741, 121, 757, 827, 924, 752, 352, 304, 351, 387, 81, 271, 713],
                )
            )
            == ([81, 271, 304, 351, 352, 387, 741, 752, 757, 827, 834, 924], 3)
        )

    def test_case6(self) -> None:
        assert (
            component_path(
                gen_vertices(
                    13,
                    [
                        (10, 13),
                        (13, 1),
                        (7, 11),
                        (3, 12),
                        (8, 5),
                        (13, 12),
                        (12, 9),
                        (8, 11),
                        (13, 9),
                        (7, 6),
                    ],
                    [523, 75, 368, 246, 21, 163, 219, 605, 140, 751, 265, 828, 956],
                )
            )
            == ([21, 75, 163, 219, 246, 265, 368, 523, 605, 751, 1924], 4)
        )
