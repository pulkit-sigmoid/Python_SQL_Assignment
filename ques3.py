import logging

import pandas
import psycopg2.extras

logging.basicConfig(filename="log.txt",
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

conn = None
cur = None
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

    # Question 3 Read and upload the above xlsx into a new table in the Postgres DB (Sigmoid)

    df = pandas.read_excel('/Users/pulkitgupta/code/PycharmProjects/pythonProject/Python_SQL_Assignment/ques2.xlsx')
    cur.execute("create table if not exists total_compensation ("
                "empno NUMERIC(4),"
                "ename VARCHAR(10),"
                "dname VARCHAR(14),"
                "compensation NUMERIC(8),"
                "months NUMERIC(2));")
    logging.info("\nTotal Compensation Table Created\n")
    insert_query = "Insert into total_compensation (empno, ename, dname, compensation, months) values (%s,%s,%s,%s,%s)"
    for index, row in df.iterrows():
        cur.execute(insert_query, (
            row['Employee Number'], row['Employee Name'], row['Department Name'], row['Compensation'],
            row['Total Months Spent']))

    conn.commit()


except:
    logging.error("Error During Connection")


finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
