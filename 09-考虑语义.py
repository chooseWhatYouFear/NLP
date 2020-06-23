# todo incorporate semantic
# 流程：语句-->分词-->语义工具（常用：language model）
# 例子：我们经常有意见分歧
# 词典：['我们','经常','有','有意见','意见','分歧']

# todo 问题
# 流程： 语句-->所有分词情况（step1）-->选择最好的（step2）
# 数据量比较大导致复杂度很高

# todo 解决（安德鲁·维特比（Andrew J. Viterbi），CDMA之父，IEEE Fellow ，高通公司创始人之一，高通首席科学家。他开发了卷积码编码的最大似然算法而享誉全球。）
# 维特比算法(DP算法)

# 例子：“经常有意见分歧”
# 词典：['经常','经','有','有意见','意见','分歧','见','意','见分歧','分']
# 概率：[0.1 , 0.05, 0.1,  0.1,   0.2,  0.2,   0.05, 0.05,  0.05, 0.1]
# -log(x):[2.3,3   ,2.3,  2.3,   1.6,   1.6,   3,    3,     3,   2.3]

# todo 总结
# 知识点总结：
    # - 基于匹配规则的方法【max-matching】
    # - 基于概率统计方法【LM(language model),HMM,CRF】
    # - 分词可以认为是已经解决的问题
# 需要掌握什么？
    # - 可以自行实现最大匹配和unigrame LM的方法