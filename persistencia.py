import json

def guardar_datos(lista, nombre_archivo="productos.json"):
    with open(nombre_archivo, 'w', encoding="utf-8") as file:
        json.dump(lista, file, indent=4, ensure_ascii=False)

def cargar_datos(nombre_archivo='productos.json'):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []