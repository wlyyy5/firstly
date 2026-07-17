from sys import argv
#导入参数变量 (argv)：程序可以接收你在终端中输入的文件名

script, filename = argv
#解包 (unpacking)：使用 script, filename = argv 将文件名保存到变量中。

txt = open(filename)
#打开文件:使用 txt = open(filename) 命令打开文件。此时，txt 就好比一个书签，指向你的文件。

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
#读取内容 (read)：使用 print(txt.read()) 把文件的内容显示在屏幕上。
#关闭文件 (close)：使用 txt.close() 关闭文件，释放系统资源。

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

