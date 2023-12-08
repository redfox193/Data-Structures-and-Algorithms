from typing import Any


class minheap:
    
    def heapify(l: list) -> list:    
        for i in range(len(l)):
            minheap.__pushup(l, i)
        return l
    
    def getmin(l: list) -> Any:
        return l[0]
    
    def popmin(l: list) -> Any:
        m = l[0]
        l[0] = l[-1]
        l.pop()
        minheap.__pushdown(l, 0)
        return m
    
    def insert(l: list, value: Any) -> None:
        l.append(value)
        minheap.__pushup(l, len(l) - 1)
            
    def __pushup(l: list, i: int) -> None:
        while i > 0:
            j = (i - 1) // 2
            if l[j] <= l[i]:
                break
            l[j], l[i] = l[i], l[j]
            i = j
            
    def __pushdown(l: list, i: int) -> None:
        while 2 * i + 1 < len(l):
            if 2 * i + 2 == len(l) or l[2 * i + 1] <= l[2 * i + 2]:
                j = 2 * i + 1
            else:
                j = 2 * i + 2
            if l[i] <= l[j]:
                break
            l[i], l[j] = l[j], l[i]
            i = j