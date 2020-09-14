import xlrd


class ReadExcel():
    '''读取Excel'''
    def readExcel(self,fileName,sheetName):
        try:
            data=xlrd.open_workbook(fileName)
            table=data.sheet_by_name(sheetName)
            list_apidata=[]
            nrows=table.nrows
            col=table.row_values(0)
            for rown in range(1,nrows):
                row=table.row_values(rown)
                if row:
                    app={}
                    for i in range(len(col)):
                        app[col[i]]=row[i]
                    list_apidata.append(app)
            return list_apidata
        except FileNotFoundError:
             print("文件不存在",fileName)


if __name__ == '__main__':
    print(ReadExcel().readExcel(r'../data/login_api.xlsx','Sheet1'))