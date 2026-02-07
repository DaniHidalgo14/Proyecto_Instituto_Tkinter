CREATE_TABLE_ALUMNOS = '''create table if not exists alumnos(
    cod_alum INTEGER primary key AUTOINCREMENT,
    nombreCompleto varchar2(50),
    edad INTEGER,
    telefono INTEGER,
    direccion varchar2(70),
    cod_curso integer references curso(cod_curso)
);'''

INSERT_ALUMNOS = '''INSERT INTO alumnos (nombreCompleto, edad, telefono, direccion)
VALUES (?, ?, ?, ?, ?);
'''

SELECT_ALL_ALUMNOS = '''select cod_alum, nombreCompleto, edad, telefono, direccion, cod_curso from alumnos'''

SELECT_ALUMNO = '''select cod_alum, nombreCompleto, edad, telefono, direccion, cod_curso from alumnos where cod_alum = ?'''

DELETE_ALUMNO = '''delete from alumnos where cod_alum = ?'''

UPDATE_ALUMNO = '''update alumnos 
                    set nombreCompleto = ?, edad = ?, telefono = ?, direccion = ?, cod_curso = ?
                    where cod_alum = ?'''