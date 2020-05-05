"""Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* задача считается решённой, если в коде использована функция вычисления хеша
(hash(), sha1() или любая другая из модуля hashlib)"""

import hashlib


def rabin_karp(haystack: str, needle: str):
    if len(haystack) < len(needle):
        return False

    needle_hash = hashlib.md5(needle.encode('utf-8')).digest()
    m = len(needle)
    for i in range(len(haystack) - m + 1):
        x = hashlib.md5(haystack[i: m + i].encode('utf-8')).digest()
        if x == needle_hash:
            return True

    return False


def dififerent_substrings_count_trivial(s: str, length: int):
    if not (0 < length < len(s)):
        return 0

    substrings = set(
        s[i: i + length]
        for i in range(len(s) - length + 1)
    )

    return len(substrings)


def dififerent_substrings_count_hash_based(s: str, length: int):
    if not (0 < length < len(s)):
        return 0

    return sum(
        0 if rabin_karp(s[: i + length - 1], s[i: i + length]) else 1
        for i in range(len(s) - length + 1)
    )


if __name__ == '__main__':
    s = 'her another brother'
    print(sum(dififerent_substrings_count_trivial(s, n) for n in range(1, len(s))))
    print(sum(dififerent_substrings_count_hash_based(s, n) for n in range(1, len(s))))
