"""
Longest Common Subsequence (Recursive)
"""

# Functions

def lcs_recursive(seq1: str, seq2: str, idx1=0, idx2=0) -> str:
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)

        return max(option1, option2)

def lcs_memo(seq1, seq2):
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

    seq = lcs_recursive(seq1, seq2)
    print(seq)

    seq = lcs_memo(seq1, seq2)
    print(seq)
