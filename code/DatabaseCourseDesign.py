# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/6/13 20:30
# 文件名：DatabaseCourseDesign.py
# 开发工具：PyCharm
import datetime
from pymysql import *
import json


class BasicSqlOperation(object):
    def __init__(self):
        # 打开数据库连接
        self.db = connect(host='localhost', port=3306, charset='utf8', database='MySQL', password='zyh20000205',
                          user='root')
        # 创建游标对象
        self.cursor = self.db.cursor()
        sql = "use bookshopmanagement"
        self.cursor.execute(sql)

    def showAllTables(self):
        sql = "show tables"
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as err:
            print("SQL执行错误，原因：", err)

    def execute_sql(self, sql):
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误，原因：", err)

    def FindAll(self):
        # 实例变量
        table_name = input("table name")
        # 定义SQL语句
        sql = "select * from %s" % table_name
        try:
            # 执行数据库操作
            self.cursor.execute(sql)
            # 处理结果
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as err:
            print("SQL执行错误，原因：", err)

    def Insert_purchase(self):
        # 实例变量
        isbn = input("isbn")
        price = int(input("price"))
        purchase_num = int(input("num"))
        # 定义SQL语句
        sql = "insert into purchasebook(isbn, price, purchasenum) values('%s','%d','%d')" % \
              (isbn, price, purchase_num)
        self.execute_sql(sql)

    def Insert_reader(self):
        reader_id = int(input("readerid"))
        reader_name = input("name")
        sex = input("sex  (男 or 女)")
        age = int(input("age"))
        tel = input("tel")
        sql = "insert into reader(readerid, readername, sex, age, tel) values('%d','%s','%s','%d','%s')" % (
            reader_id, reader_name, sex, age, tel)
        self.execute_sql(sql)

    def Insert_book(self):
        # 实例变量
        ISBN = input("ISBN:")
        bookname = input("bookname")
        author = input("author")
        price = int(input("proce"))
        # 定义SQL语句
        sql = "insert into book(ISBN, bookname, author, price) values('%s','%s','%s','%d')" % (
            ISBN, bookname, author, price)
        self.execute_sql(sql)

    def Insert_borrow(self):
        # 实例变量
        borrow_time = datetime.datetime.now().strftime("%Y-%m-%d")
        reader_id = input("readerId")
        ISBN = input("ISBN:")
        # 定义SQL语句
        sql = "insert into borrow(BorrowTime, ReaderID, ISBN) values('%s','%s','%s')" % (
            borrow_time, reader_id, ISBN)
        self.execute_sql(sql)

    def Insert_collectionofbook(self):
        # 实例变量
        isbn = input("isbn")
        total_num = int(input("totalnum"))
        # 定义SQL语句
        sql = "insert into collectionofbook(ISBN, totalnum) values('%s','%d')" % (
            isbn, total_num)
        self.execute_sql(sql)

    def Insert_return(self):
        # 实例变量
        return_time = datetime.datetime.now().strftime("%Y-%m-%d")
        reader_id = input("reader_id")
        isbn = input("isbn")
        # 定义SQL语句
        sql = "insert into returnofbook(returntime, readerid, isbn)  values('%s', '%s','%s')" % (
              return_time, reader_id, isbn)
        self.execute_sql(sql)

    def Insert_sell(self):
        # 实例变量
        isbn = input("isbn")
        already_sold = int(input("alreadysold"))
        price = int(input("price"))
        # 定义SQL语句
        sql = "insert into sell(isbn, price, AlreadySold)  values('%s','%d','%d')" % \
              (isbn, price, already_sold)
        self.execute_sql(sql)

    def del_reader(self):
        reader_id = int(input("reader_id"))
        sql = "delete from reader where readerid = " + str(reader_id)
        self.execute_sql(sql)

    # 用析构函数实现数据库关闭
    def __del__(self):
        # 关闭数据库连接
        self.db.close()


class SqlOperation(BasicSqlOperation):
    def __init__(self):
        super().__init__()

    def drop_table(self):
        table_name = input("tablename")
        sql = "drop table " + table_name
        self.execute_sql(sql)

    def Insert_employee(self):
        # 实例变量
        employee_id = int(input("employeeID"))
        employee_name = input("name")
        employee_sex = input("sex  (男 or 女)")
        employee_age = int(input("age"))
        employee_tel = input("tel")
        employee_salary = int(input("salary"))
        # 定义SQL语句
        sql = "insert into employee(employeeid, employname, employsex, employage, employtel, salary) " \
              "values('%d','%s','%s','%d','%s','%d')" % \
              (employee_id, employee_name, employee_sex, employee_age, employee_tel, employee_salary)
        self.execute_sql(sql)

    # 定义删除表数据函数
    def Del(self):
        # 实例变量
        table_name = input("table_name")
        # 定义SQL语句
        sql = "drop table table " + table_name
        self.execute_sql(sql)

    # 定义修改表数据函数
    def Update_empolyee(self):
        employee_id = int(input("employeeID"))
        employee_name = input("name")
        employee_sex = input("sex  (男 or 女)")
        employee_age = int(input("age"))
        employee_tel = input("tel")
        employee_salary = int(input("salary"))
        sql = "update employee set EmployTEL=%s,Salary=%d where EmployeeID = %d" % \
              (employee_tel, employee_salary, employee_id)
        self.execute_sql(sql)

    def del_employee(self):
        employeeid = int(input("employeeid"))
        sql = "delete from employee where employeeid = " + str(employeeid)
        self.execute_sql(sql)


def login(bookshop_admin, bookshop_employee):
    user_id = input("user_id")
    user_password = input("password")
    if user_id in bookshop_admin.keys():
        if bookshop_admin[user_id] == user_password:
            return sql_execute(1)

    elif user_id in bookshop_employee.keys():
        if bookshop_employee[user_id] == user_password:
            return sql_execute(2)

    else:
        print("no such account")
    return 0


def addUser(bookshop_admin, bookshop_employee):
    choice = int(input("admin 1  employee 2"))
    if choice is 1:
        id = input("id")
        password = input("password")

        bookshop_admin[id] = password

    else:
        print(bookshop_employee)
        id = input("id")
        password = input("password")
        bookshop_employee[id] = password
        print(bookshop_employee)


def delUser(bookshop_admin, bookshop_empolee):
    choice = int(input("admin 1  employee 2"))
    if choice is 1:
        id = input("id")
        del bookshop_admin[id]
    else:
        id = input("id")
        del bookshop_empolee[id]


def sql_execute(priority):
    if priority is 1:
        print("admin login in success")
        return 1
    else:
        print("employee login in success")
        return 2


def function_choice_employee():
    continue_flag = True
    employee = BasicSqlOperation()
    while continue_flag:
        print("查看所有列表 1")
        print("查看某个表信息 2")
        print("添加读者 3")
        print("删除读者 4")
        print("添加借阅 5")
        print("添加还书 6")
        print("购入书籍 7")
        print("卖出书籍 8")
        print("添加新出版书籍 9")
        choice = int(input("enter your choice"))
        if choice is 1:
            employee.showAllTables()
        elif choice is 2:
            employee.FindAll(input("table name"))
        elif choice is 3:
            employee.Insert_reader()
        elif choice is 4:
            employee.del_reader()
        elif choice is 5:
            employee.Insert_borrow()
        elif choice is 6:
            employee.Insert_return()
        elif choice is 7:
            employee.Insert_purchase()
        elif choice is 8:
            employee.Insert_sell()
        elif choice is 9:
            employee.Insert_book()
        else:
            print("error")

        continue_flag = input("continue? True or False")


def function_choice_admin(bookshop_admin, bookshop_employee):
    continue_flag = 1
    admin = SqlOperation()
    while continue_flag is 1:
        print("查看所有列表 1")
        print("查看某个表信息 2")
        print("添加读者 3")
        print("删除读者 4")
        print("添加借阅 5")
        print("添加还书 6")
        print("添加雇员 7")
        print("删除雇员 8")
        print("购入书籍 9")
        print("卖出书籍 10")
        print("增加操作用户 11")
        print("删除操作用户 12")
        print("修改员工信息 13")
        print("添加新出版信息 14")

        choice = int(input("enter your choice"))
        if choice is 1:
            admin.showAllTables()
        elif choice is 2:
            admin.FindAll()
        elif choice is 3:
            admin.Insert_reader()
        elif choice is 4:
            admin.del_reader()
        elif choice is 5:
            admin.Insert_borrow()
        elif choice is 6:
            admin.Insert_return()
        elif choice is 9:
            admin.Insert_purchase()
        elif choice is 10:
            admin.Insert_sell()
        elif choice is 8:
            admin.del_employee()
        elif choice is 7:
            admin.Insert_employee()
        elif choice is 11:
            addUser(bookshop_admin, bookshop_employee)
        elif choice is 12:
            delUser(bookshop_admin, bookshop_employee)
        elif choice is 13:
            admin.Update_empolyee()
        elif choice is 14:
            admin.Insert_book()
        else:
            print("error")

        continue_flag = int(input("continue? 1 continue or 0 end"))


def main():
    """read the id and password from txt which is saved in json"""
    file_name_1 = r"admin.txt"
    file_name_2 = r"employee.txt"

    with open(file_name_1, "r") as f:
        js = f.read()
        bookshop_admin = json.loads(js)
    f.close()

    with open(file_name_2, "r") as f:
        js = f.read()
        bookshop_employee = json.loads(js)
    f.close()
    # print(bookshop_employee)
    """login() function will return the priority admin user is 1, employee user is 2 and no such account is 0"""
    priority = login(bookshop_admin, bookshop_employee)
    if priority is 1:
        function_choice_admin(bookshop_admin, bookshop_employee)
    elif priority is 2:
        function_choice_employee()
    elif priority is 0:
        print("log in failed")

    jsOBJ = json.dumps(bookshop_admin)
    with open(file_name_1, "w") as f:
        f.write(jsOBJ)
    f.close()

    jsOBJ = json.dumps(bookshop_employee)
    with open(file_name_2, "w") as f:
        f.write(jsOBJ)
    f.close()


if __name__ == '__main__':
    main()
