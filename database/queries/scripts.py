#CONSULTAS PARA CONSTRUCCION DE LA BASE DE DATOS

#CREAR TABLAS
CREAR_TABLAS = '''CREATE TABLE IF NOT EXISTS profesores(
    cod_prof INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    cargo TEXT NOT NULL,
    correo TEXT NOT NULL CHECK (correo LIKE '%@%')
);

CREATE TABLE IF NOT EXISTS admins(
    usuario TEXT PRIMARY KEY,
    contrasena TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS cursos(
    cod_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT
);

CREATE TABLE IF NOT EXISTS alumnos(
    cod_alum INTEGER PRIMARY KEY AUTOINCREMENT,
    nombreCompleto TEXT,
    edad INTEGER,
    telefono INTEGER,
    direccion TEXT,
    cod_curso INTEGER,
    FOREIGN KEY (cod_curso) REFERENCES cursos(cod_curso)
);

CREATE TABLE IF NOT EXISTS asignaturas(
    cod_asign INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    horas INTEGER,
    cod_prof INTEGER,
    cod_curso INTEGER,
    FOREIGN KEY (cod_prof) REFERENCES profesores(cod_prof),
    FOREIGN KEY (cod_curso) REFERENCES cursos(cod_curso)
);

CREATE TABLE IF NOT EXISTS calificaciones(
    trimestre1 INTEGER CHECK (trimestre1 BETWEEN 1 AND 10),
    trimestre2 INTEGER CHECK (trimestre2 BETWEEN 1 AND 10),
    trimestre3 INTEGER CHECK (trimestre3 BETWEEN 1 AND 10),
    cod_alum INTEGER,
    cod_asign INTEGER,
    PRIMARY KEY (cod_alum, cod_asign),
    FOREIGN KEY (cod_alum) REFERENCES alumnos(cod_alum),
    FOREIGN KEY (cod_asign) REFERENCES asignaturas(cod_asign)
);

CREATE TABLE IF NOT EXISTS aulas(
    cod_aula INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    cod_curso INTEGER,
    FOREIGN KEY (cod_curso) REFERENCES cursos(cod_curso)
);

CREATE TABLE IF NOT EXISTS materiales(
    cod_mat INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    coste REAL,
    cod_aula INTEGER,
    FOREIGN KEY (cod_aula) REFERENCES aulas(cod_aula)
);
'''

#INSERTAR CARGAS INICIALES EN TABLAS
CARGAS_INICIALES = '''
INSERT or ignore INTO admins VALUES('danibnk14', '12345');


INSERT INTO profesores (nombre, apellidos, cargo, correo)
VALUES ('Carmen', 'Limon Echevarria', 'Profesora', 'carmen@centro');

INSERT INTO profesores (nombre, apellidos, cargo, correo)
VALUES ('Jorge', 'Sanchez Perez', 'Jefe de departamento', 'jorge@centro');

INSERT INTO profesores (nombre, apellidos, cargo, correo)
VALUES ('Tomas', 'Fernandez Cotrina', 'Director', 'tomas@centro');

INSERT INTO profesores (nombre, apellidos, cargo, correo)
VALUES ('Monica', 'Marcos Gutierrez', 'Profesora', 'monica@centro');


INSERT INTO cursos (nombre)
VALUES ('DAM');

INSERT INTO cursos (nombre)
VALUES ('DAW');


INSERT INTO alumnos (nombreCompleto, edad, telefono, direccion, cod_curso)
VALUES ('Angel Lopez Ruiz', 19, 67483653, 'Calle Benedicto 13', 1);

INSERT INTO alumnos (nombreCompleto, edad, telefono, direccion, cod_curso)
VALUES ('Hugo Delgado Fernandez', 19, 74557388, 'Calle Carlos III 44', 2);


INSERT INTO asignaturas (nombre, horas, cod_prof, cod_curso)
VALUES ('Sistemas de gestion empresarial', 40, 2, 1);

INSERT INTO asignaturas (nombre, horas, cod_prof, cod_curso)
VALUES ('Programacion de Servicios', 35, 3, 1);

INSERT INTO asignaturas (nombre, horas, cod_prof, cod_curso)
VALUES ('Acceso a Datos', 28, 1, 1);

INSERT INTO asignaturas (nombre, horas, cod_prof, cod_curso)
VALUES ('Despliegue de apps Web', 50, 2, 2);

INSERT INTO asignaturas (nombre, horas, cod_prof, cod_curso)
VALUES ('Diseño de interfaces Web', 42, 4, 2);

INSERT INTO asignaturas (nombre, horas, cod_prof, cod_curso)
VALUES ('Desarrollo Web entorno Servidor', 40, 4, 2);


INSERT INTO aulas (nombre, cod_curso)
VALUES ('Iris', 1);

INSERT INTO aulas (nombre, cod_curso)
VALUES ('Hermes', 2);


INSERT INTO materiales (nombre, coste, cod_aula)
VALUES ('Pizarra digital', 3500, 1);

INSERT INTO materiales (nombre, coste, cod_aula)
VALUES ('Ordenador', 275, 1);

INSERT INTO materiales (nombre, coste, cod_aula)
VALUES ('Servidor', 1200, 1);


INSERT INTO calificaciones (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
VALUES (7, 8, 9, 1, 1);

INSERT INTO calificaciones (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
VALUES (6, 7, 7, 1, 2);

INSERT INTO calificaciones (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
VALUES (9, 8, 9, 1, 3);

INSERT INTO calificaciones (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
VALUES (5, 6, 6, 2, 1);

INSERT INTO calificaciones (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
VALUES (8, 9, 9, 2, 2);

INSERT INTO calificaciones (trimestre1, trimestre2, trimestre3, cod_alum, cod_asign)
VALUES (4, 5, 6, 2, 3);
'''