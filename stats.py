import sys

try:
	sys.argv[1]
except IndexError:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

book = sys.argv[1]

with open(book) as f:
	contents = f.read()

def get_num_words():
	count = len(contents.split())
	return count


def count_chars():
	lower = contents.lower()
	words = lower.split()
	chars = [letter for word in words for letter in word]
	dict = {}
	for i in chars:
		dict[i] = dict.get(i,0)+1
	sorted(dict.items(), key=lambda item: item[1])
	for i,v in sorted(dict.items(), key=lambda item: item[1], reverse=True):
		if i.isalpha():
			print(f"{i}:", v)
