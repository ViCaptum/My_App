from conexion import ConexionDB

class PedidoProductoModel:
    def __init__(self):
        self.db = ConexionDB()

    def add_producto_a_pedido(self, id_order, id_prod, cantidad):
        try:
            self.db.cursor.execute('''
                INSERT INTO pedido_producto (id_order, id_prod, cantidad)
                VALUES (?, ?, ?)
            ''', (id_order, id_prod, cantidad))
            self.db.cnx.commit()
            return True
        except Exception as e:
            print("Error al agregar producto al pedido:", e)
            return False

    def remove_producto_de_pedido(self, id_order, id_prod):
        try:
            self.db.cursor.execute('''
                DELETE FROM pedido_producto
                WHERE id_order = ? AND id_prod = ?
            ''', (id_order, id_prod))
            self.db.cnx.commit()
            return True
        except Exception as e:
            print("Error al eliminar producto del pedido:", e)
            return False

    def update_cantidad(self, id_order, id_prod, nueva_cantidad):
        try:
            self.db.cursor.execute('''
                UPDATE pedido_producto
                SET cantidad = ?
                WHERE id_order = ? AND id_prod = ?
            ''', (nueva_cantidad, id_order, id_prod))
            self.db.cnx.commit()
            return True
        except Exception as e:
            print("Error al actualizar cantidad:", e)
            return False

    def get_productos_de_pedido(self, id_order):
        try:
            self.db.cursor.execute('''
                SELECT pp.id_prod, p.nombre, p.precio, pp.cantidad, p.tipo
                FROM pedido_producto pp
                JOIN productos p ON pp.id_prod = p.id_prod
                WHERE pp.id_order = ?
            ''', (id_order,))
            rows = self.db.cursor.fetchall()
            productos = [dict(row) for row in rows]
            return productos
        except Exception as e:
            print("Error al obtener productos del pedido:", e)
            return []

    def cerrar_conexion(self):
        self.db.cnx.close()