Create Database Proyecto;
Use Proyecto;

CREATE TABLE Estudiantes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido_paterno VARCHAR(50) NOT NULL,
    apellido_materno VARCHAR(50) NOT NULL,
    carrera VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    calle VARCHAR(100) NOT NULL,
    colonia VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL
);
SELECT * FROM Estudiantes;