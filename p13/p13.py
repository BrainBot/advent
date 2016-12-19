import sys
import pdb
from math import sqrt
from collections import defaultdict 

FAV_NUMBER = 1358
WALL = '#'
OPEN = '.'
#TARGET = (7,4)
TARGET = (31,39)
START = (1,1)

office_map = []
biggest_row = 0

def calc_dist(start, goal):
    x_dist = goal[0] - start[0]
    y_dist = goal[1] - start[1]
    return sqrt(x_dist*x_dist + y_dist*y_dist)

def get_room(pos):
    global biggest_row
    x, y = pos
    # do we need more rows?
    while y >= len(office_map):
        office_map.append(list())

    # do we need to extend this row?
    if x >= len(office_map[y]):
        biggest_row = max(biggest_row, x)
        cur_x = len(office_map[y])
        for i in range(cur_x, x-cur_x+1):
            office_map[y].append(is_open(i, y))
    return office_map[y][x]

def adjacent_nodes(pos):
    results = []
    x,y = pos
    if x >= 1 and get_room((x-1,y)):
        results.append((x-1,y))
    if y >= 1 and get_room((x,y-1)):
        results.append((x,y-1))
    if get_room((x+1,y)):
        results.append((x+1,y))
    if get_room((x,y+1)):
        results.append((x,y+1))
    return results

valid_paths = []
visted = {}

def search2(cur_room, path, target, steps_away):
    print cur_room
    if cur_room == (20, 24):
        pdb.set_trace()
    if cur_room == target:
        valid_paths.append(path)
        return

    # early exit
    if steps_away > 7:
        return
    cur_dist = calc_dist(cur_room, target)
    visted[cur_room] = cur_dist
    adj = adjacent_nodes(cur_room)
    
    for a in adj:
        if a in visted:
            print "already visted: ", a
            next_dist = calc_dist(a, target)
            if next_dist < visted[a]:
                visted[a] = next_dist
            else:
                continue
        steps = steps_away
        if calc_dist(a, target) > cur_dist:
            steps += 1
        else:
            steps = 0
        search2(a, path+[a], target, steps)

def search(current_front):
    rooms = []
    for room in current_front:
        rooms.extend(adjacent_nodes(room))
    return rooms

def is_open(x,y):
    tmp = (x*x + 3*x + 2*x*y + y + y*y) + FAV_NUMBER
    bin_str = str(bin(tmp))[2:]
    return True if (bin_str.count('1') % 2) == 0 else False

def print_map(o_map, path):
    # print first row special
    header =  "  "
    for i in range(biggest_row):
        header += str(i % 10)
    print header

    # print the rest
    for y in range(len(o_map)):
        row_str =  str(y).ljust(2, ' ')
        for x in range(biggest_row):
            if x > len(o_map):
                row_str += '?'
                continue
            if (x,y) in path:
                row_str += 'O'
                continue
            if o_map[y][x]:
                row_str += OPEN
            else:
                row_str += WALL
        print row_str

for i in range(90):
    get_room((90,i))

i = 0
current_rooms = [START]
while TARGET not in current_rooms:
    i += 1
    current_rooms = search(current_rooms)
    print current_rooms
print i

#pdb.set_trace()
# search2(START, [START], TARGET, 0)

# for path in valid_paths:
#     print_map(office_map, path)
#     print len(path)-1, path




