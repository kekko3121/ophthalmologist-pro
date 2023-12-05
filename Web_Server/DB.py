import oracledb

class DB():
    
    def __init__(self, username, password, db_service_name, ip, port):
        dsn = oracledb.makedsn(ip, port, service_name=db_service_name)
        self.conn = oracledb.connect(user = username, password = password, dsn = dsn)
        self.cursor = self.conn.cursor()
    
    def closeConn(self):
        self.cursor.close()
        self.conn.close()
                        
    def seekMed(self, cf):
        self.cursor.execute("SELECT CF FROM MEDICO WHERE CF = :cf")
        result = self.cursor.fetchall()
        print(result[0])