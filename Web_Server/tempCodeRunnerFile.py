db.ins_patient(data)
            db.ins_prescription(data)
            db.conn_med(current_user.get_id())