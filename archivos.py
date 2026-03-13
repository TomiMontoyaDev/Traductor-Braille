def guardarArchivo(path:str, contenido:str ):
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"El contenido se a guardado satisfactoriamente en la direccion {path}")