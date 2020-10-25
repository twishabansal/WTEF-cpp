def trip():
    A = []
    for b in range(500):
        for a in range(1, b):
            c = (a * a + b * b) ** 0.5
            if c % 1 == 0 and a + b + c < 1000:
                A.append(a + b + int(c))
    return A


def peri() -> int:
    B = trip()
    ls = list(set(B))
    C = [B.count(j) for j in ls]
    return ls[C.index(max(C))]
