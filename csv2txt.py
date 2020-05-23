import csv
import os
import numpy as np

path1=os.path.abspath('.')
csv_path=path1+'/train-toneless.csv'

txt_file = 'train-toneless.txt'
with open(txt_file, "w",encoding='utf-8') as my_output_file:
    with open(csv_path, "r",encoding='utf-8') as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
print('finish!')
