import os
import shutil
import fnmatch
from math import floor
from glob import glob

source = "/input/path"
destination = "/output/path"

def move_files_tree(source, destination, op):
	dir_list = os.listdir(source)

	for dirs in dir_list:
		file_list = os.listdir(os.path.join(source, dirs))
		path = os.path.join(source, dirs)
		for file in file_list:
			if op == "copy" or op == "cpy":
				shutil.copy(os.path.join(path, file), destination)
			elif op == "move" or op == "mv":
				shutil.move(os.path.join(path, file), destination)

def rename_dir_files(dir_, name):
	count = 0
	dir_ = dir_ + "/"

	for count, filename in enumerate(os.listdir(dir_)): 
		dst = str(name) + str(count) + ".jpg"
		src = dir_ + filename
		dst = dir_ + dst
          
		os.rename(src, dst) 

def rename_files_tree(source, init_count):
	dir_list = os.listdir(source)

	for dirs in dir_list:
		file_list = os.listdir(os.path.join(source, dirs))
		path = os.path.join(source, dirs)
		for file in file_list:
			new_name = "renamed"+str(init_count) + ".jpg"
			os.rename(os.path.join(path, file), os.path.join(path, new_name)) 
			init_count = init_count + 1