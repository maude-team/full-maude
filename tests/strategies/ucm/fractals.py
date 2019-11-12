#
# Fractals drawing program using Cairo
#
# This program draws a basic shape (line, square, triangle) in every position
# in the Maude term, which is read from standard input.
#

import sys
import cairo

# Parse the lines from the Maude term (use -no-wrap when calling Maude)
def parse_line(line):
	return [float(x) for x in line.replace('(', '').replace(')', '')
			.replace('>', '').replace(',', '').split()]

def draw_line(x0, y0, x, y):
	context.move_to(x0, y0)
	context.line_to(x, y)
	context.stroke()

def draw_rect(x0, y0, x, y):
	context.rectangle(x0, y0, x - x0, x - x0)
	context.fill()

def draw_triangle(x0, y0, x, y):
	h = 3 ** .5 / 2

	context.move_to(x0, y0)
	context.line_to(x, y)
	context.line_to(x0 + (x - x0) * .5 + (y0 - y) * h,
			y0 + (y - y0) * .5 + (x - x0) * h)
	context.line_to(x0, y0)
	context.fill()

draw_funcs = {
	'l'	: draw_line,
	's'	: draw_rect,
	't'	: draw_triangle
}

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('Call the program with l (line), t (triangle) or s (square) to select the basic shape.')
		sys.exit(1)

	surface = cairo.PDFSurface("drawing.pdf", 100, 100)
	context = cairo.Context(surface)
	context.set_line_width(0.002)
	context.set_line_cap(cairo.LINE_CAP_ROUND)
	context.scale(100, 100)

	# Provides an inner margin and the usual orientation
	context.transform(cairo.Matrix(0.98, 0, 0, -0.98, .01, .99))

	draw_function = draw_funcs.get(
		sys.argv[1],
		draw_line
	)

	print('Write the Maude term for the fractal. Then type Ctrl+D.')

	for line in sys.stdin:
		x0, y0, x, y = parse_line(line)
		draw_function(x0, y0, x, y)

	surface.finish()
