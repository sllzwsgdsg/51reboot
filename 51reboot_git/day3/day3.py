#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
# created suli 
# 统计字符串内单个字符出现的次数, 根据次数进行排序, 得到前N名

note = """Iese ' s particular achievement was coming top of the ranking for customised programmes& those aimed at corporate customers."""



# 统计字符串内字符的数量
def note_count_func(note):
	note_count = {}
	for i in range(len(note)):
		# 判断 note_count 中是否有重复的key
		if note_count.get(note[i]) is None:
			# 没有重复的key, 则使用当前字符做 key, 当前字符的个数做 values
			note_count[note[i]] = note.count(note[i])
	return note_count


# 对统计好的字典进行拆分,排序
def sort_note_sub(note_count):
	sort_note_k = [] # keys
	sort_note_v = [] # values

	# 拆分key 和 value
	for k, v in note_count.items():
		sort_note_k.append(k)
		sort_note_v.append(v)

	# 开始排序
	n = len(sort_note_v)
	for i in range(n):
		for j in range(1, n-i):
			if sort_note_v[j] > sort_note_v[j-1]:
				sort_note_k[j-1], sort_note_k[j] = sort_note_k[j], sort_note_k[j-1]
				sort_note_v[j-1], sort_note_v[j] = sort_note_v[j], sort_note_v[j-1]

	# 返回keys, values
	return sort_note_k, sort_note_v


# 显示排行榜, 参数: 显示数量
def show_rank(max):
	k,v = sort_note_sub(note_count_func(note))
	print "=====       前%s名:       =====" % max
	for i in range(max):
		print "第%2d名: (字符:%s, 出现次数: %s)" % (i+1, k[i], v[i])



if __name__ == "__main__":
	show_rank(10)