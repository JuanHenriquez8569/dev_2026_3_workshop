import re


class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        if not isinstance(texto, str):
            return False
    
        limpio = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
        return limpio == limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        if not isinstance(texto, str):
            return ""
        invertida = ""
        for caracter in texto:
            invertida = caracter + invertida
        return invertida

    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        if not isinstance(texto, str):
            return 0
        vocales = "aeiouAEIOU"
        return sum(1 for caracter in texto if caracter in vocales)
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        if not isinstance(texto, str):
            return 0
    
        vocales_y_mayuscula = "aeiouAEIOUY"
        return sum(1 for c in texto if c.isalpha() and c not in vocales_y_mayuscula)
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        if not isinstance(texto1, str) or not isinstance(texto2, str):
            return False
        limpio1 = sorted(caracter.lower() for caracter in texto1 if caracter.isalnum())
        limpio2 = sorted(caracter.lower() for caracter in texto2 if caracter.isalnum())
        return limpio1 == limpio2
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        if not isinstance(texto, str):
            return 0
        palabras = texto.split()
        return len(palabras)
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        if not isinstance(texto, str):
            return ""
        return " ".join(p.capitalize() for p in texto.split(" "))
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        if not isinstance(texto, str):
            return ""
        return re.sub(r' {2,}', ' ', texto)
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if not isinstance(texto, str):
            return False
        if texto.startswith('-'):
            texto = texto[1:]
        return texto.isdigit()
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        if not isinstance(texto, str):
            return ""
        cifrada = ""
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                cifrada += chr((ord(caracter) - base + desplazamiento) % 26 + base)
            else:
                cifrada += caracter
        return cifrada
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        if not isinstance(texto, str):
            return ""
        descifrada = ""
        for caracter in texto:
            if caracter.isalpha():
                base = ord('A') if caracter.isupper() else ord('a')
                descifrada += chr((ord(caracter) - base - desplazamiento) % 26 + base)
            else:
                descifrada += caracter
        return descifrada
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if not isinstance(texto, str) or not isinstance(subcadena, str) or not subcadena:
            return []
    
        posiciones = []
        len_sub = len(subcadena)
        for i in range(len(texto) - len_sub + 1):
            if texto[i:i + len_sub] == subcadena:
                posiciones.append(i)
        return posiciones