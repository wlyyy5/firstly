#巩固练习：把代码缩成一行

#from sys import argv 
#script, from_file, to_file = argv
#open(to_file, 'w').write(open(from_file).read())
#打开 from_file 读出内容，直接喂给以 'w' 打开的 to_file 写入

from sys import argv
# 从系统的工具箱（sys）里导入参数变量（argv）
from os.path import exists
#exists:判断指定的文件或文件夹是否存在
#os.path 是 Python 标准库中 os 模块的一个子模块
#它的核心意思是“操作系统路径操作工具”。

script, from_file, to_file = argv
#接收两个文件名，from_file是源文件，to_file 是目标文件。

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
#打开源文件，读取全部内容，塞进 indata 这个变量盒子里。

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
#单纯的暂停，等待用户敲回车继续，或者按 Ctrl+C 强行退出。

out_file = open(to_file, 'w')
#创建目标文件，并以写入模式打开它。
out_file.write(indata)
#向已经创建好的文件里填入数据

print("Alright, all done.")

out_file.close()
in_file.close()
