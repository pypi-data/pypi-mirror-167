import win32com
from win32com.client import Dispatch
import requests
import json
import re
##文件加密
class set_password:
    def set_password_file(self,old_name,new_name,old_psw,new_psw):
        """

        :param old_name: 老文件名
        :param new_name:
        :param old_psw: old_psw 为当前打开密码, 若无 访问密码, 则设为 ''
        :param new_psw: 可以新设置一个密码
        :return:
        """
        xcl = win32com.client.Dispatch("Excel.Application")
        # 路径为绝对路径，不能为相对路径报错
        wb = xcl.Workbooks.Open(old_name, False, False, None, old_psw)
        xcl.DisplayAlerts = False

        # 保存时可设置访问密码.
        wb.SaveAs(new_name, None, new_psw, '')
        xcl.Quit()
###发送钉钉
class send_ding:
    def __init__(self,message,webhook):
        self.message=message
        self.webhook=webhook
    def send_message(self):
        # 发送钉钉通知
        headers = {'Content-Type': 'application/json'}
        contents = {
            "at": {"atMobiles": '', "isAtAll": False},
            "text": {"content": self.message},
            "msgtype": "text"}
        requests.post(self.webhook, data=json.dumps(contents), headers=headers)

    def send_atmessage(self,mobile:list):
        # 发送钉钉通知
        headers = {'Content-Type': 'application/json'}
        contents = {
            "at": {"atMobiles": mobile, "isAtAll": False},
            "text": {"content": self.message},
            "msgtype": "text"}
        requests.post(self.webhook, data=json.dumps(contents), headers=headers)

    def send_markdown(self,img):
        headers = {"Content-Type": "application/json ;charset=utf-8 "}
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "钉钉签到",
                "text": "![图片](%s)%s" % (img, self.message)
            },
            "at": {"atMobiles": False,
                   "isAtAll": True}
        }
        messagebody = json.dumps(data)
        response = requests.post(url=self.webhook, data=messagebody, headers=headers)
        print(response.text)
####运行sql类
class run_sql:
    def __init__(self,sql,con):
        self.sql=sql
        self.con=con
    def run(self):
        cur=self.con.cursor()
        if re.search('create',self.sql,flags=re.IGNORECASE) or re.search('drop',self.sql,flags=re.IGNORECASE) or re.search('delete',self.sql,flags=re.IGNORECASE) or re.search('insert into',self.sql,flags=re.IGNORECASE) or re.search('grant',self.sql,flags=re.IGNORECASE):
            cur.execute(self.sql)
            cur.execute('commit')
        else:
            data=cur.execute(self.sql).fetchall()
            return data
    def insert(self,data,table):
        cur = self.con.cursor()
        for i in range(len(data)):
            s = 'insert into %s values('%table + '\'' + '\',\''.join(data[i].astype('str')) + '\')'
            cur.execute(s)
            if i % 1000 == 0:
                cur.execute('commit')
        cur.execute('commit')
###写入excel
class to_excel:
    def __init__(self,data,sheetname,row,col):
        self.data=data
        self.sheet=sheetname
        self.row=row
        self.col=col
    def excel(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.sheet.cell(row=self.row+i,column=self.col+j).value=self.data[i][j]
####数据库密码
class password:
    def __init__(self):
        self.password_path=r'D:\0-客户数据调度执行文件\password.txt'
    def password_sql(self,database):

        with open(self.password_path, 'r', encoding='utf8') as f:
            passwords=f.read().split('\n')
        if database=='yxdbnew':
            password=passwords[0].split('\t')[1]
        elif database=='yxcdc':
            password = passwords[1].split('\t')[1]
        elif database == 'yxdb':
            password = passwords[2].split('\t')[1]
        elif database == 'yxcdc2':
            password = passwords[4].split('\t')[1]
        elif database == 'cdms':
            password = passwords[6].split('\t')[1]
        else:
            pass
        return password

#######路径
class paths:
    def __init__(self,classes,if_true=True,ip=''):
        self.ip=ip
        self.classes=classes
        self.if_true=if_true
        self.path=self.run()
    def run(self):
        if self.classes=='dirs' and self.if_true==False:
            path=f'\\\\{self.ip}\\客户销售部\\1、市场管理室\\【工作组】数据ETL\\sqls\\'
        elif self.classes=='dirs' and self.if_true==True:
            path = 'D:\\客户销售部\\1、市场管理室\\【工作组】数据ETL\\sqls\\'
        elif self.classes=='savepath' and self.if_true==False:
            path = f'\\\\{self.ip}\\客户销售部\\1、市场管理室\\【1】每日报表\\'
        elif self.classes=='savepath' and self.if_true==True:
            path = 'D:\\客户销售部\\【工作组】客销数据管理\\【客销报表】\\'
        else:
            pass
        return path



