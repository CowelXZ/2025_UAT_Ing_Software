import pyodbc

class Database:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={SQL Server};'
                'SERVER=DESKTOP-FDUT0ET\\SQLEXPRESS;'
                'DATABASE=Proyecto;'
                'Trusted_Connection=yes;'
            )
            self.cursor = self.conn.cursor()
            print("✅ Conexión exitosa a la base de datos")
        except Exception as e:
            print(f"❌ Error al conectar a la base de datos: {e}")

    def guardar_estudiante(self, estudiante):
        try:
            query = """INSERT INTO Estudiantes (matricula, nombre, apellido_paterno, apellido_materno, 
                       carrera, edad, calle, colonia, ciudad, cp) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            valores = (estudiante.matricula, estudiante.nombre, estudiante.ap_paterno, estudiante.ap_materno,
                       estudiante.carrera, estudiante.edad, estudiante.calle, estudiante.colonia, estudiante.ciudad, estudiante.cp)
            self.cursor.execute(query, valores)
            self.conn.commit()
            print("✅ Estudiante guardado correctamente en la base de datos.")
        except Exception as e:
            print(f"❌ Error al guardar en la base de datos: {e}")

# Prueba la conexión
if __name__ == "__main__":
    db = Database()
