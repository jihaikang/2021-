# from openpyxl import load_workbook 

# workbook = load_workbook(filename = r'D:\囧包子\Documents\ifma.xlsx')
#     # data =('D:\囧包子\Documents\ifma.xlsx')
# print(workbook.sheetnames)
# # table1 = data.sheet_by_name
# sheet = workbook['Sheet3'] # 列表中括号
# # cell = sheet['A:B']#记得大冒号
# # 获取行列，坐标
# # print(cell.row,cell.column,cell.coordinate) 
# # print(cell)
# print(sheet.cell(3,1).value)
# for i in range(1,2):
#     print('happy')

items = ['Fruits','Books','Others']
p = [96,78,85,100,120]
d = {item.upper():p  for item,p in zip(items,p)}
print(d)