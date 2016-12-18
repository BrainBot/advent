import re
import pdb

f = open("p10.input")

init_re = re.compile("(\d+) goes to bot (\d+)")
cmd_re = re.compile("(\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)")

instructions = [l.strip() for l in f.readlines()]

init_instr = []
cmd_instr = []
bots = {}

# bots are 0-9999, outputs are 10000+
OUTPUT_OFFSET = 10000
sinks = {}


class Output():
    
    def __init__(self, label):
        self.chips = []
        self.label = label


    def give_chip(self, chip):
        self.chips.append(chip)

    def __repr__(self):
        return "Output(%s) has %s" % (self.label-OUTPUT_OFFSET, self.chips)


class Bot():
    def __init__(self, label):
        # form ()
        self.low = 0
        self.high = 0

        # form (low dest, high dest)
        self.instructions = []
        self.label = label

    def __str__(self):
        return str(("Bot %s" % self.label, "Low: %s" % self.low, "High: %s" % self.high, self.instructions))

    def __repr__(self):
        return str(self)

    def give_chip(self, chip):
        #print "Bot %s gets %s" % (self.label, chip)
        if self.low == 0:
            self.low = chip
        elif chip > self.low:
            self.high = chip
        else:
            self.high = self.low
            self.low = chip
        
        if self.low and self.high:
            ####
            # Actual Solution check
            if self.low == 17 and self.high == 61:
                print "BOT %s HAS THE CHIPS" % self.label
            ####
            self.run_instruction()

    # instruction form (low dest, high dest)
    def queue_instruction(self, instr):
        self.instructions.append(instr)

    # instruction form (low dest, high dest)
    def run_instruction(self):
        if self.low == 0 or self.high == 0:
            return
        instr = self.instructions.pop(0)
        #print "Bot %s giving low(%s) to %s and high(%s) to %s" % (self.label, self.low, instr[0].label, self.high, instr[1].label)
        instr[0].give_chip(self.low)
        instr[1].give_chip(self.high)
        self.low, self.high = 0, 0

def get_sink(sink_num):
    # if sink doesn't exist make it
    if not sinks.get(sink_num):
        sink_cls = Bot
        if sink_num >= OUTPUT_OFFSET:
            sink_cls = Output
        sinks[sink_num] = sink_cls(sink_num)
    return sinks[sink_num]



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

#print cmd_instr
for cmd in cmd_instr:
    from_bot = int(cmd[0])
    low_dest = int(cmd[2]) + OUTPUT_OFFSET if cmd[1] == 'output' else int(cmd[2])
    high_dest = int(cmd[4]) + OUTPUT_OFFSET if cmd[3] == 'output' else int(cmd[4])

    bot = get_sink(from_bot)
    bot.queue_instruction((get_sink(low_dest), get_sink(high_dest)))
    sinks[from_bot] = bot
#print sinks

#print init_instr
for ins in init_instr:
    chip_val = int(ins[0])
    bot_num = int(ins[1])
    bot = get_sink(bot_num)
    bot.give_chip(chip_val)
    sinks[bot_num] = bot

#print sinks
#print "\n\n"
print sinks[OUTPUT_OFFSET].chips[0] * sinks[OUTPUT_OFFSET+1].chips[0] * sinks[OUTPUT_OFFSET+2].chips[0]
