INSERT_MATERIALES = '''insert into materiales(nombre, coste, cod_aula) values(?, ?, ?);'''

UPDATE_MATERIALES = '''update materiales set nombre = ?, coste = ?, cod_aula = ? where cod_mat = ?'''

DELETE_MATERIALES = '''delete from materiales where cod_mat = ?'''

SELECT_ALL_MATERIALES = '''select * from materiales'''

SELECT_MATERIAL = '''select * from materiales where cod_mat = ?'''