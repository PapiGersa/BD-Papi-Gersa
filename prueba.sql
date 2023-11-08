
import sqlite3

# Establecer una conexión con la base de datos
conn = sqlite3.connect('ConexionDB.php')  # Reemplaza 'nombre_de_tu_base_de_datos.db' con el nombre de tu base de datos.

# Crear la vista 'studentsANDteachers'
create_view_query = """
CREATE VIEW studentsANDteachers AS
SELECT estudiantes.*, cuentas.username AS Profe
FROM estudiantes
INNER JOIN cuentas ON estudiantes.prof_autor = cuentas.id_user;
"""

# Ejecutar la consulta para crear la vista
conn.execute(create_view_query)

# Realizar selecciones de datos
select_cuentas_query = "SELECT * FROM cuentas;"
select_estudiantes_query = "SELECT * FROM estudiantes;"
select_studentsANDteachers_query = "SELECT * FROM studentsANDteachers;"

# Ejecutar las consultas y obtener resultados
cuentas_result = conn.execute(select_cuentas_query).fetchall()
estudiantes_result = conn.execute(select_estudiantes_query).fetchall()
studentsANDteachers_result = conn.execute(select_studentsANDteachers_query).fetchall()

# Cerrar la conexión con la base de datos
conn.close()

# Imprimir los resultados
print("Tabla cuentas:")
for row in cuentas_result:
    print(row)

print("Tabla estudiantes:")
for row in estudiantes_result:
    print(row)

print("Vista studentsANDteachers:")
for row in studentsANDteachers_result:
    print(row)
