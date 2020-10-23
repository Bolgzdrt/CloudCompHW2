import os
import socket

data_dir = './data/'

files = os.listdir(data_dir)
txt_files = filter(lambda x: x[-4:] == '.txt', files)
txt_files_list = list(txt_files)

new_file = open('./output/result.txt', 'w+')

# 4a
new_file.write('Files in /data: ' + ', '.join(txt_files_list) + '\n\n')

file_directory_list = [data_dir + s for s in txt_files_list]
num_words = []
n = 0
max_words = 0
for i in file_directory_list:
  with open(i, 'r') as f:
    for line in f:
      words = line.split()
      num_words.append(len(words))
  # 4b
  new_file.write('Number of words in ' + i[7:] + ': {}'.format(num_words[n]) + '\n')
  if num_words[n] >= max_words:
    max_words = num_words[n]
    max_words_file = i[7:]
  n += 1

grand_total = sum(num_words)
# 4c
new_file.write('\nGrand total of words from all files: {}'.format(grand_total) + '\n')
# 4d
new_file.write('\nFile with highest word count: ' + max_words_file + '\n')
# 4e
new_file.write('\nComputer\'s IP Address: ' + socket.gethostbyname(socket.gethostname()))

new_file.close()
with open('./output/result.txt', 'r') as f:
    print(f.read())