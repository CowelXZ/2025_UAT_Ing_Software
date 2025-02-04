import pyodbc
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=TU_SERVIDOR;"
    "DATABASE=TU_BASE_DE_DATOS;"
    "UID=TU_USUARIO;"
    "PWD=TU_CONTRASEÑA;"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM TU_TABLA")

for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()
