# Read input and prep it
input = open('p1_input')
all_dir = [dir.strip() for dir in input.read().split(',')]
headings = ('N', 'E', 'S', 'W')
places = [(0,0)]

# Do navigation
horizontal_dist = 0
vertical_dist = 0
heading = 0
first_stop = True

def calc_move_distance(head, dist):
	v_d = 0
	h_d = 0
	if head == 'N':
		v_d += dist
	elif head == 'E':
		h_d += dist
	elif head == 'S':
		v_d -= dist
	elif head == 'W':
		h_d -= dist
	else:
		print "!!!!Everything busted. Heading %s is invalid" % head
	return v_d, h_d



for direction in all_dir:
	turn = direction[0]
	distance = int(direction[1:])
	#print direction, "=", turn, distance
	heading_change = 0
	if turn == 'R':
		heading_change = 1
	elif turn == 'L':
		heading_change = -1
	else:
		print "Turn of %s in invalid" % turn
	heading = (heading + heading_change) % len(headings)
	v_m, h_m = calc_move_distance(headings[heading], distance)

	for i in xrange(abs(v_m)):
		vertical_dist += 1 if (v_m > 0) else -1
		place = (vertical_dist, horizontal_dist)
		if first_stop and place in places:
			print "First stop at: Vertical: %s, Horizontal: %s, Total: %s" % (vertical_dist, horizontal_dist, abs(vertical_dist) + abs(horizontal_dist))
			first_stop = False
		places.append(place)

	for i in xrange(abs(h_m)):
		horizontal_dist += 1 if (h_m > 0) else -1
		place = (vertical_dist, horizontal_dist)
		if first_stop and place in places:
			print "First stop at: Vertical: %s, Horizontal: %s, Total: %s" % (vertical_dist, horizontal_dist, abs(vertical_dist) + abs(horizontal_dist))
			first_stop = False
		places.append(place)

print "final distance: Vertical: %s, Horizontal: %s, Total: %s" % (vertical_dist, horizontal_dist, abs(vertical_dist) + abs(horizontal_dist))
print places



