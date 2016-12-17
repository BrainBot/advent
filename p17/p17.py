import hashlib
from collections import defaultdict
passcode = 'pgflpeqp'
m = hashlib.md5()
m.update(passcode)

loc_hash = defaultdict(list)


class Node():
	def __init__(self, path='', n=None, pos=None):
		self.next = n if n else []
		self.path = path
		self.pos = pos

	def __str__(self):
		return str((self.path, self.pos, len(self.next)))

def check_doors(pos, h):
	doors = []
	for d in h:
		if int(d, 16) > 10:
		 	doors.append(True) 
		else:
			doors.append(False)
	if pos[0] == 1:
		doors[0] = False
	elif pos[0] == 4:
		doors[1] = False

	if pos[1] == 1:
		doors[2] = False
	elif pos[1] == 4:
		doors[3] = False

	return doors


def find_path(node):
	loc_hash[node.pos].append(node)
	# (prune) if we're at (4,4) OR have a path longer than something to (4,4), stop
	if node.pos == (4,4):
		return

	# Part 1 purning only
	#for loc in loc_hash[(4,4)]:
	#	if len(node.path) >= len(loc.path):
	#		return

	# find which doors are open
	hasher = m.copy()
	hasher.update(node.path)
	h = hasher.hexdigest()[0:4]
	u,d,l,r = check_doors(node.pos, h)
	
	# make all valid nodes
	next_nodes = []
	if u:
		n = Node(path=node.path+'U', pos=(node.pos[0]-1, node.pos[1]))
		next_nodes.append(n)
	if d:
		n = Node(path=node.path+'D', pos=(node.pos[0]+1, node.pos[1]))
		next_nodes.append(n)
	if l:
		n = Node(path=node.path+'L', pos=(node.pos[0], node.pos[1]-1))
		next_nodes.append(n)
	if r:
		n = Node(path=node.path+'R', pos=(node.pos[0], node.pos[1]+1))
		next_nodes.append(n)

	# test all valid nodes
	for n in next_nodes:
		find_path(n)


n = Node(path='', pos=(1,1))
find_path(n)
max_length = 0
for l in loc_hash[(4,4)]:
	max_length = max(max_length, len(l.path))

print max_length
	