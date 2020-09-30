import pymysql
from retrying import retry

from common.read_excel import ReadExcel


class SqlData():
        # 加载sql,返回数据
    @retry(stop_max_attempt_number=5,wait_random_max=1000)
    def themis_data(sql):
        #连接themis数据库
        con = pymysql.Connect(host='123.206.135.211',
                                   port=3306,
                                   user='vvxxthemis',
                                   password='q3YBGG6JxE67xcYY1s0jIyBY4OmKqhg=',
                                   database='themis')
        cur=con.cursor()
        cur.execute(sql)
        con.commit()
        return cur.fetchall()   #返回查询数据

if __name__ == '__main__':
    data=ReadExcel.readExcel(r'../data/ableSale&enableSale_api.xlsx','Sheet1')
    data_sql=data[0]['sql']
    find=SqlData.themis_data(data_sql)
    print(find)
