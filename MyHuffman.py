from collections import Counter
from Heap import Heap


class Node:
    def __init__(self, left, right):
        self.right = right
        self.left = left
        self.freq = left.freq + right.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def walk(self, code, str):
        self.left.walk(code, str + "0")
        self.right.walk(code, str + "1")


class Leaf:
    def __init__(self, sym, freq):
        self.sym = sym
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

    def walk(self, code, str):
        code[self.sym] = str or "0"


def huffman_encode(str):
    heap = Heap(30)
    for ch, freq in Counter(str).items():
        heap.insert(Leaf(ch, freq))

    while heap.size > 1:
        left = heap.extract_min()
        right = heap.extract_min()
        heap.insert(Node(left, right))
    code = {}
    root = heap.heap[0]
    root.walk(code, "")
    return code


if __name__ == '__main__':
    str = input()
    code = huffman_encode(str)
    encoded = "".join(code[ch] for ch in str)
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)
