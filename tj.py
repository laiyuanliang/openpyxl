#coding: utf-8
import re
def max_mount(zone_list):
    num_zone = []
    zone_dic = {'0':'0W～0.2W', '0.2':'0.2W～0.5W', '0.5':'0.5W～1W', '1':'1W～3W', '3':'3W～5W', '5':'5W～10W', '10':'10W以上'}
    for zone in zone_list:
        num = zone.split('W')[0]
        num_zone.append(num)
    ordered_num_zone = sorted(num_zone)
    max_zone = zone_dic[ordered_num_zone[-1]]
    return max_zone

reg_info = u'平台类型:银行,平台代码:GEO_0000002633,注册时间:2016-08-12 06:59:57平台类型:非银行,平台代码:GEO_0000184968,注册时间:2016-08-12 06:59:57平台类型:银行,平台代码:GEO_0000001806,注册时间:2016-08-12 06:59:57平台类型:银行,平台代码:GEO_0000000685,注册时间:2016-08-12 06:59:57'
app_info = u'平台类型:银行,平台代码:GEO_0000001806,申请时间:2016-08-12 06:59:57,申请金额区间:0W～0.2W平台类型:银行,平台代码:GEO_0000002633,申请时间:2016-08-12 06:59:57,申请金额区间:0.5W～1W平台类型:银行,平台代码:GEO_0000000685,申请时间:2016-08-12 06:59:57,申请金额区间:10W以上平台类型:非银行,平台代码:GEO_0000184968,申请时间:2016-08-12 06:59:57,申请金额区间:3W～5W'
loan_info = u'平台类型:银行,平台代码:GEO_0000001806,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W平台类型:非银行,平台代码:GEO_0000184968,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W平台类型:银行,平台代码:GEO_0000000685,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W平台类型:银行,平台代码:GEO_0000002633,放款时间:2016-08-12 06:59:57,放款金额区间:0.2W～0.5W'
rej_info = u'平台类型:非银行,平台代码:GEO_0000001668,驳回时间:2017-01-30 12:10:01平台类型:非银行,平台代码:GEO_0000001668,驳回时间:2017-03-08 11:20:00'

#注册统计
reg = len(re.findall(u'平台类型',reg_info))
reg_Bank = len(re.findall(u'平台类型:银行',reg_info))
reg_NoBank = len(re.findall(u'平台类型:非银行',reg_info))

#申请统计
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

app_Mount = re.findall('\d*\.*\d*[W][～]\d*\.*\d*[W]|10W以上', app_info)
max_app_zone = max_mount(app_Mount)

#放款统计
loan = len(re.findall(u'平台类型', loan_info))
loan_Bank = len(re.findall(u'平台类型:银行', loan_info))
loan_NoBank = len(re.findall(u'平台类型:非银行', loan_info))
loanMount_0t2k = len(re.findall(u'0W～0.2W', loan_info))
loanMount_2t5k = len(re.findall(u'0.2W～0.5W', loan_info))
loanMount_5t10k = len(re.findall(u'0.5W～1W', loan_info))
loanMount_10t30k = len(re.findall(u'1W～3W', loan_info))
loanMount_30t50k = len(re.findall(u'3W～5W', loan_info))
loanMount_50t100k = len(re.findall(u'5W～10W', loan_info))
loanMount_100kt = len(re.findall(u'10W以上', loan_info))

loan_Mount = re.findall('\d*\.*\d*[W][～]\d*\.*\d*[W]|10W以上', loan_info)
max_loan_zone = max_mount(loan_Mount)

#驳回统计
rej = len(re.findall(u'平台类型',rej_info))
rej_Bank = len(re.findall(u'平台类型:银行',rej_info))
rej_NoBank = len(re.findall(u'平台类型:非银行',rej_info))
