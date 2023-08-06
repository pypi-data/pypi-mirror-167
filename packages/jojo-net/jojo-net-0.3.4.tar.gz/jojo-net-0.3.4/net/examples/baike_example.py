#
# ZhiDao, BaiKe are the Chinese wiki searching engine of baidu.com.
#
# :Chinese:
# ZhiDao(知道)、BaiKe(百科) 是百度的搜索频道
# ZhiDao类是Spider的子类， 简化了百度知道的爬行、搜索、提取信息
# BaiKe类是Spider的子类， 简化了百度百科的爬行、搜索、提取信息
#

from net import ZhiDao, BaiKe


# 搜索百度百科 "爱在深秋", 对于多义词，辅助关键字是"谭咏麟"
b = BaiKe("爱在深秋", "谭咏麟")
print(b.catalog)  # 取得目录
if '歌词' in b:   # 如果目录中有 '歌词'
    print(b['歌词'])  # 取得 '歌词' 的文字
print(BaiKe("爱在深秋", "谭咏麟")['歌词'])  # 简写为一句话
print("-----------------------------")

# 搜索百度百科 "静夜思"
b = BaiKe("静夜思")
print(b['全文', '原文'])  # 取得目录中的 全文 或 原文 段落文字
print(BaiKe("静夜思")['全文', '原文'])  # 简写为一句话
print("")
print("-----------------------------")

b = ZhiDao("李白 出生地")
print(b.count(), "条答案")
print(b.answer())
print(ZhiDao("李白 出生地").answer())  # 简写为一句话
print("")


