import re

f = open("p15.input")

init_re = re.compile("has (\d+) positions.*=(\d+),.*n (\d+)")

setup = [l.strip() for l in f.readlines()]

discs = []

for instr in setup:
    pos = init_re.findall(instr)[0]
    discs.append((int(pos[0]), int(pos[2])))

time = 0
through = False

while not through:
    through_this_time = False
    for i, d in enumerate(discs, 1):
        cur_pos = (d[1] + time + i) % d[0]
        through_this_time = cur_pos == 0
        if not through_this_time:
            time += 1
            break
    through = through_this_time

print time
