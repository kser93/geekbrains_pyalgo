"""На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа."""

import itertools

from misc import fully_connected_graph


def are_adjacent(adjacence_matrix, i, j):
    return adjacence_matrix[i][j] != 0 and adjacence_matrix[j][i] != 0


if __name__ == '__main__':
    for n in range(99, 0, -1):
        adjacents = fully_connected_graph(n)
        handshakes = 0
        for i, j in itertools.product(range(n), range(n)):
            if i < j and are_adjacent(adjacents, i, j):
                handshakes += 1

        print(f'{n} guy{"s" if n > 1 else ""} made {handshakes} handshakes on the Wall;')

    print(f'No more guys make handshakes on the Wall.')
