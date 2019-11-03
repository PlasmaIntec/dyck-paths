from copy import deepcopy

def gen_dyck_paths(n, path=[1]):
	paths = []

	def func(_path):
		# end _paths that go under the x-axis
		if sum(_path) < 0:
			return
		# terminating condition
		if len(_path) == 2*n:
			if sum(_path) == 0:
				paths.append(deepcopy(_path))
			else:
				pass
			return
		# add upstep and backtrack
		_path.append(1)
		func(_path)
		_path.pop()
		# add downstep and backtrack
		_path.append(-1)
		func(_path)
		_path.pop()
	
	func(path)

	return paths

if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="This is a program to visualize dyck n-paths")
	parser.add_argument(
		"-n", 
		"--number"
	)
	args = parser.parse_args()

	if args.number:
		n = int(args.number)
		print("USING N = %d" % n)
		print(gen_dyck_paths(n))
	else:
		print("USING DEFAULT N = 3")
		print(gen_dyck_paths(3))