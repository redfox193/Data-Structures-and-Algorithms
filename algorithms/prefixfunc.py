from typing import List

def prefixFunc(s: str) -> List[int]:
    p = [0] * len(s)
    for i in range(1, len(s)):
        j = p[i - 1]
        while j != 0 and s[i] != s[j]:
            j = p[j - 1]
        p[i] = j + 1 if s[i] == s[j] else j
    return p

if __name__ == "__main__":
    print(prefixFunc("aabaaab"))
    print(prefixFunc("abcaabcd"))