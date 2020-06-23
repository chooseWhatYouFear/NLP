import jieba

seg_list = jieba.cut('贪心学院专注于人工智能教育',cut_all=False)
print('Default Mode:'+'/ '.join(seg_list))

jieba.add_word('贪心学院')
seg_list = jieba.cut('贪心学院专注于人工智能教育',cut_all=False)
print('Default Mode:'+'/ '.join(seg_list))