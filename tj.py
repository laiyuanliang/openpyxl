#coding: utf-8
import re

reg_info = u'平台类型:银行,平台代码:GEO_0000002633,注册时间:2016-08-12 06:59:57平台类型:非银行,平台代码:GEO_0000184968,注册时间:2016-08-12 06:59:57平台类型:银行,平台代码:GEO_0000001806,注册时间:2016-08-12 06:59:57平台类型:银行,平台代码:GEO_0000000685,注册时间:2016-08-12 06:59:57'
app_info = u'平台类型:银行,平台代码:GEO_0000001806,申请时间:2016-08-12 06:59:57,申请金额区间:0W～0.2W平台类型:银行,平台代码:GEO_0000002633,申请时间:2016-08-12 06:59:57,申请金额区间:0.5W～1W平台类型:银行,平台代码:GEO_0000000685,申请时间:2016-08-12 06:59:57,申请金额区间:10W以上平台类型:非银行,平台代码:GEO_0000184968,申请时间:2016-08-12 06:59:57,申请金额区间:3W～5W'
loan_info = u'平台类型:银行,平台代码:GEO_0000001806,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W平台类型:非银行,平台代码:GEO_0000184968,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W平台类型:银行,平台代码:GEO_0000000685,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W平台类型:银行,平台代码:GEO_0000002633,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W'

reg = len(re.findall(u'平台类型',reg_info))
reg_Bank = len(re.findall(u'平台类型:银行',reg_info))
reg_NoBank = len(re.findall(u'平台类型:非银行',reg_info))

app = len(re.findall(u'平台类型', app_info))
app_Bank = len(re.findall(u'平台类型:银行', app_info))
app_NoBank = len(re.findall(u'平台类型:非银行', app_info))

appMount_0t2k = len(re.findall(u'0W～0.2W', app_info))
appMount_2t5k = len(re.findall(u'0.2W～0.5W', app_info))
appMount_5t10k = len(re.findall(u'0.5W～1W', app_info))
appMount_10t30k = len(re.findall(u'1W～3W', app_info))
appMount_30t50k = len(re.findall(u'3W～5W', app_info))
appMount_50t100k = len(re.findall(u'5W～10W', app_info))
appMount_100kt = len(re.findall(u'10W以上', app_info))

app_Mount = sorted(re.findall('\d*\.*\d*[W][～]\d*\.*\d*[W]|10W以上', app_info))
print(app_Mount)
#max_appMount = 
#print(app, app_Bank, app_NoBank, appMount_0t2k, appMount_2t5k, appMount_5t10k, appMount_10t30k, appMount_30t50k, appMount_50t100k, appMount_100kt)
