def obtener_secciones(adn, n):
    """
    Una función obtener secciones que entregue una lista de secciones, dada una cadena de adn y un numero de secciones
    str -> list of str
    >>> obtener_secciones('AGATAGA', 3)

    >>> obtener_secciones('GATATACA', 4)

    >>> obtener_secciones('tacaga', 2)
    >>> obtener_secciones('GTI', 2)
    Traceback (most recent call last):
    ..
    ValueError: la cadena no es valida

    :param adn: Ingresa una caracteres representada por adn
    :param n: Ingresa un numero representado por n
    :return: se retornara una lista de las secciones del srt
    """


def obtener_complementos(lista_adn):
    """
    Una función complementos_por_secciones que entregue una lista de cadenas de adn complementarias dada una lista de cadenas de adn
    (list of str, str) -> list of str
    >>> obtener_complementos(['GATATACA', 'TATACACA', 'TCTATGTA', 'TAGAGATA','GATA'])
    ['CTATATGT','ATATGTGT','AGATACAT', 'ATCTCTAT','CTAT']
    >>> obtener_complementos(['tagata', 'cataga', 'gataca'])
     ['ATCTAT', 'GTATGT', 'CTATGT']
    >>> obtener_complementos(['GCTA', 'UTASF'])
    Traceback (most recent call last):
    ..
    ValueError: la cadena no es valida

    :param lista_adn: list of str entrega una lista de cadenas complemento
    :return: se retornara una lista de cadenas complementarias
    """


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
    ValueError: la cadena no es valida

    :param lista_adn: ingresa una list of str de cadenas adn
    :return: retorna una cadena completa
    """


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
