from dicts import (alfabeto_braille)
from archivos import guardarArchivo

def pedirTexto(palabra=""):
    palabra = input(palabra)
    return palabra.lower().strip()

#Traduccion letra a letra   
def traducir_caracter_a_braile(text: str):
    """
    Funcion que traduce numeros enteros a braile. compara numero a numero
     input: numeros String
     output: numeros String: a Braile
    """
    if not text: return ""
    resultado = ""
    for letra in text.lower(): 
        if letra in alfabeto_braille:
            resultado += alfabeto_braille[letra] + " "
        else:
            resultado += letra
    print("\n")
    print("Palabra a traducir al Braille: ", text)
    print("Palabra en braile: ", resultado)
    return resultado

def main():
    entrada = pedirTexto("Ingrese el texto o número a traducir: ")
    
    if not entrada:
        print("No ingresaste ningun texto.")
        return
    
    resultado_final = traducir_caracter_a_braile(entrada)

    # Guardamos el resultado obtenido en el TXT
    guardarArchivo("español_abraile.txt",resultado_final)

if __name__ == "__main__":
    main()