def divmod(a, b, p):
    a %= p
    b %= p
    res = 1
    k = p - 2

    while(k != 0):
        if(k % 2 == 0):
            k >>= 1
            b = (b * b) % p
        else:
            k -= 1
            res = (res * b) % p

    return (a * res) % p


def nCrModPrime(n, r, p):
    """
    Compute the binomial coefficient "n choose r" modulo a prime number 'p' efficiently.

    The binomial coefficient "n choose r" represents the number of ways to choose 'r' items from a set of 'n' items, 
    and it can be computed as C(n, r) = n! / (r! * (n - r)!), where '!' denotes factorial.

    This function calculates C(n, r) % p, where '%' denotes the modulo operation.

    Parameters:
    - n (int): The total number of items in the set.
    - r (int): The number of items to choose from the set.
    - p (int): A prime number, the modulo value.

    Returns:
    - int: The binomial coefficient "n choose r" modulo 'p'.

    Example:
    >>> nCrModPrime(5, 2, 1000000007)
    10
    >>> nCrModPrime(10, 3, 1000000007)
    120

    Note:
    This function uses an efficient method to compute the binomial coefficient modulo a prime number
    without explicitly calculating factorials, which can quickly become impractical for large 'n' and 'r'.
    The method is based on the Lucas Theorem and modular arithmetic.
    """
    r = min(n - r, r) + 1
    ncr = 1
    while(r := r - 1):
        ncr = (ncr * divmod(n - r + 1, r, p)) % p
    return ncr
