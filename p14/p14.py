import hashlib

m = hashlib.md5()

hashes = {}
keys = []

salt = "jlmsuwbz"
index = 0

def is_cand_key(s, num_chars, match_char=''):
    key_char = ""
    is_cand = False
    for i in range(len(s) - (num_chars - 1)):
        substr = s[i:i+num_chars]
        cand_char = match_char if match_char else substr[0]
        if substr == len(substr) * cand_char:
            key_char = s[i]
            is_cand = True
            break
    return is_cand, key_char


def make_hash(index):
    if index not in hashes:
        tmp_hash = salt + str(index)
        for i in range(2017):
            hasher = m.copy()
            hasher.update(tmp_hash)
            tmp_hash = hasher.hexdigest()   
        hashes[index] = tmp_hash
    return hashes[index]



while len(keys) < 64:

    # create hash (if needed)
    cur_hash = make_hash(index)

    # check for cand key
    cand_key, key_char = is_cand_key(cur_hash, 3)

    if cand_key:
        # if key look ahead for 5x char
        for i in range(index+1, index+1001):
            cand_key_hash = make_hash(i)
            is_key, _ = is_cand_key(cand_key_hash, 5, key_char)
            
            if is_key:
                keys.append((index, i, cur_hash, cand_key_hash))
                break

    index += 1


for key in keys:
    print key