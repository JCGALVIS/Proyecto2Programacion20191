def obtener_secciones(adn, n):
    """
    Una función obtener secciones que entregue una lista de secciones, dada una cadena de adn y un numero de secciones
    str -> list of str
     >>> obtener_secciones('AGATAGA', 3)
    'AG ATAGA'
    >>> obtener_secciones('GATATACA', 4)
    'GA TATACA'
    >>> obtener_secciones('tacaga', 2)
    'TAC AGA'
    >>> obtener_secciones('ACGC', 'A')
    Traceback (most recent call last):
    TypeError: A no es numerico
    >>> obtener_secciones('ACCG', 0)
    Traceback (most recent call last):
    ..
    ZeroDivisionError: La división por cero no es posible
    >>> obtener_secciones('GTI', 2)
    'GTI no es cadena valida'

    :param adn: Ingresa una caracteres representada por adn
    :param n: Ingresa un numero representado por n
    :return: se retornara una lista de las secciones del srt
    """
    validar_cadena = es_cadena_valida(adn)
    dato = len(adn)
    if validar_cadena:
        if (type(n) != float and type(n) != int):
            raise TypeError(str(n) + ' no es numerico')
        else:
            if n > dato:
                return ValueError('el numero debe ser menor a ' + str(len(adn)))
            if n < dato:
                if n > 0:
                    sec = dato // n
                    return adn[:sec] + ' ' + adn[sec:]
                else:
                    raise ZeroDivisionError('La división por cero no es posible')
            if n == dato:
                return ValueError('Los numeros no pueden ser iguales')
    else:
        return adn + ' no es cadena valida'

def obtener_complementos(lista_adn):
    """
    Una función complementos_por_secciones que entregue una lista de cadenas de adn complementarias dada una lista de cadenas de adn
    (list of str, str) -> list of str
    >>> obtener_complementos(['GATATACA', 'TATACACA', 'TCTATGTA', 'TAGAGATA','GATA'])
    ['CTATATGT','ATATGTGT','AGATACAT','ATCTCTAT','CTAT']
    >>> obtener_complementos(['tagata', 'cataga', 'gataca'])
    ['ATCTAT','GTATGT','CTATGT']
    >>> obtener_complementos(['GCTA', 'UTASF'])
    Traceback (most recent call last):
    ..
    ValueError: la cadena no es valida

    :param lista_adn: list of str entrega una lista de cadenas complemento
    :return: se retornara una lista de cadenas complementarias
    """
    nueva_lista = []
    for neu in lista_adn:
        if es_cadena_valida(neu):
            chick = complementar_cadenas(neu)
            nueva_lista += chick
        else:
            raise ValueError('Una de las cadenas no es valida')
    return nueva_lista

def unir_cadena(lista_adn):
    """
    Una función unir cadenas que retorne una cadena de adn dada una lista de cadenas (debe validar que sean secuencias validas)
    (list of str, str) -> str
    >>> unir_cadena(['GACA', 'TAC', 'GATA'])
    'GACATACGATA'
    >>> unir_cadena(['TATA', 'GATAGA', 'TG'])
    'TATAGATAGATG'
    >>> unir_cadena(['FAFSAS', 'UTASF'])
    Traceback (most recent call last):
    ..
    ValueError: la cadenas no es valida

    :param lista_adn: ingresa una list of str de cadenas adn
    :return: retorna una cadena completa
    """

    concat = ''

    for list_new in lista_adn:
        if es_cadena_valida(list_new):
            concat += str(list_new)
        else:
            raise ValueError('la cadenas no es valida')
    return concat


def complementar_cadenas(lista_adn):
    """
    Una función complemento de cadenas que retorne una cadena complementaria dada una lista de cadenas (debe validar las secuencias)
    (list of str, str) -> list of str
    >>> complementar_cadenas(['GATATA','TATACA','CAGATCA'])
    ['CTATAT', 'ATATGT', 'GTCTAGT']
    >>> complementar_cadenas(['TATACAGA','TATAGA','TCACAG'])
    ['ATATGTCT','ATATCT','AGTGTC']
    >>> complementar_cadenas(['AFTAGA','UTASF'])
    Traceback (most recent call last):
    ..
    ValueError: la cadena no es valida

    :param lista_adn: ingresa una list of str de cadenas complemento
    :return:se retornara una lista de cadenas complementarias
    """
    lista_nueva = ''
    for neue in lista_adn:
        if es_cadena_valida(neue):
            chiq = generar_cadena_complementaria(neue)
            if len(neue) == len(chiq):
                new_chiq = unir_cadena(chiq)
                lista_nueva += new_chiq
        else:
            raise ValueError('las cadenas no es valida')
    return [lista_nueva[0:len(neue)], lista_nueva[len(neue):len(neue) * 2]]