import random,sys  # 问题是:怎么自动停止了
def 投骰子(颜色):
	骰子点数 = random.randint(1,6)
	if 骰子点数 == 1 or 骰子点数 == 6:
		骰子信息 = '足迹'
	elif 骰子点数 == 2:
		骰子信息 = '大脑'
	elif 骰子点数 == 3:
		if 颜色 == '红色':
			骰子信息 = '猎枪'
		else:
			骰子信息 = '大脑'
	elif 骰子点数 == 4:
		if 颜色 == '绿色':
			骰子信息 = '大脑'
		else:
			骰子信息 = '猎枪'
	else:
		骰子信息 = '猎枪'
	return 骰子信息

def 玩家取名():
	玩家数量 = int(input('请问有多少个玩家？（最多不能超过10个玩家！）'))
	for i in range(玩家数量):
		玩家名 = input(f'请输入第{i+1}个玩家名字：')
		玩家信息.setdefault(玩家名,0)
玩家信息 = {}
骰子 = ['绿色','绿色','绿色','绿色','绿色','绿色','黄色','黄色','黄色','黄色','红色','红色','红色']
玩家取名()
while True:
	for a in 玩家信息.keys():
		print(f'玩家{a}开始抽骰子。')
		玩家骰子 = 骰子
		足迹 = 0
		猎枪 = 0
		大脑 = 0
		while len(玩家骰子) > 1:
			抽取结果 = []
			for b in range(3):
				ba = random.choice(玩家骰子)
				抽取结果.append(ba)
				玩家骰子.remove(ba)
			print(f'本次抽取骰子的颜色为{抽取结果}。')
			for c in 抽取结果:
				骰子信息 = 投骰子(c)
				if 骰子信息 == '足迹':
					足迹 += 1
				elif 骰子信息 == '猎枪':
					猎枪 += 1
				elif 骰子信息 == '大脑':
					大脑 += 1
			del 抽取结果
			print(f'本轮投骰子有足迹{足迹}个,有猎枪{猎枪}个，有大脑{大脑}个。')
			if 猎枪 >= 3:
				大脑 = 0
				del 足迹,玩家骰子,猎枪
				break
			else:
				continue
			if 足迹 >= 3:
				d = input('您在本轮，已经得到3个或以上的足迹。是否结束本轮？（是/否）')
				if d == '是':
					del 足迹,玩家骰子,猎枪
					break
				else:
					continue
			else:
				continue
		玩家信息[a] += 大脑  #看中文字符变量真不习惯
		del 大脑
		print(f'{a}一共拥有大脑{玩家信息[a]}个。')
		z = input('是否退出程序(输入q退出):')
		if z == 'q':
			exit()
		else:
			continue
