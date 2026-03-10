# Proyecto_Instituto_Tkinter

DANIEL HIDALGO RODRÍGUEZ

PROYECTO INSTITUTO TKINTER SGE

1. Ventana con pantalla dividida para menu y contentpane
2. Pantalla de Login (Usuario: danibnk14, Contraseña: 12345), habilita los botones del menu
para navegar
3. Gestion de alumnos, botones para operaciones CRUD, pantalla dividida para ver datos 
personales del alumno y calificaciones, botones anterior y siguiente para navegar sobre la tabla de alumnos, ver notas 
y exportar e importar calificaciones (para modificar notas, hacerlo en el csv)
4. Gestion de la direccion, botones para hacer operaciones CRUD y treeview para ver todos los
datos de la tabla de profesores
5. Gestion de recursos del instituto, tabview para dividir entre materiales, aulas y 
asignaturas, con botones para operaciones CRUD y treeview para ver todos los datos de las 
tablas
6. Boton de Logout para cerrar sesion y volver a la pantalla de Login

DISEÑO DE LA BASE DE DATOS

                             |-------|
                             | ADMIN |  (Para logearse)
                             |-------|


            ALUMNOS <--------- CURSOS        DIRECCION
            (cod_curso)          |              |
                 |               |--------|     |
                 |               |        |     |
                 |               \/       |     \/ 
                 |             AULAS      |-> ASIGNATURAS
                 |           (cod_curso)       (cod_curso)
                 |               |             (cod_prof)
                 |               \/                | 
                 |           MATERIALES            | 
                 |           (cod_aula)            |
                 |                                 |
                 |-------> CALIFICACIONES <--------|
                            (cod_alum)
                            (cod_asign)

