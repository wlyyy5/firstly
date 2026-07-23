from sys import argv
# 从系统的工具箱（sys）里导入参数变量（argv）
from os.path import exists
#exists:判断指定的文件或文件夹是否存在
#os.path 是 Python 标准库中 os 模块的一个子模块
#它的核心意思是“操作系统路径操作工具”。

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
