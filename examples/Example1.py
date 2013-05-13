
################################################################################

from jsoncomment import JsonComment

import ujson

################################################################################

if __name__ == '__main__':

	string = """
		/******************
		Comment 1
		Comment 2
		******************/
		[
			# Objects
			{
				"key" : "value"
			},
			; Other Values
			81,
			true
		]
	"""

	parser = JsonComment(ujson)
	parsed_object = parser.loads(string)

	print(parsed_object)
	print(parser.dumps(parsed_object))

################################################################################
