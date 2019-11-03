def gen_dyck_paths(n, path=[1]):
	# end paths that go under the x-axis
	if sum(path) < 0:
		return
	# terminating condition
	if len(path) == 2*n:
		if sum(path) == 0:
			print(path)
		else:
			pass
		return
	# add upstep and backtrack
	path.append(1)
	gen_dyck_paths(n, path)
	path.pop()
	# add downstep and backtrack
	path.append(-1)
	gen_dyck_paths(n, path)
	path.pop()

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
		gen_dyck_paths(n)
	else:
		print("USING DEFAULT N = 3")
		gen_dyck_paths(3)