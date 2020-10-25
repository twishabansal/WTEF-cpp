def setbit(val, i, bit):

    num = 1 << i

    if bit:
        return val or num

    return val and ~num


print(setbit('10001',1,1))