from random import randint

a = input('Введите строку: ')
m = 256
def hash(a, m):
    summ = 0
    for i in range(len(a)):
        summ += ord(a[i])
    h = summ % m
    return h

hv = str(hash(a, m))

words = [chr(i) for i in range(97, 120)]

s = {}

for i in words:
    for j in words:
        for k in words:
            for p in words:
                h = str(hash(i+j+k+p, m)) + '0000'
                while h in s:
                    r = str(randint(1, 9999))
                    if len(r) < 4:
                        r = '0' * (4 - len(r)) + r
                    h = h[:-4] + r
                s[h] = i+j+k+p

print(hv)
print()
for i in s.keys():
    if i[:-4] == hv:
        print(f'{i} -- {s[i]}')