from typing import List

def zFunc(s: str) -> List[int]:
    """
    Calculates the Z-values for each position in the input string 's' using the Z algorithm.

    Args:
        s (str): The input string for which Z-values need to be calculated.

    Returns:
        List[int]: A list of Z-values for each position in the input string.

    Example:
        zFunc("abacabadabacaba") -> [0, 0, 1, 0, 3, 0, 1, 0, 1, 0, 1, 0, 7, 0, 1, 0, 1, 0]

    Reference:
        The Z algorithm is a linear time pattern matching algorithm.
        More information about the Z algorithm can be found at:
        https://en.wikipedia.org/wiki/Z_algorithm
    """
    z = [0] * len(s)  # Create a list to store the Z-values
    l, r = 0, 0  # Initialize the left and right indices of the Z-box

    for i in range(1, len(s)):
        z[i] = 0 if i > r else min(r - i + 1, z[i - l])

        # Extend the Z-box to find matches
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Update the Z-box boundaries if necessary
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    return z


if __name__ == "__main__":
    print(zFunc("aabaaab"))
    print(zFunc("abcaabcd"))