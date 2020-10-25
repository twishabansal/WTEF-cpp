def convert_list(n: int) -> [int]:
    return list(map(int, str(n)))


def sumpowers(k: [int]) -> int:
    c = 0
    for element in k:
        c += element ** len(k)
    return c


def armstrong(n: int) -> bool:
    if sumpowers(convert_list(n)) == n:
        return True
    return False
