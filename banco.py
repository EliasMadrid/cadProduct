
import _sqlite3

conn = _sqlite3.connect('cadastro_produtos.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    preco TEXT NOT NULL,
    categoria TEXT NOT NULL                
        
);
""")
print("Conectado com suscesso")