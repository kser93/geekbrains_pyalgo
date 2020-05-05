"""Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны
(дерево), по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

from collections import deque
from misc import random_dag, adjacent_list


def dfs(g, start):
    remained = deque()
    visited = set()
    remained.appendleft(start)
    while len(remained) > 0:
        current = remained.popleft()
        if current not in visited:
            visited.add(current)
            for adjacent in reversed(g[current]):
                remained.appendleft(adjacent)

            yield current


if __name__ == '__main__':
    g = adjacent_list(random_dag(10))
    print(*g, sep='\n')
    for i in range(len(g)):
        print(f'{i}:\t{list(dfs(g, start=i))}')
