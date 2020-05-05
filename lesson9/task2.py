"""Закодируйте любую строку по алгоритму Хаффмана."""
# Примечание: отказался от использования PriorityQueue и heapq, чтобы не писать дерево со сравнимыми узлами

from collections import Counter, defaultdict, deque


def get_orthogonal(q: defaultdict):
    priority = min(q.keys())
    ch = q[priority].popleft()
    if len(q[priority]) == 0:
        q.pop(priority)

    return priority, ch


def traverse_code_tree(code_tree, prefix=''):
    try:
        left, right = code_tree['0'], code_tree['1']
    except:  # found a leave
        yield code_tree, prefix
        return code_tree, prefix
    else:
        yield from traverse_code_tree(left, prefix + '0')
        yield from traverse_code_tree(right, prefix + '1')


def huffman_encode(s):
    if len(s) == 0:
        return ''
    elif len(s) == 1:
        return '0'

    q = defaultdict(deque)
    for ch, priority in Counter(s).items():
        q[priority].append(ch)

    while True:
        p0, i0 = get_orthogonal(q)
        p1, i1 = get_orthogonal(q)
        subtree = {'0': i0, '1': i1}
        if p0 + p1 < len(s):
            q[p0 + p1].append(subtree)
        else:
            break

    encode_table = {char: code for char, code in traverse_code_tree(subtree)}
    decode_table = {code: char for char, code in encode_table.items()}
    return ''.join(encode_table[char] for char in s), decode_table


def huffman_decode_recursive(s, decode_table, prefix=''):
    if len(s) == 0:
        if prefix in decode_table.keys():
            return decode_table[prefix]
        else:
            return ''
    else:
        if prefix in decode_table.keys():
            return decode_table[prefix] + huffman_decode_recursive(s, decode_table)
        else:
            return huffman_decode_recursive(s[1:], decode_table, prefix + s[0])


def huffman_decode_generator(s, decode_table):
    code = ''
    while len(s) > 0:
        code, s = code + s[0], s[1:]
        if code in decode_table.keys():
            yield decode_table[code]
            code = ''


if __name__ == '__main__':
    s = 'her anoother brother'
    encoded, decode_table = huffman_encode(s)
    print(encoded)
    assert s == ''.join(huffman_decode_generator(encoded, decode_table))
