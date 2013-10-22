
################################################################################

from timeit import repeat

try:
	import ujson as json
except ImportError:
	import json

from jsoncomment import JsonComment

import commentjson

################################################################################

STRING = """
# Comment 1
[
	# Objects
	{
		"key" : "value",
		"another key" :
		"A multiline string.\\n"
		# It will wrap to single line, 
		# but a trailing space per line is kept.
	},
	# Other Values
	81,
	# Allow a non standard trailing comma
	true
]
"""

STRING_PURE = """
[
	{
		"key" : "value",
		"another key" : "A multiline string.\\n"
	},
	81,
	true
]
"""

REPEAT = 10
LOOPS = 10000

################################################################################

if __name__ == '__main__':

	parser = JsonComment(json)

	print("\n", "*"*80, "\n")

	p_tests = {}

	p_tests["jsoncomment"] = repeat(
		stmt="parsed_object = parser.loads(STRING)",
		setup="from __main__ import parser, STRING;",
		repeat=REPEAT,
		number=LOOPS
	)

	p_tests["commentjson"] = repeat(
		stmt="parsed_object = commentjson.loads(STRING)",
		setup="from __main__ import commentjson, STRING;",
		repeat=REPEAT,
		number=LOOPS
	)

	p_tests["uncommented json"] = repeat(
		stmt="parsed_object = json.loads(STRING_PURE)",
		setup="from __main__ import json, STRING_PURE;",
		repeat=REPEAT,
		number=LOOPS
	)

	for loop in range (0,REPEAT):
		for name in sorted(p_tests.keys()):
			print(name, "\n")
			print(
				"Loops:{}\tTotal time:{:f}s\tMean Time per loop:{:f}us \
				\n".format(
					LOOPS,
					p_tests[name][loop],
					p_tests[name][loop]/LOOPS*10**6)
				)
		print("\n")

	print("\n", "*"*80, "\n")

################################################################################
