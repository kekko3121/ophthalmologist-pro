import oracledb

class DB():
    
    def __init__(self, username, password, db_service_name, ip, port):
        db_connection_string = f"{username}/{password}@{ip}:{port}/{db_service_name}"
        self.conn = oracledb.connect(db_connection_string)
        self.cursor = self.conn.cursor()

    
    def closeConn(self):
        self.cursor.close()
        self.conn.close()
                        
    def is_Doctor(self, cf):
        self.cursor.execute("SELECT CF FROM MEDICO WHERE CF = :cf", cf = cf)
        result = self.cursor.fetchone()
        if(result):
            return True
        else:
            return False