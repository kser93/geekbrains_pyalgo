"""Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно
возвращал список вершин, которые необходимо обойти."""

import math

from misc import random_positive_weighted_graph


def dijkstra_shortest(g, start=0):
    remained, visited = list(), set()
    shortest = [{
        'length': math.inf,
        'path': []
    } for _ in g]

    remained.append(start)
    visited.add(start)
    shortest[start] = {
        'length': 0,
        'path': [start]
    }

    for current in remained:
        visited.add(current)
        adjacent = ((vertex, weight) for vertex, weight in enumerate(g[current]) if weight > 0)
        for vertex, weight in adjacent:
            if shortest[current]['length'] + weight < shortest[vertex]['length'] and vertex not in visited:
                shortest[vertex] = {
                    'length': shortest[current]['length'] + weight,
                    'path': shortest[current]['path'] + [vertex]
                }
                remained.append(vertex)

    return shortest


if __name__ == '__main__':
    g = [
        [0, 0, 1, 1, 9, 0, 0, 0],
        [0, 0, 9, 4, 0, 0, 5, 0],
        [0, 9, 0, 0, 3, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 7, 0, 8, 1, 0, 0],
        [0, 0, 0, 0, 8, 1, 2, 0],
    ]
    # g = random_positive_weighted_graph(10)
    for i in range(len(g)):
        print(dijkstra_shortest(g, start=i))
