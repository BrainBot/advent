f = open("p20.input")

ranges = []

inputs = [l.strip() for l in f.readlines()]

for i in  inputs:
    low, high = i.split('-')
    ranges.append((long(low), long(high)))

index = 0
new_val = True

while new_val:
    remove_list = -1
    new_val = False
    for i, r in enumerate(ranges):
        if r[0] <= index and r[1] >= index:
            new_val = True
            index = r[1] + 1
            remove_list = i
            break
    if remove_list > 0:
        ranges.pop(remove_list)
        remove_list = -1

print index

