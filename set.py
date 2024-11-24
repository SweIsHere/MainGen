import os
import csv
import random
from faker import Faker

faker = Faker()

adjetivos_sets = [
    "Mythic", "Epic", "Ancient", "Reborn", "Lost", "Legendary", "Dark", "Radiant", "Ascending",
    "Supreme", "Infinite", "Primordial", "Majestic", "Resplendent", "Unbreakable", "Shadowy",
    "Mystic", "Forgotten", "Vengeful", "Glorious", "Transcendent", "Ethereal", "Timeless",
    "Fabled", "Divine", "Infernal", "Shattered", "Unholy", "Sacred", "Noble", "Celestial",
    "Cosmic", "Astral", "Lunar", "Solar", "Immortal", "Unseen", "Eclipsed", "Haunted",
    "Forsaken", "Boundless", "Immutable", "Omniscient", "Arcane", "Fierce", "Phantom",
    "Vanished", "Eternal", "Crimson", "Abyssal", "Blazing", "Frozen", "Windswept", "Stormborn",
    "Silent", "Hallowed", "Profane", "Enigmatic", "Doomed", "Exalted", "Ruthless", "Dreadful",
    "Sacrosanct", "Paradoxical", "Unending", "Exquisite", "Brilliant", "Fleeting", "Grim",
    "Triumphant", "Wretched", "Majestic", "Ominous", "Serene", "Luminous", "Radiant", "Spectral",
    "Dreaded", "Unyielding", "Veiled", "Vivid", "Bound", "Empowered", "Fractured", "Kindred",
    "Mirrored", "Unforgiving", "Shimmering", "Chaotic", "Peaceful", "Fervent", "Resurgent"]

sustantivos_sets = [
    "Legacy", "Dawn", "Twilight", "Eternity", "Genesis", "Judgment", "Nexus", "Annihilation",
    "Aurora", "Eclipse", "Conspiracy", "Dominion", "Redemption", "Omen", "Cycle", "Void",
    "Clash", "Rebellion", "Horizon", "Cataclysm", "Whisper", "Resurgence", "Balance", "Fate",
    "Prophecy", "Reckoning", "Desolation", "Ascension", "Saga", "Apocalypse", "Labyrinth",
    "Realm", "Pantheon", "Conflict", "Union", "Beacon", "Destiny", "Inferno", "Tranquility",
    "Reverie", "Enigma", "Carnage", "Odyssey", "Tribute", "Chronicle", "Illusion", "Crusade",
    "Vortex", "Sanctuary", "Conviction", "Valor", "Veil", "Hollow", "Elegy", "Tapestry",
    "Equinox", "Mythos", "Rift", "Aegis", "Threshold", "Revelation", "Expanse", "Essence",
    "Oblivion", "Awakening", "Labyrinth", "Dominion", "Convergence", "Effigy", "Collapse",
    "Conflagration", "Shroud", "Serenity", "Pinnacle", "Haven", "Gauntlet", "Ascendancy",
    "Eminence", "Cradle", "Pyre", "Chorus", "Paradox", "Eulogy", "Tempest", "Legacy",
    "Reclamation", "Oblivion", "Remnant", "Labyrinth", "Harmony", "Eclipse", "Reverie",
    "Requiem", "Harbinger", "Covenant", "Reverence", "Requiem", "Harbinger"]

temas_sets = [
    "Kanto", "Zendikar", "Ravnica", "Johto", "Sinnoh", "Innistrad", "Kaladesh", "Galar",
    "Unova", "Hoenn", "Theros", "Eldraine", "Alola", "Paldea", "Ixalan", "Kamigawa", "Lorwyn",
    "Dominaria", "Strixhaven", "Amonkhet", "Ikoria", "Shadowmoor", "Tarkir", "Fiora", "Muraganda",
    "Celestia", "Ephyra", "Nebelmoor", "Agros", "Velis Vel", "Norn's Realm", "Arcavios",
    "Skalla", "Vryn", "Shandalar", "Serra's Realm", "The Abyss", "The Maelstrom", "New Capenna",
    "Phyrexia", "Ulgrotha", "Mirrodin", "Argoth", "Sengir", "Tolaria", "Fate's End", "Timaran",
    "Griselda", "Avalon", "Elysium", "Erebor", "Silvaria", "Nemesis", "Arcturus", "Vanguard",
    "Volcanus", "Draconis", "Underdark", "Skyreach", "Cloudspire", "Moonveil", "Oceanis",
    "Mysthaven", "Starborn", "Earthshine", "Ironforge", "Shadowlands", "Fireheart", "Everlight",
    "Stormpeaks", "Frosthold", "Flamebound", "Spectrawind", "Mistral", "Soulforge", "Bloodhaven",
    "Nightshade", "Auroria", "Astralis", "Duskveil", "Hollowspire", "Demacia", "Noxus", "Ionia",
    "Piltover", "Zaun", "Shurima", "Freljord", "Bandle City", "Bilgewater", "Targon", "Runeterra",
    "Sleepy Hollow", "Gotham City", "Metropolis", "Central City", "Star City", "Atlantis",
    "Themyscira", "Asgard", "Wakanda", "Xandar", "Korugar", "Oa", "Mogo", "Krypton", "Avalon",
]

def generar_sets(num_sets=10000):
    os.makedirs("data/Set", exist_ok=True)
    sets = set()

    with open("data/Set/sets.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre", "Fecha lanzamiento", "Franquicia"])
        while len(sets) < num_sets:
            nombre = f"{random.choice(adjetivos_sets)} {random.choice(sustantivos_sets)} of {random.choice(temas_sets)}"
            if nombre not in sets:
                sets.add(nombre)
                fecha_lanzamiento = faker.date_between(start_date="-45y", end_date="today")
                franquicia = random.choice(["Pokemon", "Magic", "Yu-Gi-Oh"])
                writer.writerow([nombre, fecha_lanzamiento, franquicia])

