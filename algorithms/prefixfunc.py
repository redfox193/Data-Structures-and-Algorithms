from typing import List

def prefixFunc(s: str) -> List[int]:
    """
    Calculates the prefix function values for each position in the input string 's'.

    Args:
        s (str): The input string for which prefix function values need to be calculated.

    Returns:
        List[int]: A list of prefix function values for each position in the input string.

    Example:
        prefixFunc("abacabadabacaba") -> [0, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    Reference:
        The prefix function is a string matching algorithm.
        More information about the prefix function can be found at:
        https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    """
    p = [0] * len(s)  # Create a list to store the prefix function values

    for i in range(1, len(s)):
        j = p[i - 1]

        # Find the longest prefix of s[i] that is also a suffix
        while j != 0 and s[i] != s[j]:
            j = p[j - 1]

        p[i] = j + 1 if s[i] == s[j] else j

    return p


if __name__ == "__main__":
    print(prefixFunc("aabaaab"))
    print(prefixFunc("abcaabcd"))