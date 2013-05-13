
# Json Comment

A wrapper to JSON parsers allowing comments

- - -

## Dependencies

Python 3.3.1+

### Optional

ujson 1.30+

- - -

## Description

This package allows to parse JSON files or strings with comments.

Comments have to be in their own lines.

* "#" and ";" are for single line comments
* "/*" and "*/" enclose multi line comments

It works with any JSON parser which supports "load" and "loads".

- - -

## Usage

### Install

python setup.py install

### Example

	from jsoncomment import JsonComment
	import ujson

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

Other examples in the Example directory

- - -

## Contact

Dando Real ITA @ [Steam Profile](http://steamcommunity.com/id/dandorealita)
