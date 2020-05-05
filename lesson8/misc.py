import random


def fully_connected_graph(n):
    """uses adjacence matrix"""
    return [[1 for _ in range(n)] for _ in range(n)]


def random_graph(n):
    return [
        [random.choice([0, 1]) for _ in range(n)]
        for _ in range(n)
    ]


def random_positive_weighted_graph(n, max_weight=None):
    if max_weight is None or max_weight <= 0:
        max_weight = 2 * n

    graph = random_graph(n)
    for i, row in enumerate(graph):
        for j, el in enumerate(row):
            if el > 0:
                graph[i][j] = random.randrange(1, max_weight + 1)
    return graph


def random_dag(n):
    # triangular matrix sets DAG
    result = [
        [
            random.choice([0, 1]) if i < j else 0
            for j in range(n)
        ]
        for i in range(n)
    ]

    # update isolated vertices by connecting from 0
    # if vertex{0} is isolated connect it to vertex{1}
    for vertex in range(n):
        no_one_connected_from = all(edge == 0 for edge in result[vertex])
        no_one_connected_to = all(row[vertex] == 0 for row in result)
        if no_one_connected_from and no_one_connected_to:
            if vertex == 0:
                result[vertex][1] = 1
            else:
                result[0][vertex] = 1

    return result


def adjacent_list(adjacent_matrix):
    result = []
    for i, row in enumerate(adjacent_matrix):
        result_row = []
        for j, item in enumerate(row):
            if adjacent_matrix[i][j] != 0:
                result_row.append(j)

        result.append(result_row)

    return result
