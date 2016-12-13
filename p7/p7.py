f = open("p6.input")

most_common = [{},{},{},{},{},{},{},{}]

lines = [l.strip() for l in f.readlines()]

def supports_abba(s):
	start = 0
	while start + 4 < len(4):
		cand = s[start:start+4]