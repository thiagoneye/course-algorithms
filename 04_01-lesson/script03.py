"""
Longest Common Subsequence (Dynamic Programming)
"""

# Functions

def lcs_dp(seq1: str, seq2: str) -> int:
    n1, n2 = len(seq1), len(seq2)
    table = [(n1+1)*[0] for i in range(n2+1)]

    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                table[idx1+1][idx2+1] = 1 + table[idx1][idx2]
            else:
                table[idx1+1][idx2+1] = max(table[idx1][idx2+1], table[idx1+1][idx2])

    return table[-1][-1]


# Main

if __name__ == '__main__':
    seq1 = 'serendipitous'
    seq2 = 'precipitation'

    seq = lcs_dp(seq1, seq2)
    print(seq)
