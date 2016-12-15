import re

f = open("p10_test.input")

init_re = re.compile("(\d+) goes to bot (\d+)")
cmd_re = re.compile("(\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)")

instructions = [l.strip() for l in f.readlines()]

init_instr = []
cmd_instr = []
bots = {}
bins = {}


class Output():
    
    def __init__(self, label):
        self.label = label
        self.chips = []

    def give_chip(self, chip):
        self.chips.append(chip)

class Bot():
    def __init__(self, label):
        # form ()
        self.low = 0
        self.high = 0

        # form (low dest, high dest)
        self.instructions = []
        self.label = label

    def give_chip(self, chip):
        if self.low == 0:
            self.low = chip
        elif chip > low:
            self.high = chip
        else:
            self.high = low
            self.low = chip

    def queue_instruction(self, instr):
        instructions.append(instr)

    def 

# divide all instructions into init or command
for instr in instructions:
    
    # cmd
    if instr[0] == 'b':
        cmd = cmd_re.findall(instr)[0]
        cmd_instr.append(cmd)
    
    # init
    else:
        init = init_re.findall(instr)[0]
        init_instr.append(init)

print init_instr

print cmd_instr
