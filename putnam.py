from dyck import gen_dyck_paths
from returns import split_path_at_returns, find_return_length

def is_all_odd(array):
	for element in array:
		if element % 2 == 0:
			return False
	return True

def gen_input_paths(n, path=[]):
	valid_paths = []
	paths = gen_dyck_paths(n, path)
	for path in paths:
		split_paths = split_path_at_returns(path)
		return_lengths = []
		for split_path in split_paths:
			return_lengths.append(find_return_length(split_path))
		if is_all_odd(return_lengths):
			valid_paths.append(path)
	return valid_paths

if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="This program is used to generate Dyck Paths with no returns of even length")
	parser.add_argument(
		"-n", 
		"--number"
	)
	args = parser.parse_args()

	if args.number:
		n = int(args.number)
		print("USING N = %d" % n)
		print(gen_input_paths(n))
	else:
		print("USING DEFAULT N = 3")
		print(gen_input_paths(3))