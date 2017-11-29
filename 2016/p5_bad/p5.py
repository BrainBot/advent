import hashlib
inp = "abc"#"ugkcyxxp"

password = ""
counter = 0#0

while len(password) < 8:
	m = hashlib.md5()
	m.update(inp + str(counter))
	hd = m.hexdigest()
	if hd.startswith('00000'):
		print counter, hd
		password += hd[5]

