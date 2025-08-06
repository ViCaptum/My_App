from conexion import ConexionDB

class PedidoModel:
    def __init__(self):
        self.db = ConexionDB()

    def crear_pedido(self, id_user, cliente, num_cups, pay_mtd, cuenta, estado, pago, fecha):
        try:
            self.db.cursor.execute('''
                INSERT INTO pedidos (id_user, cliente, num_cups, pay_mtd, cuenta, estado, pago, fecha)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (id_user, cliente, num_cups, pay_mtd, cuenta, estado, pago, fecha))
            self.db.cnx.commit()
            return True
        except Exception as e:
            print("Error al crear pedido:", e)
            return False

    def get_pedidos(self):
        try:
            self.db.cursor.execute('SELECT * FROM pedidos')
            rows = self.db.cursor.fetchall()
            pedidos = [dict(row) for row in rows]
            return pedidos
        except Exception as e:
            print("Error al obtener pedidos:", e)
            return []

    def get_pedido_por_id(self, id_order):
        try:
            self.db.cursor.execute('SELECT * FROM pedidos WHERE id_order = ?', (id_order,))
            row = self.db.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            print("Error al obtener pedido:", e)
            return None

    def actualizar_estado(self, id_order, nuevo_estado=None, pago_realizado=None):
        try:
            if nuevo_estado and pago_realizado is not None:
                self.db.cursor.execute('''
                    UPDATE pedidos
                    SET estado = ?, pago = ?
                    WHERE id_order = ?
                ''', (nuevo_estado, pago_realizado, id_order))
            elif nuevo_estado:
                self.db.cursor.execute('''
                    UPDATE pedidos
                    SET estado = ?
                    WHERE id_order = ?
                ''', (nuevo_estado, id_order))
            elif pago_realizado is not None:
                self.db.cursor.execute('''
                    UPDATE pedidos
                    SET pago = ?
                    WHERE id_order = ?
                ''', (pago_realizado, id_order))
            else:
                return False  # No hay cambios

            self.db.cnx.commit()
            return True
        except Exception as e:
            print("Error al actualizar estado del pedido:", e)
            return False

    def eliminar_pedido(self, id_order):
        try:
            self.db.cursor.execute('DELETE FROM pedidos WHERE id_order = ?', (id_order,))
            self.db.cnx.commit()
            return True
        except Exception as e:
            print("Error al eliminar pedido:", e)
            return False

    def cerrar_conexion(self):
        self.db.cnx.close()