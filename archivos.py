

def guardarArchivo(path:str, contenido:str ):
    """
    funcion para guardar un archivo txt
    
    parametro path:str direccion donde se quiere guardar el archivo, por defecto
    la carpeta raiz del proyecto 
    
    param contenido:str El texto el ual es el que se desea añadir al archvo. puede ser usado para español o braile
    
    """
    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)
    print(f"El contenido se a guardado satisfactoriamente en la direccion {path}")