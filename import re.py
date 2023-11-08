import re

token_patterns = [
    (r'[0-9]+', 'NUMERO'),                              # Números enteros
    (r'"[^"]*"', 'CADENA'),                             # Cadenas de texto entre comillas dobles
    (r'\bif\b', 'IF'),                                  # Palabra clave "if"
    (r'\belse\b', 'ELSE'),                              # Palabra clave "else"
    (r'\bwhile\b', 'WHILE'),                            # Palabra clave "while"
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFICADOR'),       # Identificadores
    (r'\+', 'MAS'),                                     # Operador de suma
    (r'-', 'MENOS'),                                    # Operador de resta
    (r'\*', 'POR'),                                     # Operador de multiplicación
    (r'/', 'ENTRE'),                                    # Operador de división
    (r'\(', 'PARENIZQUIERDO'),                          # Paréntesis izquierdo
    (r'\)', 'PARENDERECHO'),                            # Paréntesis derecho
    (r'\s+', 'ESPACIO')                                 # Espacios en blanco (uno o más)
]

def tokenize(code):
    tokens = []
    while code:
        for pattern, token_type in token_patterns:
            regex = re.compile('^' + pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                if token_type != 'ESPACIO':  
                    tokens.append((value, token_type))
                code = code[len(value):]
                break
        else:
            raise Exception('Error: No se pudo analizar el código.')
    return tokens

# Ejemplo de uso
codigo_fuente = 'if 5 then print("¡Hola mundo!")'

tokens = tokenize(codigo_fuente)
print(tokens)
