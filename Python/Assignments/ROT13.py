def change(i):
    if ord(i) in range(65,78) or ord(i) in range(97,110):
        return chr(ord(i)+13)
    elif ord(i) in range(78,91) or ord(i) in range(110,123):
        return chr(ord(i)-13)
    else:
        return i
    
def generate_encrypted_string(string):
    s=''
    for i in string:
        s+=change(i)
    return s
print (generate_encrypted_string('Z'))
