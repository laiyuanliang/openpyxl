# -*- coding: utf-8 -*-
import io,os
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl import load_workbook
import datetime,time
import traceback

sourcefile = u'/root/ms.xlsx' 
outputfile = u'/root/msout-24.xlsx'  
BackTracking_Month = 24

index = 1;

wb = load_workbook(sourcefile)
# sheet = wb[u'内部日志详情']
# sheet = wb[u'工作表1']
sheet = wb.active

wbout = Workbook()
ws = wbout.active
ws.cell(column=1, row=1).value = u"序号"
ws.cell(column=2, row=1).value = u"姓名"
ws.cell(column=3, row=1).value = u"手机号"
ws.cell(column=4, row=1).value = u"身份证号"
ws.cell(column=5, row=1).value = u"创建时间"
ws.cell(column=6, row=1).value = u"信贷平台注册详情(如有多条命中，以分号分隔)"
ws.cell(column=7, row=1).value = u"贷款申请详情"
ws.cell(column=8, row=1).value = u"贷款放款详情"
ws.cell(column=9, row=1).value = u"贷款驳回详情"

writeIndex = 2
try:
    for row in sheet.rows:
        if index > 1:
            serialNO = row[0].value
            if serialNO <> None:
                name = row[1].value
                phoneNO = row[2].value
                IDNO = row[3].value
                EndTime = row[4].value
                Platfrom_Info = row[6].value
                Application_Info = row[7].value
                Loans_Info = row[8].value
                Reject_Info = row[9].value

                # print EndTime
                # print type(EndTime)
                year = EndTime.year
                month = EndTime.month
                days = EndTime.day

                year_delta = BackTracking_Month/12
                month_delta = BackTracking_Month%12

                cmonth = month - month_delta
                # print '%d-%d-%d'%(year,cmonth, days)
                if cmonth <= 0:
                    cmonth = cmonth + 12
                    year = year - 1

                if cmonth == 2:
                    if year % 100 == 0:
                        if year % 400 == 0:
                            if days > 29:
                                days = 29
                        else:
                            if days > 28:
                                days = 28
                    else:
                        if year % 4 == 0:
                            if days > 29:
                                days = 29
                        else:
                            if days > 28:
                                days = 28
                else:
                    if (cmonth == 4 or cmonth == 6 or cmonth == 9 or cmonth == 11) and days == 31:
                        days = 30

                BeginTime = datetime.datetime(year=year-year_delta, month=cmonth, day=days)
                # print BeginTime
                # print EndTime
                #Process Platfrom_Info
                #平台类型:非银行,平台代码:EM21_102062,注册时间:2017/4/16 0:00:00;
                outplatforminfo = []
                if Platfrom_Info != None:
                    Platfrom_Info_list = Platfrom_Info.split(';')
                    for platform in Platfrom_Info_list:
                        timeStr = platform.split(u'注册时间:')[-1]
                        if timeStr != '':
                            time_attribute = timeStr.split(' ')[0].split('-')
                            #print time_attribute
                            platformtime = datetime.datetime(int(time_attribute[0]),int(time_attribute[1]),int(time_attribute[2]))
                            if BeginTime <= platformtime <= EndTime:
                                outplatforminfo.append(platform)

                #Process Application_Info
                #平台类型:非银行,平台代码:EM21_101978,申请时间:2017/3/14 0:00:00,申请金额区间:0W～0.2W
                outApplicationinfo = []
                if Application_Info != None:
                    Application_Info_list = Application_Info.split(';')
                    for Application in Application_Info_list:
                        timeStr = Application.split(u'申请时间:')[-1]
                        if timeStr != '':
                            time_attribute = timeStr.split(',')[0].split(' ')[0].split('-')
                            Applicationtime = datetime.datetime(int(time_attribute[0]),int(time_attribute[1]),int(time_attribute[2]))
                            if BeginTime <= Applicationtime <= EndTime:
                                outApplicationinfo.append(Application)

                #Process Loans_Info
                #平台类型:非银行,平台代码:EM21_100047,放款时间:2016/9/24 0:00:00,放款金额区间:0W～0.2W;
                outLoansinfo = []
                if Loans_Info != None:
                    Loans_Info_list = Loans_Info.split(';')
                    for Loans in Loans_Info_list:
                        timeStr = Loans.split(u'放款时间:')[-1]
                        if timeStr != '':
                            time_attribute = timeStr.split(',')[0].split(' ')[0].split('-')
                            Loanstime = datetime.datetime(int(time_attribute[0]),int(time_attribute[1]),int(time_attribute[2]))
                            if BeginTime <= Loanstime <= EndTime:
                                outLoansinfo.append(Loans)

                # print len(outLoansinfo)
                #Process Reject_Info
                #平台类型:非银行,平台代码:EM21_100830,驳回时间:2016/3/18 0:00:00
                outRejectinfo = []
                if Reject_Info != None:
                    Reject_Info_list = Reject_Info.split(';')
                    for Reject in Reject_Info_list:
                        timeStr = Reject.split(u'驳回时间:')[-1]
                        if timeStr != '':
                            time_attribute = timeStr.split(' ')[0].split('-')
                            Rejecttime = datetime.datetime(int(time_attribute[0]),int(time_attribute[1]),int(time_attribute[2]))
                            if BeginTime <= Rejecttime <= EndTime:
                                outRejectinfo.append(Reject)

                #Process
                # print Platfrom_Info
                # print Application_Info
                # print Loans_Info
                #Write File
                if len(outplatforminfo) > 0 or len(outApplicationinfo) > 0 or len(outLoansinfo) > 0 or len(outRejectinfo) > 0:
                    # print 'write file'
                    ws.cell(column=1, row=writeIndex).value = serialNO
                    ws.cell(column=2, row=writeIndex).value = name
                    ws.cell(column=3, row=writeIndex).value = phoneNO
                    ws.cell(column=4, row=writeIndex).value = IDNO
                    ws.cell(column=5, row=writeIndex).value = EndTime

                    platformStr = ''
                    for platform in outplatforminfo:
                        platformStr = platform + '' + platformStr
                    ws.cell(column=6, row=writeIndex).value = platformStr

                    ApplicationStr = ''
                    for Application in outApplicationinfo:
                        ApplicationStr = Application + '\r' + ApplicationStr
                    ws.cell(column=7, row=writeIndex).value = ApplicationStr

                    LoansStr = ''
                    for Loans in outLoansinfo:
                        LoansStr = Loans + '\r' + LoansStr
                    ws.cell(column=8, row=writeIndex).value = LoansStr

                    RejectStr = ''
                    for Reject in outRejectinfo:
                        RejectStr = Reject + '\r' + RejectStr
                    ws.cell(column=9, row=writeIndex).value = RejectStr

                    writeIndex = writeIndex + 1
            # break
        index += 1
        if index%1000 == 0:
            print index


        #写文件

except Exception , e:
    print traceback.print_exc()
    print u"在第%d行出错"%(index)
finally:
    wbout.save(outputfile)
