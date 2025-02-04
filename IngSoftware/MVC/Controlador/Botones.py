from IngEconomica.MVC.Modelo.Estudiante import Estudiante


class Controlador:
    def __init__(self, vista, db):
        self.vista = vista
        self.db = db
        self.vista.btn_guardar.clicked.connect(self.guardar_estudiante)

    def guardar_estudiante(self):
        print("🔄 Intentando guardar estudiante...")

        matricula = self.vista.input_matricula.text()
        nombre = self.vista.input_nombre.text()
        ap_paterno = self.vista.input_apellido_paterno.text()
        ap_materno = self.vista.input_apellido_materno.text()
        carrera = self.vista.input_carrera.text()
        edad = self.vista.input_edad.text()
        calle = self.vista.input_calle.text()
        colonia = self.vista.input_colonia.text()
        ciudad = self.vista.input_ciudad.text()
        cp = self.vista.input_cp.text()

        if not all([matricula, nombre, ap_paterno, ap_materno, carrera, edad, calle, colonia, ciudad, cp]):
            print("❌ Error: Todos los campos deben estar llenos")
            return

        try:
            edad = int(edad)  # Convierte edad a entero
        except ValueError:
            print("❌ Error: La edad debe ser un número entero")
            return

        estudiante = Estudiante(matricula, nombre, ap_paterno, ap_materno, carrera, edad, calle, colonia, ciudad, cp)

        try:
            print(f"Guardando estudiante: {estudiante.nombre} {estudiante.ap_paterno}...")
            self.db.guardar_estudiante(estudiante)
            print("✅ Estudiante guardado correctamente")
        except Exception as e:
            print(f"❌ Error al guardar en la base de datos: {e}")


