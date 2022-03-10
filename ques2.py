import logging

import psycopg2.extras
import xlsxwriter

logging.basicConfig(filename="log.txt",
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = None
cur = None
wb2 = None
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

    # Question 2 Write a python program to list the Total compensation  given till his/her last date or till now of all
    # the employees till date in a xlsx file.

    logging.info("Question 2")
    logging.info("\nTotal Compensation by Employee till date\n")
    cur.execute("select jh.empno as employee_number, emp.ename as employee_name, dept.dname as department_name, "
                "sum(round((jh.enddate - jh.startdate)/30) * jh.sal) as "
                "total_compensation, "
                "sum(date_part('month',age(jh.enddate, jh.startdate))) as employee_month_spent from "
                "jobhist as jh "
                "join dept on "
                "jh.deptno = dept.deptno "
                "join emp on "
                "jh.empno = emp.empno "
                "GROUP BY "
                "jh.empno, emp.ename, dept.dname;")
    data = cur.fetchall()

    logging.info("empno ename dname tot_comm month")
    for record in data:
        logging.info(f"{record['employee_number']} "
                     f"{record['employee_name']} "
                     f"{record['department_name']} "
                     f"{record['total_compensation']} "
                     f"{record['employee_month_spent']}")

    wb2 = xlsxwriter.Workbook('/Users/pulkitgupta/code/PycharmProjects/pythonProject/Python_SQL_Assignment/ques2.xlsx')
    worksheet = wb2.add_worksheet()
    worksheet.write('A1', 'Employee Number')
    worksheet.write('B1', 'Employee Name')
    worksheet.write('C1', 'Department Name')
    worksheet.write('D1', 'Compensation')
    worksheet.write('E1', 'Total Months Spent')

    row = 1
    col = 0
    for num, name, dname, comp, month in data:
        worksheet.write(row, col, num)
        worksheet.write(row, col + 1, name)
        worksheet.write(row, col + 2, dname)
        worksheet.write(row, col + 3, comp)
        worksheet.write(row, col + 4, month)
        row += 1

    conn.commit()

except:
    logging.error("Error During Connection")


finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    if wb2 is not None:
        wb2.close()
