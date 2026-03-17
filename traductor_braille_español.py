# Diccionario Braille a Español (letras minúsculas)
braille_dict = {
    '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd',
    '⠑': 'e', '⠋': 'f', '⠛': 'g', '⠓': 'h',
    '⠊': 'i', '⠚': 'j', '⠅': 'k', '⠇': 'l',
    '⠍': 'm', '⠝': 'n', '⠕': 'o', '⠏': 'p',
    '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't',
    '⠥': 'u', '⠧': 'v', '⠺': 'w', '⠭': 'x',
    '⠽': 'y', '⠵': 'z', ' ': ' ',  # Espacio en Braille
}

def traducir_braille(braille_texto):
    """
    Traduce una cadena de Braille (símbolos Braille) a español.
    Ejemplo de entrada: '⠎⠁⠝⠞⠊⠁⠛⠕ ⠓⠕⠇⠁' (que representa "santiago hola")
    """
    letras = braille_texto.strip()
    resultado = ''
    for letra in letras:
        resultado += braille_dict.get(letra, '?')
    return resultado

if __name__ == "__main__":
    print("Introduce el texto en Braille (símbolos Braille ):")
    entrada = input()
    traduccion = traducir_braille(entrada)
    print("Traducción:", traduccion)

    # Para el segundo equipo adherir la función de traducir de español a Braille