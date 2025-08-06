from conexion import ConexionDB

class UserModel:
    def __init__(self):
        self.db = ConexionDB()

    def register_user(self, nombre, gmail, username, password):
        try:
            self.db.cursor.execute('''
                insert into usuarios (nombre, gmail, username, password)
                values (?, ?, ?, ?)
            ''',(nombre, gmail,username, password))
            self.db.cnx.commit()
            return True
        except Exception as e:
            return False

    def del_user(self, id_user):
        try:
            self.db.cursor.execute('delete from usuarios where id_user = ?',(id_user,))
            self.db.cnx.commit()
            return True
        except Exception:
            return False

    def verificar_user(self, username):
        self.db.cursor.execute('select * from usuarios where username = ?',(username,))
        return self.db.cursor.fetchone()
    
    def cerrar_conexion(self):
        self.db.cerrar_db()