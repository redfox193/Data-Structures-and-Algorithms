def m1_func(s):
    l, r = 0, -1
    m = [0] * len(s)
    for i in range(len(s)):
        k = 0 if i > r else min(m[l + r - i], r - i + 1)
        while i + k < len(s) and i - k >= 0 and s[i + k] == s[i - k]:
            k += 1
        m[i] = k
        if i + k - 1 > r:
            l, r = i - k + 1, i + k - 1
    return m


def m2_func(s):
    l, r = 0, -1
    m = [0] * len(s)
    for i in range(len(s)):
        k = 0 if i > r else min(m[l + r - i + 1], r - i + 1)
        while i + k < len(s) and i - k - 1 >= 0 and s[i + k] == s[i - k - 1]:
            k += 1
        m[i] = k
        if i + k - 1 > r:
            l, r = i - k, i + k - 1
    return m
