# this is a pseudocode, may not work


class AdjListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def inverse_edges_from_adj_list(adj_list):
    new_adj_list = {}

    for vertex_src in adj_list.keys():
        node_dst = adj_list[vertex_src]

        while node_dst:
            vertex_dst = node_dst.val

            if vertex_dst in new_adj_list:
                node = new_adj_list[vertex_dst]

                while node.next:
                    node = node.next

                node.next = AdjListNode(vertex_src)
            else:
                new_adj_list[vertex_dst] = AdjListNode(vertex_src)

            node_dst.next

    return new_adj_list


def inverse_edges_from_adj_matrix(adj_matrix, size):
    for row in range(size):
        for col in range(row, size):
            adj_matrix[col][row], adj_matrix[row][col] = (
                adj_matrix[row][col],
                adj_matrix[col][row],
            )
