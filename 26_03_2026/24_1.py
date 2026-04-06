f = open('24_1866.txt').readline()

f = f.replace('ad', 'a*d')
f = f.replace('da', 'd*a')

s = f.split('*')


print(len(max(s, key=len)))