from filecmp import dircmp
import os
import json
import subprocess
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
shutil.rmtree(base)
# with open(os.path.join(base, return_val), 'r') as f:
# 	data = json.load(f)
# 	print(data)