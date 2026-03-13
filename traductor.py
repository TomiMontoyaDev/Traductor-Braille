from dicts import (alfabeto_braille,numeros_braille)

def pedirTexto(palabra:str):
    palabra = input("Ingrese el texto a traducir: ")
    return palabra.lower()

palabra = pedirTexto("Ingrese el texto a traducir: ")

#Traduccion letra a letra   
def traducir_caracter_a_braile(text:str):
    for letra in text: 
        if letra in alfabeto_braille:
            print(alfabeto_braille[letra], " ", end="")
        else:
            print(letra, end="")

    print("\n")
    print("Palabra traducida a Braille: ", palabra)



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
    print("Traductor de Español a Braile: ")
    pedirTexto()
    