import re

rect_cmd = re.compile(r'([0-9]+)x([0-9]+)')
rotate_cmd = re.compile(r'([xy])=([0-9]+) by ([0-9]+)')

def make_screen(height, width):
	return [[0 for cols in range(width)] for rows in range(height)]

def print_screen(screen):
	for row in screen:
		for col in row:
			print '#' if col == 1 else '-',
		print ""

def rect(a, b, s):
	for row in range(b):
		for col in range(a):
			screen[row][col] = 1

def rotate_row(row, shift, s):
	width = len(s[0])
	corrected_shift = shift % width
	new_row = s[row][-corrected_shift:] + s[row][:-corrected_shift]
	s[row] = new_row

def rotate_col(col, shift, s):
	height = len(s)
	corrected_shift = shift % height
	tmp_col = [row[col] for row in s]
	tmp_col = tmp_col[-corrected_shift:] + tmp_col[:-corrected_shift]

	for row, val in zip(s,tmp_col):
		row[col] = val

screen = make_screen(6, 50)

f = open('p8.input')
cmds = [l.strip() for l in f.readlines()]

for cmd in cmds:
	if cmd.startswith('rect'):
		a, b = rect_cmd.findall(cmd)[0]
		a = int(a)
		b = int(b)
		rect(a, b, screen)
	elif cmd.startswith('rotate'):
		op, a, b = rotate_cmd.findall(cmd)[0]
		a = int(a)
		b = int(b)
		if op == 'x':
			rotate_col(a, b, screen)
		else:
			rotate_row(a, b, screen)
	else:
		print "bad command"
		sys.exit(1)
	print ""

print_screen(screen)
count = 0
for row in screen:
	for col in row:
		if col == 1:
			count += 1
print "\nCount: %s" % count

