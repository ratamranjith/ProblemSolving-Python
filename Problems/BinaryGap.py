














# Optimized Solution
def solution(n):
    # bin representation of N
    b = bin(n)[2:]
    print(b)
    # trim zeros from the right
    b = b.strip("0")
    print(b)
    l = b.split("1")    
    print(l)
    return len(max(l, key=len))

print(solution(10))
