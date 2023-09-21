import re

def getData():
	pattern = r"([\w.]+@[\w.]+)"

	with open("Data/mbox-short.txt") as infile:
		for line in infile:
			address = re.findall(pattern, line)
			for a in address:
				print(a)

getData()
