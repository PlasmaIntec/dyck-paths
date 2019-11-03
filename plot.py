from plotly.subplots import make_subplots
import plotly.graph_objects as go
from putnam import gen_input_paths, gen_output_paths

def convert_path_to_coordinates(path):
	coordinates = [0]
	coordinate = 0
	for step in path:
		coordinate += step
		coordinates.append(coordinate)
	return coordinates

def plot(n):
	input_paths = gen_input_paths(n)
	output_paths = gen_output_paths(n)
	fig = make_subplots(
		rows=len(input_paths), 
		cols=2,
		column_titles=("Input", "Output")
	)

	# populate inputs
	for index, path in enumerate(input_paths):
		series = convert_path_to_coordinates(path)
		x = series
		i = [i for i in range(len(x))]
		fig.add_trace(
			go.Scatter(x=i, y=x), 
			row=index+1, col=1
		)

	# populate outputs
	for index, path in enumerate(output_paths):
		series = convert_path_to_coordinates(path)
		x = series
		i = [i for i in range(len(x))]
		fig.add_trace(
			go.Scatter(x=i, y=x), 
			row=index+1, col=2
		)

	fig.update_layout(
		width=900,
		height=800,
		showlegend=False,
		title_text="Dyck %s-Path" % n,
		font=dict(
			family="Courier New, monospace",
			size=18,
			color="#7f7f7f"
		)
	)

	fig.show()

if __name__ == "__main__":
	import argparse
	
	parser = argparse.ArgumentParser(description="This is Tinder for Dyck n Paths of no even return lengths and Dyck n-1 Paths")
	parser.add_argument(
		"-n", 
		"--number"
	)
	args = parser.parse_args()

	if args.number:
		n = int(args.number)
	else:
		n = 3

	plot(n)