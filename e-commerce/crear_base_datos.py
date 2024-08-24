import sqlite3

def main():
    query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT(30),
        username TEXT(30),
        password TEXT(30)
    );
    """
    query2 = """
    CREATE TABLE IF NOT EXISTS videojuegos (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT(30),
        plataforma TEXT(30),
        categoria VARCHAR(20) NOT NULL,
        precio INTEGER NOT NULL
    );
    """
    query3 = """
    CREATE TABLE IF NOT EXISTS favoritos (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        videojuegos_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES usuarios(id),
        FOREIGN KEY (videojuegos_id) REFERENCES videojuegos(id)
    );
    """
    query4 = """
    CREATE TABLE IF NOT EXISTS comprados (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id INTEGER NOT NULL,
        videojuegos_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES usuarios(id),
        FOREIGN KEY (videojuegos_id) REFERENCES videojuegos(id)
    );
    """

    with sqlite3.connect("tienda_videojuegos.db") as conn:
        conn.execute(query)
        conn.execute(query2)
        conn.execute(query3)
        conn.execute(query4)

def datos_videojuegos_consulta():
    query = "SELECT nombre, plataforma, categoria, precio FROM videojuegos"

    with sqlite3.connect("tienda_videojuegos.db") as conn:
        cursor = conn.cursor()
        
        conn.commit()
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        return results

def datos_persona_consulta():
    query = "SELECT nombre, username, password FROM usuarios"

    with sqlite3.connect("tienda_videojuegos.db") as conn:
        cursor = conn.cursor()

        conn.commit()

        cursor.execute(query)
        result = cursor.fetchall()

        return result
    
def persona_juego_favoritos(user, password):
    pass

def persona_juegos_comprados(user, password):
    pass


"""  
insertar_videojuegos = 
INSERT INTO videojuegos (nombre, plataforma, categoria, precio) VALUES
('The Legend of Zelda', 'Nintendo Switch', 'Aventura', 599),
('Super Mario Odyssey', 'Nintendo Switch', 'Plataformas', 499),
('Horizon Zero Dawn', 'PlayStation 4', 'Acción', 699),
('God of War', 'PlayStation 4', 'Acción', 649),
('Halo Infinite', 'Xbox Series X', 'FPS', 699),
('Forza Horizon 5', 'Xbox Series X', 'Carreras', 599),
('Minecraft', 'PC', 'Sandbox', 299),
('The Witcher 3', 'PC', 'RPG', 399),
('FIFA 23', 'PlayStation 5', 'Deportes', 499),
('Animal Crossing', 'Nintendo Switch', 'Simulación', 449);

"""
