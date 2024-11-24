import os
import csv
import random

productos_csv_path = "data/producto/productos.csv"

def cargar_productos_booster_box():
    booster_boxes = []
    with open(productos_csv_path, mode="r", encoding="utf-8") as file:
        next(file)  # Saltar el encabezado
        for line in file:
            datos = line.strip().split(",")
            if datos[3] == "Booster Box":
                booster_boxes.append(datos[0])  # ID del producto
    return booster_boxes

def generar_booster_boxes():
    os.makedirs("data/BoosterBox", exist_ok=True)
    booster_boxes = cargar_productos_booster_box()

    with open("data/BoosterBox/booster_boxes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Producto_ID", "Descripcion", "Cantidad_Sobres", "Edicion_Especial"])
        for box_id in booster_boxes:
            writer.writerow([
                box_id,
                "Contains exclusive cards and premium items.",
                random.randrange(12, 33, 2),
                random.choices([True, False], [0.2, 0.8])[0]
            ])
