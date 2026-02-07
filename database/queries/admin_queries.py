CREATE_TABLE_ADMINS = '''create table if not exists admins(
    usuario text primary key,
    contrasena text not null
);'''

INSERTS_ADMINS = '''INSERT INTO admins (usuario, contrasena)
VALUES (?, ?);
'''

VALIDAR = '''SELECT USUARIO FROM ADMINS WHERE USUARIO = ? AND CONTRASENA = ?'''