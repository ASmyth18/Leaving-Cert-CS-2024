"""
The Rabin-Karp algorithm uses a rolling hash function to efficiently calculate the hash values of substrings of the text.
The hash function is designed to avoid collisions and ensure that different substrings have different hash values with high probability.
"""

def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    prime = 101  # A prime number for the hash function
    d = 256  # The number of characters in the input alphabet
    h = pow(d, m - 1) % prime  # The value of d^(m-1) % prime
    p_hash = 0  # Hash value for the pattern
    t_hash = 0  # Hash value for the current substring of text
    result = []  # List to store the starting indices of pattern occurrences

    # Calculate the hash value of the pattern and the first substring of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    # Slide the pattern over the text one by one
    for i in range(n - m + 1):
        # Check if the hash values of the current substring and pattern match
        if p_hash == t_hash:
            # If the hash values match, compare the characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)

        # Calculate the hash value for the next substring of text
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime

    return result

text = "ABCDEFGHAIJKABCLMNOP"
pattern = "ABC"
occurrences = rabin_karp(text, pattern)
print(occurrences)  # Output: [0, 12]