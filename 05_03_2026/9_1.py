f = open('9_27287.csv')

k = 1

for index, line in enumerate(f, 1):
    nums = sorted([int(x) for x in line.split()])
    counts = [nums.count(x) for x in nums]

    povt = [x for x in nums if nums.count(x) > 1]
    ne_povt = [x for x in nums if nums.count(x) == 1]

    if counts.count(3) == 6 and counts.count(1) == 1:
        if ne_povt[0] <= min(povt):
            print(abs(max(povt)))

