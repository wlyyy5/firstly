from sys import argv
# 从系统的工具箱（sys）里导入参数变量（argv）,来抓取终端后面敲的单词

script,filename = argv
#  解包（unpacking）：把抓到的参数依次塞进变量盒子里。
#    script 自动拿到脚本名，filename 拿到你要操作的文件名

print(f"We're going to erase {filename}.")
#  打印提示，告诉用户我们准备要擦除（抹去）这个文件了

print("If you don't want that, hit CTRL-C (^C).")
#  给出硬核警告：如果反悔了，可以在键盘上按 Ctrl+C 来强行掐死（退出）程序

print("If you do want that, hit RETURN.")
#  如果同意这么干，就直接敲回车（RETURN）继续

input("?")
#  这里利用 input 弹出一个问号，为了让程序暂停住，等待用户的键盘反馈

print("Opening the file...")
#  打印提示，表示程序要开始去打开文件了
target = open(filename,'w')
#  全场核心！用 'w'（写入模式）打开文件，并赋值给 target 盒子。
#    ⚠️ 注意：'w' 模式一开启，文件里的旧内容会瞬间被自动清空！

print("Truncating the file. Goodbye!")
#  打印提示，表示要执行 truncate（截断/清空）操作
target.truncate()
#  手动清空文件内容（虽然 'w' 模式已经把文件变空了，这里是双重保险）

print("Now I'm going to ask you for three lines.")
#  打印提示，准备连续向用户索要三行全新的文本内容

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")
#收集用户想写的话

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#正式把三行文本写入文件里，每行后面都加上换行符 \n
#"\n" 是“换行符”
#可以写成target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally,we close it.")
target.close()
#关闭文件，释放系统资源

