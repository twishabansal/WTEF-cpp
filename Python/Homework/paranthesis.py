def SplitParenthesis(txt):
    A = []
    i = 0
    while i < len(txt):
        if txt[i] == ')':
            if txt[:i].count('(') - txt[:i].count(')') == 1:
                A.append(txt[:i + 1])
                print(txt[:i + 1])
                txt = txt[i + 1:]
                i = 0
        i += 1
    return A


print(SplitParenthesis("((()))"))
