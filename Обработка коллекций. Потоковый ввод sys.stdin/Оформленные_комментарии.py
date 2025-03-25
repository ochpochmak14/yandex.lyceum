import sys


def format_comment(line_info):
    line_number, comment = line_info
    return "Line {}: {}".format(line_number, comment.lstrip("#").strip())


input_lines = map(str.lstrip, sys.stdin)
comment_lines = filter(lambda line: line[1].startswith("#"), enumerate(input_lines, 1))
formatted_comments = map(format_comment, comment_lines)

print(*formatted_comments, sep="\n")
