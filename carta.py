import os
import csv
import random
from faker import Faker

faker = Faker()

productos_csv_path = "data/producto/productos.csv"

def cargar_productos_carta():
    cartas = []
    with open(productos_csv_path, mode="r", encoding="utf-8") as file:
        next(file)  # Skip the header
        for line in file:
            datos = line.strip().split(",")
            if datos[3] == "Carta":
                cartas.append(datos[0])  # Product ID
    return cartas

def generar_cartas():
    os.makedirs("data/Carta", exist_ok=True)
    cartas = cargar_productos_carta()
    carta_id_counter = 1  # Initialize the counter

    with open("data/Carta/cartas.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Producto_ID", "ID", "Descripcion", "Rareza", "Estado"])
        for producto_id in cartas:
            writer.writerow([
                producto_id,
                carta_id_counter,  # Use the counter for Carta_ID
                faker.sentence(),
                random.choice(["Common", "Uncommon", "Rare", "Special", "Promotional"]), # Rareza
                random.choice(["Poor", "Played", "Light Played", "Good", "Excellent", "Mint"]) # Estado
            ])
            carta_id_counter += 1  # Increment the counter
