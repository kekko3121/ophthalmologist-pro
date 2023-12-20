import oracledb

class DB():
    
    def __init__(self, username, password, db_service_name, ip, port):
        try:
            self.conn = oracledb.connect(f"{username}/{password}@{ip}:{port}/{db_service_name}")
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(f"Error during database connection: {e}")

    
    def closeConn(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(f"Error during connection closure: {e}")

    def is_Doctor(self, cf):
        self.cursor.execute("SELECT CF FROM DOCTOR WHERE CF = :cf", cf = cf)
        result = self.cursor.fetchone()
        if result:
            return True
        else:
            return False
    
    def set_patient(self, data):
        self.cursor.execute("INSERT INTO PATIENT VALUES (:cf, :name, :surname)", cf = data.get("cf"), name = data.get("firstname"), surname = data.get("lastname"))