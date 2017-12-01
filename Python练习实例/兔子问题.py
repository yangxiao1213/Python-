古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21

# 这就是典型的斐波那契数列
def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

def fib1(max):
	if n == 1 or n == 2:
		return 1
	while n < max:
		yield b
		a , b = b , a + b
		n += 1
	return 'done'