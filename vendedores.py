import pandas as pd
import random
from faker import Faker

def generate_vendors(input_csv, output_csv, num_records):
    """
    Genera un archivo CSV con datos de vendedores basado en usernames de un archivo existente.

    Args:
        input_csv (str): Ruta del archivo CSV de entrada que contiene los usernames.
        output_csv (str): Ruta del archivo CSV de salida para los vendedores generados.
        num_records (int): Número de registros a procesar desde el archivo de entrada.

    Returns:
        None
    """
    # Configurar Faker
    fake = Faker()

    # Leer el archivo CSV de entrada y extraer usernames
    usuarios_df = pd.read_csv(input_csv, usecols=["username"], nrows=num_records)
    usuarios = usuarios_df["username"].tolist()

    # Lista para almacenar los registros generados para Vendedor
    vendedores = []

    # Generar registros para la tabla Vendedor
    for username in usuarios:
        vendedor = {
            "Username": username,
            "Verificado": random.choice([True, False]),
            "Valoracion": round(random.uniform(1.0, 5.0), 2),  # Generar valoración entre 1.0 y 5.0
        }
        vendedores.append(vendedor)

    # Convertir la lista de vendedores a un DataFrame
    vendedores_df = pd.DataFrame(vendedores)

    # Exportar los registros generados a un archivo CSV
    vendedores_df.to_csv(output_csv, index=False)
    print(f"{len(vendedores)} registros de vendedores generados y guardados en: {output_csv}")
