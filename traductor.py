


from dicts import (alfabeto_braille)
from archivos import guardarArchivo

def pedirTexto(palabra=""):
    palabra = input(palabra)
    return palabra.lower().strip()

#Traduccion letra a letra   
def traducir_caracter_a_braile(text: str):
    resultado = ""
    for letra in text.lower(): 
        if letra in alfabeto_braille:
            resultado += alfabeto_braille[letra] + " "
        else:
            resultado += letra
    print("\n")
    print("Palabra traducida a Braille: ", text)
    print("Palabra en braile: ", resultado)
    return resultado





def traducir_numeros_a_braille(texto_numerico):
    """
    Funcion que traduce numeros enteros a braile. compara numero a numero
     input: numeros String
     output: numeros String: a Braile
    """

    if not texto_numerico:
        return ""
    prefijo_numero = '⠼'
    resultado = prefijo_numero
    for caracter in str(texto_numerico):
        if caracter in alfabeto_braille:
            resultado += alfabeto_braille[caracter]
    print("\n")
    print("Numero traducida a Braille: ", texto_numerico)
    print("Numero a braile: ", resultado)
    return resultado

def main():
    entrada = pedirTexto("Ingrese el texto o número a traducir: ")
    
    if not entrada:
        print("No ingresaste nada.")
        return

    # Identificamos si es número o texto
    if entrada.isdigit():
        print("Detectado: Entrada numérica.")
        resultado_final = traducir_numeros_a_braille(entrada)
    else:
        print("Detectado: Entrada de texto.")
        resultado_final = traducir_caracter_a_braile(entrada)

    # Guardamos el resultado obtenido en el TXT
    guardarArchivo("español_abraile.txt",resultado_final)

if __name__ == "__main__":
    main()