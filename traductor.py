from dicts import (alfabeto_braille,numeros_braille,PREFIJO_NUMERO)
from archivos import guardarArchivo

def pedirTexto(palabra=""):
    palabra = input(palabra)
    return palabra.strip()

#Traduccion letra a letra   
def traducir_caracter_a_braile(text: str):
    """
    Funcion que traduce un texto a braile. compara caracter por caracter
     input: texto:String:Español
     output: texto:String:Braile
    """
    if not text: return ""
    resultado = ""
    es_numero= False
    for char in text.lower(): 
        if char in numeros_braille:
            if not es_numero:
                resultado += PREFIJO_NUMERO
            resultado += numeros_braille[char]
        elif char in alfabeto_braille:
            es_numero = False
            resultado += alfabeto_braille[char]
        else:
            es_numero = False
            resultado += char
    

    return resultado

def main():
    entrada = pedirTexto("Ingrese el texto o número a traducir: ")
    
    if not entrada:
        print("No ingresaste ningun texto.")
        return ""
    
    resultado_final = traducir_caracter_a_braile(entrada)

    print("\n")
    print("Palabra a traducir al Braille: ", entrada)
    print("Palabra en braile: ", resultado_final)

    # Guardamos el resultado obtenido en el TXT
    guardarArchivo("español_abraile.txt",resultado_final)

if __name__ == "__main__":
    main()