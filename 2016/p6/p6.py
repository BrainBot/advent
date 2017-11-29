f = open("p6.input")

most_common = [{},{},{},{},{},{},{},{}]

lines = [l.strip() for l in f.readlines()]

for line in lines:
	for i, c in enumerate(line):
		cur_val = most_common[i].get(c, 0)
		most_common[i][c] = cur_val + 1

for d in most_common:
	max_count = len(lines) + 10
	selected = ''
	for k,v in d.iteritems():
		if v < max_count:
			max_count = v
			selected = k

	print selected,
print ""

print most_common