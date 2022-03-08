import logging
import psycopg2.extras


def data():
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

        logging.info("\nData in Employee table\n")
        cur.execute("SELECT * FROM emp;")
        for record in cur.fetchall():
            logging.info(record)

        logging.info("\nData in Department table\n")
        cur.execute("SELECT * FROM dept;")
        for record in cur.fetchall():
            logging.info(record)

        logging.info("\nData in Jobhist Table\n")
        cur.execute("SELECT * FROM jobhist;")
        for record in cur.fetchall():
            logging.info(record)

        conn.commit()
        return True

    except:
        logging.error("Error During Connection")


    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

