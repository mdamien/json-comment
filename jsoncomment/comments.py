
################################################################################

from .wrapper import GeneralWrapper

################################################################################

COMMENT_PREFIX = ("#",";")
MULTILINE_START = "/*"
MULTILINE_END = "*/"

################################################################################

class JsonComment(GeneralWrapper):

	def loads(self, commented_string, *args, **kwargs):
		lines = commented_string.splitlines()
		clean_string = remove_comments(lines)
		return self.object_to_wrap.loads(clean_string, *args, **kwargs)

################################################################################

def remove_comments(lines):

	clean_string = ""
	is_multiline = False

	for line in lines:
		line = line.strip()
		output_line = line

		if line.startswith(COMMENT_PREFIX):
			output_line = ""
		elif line.startswith(MULTILINE_START):
			is_multiline = True

		if is_multiline:
			output_line = ""
			if line.endswith(MULTILINE_END):
				is_multiline = False

		clean_string += output_line

	return clean_string

################################################################################
