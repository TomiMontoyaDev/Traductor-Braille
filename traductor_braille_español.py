# Diccionario Braille a Español (letras minúsculas)
braille_dict = {
    '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd',
    '⠑': 'e', '⠋': 'f', '⠛': 'g', '⠓': 'h',
    '⠊': 'i', '⠚': 'j', '⠅': 'k', '⠇': 'l',
    '⠍': 'm', '⠝': 'n', '⠕': 'o', '⠏': 'p',
    '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't',
    '⠥': 'u', '⠧': 'v', '⠺': 'w', '⠭': 'x',
    '⠽': 'y', '⠵': 'z', ' ': ' ',  # Espacio en Braille

    # Acentuadas
    'á': '⠷', 'é': '⠿', 'í': '⠾', 'ó': '⠓', 'ú': '⠜', 'ü': '⠳',
    # Espacio
    ' ': '⠀',
    # Puntuación básica
    '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖',

}
PREFIJO_NUMERO = '⠼'
numeros_braille = {
    '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
    '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
}
braille_numeros_invertidos = {v: k for k, v in numeros_braille.items()}  # Para traducir de Braille a números
def traducir_braille(braille_texto):
    """
    Traduce una cadena de Braille (símbolos Braille) a español.
    Ejemplo de entrada: '⠎⠁⠝⠞⠊⠁⠛⠕ ⠓⠕⠇⠁' (que representa "santiago hola")
    """
    letras = braille_texto.strip()
    resultado = ''
    for i,letra in enumerate(letras):
        if letra == '⠼' or letras [i-1] == '⠼':  # Prefijo de número, se ignora en la traducción
            if letra in braille_numeros_invertidos:
                resultado += braille_numeros_invertidos[letra]
        else:
             resultado += braille_dict.get(letra, ' ')
    return resultado

if __name__ == "__main__":
    print("Introduce el texto en Braille (símbolos Braille ):")
    entrada = input()
    traduccion = traducir_braille(entrada)
    print("Traducción:", traduccion)

    # Para el segundo equipo adherir la función de traducir de español a Braille