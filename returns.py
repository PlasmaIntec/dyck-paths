def split_path_at_returns(path):
	returns = []

	def reduce_with_index(func, seq):
		total = 0
		prevIndex = 0
		for i in range(len(seq)):
			prevIndex, total = func(seq[i], total, prevIndex, i+1)

	def reducer(element, total, prevIndex, index):
		total += element
		if total == 0:
			returns.append(path[prevIndex:index])
			prevIndex = index
		return prevIndex, total

	reduce_with_index(reducer, path)
	return returns # high returns buy now!
	
def find_return_length(path):
	length = 0
	for i in range(len(path)-1, 0, -1):
		if path[i] != -1:
			break
		length += 1
	return length

if __name__ == "__main__":
	print(split_path_at_returns([1, 1, -1, 1, -1, -1]))
	print(find_return_length([1, 1, -1, 1, -1, -1]))