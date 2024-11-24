from usuarios import generate_users
from vendedores import generate_vendors
from compradores import generate_buyers
import producto
import carta
import booster_box
import set


# Configuración de parámetros
output_file_users = r"C:\Users\tokio\OneDrive\Escritorio\faker\user_data_2m.csv"
output_file_vendors = r"C:\Users\tokio\OneDrive\Escritorio\faker\vendedores1m.csv"
output_file_buyers = r"C:\Users\tokio\OneDrive\Escritorio\faker\compradores1m.csv"

num_records_users = 1_000_000
num_records_buyers = 1_000_000

# Paso 1: Generar usuarios
generate_users(output_file_users, num_records_users)

# Paso 2: Generar vendedores utilizando el archivo de usuarios generado
generate_vendors(output_file_users, output_file_vendors, num_records_users)

# Paso 3: Generar compradores utilizando el archivo de usuarios generado
generate_buyers(output_file_users, output_file_buyers, start_row=1000001, num_records=num_records_buyers)



print("Generando Sets...")
set.generar_sets()

print("Generando Productos...")
producto.generar_productos()

print("Generando Cartas...")
carta.generar_cartas()

print("Generando Booster Boxes...")
booster_box.generar_booster_boxes()


