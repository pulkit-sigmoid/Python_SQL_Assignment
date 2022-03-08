import logging
import psycopg2.extras


def connection():
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
        return True

    except:
        logging.error("Error During Connection")


    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


