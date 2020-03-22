import pymysql
import sys
sys.path.append("../../")
from NewsRecSys_myself.settings import DB_HOST,DB_PORT,DB_USER,DB_PASSWD,DB_NAME,ALLOW_TAGS
import os
import xlrd


class WriteToMysql:
    def __init__(self,file):
        self.db = self.connect()
        self.cursor = self.db.cursor()
        self.file = file

    def connect(self):
        db = pymysql.Connect(DB_HOST, DB_USER, DB_PASSWD, DB_NAME, DB_PORT, charset='utf8')
        return db

    def writeNews(self):
        fr = xlrd.open_workbook(self.file).sheets()[0]
        for row in range(1,fr.nrows):
            line = fr.row_values(row, start_colx=0,end_colx=None)
            if line[1] == "国际要闻":
                line[1] = 3
            elif line[1] == "互联网":
                line[1] = 4
            elif line[1] == "经济要闻":
                line[1] = 5
            elif line[1] == "中国军事":
                line[1] = 6
            elif line[1] == "社会公益":
                line[1] = 7
            elif line[1] == "书评":
                line[1] = 8
            elif line[1] == "影视综艺":
                line[1] = 9
            else:
                continue
            # print(line[0],line[1],line[2],line[3],line[4],line[5])
            sql = "insert into new(new_id,new_cate_id,new_time,new_seenum,new_disnum,new_title,new_content) values(" \
                  "'%s','%s','%s','%s','%s','%s','%s')" % (line[0],line[1],line[2],int(line[3]),int(line[4]),line[5],line[6])
            try:
                self.cursor.execute(sql)
                self.db.commit()
            except:
                print("rollback",line)
                self.db.rollback()


if __name__ == "__main__":
    # file_path = "../data/original/"
    # files = os.listdir(file_path)
    # for file in files:
    #     wtm = WriteToMysql(file_path+file)
    #     wtm.writeNews()
    # print("写入表new完成")
    newsim.objects.filter(new_id_base=browse_one['new_id']).order_by("-new_correlation")[:5]