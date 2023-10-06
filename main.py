import argparse
import json
import logging

from bof_aeg import *

logging.basicConfig()
logging.root.setLevel(logging.INFO)

log = logging.getLogger(__name__)

def is_valid_file(filename):
	try:
		file = open(filename, 'r')
		return True
	except Exception as e:
   		log.error("Error:", e)
   		exit(1)

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument("-f", "--file", help="File to exploit")
	parser.add_argument("-t", "--template", help="Template file path")

	args = parser.parse_args()

	binary = args.file
	template = args.template
		
	if not is_valid_file(binary) or not is_valid_file(template):
		exit(1)

	# arbx = ArbiterX(binary, template)
	


if __name__ == '__main__':
	main()
