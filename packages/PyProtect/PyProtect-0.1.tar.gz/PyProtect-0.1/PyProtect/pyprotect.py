import os

def protect(password, file_path):
	inp = input("Enter password to open this file: ")
	if inp != str(password):
		exit()
	else:
		os.startfile(file_path, 'open')