INSERT_AULA = '''insert into aulas(nombre, cod_curso) values (?, ?);'''

UPDATE_AULA = '''update aulas set nombre = ?, cod_curso = ? where cod_aula = ?'''

DELETE_AULA = '''delete from aulas where cod_aula = ?'''

SELECT_ALL_AULAS = '''select * from aulas'''

SELECT_AULA = '''select * from aulas where cod_aula = ?'''