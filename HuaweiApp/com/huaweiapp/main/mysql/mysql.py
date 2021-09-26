import pymysql


class mysql:
    conn, cur = None, None

    def __init__(self):
        self.conn = pymysql.Connect(user='root',
                                    password='tqf1234321fqt',
                                    host='localhost',
                                    port=3306,
                                    database='huaweiapp')
        self.cur = self.conn.cursor()

    def execute_(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def select_(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def close_(self):
        self.conn.close()
        self.cur.close()
