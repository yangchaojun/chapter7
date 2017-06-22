import os

def run(**args):
	
	print "[*] In dirlister module."
	files = os.lister(".")
	
	return str(files)