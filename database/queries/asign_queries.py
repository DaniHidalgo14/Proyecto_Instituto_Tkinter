INSERT_ASIGN = '''INSERT INTO asignaturas (nombre, horas, cod_curso, cod_prof)
VALUES (?, ?, ?, ?);
'''

SELECT_ALL_ASIGNS = '''select * from asignaturas'''

SELECT_ASIGN = '''select * from alumnos where cod_asign = ?'''

DELETE_ASIGN = '''delete from asignaturas where cod_asign = ?'''

UPDATE_ASIGN = '''update asignaturas 
                    set nombre = ?, horas = ?, cod_curso = ?, cod_prof = ?
                    where cod_asign = ?'''