'''
This script is used for compliance 
control pipeline execution through Github.
Why this change?
This will only going to load the list of
modified files to the database instead of 
opening the entire folder to read and write.
This implementation will save a lot of cpu
bound memory and execution complexity as per
pipeline deafult timeout is set to 720 minutes.
'''
from filecmp import dircmp
import os
import json
import shutil

def find_folder_diff(dcmp):
	for name in dcmp.diff_files:
		return name
	for sub_dir in dcmp.subdirs.values():
		find_folder_diff(sub_dir)
def caller():
	d = dircmp('files_original', 'duplicates')
	val = find_folder_diff(d)
	return val
return_val = caller()
base = 'tmp/'
if not os.path.isdir(base):
	os.mkdir(base)
files_original = 'files_original'
os.popen('cp -r {}/{} tmp'.format(files_original, return_val))


def remove_folder(folder_name):
	shutil.rmtree(folder_name)
# remove_folder(base)
# shutil.rmtree(base)
# with open(os.path.join(base, return_val), 'r') as f:
# 	data = json.load(f)
# 	print(data)
