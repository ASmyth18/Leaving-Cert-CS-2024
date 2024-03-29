"""
Huffman sounds like a Harry Potter reject:

Implement the Huffman coding algorithm for data compression.
Given a set of characters and their frequencies,
build a Huffman tree and determine the optimal binary code for each character to minimize the total length of the encoded data.
"""

import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, parent)

    return heap[0]

def build_huffman_codes(root):
    codes = {}

    def traverse(node, code):
        if node.char is not None:
            codes[node.char] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return codes

def huffman_encoding(text):
    freq_dict = defaultdict(int)
    for char in text:
        freq_dict[char] += 1

    root = build_huffman_tree(freq_dict)
    codes = build_huffman_codes(root)

    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    inv_codes = {code: char for char, code in codes.items()}
    decoded_text = []
    code = ''

    for bit in encoded_text:
        code += bit
        if code in inv_codes:
            decoded_text.append(inv_codes[code])
            code = ''

    return ''.join(decoded_text)

text = "Hello, World!"
encoded_text, codes = huffman_encoding(text)
print("Encoded Text:", encoded_text)
print("Huffman Codes:", codes)

decoded_text = huffman_decoding(encoded_text, codes)
print("Decoded Text:", decoded_text)