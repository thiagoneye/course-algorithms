"""
Longest Common Subsequence (Memoization)
"""

# Functions

def lcs_memo(seq1: str, seq2: str) -> int:
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))

        return memo[key]

    return recurse(0, 0)


# Main

if __name__ == '__main__':
    seq1 = 'serendipitous'
    seq2 = 'precipitation'

    seq = lcs_memo(seq1, seq2)
    print(seq)
