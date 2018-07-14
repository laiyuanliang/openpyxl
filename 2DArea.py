from openpyxl import Workbook
from openpyxl.chart import AreaChart,Reference

wb = Workbook()
ws = wb.active

rows = [['Number', 'Batch 1', 'Batch 2'],
        [12, 50, 40],
        [13, 20, 15],
        [14, 70, 10],
        [15, 90, 20]
]

for row in rows:
    ws.append(row)

chart = AreaChart()
chart.title = 'Area Chart'
chart.style = 12
chart.x_axis.title = 'ID'
chart.y_axis.title = 'Percentage'

cats = Reference(ws, min_col =1, min_row =2, max_row =5)
data = Reference(ws, min_col =2, min_row =1, max_col =3, max_row =5)
chart.add_data(data, titles_from_data =True)
chart.set_categories(cats)

ws.add_chart(chart, 'A10')

wb.save('2DAreachart.xlsx')
