f = open("p12.input")

instructions = [l.strip() for l in f.readlines()]

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

def get_reg_val(reg):
	return registers[reg]

def cpy(x, y):
	value = int(x) if x.isdigit() else get_reg_val(x)
	registers[y] = value

def inc(x):
	registers[x] += 1

def dec(x):
	registers[x] -= 1

def jnz(x, y):
	decision_val = int(x) if x.isdigit() else get_reg_val(x)
	try:
		jmp_val = int(y)
	except ValueError:
		jmp_val = get_reg_val(y)
	return  1 if decision_val == 0 else jmp_val


def parse_instruction(instr):
	# by default we're going to run the next instruction
	next_instr_index = 1
	cmd, rest = instr[0:3], instr[4:].split(' ')
	#print cmd, rest
	#print registers
	result = globals()[cmd](*rest)
	return result if result is not None else next_instr_index 

index = 0
while index < len(instructions):
	index += parse_instruction(instructions[index])

print registers
