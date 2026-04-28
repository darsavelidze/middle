from itertools import product

alf = 'ВИЛМОС'
k = 1
for x in product(alf, repeat=5):
    w = ''.join(x)
    if w[0] not in 'ВИ' and w.count('В') <= 1 and w.count('С') == 1:
        if k % 2 != 0:
            print(k)
            break
    k += 1
