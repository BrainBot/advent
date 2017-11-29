f = open("p20.input")
max_val = 4294967295
ranges = []

inputs = [l.strip() for l in f.readlines()]

for i in  inputs:
    low, high = i.split('-')
    ranges.append((long(low), long(high)))

index = 0
valid_count = 0

while index <= max_val:
    remove_list = -1
    for i, r in enumerate(ranges):
        if r[0] <= index and r[1] >= index:
            index = r[1] + 1
            break
    else:
        valid_count += 1
        index += 1

print index, valid_count

