import pandas as pd
import random
from faker import Faker

def generate_buyers(input_csv, output_csv, start_row=1000001, num_records=None):
    """
    Genera un archivo CSV con datos de compradores, incluyendo direcciones y países, basado en un archivo de usuarios.

    Args:
        input_csv (str): Ruta del archivo CSV de entrada que contiene los usernames.
        output_csv (str): Ruta del archivo CSV de salida para los compradores generados.
        start_row (int): Fila inicial desde donde empezar a leer en el archivo de entrada.
        num_records (int, optional): Número de registros a procesar. Si es None, procesará hasta el final del archivo.

    Returns:
        None
    """
    # Configurar Faker con localizaciones por país
    fake_generators = {
        country: Faker(locale) for country, locale in {
            # América del Norte
            "United States": "en_US",
            "Canada": "en_CA",
            "Mexico": "es_MX",

            # América Latina
            "Argentina": "es_AR",
            "Brazil": "pt_BR",
            "Chile": "es_CL",
            "Colombia": "es_CO",
            "Peru": "es_ES",
            "Uruguay": "es_ES",
            "Ecuador": "es_ES",
            "Bolivia": "es_ES",

            # Europa Occidental
            "Spain": "es_ES",
            "France": "fr_FR",
            "Germany": "de_DE",
            "Italy": "it_IT",
            "United Kingdom": "en_GB",

            # Europa del Este y Rusia
            "Russia": "ru_RU",
            "Poland": "pl_PL",

            # Países Nórdicos
            "Sweden": "sv_SE",
            "Norway": "no_NO",
            "Denmark": "da_DK",
            "Finland": "fi_FI",

            # Asia
            "China": "zh_CN",
            "India": "en_IN",
            "Japan": "ja_JP",
            "South Korea": "ko_KR",

            # Oceanía
            "New Zealand": "en_NZ",
            "Australia": "en_AU",
        }.items()
    }

    # Leer usuarios desde el archivo CSV
    usuarios_df = pd.read_csv(input_csv, usecols=["username"], skiprows=range(1, start_row), nrows=num_records, header=0)
    usuarios = usuarios_df["username"].tolist()

    # Generar datos de compradores
    compradores = []
    for username in usuarios:
        pais = random.choice(list(fake_generators.keys()))
        fake = fake_generators[pais]
        compradores.append({
            "Username": username,
            "Direccion_Envio": fake.address().replace("\n", ", "),
            "Pais": pais,
        })

    # Convertir los datos a un DataFrame
    compradores_df = pd.DataFrame(compradores)

    # Exportar a un archivo CSV
    compradores_df.to_csv(output_csv, index=False)
    print(f"Registros generados para la tabla Comprador y guardados en: {output_csv}")
