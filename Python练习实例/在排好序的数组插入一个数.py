# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

# 程序分析：首先判断此数是否大于最后一个数，
# 然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

l = [1, 2, 4, 6, 7, 8, 10]

a = 3

# 这是用insert的方法插入到数组中
if a > l[-1]:
	l.append(a)
else:
	for i in range(len(l)):
		if  l[i] < a < l[i+1]:
			l.insert(i+1, a)

print(l)


