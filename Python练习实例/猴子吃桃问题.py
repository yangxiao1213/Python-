# 猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

# 程序分析：
# 逆向思维，从后面往前推,每次前一天是后一天的多一个的两倍
# x2表示最后一天的桃子个数
x2 = 1
# 从第九天开始往回倒推
for i in range(9):
	x1 = (x2 + 1) * 2
	x2 = x1
print(x1)