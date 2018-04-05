# python-multiprocessing-2.5

import subprocess
import os
import shutil

if name == "main":
    process = subprocess.call(['convert.exe', 'input.jpg', '-resize', '200', 'output.jpg'])
    file_path = "/Result"
    directory = os.path.dirname(file)
    src = r'{}/output.jpg'.format(directory)
    dst = r'{}/result/output.jpg'.format(directory)
    directory = r'{}/result'.format(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    shutil.move(src, dst)
