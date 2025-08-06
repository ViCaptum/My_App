from conexion import ConexionDB

class ProducModel:
    def __init__(self):
        self.db = ConexionDB()

    def getProduc(self, nombre, precio, tipo):
        try:
            self.db.cursor.execute('insert into (nombre, precio, tipo) values(?,?,?,?)',(nombre, precio, tipo))
            self.db.cnx.commit()
            return True
        except Exception:
            return False

    def del_produc(self, id_prod):
        try:
            self.db.cursor.execute('delete from productos where id_prod = ?',(id_prod))
            self.db.cnx.commit()
            return True
        except Exception:
            return False

    def up_produc(self, id_prod, nombre, precio, tipo):
        try:
            self.db.cursor.execute('update set nombre = ?, precio = ?, tipo = ? where id_prod = ?',(nombre, precio, tipo, id_prod))
            self.db.cnx.commit()
            return True
        except Exception:
            return False:

    def get_produc(self):
        try:
            self.db.cursor.execute('select * productos')
            rows = self.db.cursor.fetchall()
            productos = [dict(row) for row in rows]
            return productos
        except Exception:
            return []

    def cerrar_conexion(self):
        self.db.cnx.close()