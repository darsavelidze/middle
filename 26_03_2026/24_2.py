f = open('24_1975.txt').readline()

while 'PP' in f:
    f = f.replace('PP', 'P*P')

s = f.split('*')
print(len(max(s, key=len)))