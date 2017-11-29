import re

from collections import defaultdict

GOAL_CHAR = 'G'
EMPTY_CHAR = '_'
NORMAL_CHAR = '.'
BIG_CHAR = '#'

START = (35,0)

def print_grid(grid, goal, goal_size):
    for l, j in enumerate(grid):
        for k, i in enumerate(j):
            print_char = NORMAL_CHAR
            if i[1] > 100:
                print_char = BIG_CHAR
            elif i[0] - i[1] > goal_size:
                print_char = EMPTY_CHAR
            if (k,l) == goal:
                print_char = GOAL_CHAR
            print print_char,
        print "\n"


f = open("p22.input")
inputs = [l.strip() for l in f.readlines()]
number_re = re.compile(r'(\d+)')

# remove the headers
inputs = inputs[2:]

nodes_map = {}
nodes_list = []
viable_pairs = defaultdict(list)
num_v_pairs = 0

grid = []

for i in range(30):
    grid.append([0 for i in range(36)])


for i in inputs:
    # Filesystem              Size  Used  Avail  Use%
    #/dev/grid/node-x0-y0     91T   66T    25T   72%
    x, y, size, used, avail, use_per = number_re.findall(i)
    x, y = int(x), int(y)
    nodes_list.append((x,y))
    node_data = (int(size), int(used))
    nodes_map[(x,y)] = node_data
    grid[y][x] = node_data


def part1():
    for A in nodes_list:
        if nodes_map[A][1] == 0:
            continue
        for B in nodes_list:
            if B == A:
                continue
            if nodes_map[A][1] <= nodes_map[B][0] - nodes_map[B][1]:
                viable_pairs[A].append(B)
                num_v_pairs += 1
    print num_v_pairs

def part2():
    # we could have a BFS to move the empty space next to the goal on the top row
    # then do the shuffle algo to move it all along
    # or just look at the data and see we can solve it by hand...
    print_grid(grid, START, nodes_map[START][1])

