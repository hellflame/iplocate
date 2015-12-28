

class Mysql:
    def __init__(self, user='root', password='', host='127.0.0.1', db_name='iplocate'):
        import MySQLdb
        self.connect = MySQLdb.connect(host=host,
                                       user=user,
                                       passwd=password,
                                       db=db_name,
                                       charset='utf8')
        self.cursor = self.connect.cursor(cursorclass=MySQLdb.cursors.DictCursor)
        self.db_name = db_name

    def insert(self, ip, loc='', city='', country='', region='', hostname='', org='', postal='', phone=''):
        self.cursor.execute("INSERT INTO ip_locate (ip, loc, city, country, region, hostname, org, postal, phone) "
                            "VALUE ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                                                                                                ip, loc, city,
                                                                                                country, region,
                                                                                                hostname, org,
                                                                                                postal, phone))

    def ip_get(self, ip):
        self.cursor.execute("SELECT * FROM ip_locate WHERE ip = '{}'".format(ip))
        result = self.cursor.fetchone()
        return result

    def create_table(self):
        self.cursor.execute("CREATE TABLE ip_locate ("
                            "ip VARCHAR(40) NOT NULL DEFAULT '0.0.0.0',"
                            "loc VARCHAR(20),"
                            "city VARCHAR(250),"
                            "country VARCHAR(20),"
                            "region VARCHAR(250),"
                            "hostname text,"
                            "org text,"
                            "postal VARCHAR(20),"
                            "phone VARCHAR(20))")

    def clear_all(self):
        self.cursor.execute("DROP TABLE ip_locate")
        self.create_table()

    def update_ip(self, ip, data):
        sql = "UPDATE ip_locate SET "
        for i in data:
            sql += " {} = '{}' ,".format(i, data[i])
        sql = sql[:-1] + " where ip = '{}' ".format(ip)
        self.cursor.execute(sql)

    def __del__(self):
        self.connect.commit()
        self.connect.close()
