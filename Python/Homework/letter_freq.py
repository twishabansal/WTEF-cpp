import matplotlib.pyplot as plt


def read_file(file_name):
    return open(file_name)


def all_freqs(file_name, all_chars):
    for line in read_file(file_name):
        for char in line:
            if char.isalpha():
                all_chars[char.lower()] += 1
    return all_chars


def ordered_freqs(file_name, all_chars):
    freqs = all_freqs(file_name, all_chars)
    return sorted(freqs.items(), key=lambda x: (x[1], x[0]))


all_chars = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
             'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
od = ordered_freqs('abc.txt', all_chars)
print(od)
letter, frequency = zip(*od)
plt.figure(figsize=(10, 5))
plt.bar(letter, frequency, width=0.9, color='brown')
plt.xlabel('Letter')
plt.ylabel('Frequency')
plt.title('Letter Frequency Distribution')
plt.show()
