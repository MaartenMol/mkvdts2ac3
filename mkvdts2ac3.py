import os
import fnmatch
import sys

execute_path = os.getcwd()

def find(pattern, path):
	result = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, pattern):
				result.append(os.path.join(root, name))
	return result


all_mkv_files = find('*.mkv', execute_path)

sys.stdout.write('Found {} .mkv files\n'.format(len(all_mkv_files)))

counter = 1

for mkv_file in all_mkv_files:
	sys.stdout.write('Starting conversion for: {}.\n'.format(mkv_file))
	os.system('mkvdts2ac3.sh -w . -n -d "{}"'.format(mkv_file))
	sys.stdout.write('Processed {} out of {} mkv files.\n\n'.format(counter, len(all_mkv_files)))
	counter += 1

sys.stdout.write('Done processing all mkv files!\n')
