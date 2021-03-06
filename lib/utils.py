import os
from glob import glob

# File and Directory functions
def update_dir_link(dir):
	return dir if dir[-1] == os.path.sep else dir + os.path.sep

def get_working_dir():
	return os.getcwd() + os.path.sep

def get_full_dir_link(dir):
	return get_working_dir() + update_dir_link(dir)

def get_dir_for_file(file):
	return os.path.sep.join(file.split(os.path.sep)[:-1])

def check_dir_exists(dir):
	return os.path.isdir(dir)

def check_file_exists(file):
	return os.path.isfile(file)

def create_dir_if_not_exists(dir):
	if not check_dir_exists(dir):
		os.mkdir(dir)
	return True

def create_file_if_not_exists(file):
	if not check_file_exists(file):
		open(file, "a").close()
	return True

def check_can_read(file):
	return os.access(file, os.R_OK)

def check_can_write(file):
	return os.access(file, os.W_OK)

def list_dir_contents(dir):
	# return [i for i in glob("%s*" % dir)]
	return [i for i in os.listdir(dir)]

