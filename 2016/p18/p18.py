SAFE = '.'
TRAP = '^'

# Test input
#FIRST_ROW = '.^^.^.^^^^'

FIRST_ROW = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
NUM_ROWS = 400000

rows = [ [False] + [False if i == SAFE else True for i in FIRST_ROW] + [False]]

def is_trap(left, right, centre):
	trap = False
	if left and centre and not right:
		trap = True
	elif centre and right and not left:
		trap = True
	elif left and not right and not centre:
		trap = True
	elif right and not left and not centre:
		trap = True

	return trap

def gen_next_row(last_row):
	new_row = [False]
	for i in range(1, (len(FIRST_ROW)+1)):
		trap = is_trap(last_row[i-1], last_row[i+1], last_row[i])
		new_row.append(trap)
	return new_row + [False]

def print_row(row):
	str_row = ""
	for tile in row[1:len(row)-1]:
		if tile:
			str_row += TRAP
		else:
			str_row += SAFE
	print str_row
i = 0
while len(rows) < NUM_ROWS:
	rows.append(gen_next_row(rows[i]))
	i += 1

num_safe = 0
for row in rows:
	num_safe += row[1:len(row)-1].count(False)
	#print_row(row)

print num_safe
