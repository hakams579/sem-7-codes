import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Defining comparison operators for priority queue (heapq)
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Removing two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Creating a new node with the sum of the frequencies
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Adding the new node to the heap
        heapq.heappush(heap, merged)

    return heap[0]

# Function to generate the Huffman codes
def generate_huffman_codes(root, prefix="", huffman_code={}):
    if root is None:
        return

    # If it's a leaf node, store the code
    if root.char is not None:
        huffman_code[root.char] = prefix

    generate_huffman_codes(root.left, prefix + "0", huffman_code)
    generate_huffman_codes(root.right, prefix + "1", huffman_code)

    return huffman_code

# Function to encode a text using Huffman Encoding
def huffman_encoding(text, huffman_code):
    # Encode the text
    encoded_text = ''.join(huffman_code[char] for char in text if char in huffman_code)
    return encoded_text

# Function to decode a Huffman encoded string
def huffman_decoding(encoded_text, huffman_code):
    reverse_huffman_code = {v: k for k, v in huffman_code.items()}

    decoded_text = ""
    current_code = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_huffman_code:
            decoded_text += reverse_huffman_code[current_code]
            current_code = ""

    return decoded_text

# Function to get user input for characters and frequencies
def get_user_input():
    print("Enter characters and their frequencies.")
    print("Type 'done' when you are finished.")
    
    frequency = {}
    while True:
        char = input("Enter character: ")
        if char.lower() == 'done':
            break
        freq = int(input(f"Enter frequency of '{char}': "))
        frequency[char] = freq

    return frequency

# Main function
def main():
    frequency = get_user_input()

    if not frequency:
        print("No input provided. Exiting.")
        return

    # Building Huffman Tree
    root = build_huffman_tree(frequency)

    # Generating Huffman Codes
    huffman_code = generate_huffman_codes(root)

    # Displaying Huffman Codes
    print("\nHuffman Codes:")
    for char, code in huffman_code.items():
        print(f"{char}: {code}")

    text = ''.join(frequency.keys())  
    encoded_text = huffman_encoding(text, huffman_code)
    decoded_text = huffman_decoding(encoded_text, huffman_code)

    print(f"\nEncoded text: {encoded_text}")
    print(f"Decoded text: {decoded_text}")

if __name__ == "__main__":
    main()
