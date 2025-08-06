import sqlite3

class ConexionDB:
    def __init__(self,ruta="db_Kafe.db"):
        self.ruta = ruta
        self.cnx = sqlite3.connect(self.ruta)
        self.cursor = self.cnx.cursor()

    def crear_db(self):
        self.tabla_users()
        self.tabla_productos()
        self.tabla_pedidos()
        self.tabla_intermedia()

    def tabla_users(self):
        self.cursor.execute('''
        create table if not exists usuarios(
            id_user integer primary key autoincrement,
            nombre text not null,
            gmail text unique not null,
            username text unique not null,
            password text not null
        )
        ''')
        self.cnx.commit()

    def tabla_productos(self):
        self.cursor.execute('''
        create table if not exists productos(
            id_prod integer primary key autoincrement,
            nombre text not null,
            precio real not null,
            tipo text not null check(tipo in('bebida','consumible'))
        )
        ''')
        self.cnx.commit()

    def tabla_intermedia(self):
        self.cursor.execute('''
        create table if not exists pedido_producto(
            id_order integer,
            id_prod integer,
            cantidad integer not null,
            foreign key (id_order) references pedidos(id_order),
            foreign key (id_prod) references productos(id_prod),
            primary key (id_order,id_prod)
        )
        ''')
        self.cnx.commit()

    def tabla_pedidos(self):
        self.cursor.execute('''
        create table if not exists pedidos(
            id_order integer primary key autoincrement,
            id_user integer,
            cliente text not null,
            num_cups integer not null,
            pay_mtd text not null check (pay_mtd in ('fisico','yape')),
            cuenta real not null,
            estado text not null check (estado in ('pendiente','enviado')),
            pago boolean not null default 0,
            fecha text not null,
            foreign key (id_user) references usuarios(id_user)
        )
        ''')
        self.cnx.commit()

    def cerrar_db(self):
        self.cnx.close()