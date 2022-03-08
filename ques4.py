import logging

import psycopg2.extras
import xlsxwriter

logging.basicConfig(filename="log.txt",
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = None
cur = None
wb3 = None
try:

    conn = psycopg2.connect(
        host="localhost",
        dbname="Sigmoid",
        user="postgres",
        password="1234",
        port="5432"
    )
    logging.info("Connection Successful")

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Question 4 From the xlsx in 2) create another xlsx to list total compensation given at Department level till date.
    # Columns: Dept No, Dept,Name, Compensation

    logging.info("\nTotal Compensation by Department till date\n")
    cur.execute("select dept.deptno as department_number, dept.dname as department_name, sum(com.compensation) "
                "as compensation from total_compensation as com "
                "join dept "
                "on "
                "com.dname=dept.dname "
                "group by dept.deptno, dept.dname;")
    data = cur.fetchall()

    logging.info("deptno dname compensation")
    for record in data:
        logging.info(f"{record['department_number']} "
                     f"{record['department_name']} "
                     f"{record['compensation']}")

    wb3 = xlsxwriter.Workbook('/Users/pulkitgupta/code/PycharmProjects/pythonProject/Python_SQL_Assignment/ques3.xlsx')
    worksheet = wb3.add_worksheet()
    worksheet.write('A1', 'Department Number')
    worksheet.write('B1', 'Department Name')
    worksheet.write('C1', 'Compensation')

    row = 1
    col = 0
    for number, name, comp in data:
        worksheet.write(row, col, number)
        worksheet.write(row, col + 1, name)
        worksheet.write(row, col + 2, comp)
        row += 1

    conn.commit()


except:
    logging.error("Error During Connection")


finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    if wb3 is not None:
        wb3.close()
