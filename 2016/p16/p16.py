target_len = 35651584
init_data = '10111011111001111'

f = open("p16_test.input")
inputs = [l.strip() for l in f.readlines()]


def make_data(init_data, target_len):
    data = init_data
    while len(data) < target_len:
        a = data
        b = a[::-1]
        b = b.replace('0', 't')
        b = b.replace('1', '0')
        b = b.replace('t', '1')
        data = a + '0' + b
    return data

def make_checksum(data, target_len):
    checksum = ''
    trimmed_data = data[0:target_len]
    i = 0
    while i < len(trimmed_data):
        same = trimmed_data[i] == trimmed_data[i+1]
        checksum += '1' if same else '0' 
        i += 2
    if len(checksum) % 2 == 0:
        checksum = make_checksum(checksum, len(checksum))
    return checksum

data = make_data(init_data, target_len)
print make_checksum(data, target_len)

# test stuff
#print make_checksum('110010110100', 12)
#for i in inputs:
#    print make_data(i, len(i) + 1)
