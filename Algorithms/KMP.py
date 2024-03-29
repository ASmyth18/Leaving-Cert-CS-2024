"""
Programme that implements the Knuth-Morris-Pratt (KMP) algorithm for string pattern matching
"""

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    i = 1
    j = 0

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    occurrences = []

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return occurrences

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

occurrences = kmp_search(text, pattern)

if occurrences:
    print("Pattern found at positions:", occurrences)
else:
    print("Pattern not found.")