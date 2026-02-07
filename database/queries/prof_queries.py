CREATE_TABLE_PROFESORES = '''create table if not exists profesores(
    cod_prof INTEGER primary key AUTOINCREMENT,
    nombre text not null,
    apellidos text not null,
    cargo text not null,
    correo text CHECK (correo like '%@%') not null
);'''

INSERTS_PROFESORES = '''INSERT INTO profesores (nombre, apellidos, cargo, correo)
VALUES (?, ?, ?, ?);
'''

SELECT_ALL_PROFESORES = '''select cod_prof, nombre, apellidos, cargo, correo from profesores'''

SELECT_PROFESOR_BY_ID = 'select cod_prof, nombre, apellidos, cargo, correo from profesores WHERE cod_prof = ?'

# Deletes
DELETE_PROFESORES = 'DELETE FROM profesores WHERE cod_prof = ? '

# Updates
UPDATE_PROFESORES = '''
    UPDATE profesores 
    SET nombre = ?, apellidos = ?, cargo = ?, correo = ?
    WHERE cod_prof = ?
'''