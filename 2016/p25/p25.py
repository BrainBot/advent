import sys

f = open("p25.input")

instructions = [l.strip() for l in f.readlines()]

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

toggled = {}

toggle_map = {'inc': 'dec', 'dec': 'inc', 'tgl': 'inc', 'out': 'inc', 'jnz': 'cpy', 'cpy': 'jnz'}

cmd_count = {}

init_expected_output = 0

output_count = 0

completed = False

done = False


def check_output(val):
    global output_count, completed, done
    expected_output = output_count % 2
    if val != expected_output:
        #print "Input %s was wrong, output was %s instead of %s" % (registers['a'], val, expected_output)
        #print "Got though %s expected outputs" % output_count
        completed = True
        done = False
    else:
        output_count += 1

    if output_count > 100:
        #print "This input a=%s was correct" % registers['a]']
        done = True
        completed = True


def get_reg_val(reg):
    return registers[reg]

def out(x):
    value = int(x) if x not in registers else get_reg_val(x)
    check_output(value)


def cpy(x, y):
    value = int(x) if x not in registers else get_reg_val(x)

    # if y isn't a register abort
    if y not in registers:
        return
    registers[y] = value

def inc(x):
    registers[x] += 1

def dec(x):
    registers[x] -= 1

def jnz(x, y):
    decision_val = int(x) if x not in registers else get_reg_val(x)
    try:
        jmp_val = int(y)
    except ValueError:
        jmp_val = get_reg_val(y)
    return  1 if decision_val == 0 else jmp_val

# x = x+y, y=0
def add(x, y):
    registers[x] = registers[x] + abs(registers[y])
    registers[y] = 0

def tgl(x):
    # Triggering intensifies
    global index
    value = int(x) if x not in registers else get_reg_val(x)
    toggled[index + value] = not toggled.get(index + value, False)

def parse_instruction(cmd, rest, index):
    # by default we're going to run the next instruction
    next_instr_index = 1
    #print cmd, rest
    if index in toggled:
        #print "%s is togged to %s" % (cmd, toggle_map[cmd])
        cmd = toggle_map[cmd]

    result = globals()[cmd](*rest)
    return result if result is not None else next_instr_index

#counter = 10000
def run_code(inp):
    index = 0
    global registers, completed
    registers = {'a': inp, 'b': 0, 'c': 0, 'd': 0} 
    while index < len(instructions) and not completed:
        #print index, instructions[index]

        cmd, rest = instructions[index][0:3], instructions[index][4:].split(' ')


        # fake a multiply operator
        if index + 4 < len(instructions) and index - 1 > 0 and cmd == 'inc':
            poss_multi_instr = []

            # get the instr before and that line has been toggled
            for i in range(index-1, index+5):
                c, r = instructions[i][0:3], instructions[i][4:].split(' ')

                if i in toggled:
                    #print "%s is togged to %s" % (cmd, toggle_map[cmd])
                    cmd = toggle_map[cmd]

                poss_multi_instr.append((c,r))


            # *HACK HACK HACK* 
            # do the ugly, ugly look ahead
            # example
            # cpy b c, inc a, dec c, jnz c -2, dec d, jnz d, -5
            # this works out to be a = b*d, c=0, d=0
            # so just do that rather than looping
            if len(poss_multi_instr) == 6 and \
            poss_multi_instr[3][0].startswith('jnz') and \
            poss_multi_instr[5][0].startswith('jnz') and \
            poss_multi_instr[0][0].startswith('cpy'):
                x = poss_multi_instr[0][1][0]
                cpy_reg = int(x) if x not in registers else get_reg_val(x)
                inc_reg = poss_multi_instr[1][1][0]
                jmp3_reg = poss_multi_instr[3][1][0]
                jmp5_reg = poss_multi_instr[5][1][0]

                registers[inc_reg] = registers[inc_reg] + cpy_reg * registers[jmp5_reg]
                registers[jmp3_reg] = 0
                registers[jmp5_reg] = 0
                index += 5
                continue

        index += parse_instruction(cmd, rest, index)


init_a = 0
while not done:
    toggled = {}
    cmd_count = {}
    init_expected_output = 0
    output_count = 0
    completed = False

    if init_a % 1000 == 0:
        print init_a
    run_code(init_a)
    init_a += 1
print 'exit'


    #counter -= 1
    #if counter == 0:
        #break
    #print registers
#print cmd_count
print init_a - 1
