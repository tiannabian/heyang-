__author__ = '何旺彤'

#操作mysql
#pip install pymysql
#pip install mysql-connector-python
from mysql import connector
from complete_test.read_config import ReadConfig
from complete_test.common import project_path

class DoMysql:
    '''操作数据库类，专门进行数据的读写'''
    def do_mysql(self,query,flag=1):#query是查询语句
        '''flag标志  1获取一条数据  2获取多条数据'''
        db_config=ReadConfig(project_path.conf_path).get_data('DB','db_config')
        cnn=connector.connect(**db_config)#建立一个链接
        cursor=cnn.cursor()

        cursor.execute(query)
        if flag==1:
        #第四步：获取结果打印结果
        #每一个符合条件的数据都会存在元组里面
            res=cursor.fetchone()#返回的元祖
        else:
            res=cursor.fetchall()#返回的是列表嵌套元组
        return res

if __name__ == '__main__':
    pass
    query='select max(Id) from loan where MemberID=1123888'
    DoMysql().do_mysql(query,1)
