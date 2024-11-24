import os
import csv
import random
import uuid

sets_csv_path = "data/Set/sets.csv"

prefijos = ["Dragon", "Knight", "Sorcerer", "Angel", "Titan", "Phoenix", "Wolf", "Archon", "Herald", "Guard",
            "Destroyer", "Spirit", "Master", "Shadow", "Demon", "Ray", "Wind", "Fury", "Soul", "Flame",
            "Ninja","Ogre", "Goblin", "Vampire", "Elf", "Dwarf", "Giant", "Fairy", "Mermaid", "Pirate",
            "Warrior", "Mage", "Priest", "Paladin", "Rogue", "Bard", "Druid", "Shaman", "Monk", "Barbarian",
            "Ranger", "Berserker", "Alchemist", "Sorceress", "Enchanter", "Summoner", "Illusionist", "Necromancer"]
sufijos = ["Celestial",
           "Ghost", "Mystic", "Guardian", "of the Abyss", "Eternal", "Shadowy", "Luminous", "of the Storm", "of Eternity", "of Souls", "Avenger", "of Darkness", "of Twilight", "of Judgment", "Primordial", "Eternal"]
colores = ["Red",
           "Blue", "Black", "White", "Green", "Golden", "Silver", "Crimson", "Emerald", "Sapphire", "Amethyst","Ruby", "Topaz", "Obsidian", "Onyx", "Pearl", "Opal", "Jade", "Turquoise", "Coral", "Aquamarine", "Garnet",]
elementos = ["Fire", "Water", "Earth", "Air", "Aether", "Lightning", "Ice", "Crystal", "Shadow", "Light", "Metal", "Wood",
             "Spirit", "Void", "Plasma", "Lava", "Steam", "Mist", "Sand", "Storm",
             "Magma", "Frost", "Thunder", "Rain", "Snow", "Sun", "Moon", "Star", "Galaxy", "Cosmos", "Universe", "Infinity"]



def cargar_sets():
    sets = []
    with open(sets_csv_path, mode="r", encoding="utf-8") as file:
        next(file)
        for line in file:
            nombre = line.split(",")[0]
            sets.append(nombre)
    return sets

def generar_nombre(categoria):
    if categoria == "Carta":
        return f"{random.choice(prefijos)} {random.choice(sufijos)} of {random.choice(colores)} {random.choice(elementos)}"
    else:  # Booster Box
        return f"{random.choice(prefijos)} {random.choice(sufijos)}: {random.choice(elementos)} {random.choice(colores)}"

def generar_productos(num_productos=2000000):
    os.makedirs("data/producto", exist_ok=True)
    sets = cargar_sets()

    with open("data/producto/productos.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nombre", "Precio", "Categoria", "Set_Nombre"])
        for _ in range(num_productos):
            categoria = random.choices(["Carta", "Booster Box"], [0.60, 0.40])[0]
            nombre = generar_nombre(categoria)
            set_nombre = random.choice(sets)
            writer.writerow([
                str(uuid.uuid4())[:12],
                nombre,
                round(random.uniform(1, 100), 2),
                categoria,
                set_nombre
            ])
