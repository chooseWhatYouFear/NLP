# todo 最大匹配算法（贪心的算法）
# 前向最大匹配（forward-max matching）----需要定义一个参数max_len=5
# 例子：我们经常有意见分歧
# 词典：['我们','经常','有','有意见','意见','分歧']
# 后向最大匹配（backward-max matching）----需要定义一个参数max_len=5
# https://blog.csdn.net/mandagod/article/details/97106717
# todo 缺点
# 1、无法细分（有时候细分可能是更好的）
# 2、局部最优
# 3、效率低（依赖于max_len）
# 4、歧义（不能考虑语义）------很重要的点
    # 我们经常有意见分歧