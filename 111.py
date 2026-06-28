#从第一个数字开始是0、1、2、3、4、5，
#从最后一个数字开始是-1、-2、-3、-4、-5
#在 Python 里，切片有一条雷打不动的铁律：“顾头不顾尾”（左闭右开）。
#它的公式是：list[起始位置 : 结束位置]——print ("list[1:-2]: ", list[1:-2])

numbers = [1,5,9,2,4,5]
numbers += [3,8]
#拼接操作,加在上面的列表后面

print(len(numbers))
print(max(numbers))
#几个数字、最大数字

print(numbers[1:])
#从第一个数字开始到最后一个数字。

print ("numbers[1:-2]: ", numbers[1:-2])
#全部数字[1, 5, 9, 2, 4, 5, 3, 8]
#结果：numbers[1:-2]:  [5, 9, 2, 4, 5]

print(numbers.count(5))
#统计某个元素在列表中出现的次数

#hehehheheheh

