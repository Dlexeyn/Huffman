import heapq
from collections import Counter
from Heap import Heap


class Node:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def walk(self, code, str):
        self.left.walk(code, str + "0")
        self.right.walk(code, str + "1")


class Leaf:
    def __init__(self, sym):
        self.sym = sym

    def walk(self, code, str):
        code[self.sym] = str or "0"


def huffman_encode(str):
    h = []
    for ch, freq in Counter(str).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        fr1, count1, left = heapq.heappop(h)
        fr2, count2, right = heapq.heappop(h)
        heapq.heappush(h, (fr1 + fr2, count, Node(left, right)))
        count += 1

    if h:
        [(_freq, _code, root)] = h
    code = {}
    root.walk(code, "")
    return code


if __name__ == '__main__':
    str = input()
    code = huffman_encode(str)
    encoded = "".join(code[ch] for ch in str)
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)
