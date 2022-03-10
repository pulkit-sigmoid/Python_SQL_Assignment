import logging

import psycopg2.extras
import xlsxwriter

logging.basicConfig(filename="log.txt",
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = None
cur = None
wb1 = None
try:

    conn = psycopg2.connect(
        host="localhost",
        dbname="Sigmoid",
        user="postgres",
        password="Pulkit@22",
        port="5432"
    )
    logging.info("Connection Successful")

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Question 1 Write a Python program to list employee numbers, names and their managers and save in a xlsx file.

    logging.info("\nQuestion1")
    logging.info("\nList of employee numbers, names and their managers are\n")
    cur.execute("SELECT a.empno as Employee_Number, a.ename as Employee_Name, b.ename as Manager_Name from emp as a "
                "left join emp "
                "as b on "
                "b.empno=a.mgr")
    data = cur.fetchall()

    logging.info("empno ename mgr_name")
    for record in data:
        logging.info(f"{record['employee_number']} "
                     f"{record['employee_name']} "
                     f"{record['manager_name']}")  # always write column name # in small letters

    wb1 = xlsxwriter.Workbook('/Users/pulkitgupta/code/PycharmProjects/pythonProject/Python_SQL_Assignment/ques1.xlsx')
    worksheet = wb1.add_worksheet()
    worksheet.write('A1', 'Employee Number')
    worksheet.write('B1', 'Employee Name')
    worksheet.write('C1', 'Manager Name')

    row = 1
    col = 0
    for num, name, mgr in data:
        worksheet.write(row, col, num)
        worksheet.write(row, col + 1, name)
        worksheet.write(row, col + 2, mgr)
        row += 1

    conn.commit()


except:
    logging.error("Error During Connection")


finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    if wb1 is not None:
        wb1.close()
