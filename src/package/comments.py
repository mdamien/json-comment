
################################################################################

from io import StringIO

from .wrapper import GenericWrapper

################################################################################

# Comments
COMMENT_PREFIX = ("#",";")
MULTILINE_START = "/*"
MULTILINE_END = "*/"

# Data strings
LONG_STRING = '"""'

################################################################################

class JsonComment(GenericWrapper):

	def loads(self, custom_json_string, *args, **kwargs):
		# lines = custom_json_string.splitlines()
		standard_json = json_preprocess(custom_json_string)
		# return self.object_to_wrap.loads(standard_json, *args, **kwargs)

	def load(self, custom_json_file, *args, **kwargs):
		return self.loads(custom_json_file.read(), *args, **kwargs)

################################################################################

def json_preprocess(custom_json_string):

	stream_in = StringIO(custom_json_string)
	stream_out = StringIO()

	first_char_in_line = stream_in.read(1)
	while first_char_in_line:

		while first_char_in_line in (" ","\t","\n"):
			first_char_in_line = stream_in.read(1)

		if first_char_in_line in COMMENT_PREFIX:
			stream_in.readline()

		# /
		elif first_char_in_line == MULTILINE_START[0]:
			second_char_in_line = stream_in.read(1)

			# * oppure altro
			if second_char_in_line == MULTILINE_START[1]:

				first_char = stream_in.read(1)
				is_multiline = True

				while is_multiline:
					second_char = stream_in.read(1)
					if (first_char + second_char) == MULTILINE_END:
						is_multiline = False
						stream_in.readline()
					else:
						first_char = second_char

				first_char_in_line = stream_in.read(1)
				print(first_char_in_line)

			# Se altro, scrivo i 2 char e la riga
			else:
				stream_out.write(first_char_in_line)
				stream_out.write(second_char_in_line)
				stream_out.write(stream_in.readline())

		else:
			stream_out.write(first_char_in_line)
			stream_out.write(stream_in.readline())

		first_char_in_line = stream_in.read(1)

	# print(stream_out.getvalue())
	stream_in.close()
	stream_out.close()

	# standard_json = ""
	# is_multiline = False
	# keep_trail_space = 0

	# for line in lines:

		# # 0 if there is no trailing space
		# # 1 otherwise
		# keep_trail_space = int(line.endswith(" "))

		# # Remove all whitespace on both sides
		# line = line.strip()

		# # Mark the start of a multiline comment
		# # Not skipping, to identify single line comments using
		# #   multiline comment tokens, like
		# #   /***** Comment *****/
		# if line.startswith(MULTILINE_START):
			# is_multiline = True

		# # Skip a line of multiline comments
		# if is_multiline:
			# # Mark the end of a multiline comment
			# if line.endswith(MULTILINE_END):
				# is_multiline = False
			# continue

		# # Replace the multi line data token to the JSON valid one
		# if LONG_STRING in line:
			# line = line.replace(LONG_STRING, '"')

		# standard_json += line + " " * keep_trail_space

	# # Removing non-standard trailing commas
	# standard_json = standard_json.replace(",]", "]")
	# standard_json = standard_json.replace(",}", "}")

	# return standard_json

################################################################################
