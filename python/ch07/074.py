import os
currentdir = os.path.dirname(__file__) + '/'

# ls = [
#     ['指标', '2018年', '2019年', '2020年'],
#     ['居民消费价格指数', '102.7', '102.9', '103.3'],
#     ['食品烟酒', '103.3', '103.6', '104.1'],
#     ['衣着', '99.8', '100.2', '100.5'],
#     ['居住', '101.3', '101.8', '102.1'],
#     ['生活用品及服务', '100.6', '100.9', '101.2'],
#     ['交通通信', '100.3', '100.7', '101.0'],
#     ['教育文化娱乐', '100.5', '100.8', '101.1'],
#     ['医疗保健', '100.2', '100.5', '100.8'],
#     ['其他用品及服务', '100.1', '100.4', '100.7'],
# ]

# f = open(currentdir + 'cpi.csv', 'w', encoding='utf-8')
# for row in ls:
#     f.write(','.join(row) + '\n')
# f.close()


ls = []
str = ''
f = open(currentdir + 'cpi.csv', 'r', encoding='utf-8')
for line in f:
    str = line.strip('\n').split(',')
    # print(str)
    ls.append(str)
f.close()
print(ls)

# for row in ls:
#     # line = ''
#     # for item in row:
#     #     # line += '{:10}\t'.format(item)
#     #     # line += '{:<20}{:<10}{:<10}{:<10}'.format(item[0], item[1], item[2], item[3])
#     #     line += "{:<20}{:<10}{:<10}{:<10}".format(row[0], row[1], row[2], row[3])
#     # line += "{:<20}{:<10}{:<10}{:<10}".format(row[0], row[1], row[2], row[3])
#     line = "{:<20}{:<10}{:<10}{:<10}".format(row[0], row[1], row[2], row[3])
#     print(line)

# for row in ls:
#     # 第一列固定20字符左对齐，后三列10字符
#     # col0 = row[0].ljust(30)
#     # col1 = row[1].ljust(10)
#     # col2 = row[2].ljust(10)
#     # col3 = row[3].ljust(10)
#     # print(col0 + col1 + col2 + col3)
#     print(f"{row[0]:<20}{row[1]:<10}{row[2]:<10}{row[3]:<10}")

# # 1. 获取每一列最大字符长度
# col_max_len = [0] * len(ls[0])
# for row in ls:
#     for idx, word in enumerate(row):
#         if len(word) > col_max_len[idx]:
#             col_max_len[idx] = len(word)

# # 2. 按最大宽度打印
# for row in ls:
#     line = ""
#     for idx, word in enumerate(row):
#         line += word.ljust(col_max_len[idx] + 3)  # +3额外留白
#     print(line)

# for row in ls:
#     c0 = row[0].ljust(20)
#     print(f"{c0}\t{row[1]}\t{row[2]}\t{row[3]}")

# def fill_full_width(s, target_len):
#     # 计算字符串实际占用宽度：汉字2，英文数字1
#     real_width = sum(2 if '\u4e00' <= c <= '\u9fff' else 1 for c in s)
#     need_fill = target_len - real_width
#     return s + "　" * need_fill  # "　" 全角空格

# for row in ls:
#     c0 = fill_full_width(row[0], 20)
#     print(f"{c0}{row[1]:<10}{row[2]:<10}{row[3]:<10}")


# from tabulate import tabulate
# # 表头取第一行，数据取剩下行
# header = ls[0]
# table_data = ls[1:]
# # plain格式无表格边框，也可换grid/fancy_grid带框
# print(tabulate(table_data, headers=header, tablefmt="plain"))

# import pandas as pd
# df = pd.DataFrame(ls[1:], columns=ls[0])
# # 控制台打印对齐表格
# print(df.to_string(index=False))

# 4列对应4个格式化占位符
fmt = "{:<20}{:<10}{:<10}{:<10}"
for row in ls:
    print(fmt.format(*row))

f.close()

# https://data.stats.gov.cn/







