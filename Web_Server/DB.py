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
    
    def ins_patient(self, data):
        try: 
            self.cursor.execute("INSERT INTO PATIENT VALUES (:cf, :firstname, :surname)", cf = data.get("cf"), firstname = data.get("firstname"), surname = data.get("lastname"))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()  # Roll back the transaction in case of an error.
    
    def ins_prescription(self, data):
        try:
            self.cursor.execute("""INSERT INTO PRESCRIPTION (PRESCRIPTION_DATE, PRESCRIPTION_DUR, INTERPUPILLARY_DIST, SEMIDAV, CORNEAL_APEX_DIST, 
                                PANTHOSCOPIC_ANGLE, INSET, LENS_TYPE, CF_PAZ)
                                VALUES (SYSDATE, ADD_MONTHS(SYSDATE, 1), :interpupillary, :semidav, :corneal, :panthoscopic, :inset, :lens, :cf)""",
                                interpupillary=data.get("interpupillary"), semidav=data.get("semidav"), corneal=data.get("corneal"),
                                panthoscopic=data.get("panthoscopic"), inset=data.get("inset"), lens=data.get("lens"), cf=data.get("cf"))


            self.cursor.execute("SELECT NUM_PRESCRIPTION_INC.CURRVAL FROM dual")
            
            result = self.cursor.fetchone()[0]
            
            self.cursor.execute("INSERT INTO FAR VALUES(:num_prescr, :left_axle, :right_axle, :left_sphere, :right_sphere, :left_cylinder, :right_cylinder)", 
                              num_prescr = result, right_sphere = float(data.get("sferoSelect")), right_cylinder = float(data.get("sferoSelect1")), 
                              right_axle = float(data.get("sferoSelect2")), left_sphere = float(data.get("sferoSelect3")), left_cylinder = float(data.get("sferoSelect4")), 
                              left_axle = float(data.get("sferoSelect5")))

            self.cursor.execute("INSERT INTO DURATIONS VALUES(:num_prescr, :left_axle, :right_axle, :left_sphere, :right_sphere, :left_cylinder, :right_cylinder)",
                              num_prescr = result, right_sphere=data.get("sferoSelect6"), right_cylinder=data.get("sferoSelect7"), right_axle=data.get("sferoSelect8"),
                              left_sphere=data.get("sferoSelect9"), left_cylinder=data.get("sferoSelect10"), left_axle=data.get("sferoSelect11"))

            self.cursor.execute("INSERT INTO NEAR VALUES(:num_prescr, :left_axle, :right_axle, :left_sphere, :right_sphere, :left_cylinder, :right_cylinder)",
                              num_prescr = result, right_sphere=data.get("sferoSelect12"), right_cylinder=data.get("sferoSelect13"), right_axle=data.get("sferoSelect14"),
                              left_sphere=data.get("sferoSelect15"), left_cylinder=data.get("sferoSelect16"), left_axle=data.get("sferoSelect17"))

            self.cursor.execute("INSERT INTO NOTE VALUES(:num_prescr, :othernote, :finalnote)", num_prescr = result, 
                              othernote = data.get("othernote"), finalnote = data.get("finalnote"))

            self.cursor.execute("INSERT INTO TREATMENT VALUES(:num_prescr, :hard, :antireflective, :satin, :performance)", num_prescr = result,
                              hard = int(data.get("hard", "0")), antireflective = int(data.get("antireflective", "0")), satin = int(data.get("satin", "0")), 
                              performance = int(data.get("performance", "0")))

            self.conn.commit()

        except Exception as e:
            self.conn.rollback()  # Roll back the transaction in case of an error.

    def conn_med(self, cf_med):
        try:
            self.cursor.execute("SELECT MAX(NUM_PRESCRIPTION) FROM PRESCRIPTION")
            self.cursor.execute("INSERT INTO PRESCRIBES VALUES (:cf, :num)", cf = cf_med, num = self.cursor.fetchone()[0])

            self.conn.commit()

        except Exception as e:
            self.conn.rollback()  # Roll back the transaction in case of an error.