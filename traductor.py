from dicts import (alfabeto_braille,numeros_braille)
from archivos import guardarArchivo

def pedirTexto(palabra:str):
    palabra = input("Ingrese el texto a traducir: ")
    return palabra.lower()

palabra = pedirTexto("Ingrese el texto a traducir: ")

#Traduccion letra a letra   
def traducir_caracter_a_braile(text: str):
    resultado = ""
    for letra in text.lower(): 
        if letra in alfabeto_braille:
            resultado += alfabeto_braille[letra] + " "
        else:
            resultado += letra
        print("\n")
        print("Palabra traducida a Braille: ", palabra)
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
        if caracter in numeros_braille:
            resultado += numeros_braille[caracter]
    return resultado




def main():
    entrada = input("Ingresa el texto o número a traducir: ").strip()
    
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
    guardar_en_archivo(resultado_final)
    