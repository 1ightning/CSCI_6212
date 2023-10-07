import heapq
from collections import defaultdict
import time
import random
import string

# Define a Node class for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1

    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate Huffman Codes
def generate_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + '0', huffman_codes)
    generate_huffman_codes(root.right, current_code + '1', huffman_codes)

# Generate random characters of a given length
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Main function
if __name__ == "__main__":
    char_length = int(input("Enter the length of characters to generate: "))

    # Generate random input
    random_input = generate_random_string(char_length)

    start_time = time.time_ns()

    root = build_huffman_tree(random_input)
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)

    end_time = time.time_ns()

    # print(f"Random Input: {random_input}")
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    print(f"Time taken for encoding: {end_time - start_time} nano seconds")
