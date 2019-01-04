from openpyxl import *
from classes import Store_data,root


def main():
    try:
        wb = load_workbook('excel.xlsx')
        sheet = wb.active
        obj1 = Store_data(sheet)
        obj1.layout()
        root.mainloop()
        obj1.excel()
        obj1.insert()
        wb.save('excel.xlsx')
    except PermissionError:
        print('Permission denied : excel.xlsx file is already opened for other use')