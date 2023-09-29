from jqdatasdk import *
import pandas as pd
import datetime
auth("17780424521", "Libenyang1.01365")


# 设置行列不忽略
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 10)


# 上海 XSHG
# 深圳 XSHE
# df = get_price('000001.XSHE', start_date='2022-06-12 09:00:00', end_date='2022-06-13 14:00:00', fq='post',
#                frequency='minute', fields=['open', 'close', 'high', 'factor'],
#                round=False, panel = True)
# print(df[:4])
#
# stocks = list(get_all_securities(['stock']).index)
# print(stocks)


# resample 函数函数的使用
# 汇总统计： 统计月成交量成交额
# 转换周期 日k => 周k, first(), max(), min(), sum(),last()
# df = get_price('000001.XSHE',end_date='2023-06-19 14:00:00',count=10,
#                frequency='daily', panel=False)
# df['weekday'] = df.index.weekday
# print(df)
#
# df_week = pd.DataFrame()
# df_week['open'] = df['open'].resample('W').first()
# print(df_week)

'''获取股票财务数据'''
# 查询'000001.XSHE'的所有市值数据, 时间是2015-10-15
q = query(
    valuation
).filter(
    valuation.code == '000001.XSHE'
)
df = get_fundamentals(q, statDate = datetime.datetime.today())
df.to_csv(r'C:\Users\BenYoung\PycharmProjects\JQData\Data\finance\finance2020.csv')