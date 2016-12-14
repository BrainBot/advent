f = open('p9_test2.input')

compressed_seqs = [l.strip() for l in f.readlines()]


def decompress(start, seq):
	chars_to_skip = 0
	decompressed_length = 0
	marker_start = start
	

	### #parse till marker or end

	marker_end = marker_start+1
	### grab marked section
	while marker_end < len(seq):
		if seq[marker_end] != ')':
			marker_end += 1
		else:
			break

	print seq, marker_start, marker_end, seq[marker_start:marker_end]
	cand_seq = seq[marker_start:marker_end].strip("(").split('x')


	# just chars, no decompression
	if len(cand_seq) == 1:
		num_chars = len(cand_seq[0])
		#print "terminal", cand_seq, num_chars
		return num_chars, num_chars

	# more to decompress inside
	else:
		num_chars, repeat_times = cand_seq
		num_chars = int(num_chars)
		repeat_times = int(repeat_times)

		#grab the section to repeat and decompress it!
		repeat_section = seq[marker_end+1:marker_end+1+num_chars]
		skip, length = decompress(0, repeat_section)
		#print skip, length
		decompressed_length = length * repeat_times


		return num_chars + (marker_end - marker_start), decompressed_length


def decompress2(start, seq):
	length = 0
	data = seq
	cur = start
	marker = False
	while data:
		# read chars until marker
		while cur < len(data):
			if data[cur] != '(':
				length += 1
				cur += 1
			else:
				marker = True
				break
		# Find end of marker
		marker_end = cur + 1
		while marker_end < len(seq):
			if seq[marker_end] != ')':
				marker_end += 1
			else:
				break

		# Read marker and grab marked section
		if marker:
			marker_start = cur + 1
			num_chars, repeat_times = seq[marker_start:marker_end].split('x')
			num_chars = int(num_chars)
			repeat_times = int(repeat_times)
			data_start = marker_end + 1
			compressed_seq = seq[data_start:data_start+num_chars]
			print compressed_seq
			#data, decompressed_length = decompress2(marker_end+1, )

		# No marker found before end of data
		else:
			return None, length








	return data, length




for seq in compressed_seqs:
	_, decompressed_length = decompress2(0, seq)
	print decompressed_length
	break
	

