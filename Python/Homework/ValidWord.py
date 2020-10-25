n = int(input())
for _ in range(n):
    s = input()
    if 'abcde' in s:
        while len(s) > 4:
            s = s.replace("abcde", "")
    if s == '':
        print("True")
    else:
        print("False")
