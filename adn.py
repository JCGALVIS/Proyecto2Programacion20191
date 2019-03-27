def obtener_complemento(base):
    # retorna caracter
    pass


def generar_cadena_complementaria(adn):
    pass


def calcular_correspondencia(adn1, adn2):
    # retorna num
    pass


def corresponden(adn1, adn2):
    # retorna Bool
    pass


def es_cadena_valida(adn):
    """

    Ingresa una cadena y determina si es valida o no

    :param adn: Ingresa unos caracteres en mayuscula para validar si estan o no en el rango
    :return: True o False si es o no cadena respectivamente

    >>> es_cadena_valida('AGATA')
    True
    >>> es_cadena_valida('GATA')
    True
    >>> es_cadena_valida('CCTT')
    True
    >>> es_cadena_valida('ALAT')
    False
    >>> es_cadena_valida('ATCB')
    False
    >>> es_cadena_valida('OGTAU')
    False
    >>> es_cadena_valida('SF')
    False

    """

    for letra in adn:
        if not es_base(letra):
            return False
    return True


def es_base(caracter):
    """

    Ingresa un caracter, se determina si es True o False

    Str -> Bool

    :param caracter: Una letra en mayuscula
    :return: Si es valida o no

    >>> es_base('A')
    True
    >>> es_base('T')
    True
    >>> es_base('C')
    True
    >>> es_base('G')
    True
    >>> es_base('L')
    False
    >>> es_base('H')
    False
    >>> es_base('a')
    True
    >>> es_base('AT')
    Traceback (most recent call last):
    ..
    ValueError: AT no es una base
    >>> es_base('BB')
    Traceback (most recent call last):
    ..
    ValueError: BB no es una base
    >>> es_base('1')
    Traceback (most recent call last):
    ..
    ValueError: 1 no es una base

    """

    if (base == 'A'):
        return 'T'
    if(base == 'T'):
        return 'A'
    if(base == 'C'):
        return 'G'
    if (base == 'G'):
        return 'C'
    else:
        raise ValueError (base + ' no es una base')


def es_subcadena(adn1, adn2):
    """

    Ingresan dos cadenas y se determina si una es complemento de la otra

    (Str, Str) -> Bool

    :param adn1: La primera cadena de ADN
    :param adn2: La segunda cadena de ADN
    :return: True Or false, rependiendo el caso

    >>> es_subcadena('AGATA','ATA')
    True
    >>> es_subcadena('GGCT','GCT')
    True
    >>> es_subcadena('GTAC','TA')
    True
    >>> es_subcadena('CCTT','CTC')
    False
    >>> es_subcadena('TC','TCP')
    Traceback (most recent call last):
    ..
    ValueError: Una de las cadenas no es valida
    >>> es_subcadena('AGATA','ATC')
    False
    >>> es_subcadena('ATA','ATA')
    'Las cadenas son iguales'
    >>> es_subcadena('AT','AT')
    'Las cadenas son iguales'
    >>> es_subcadena('JJ','AT')
    Traceback (most recent call last):
    ..
    ValueError: Una de las cadenas no es valida
    >>> es_subcadena('TC','HY')
    Traceback (most recent call last):
    ..
    ValueError: Una de las cadenas no es valida
    >>> es_subcadena('LI','KO')
    Traceback (most recent call last):
    ..
    ValueError: Una de las cadenas no es valida

    """

    if not es_cadena_valida(adn1) or not es_cadena_valida(adn2):
        raise ValueError('Una de las cadenas no es valida')
    if len(adn1) > len(adn2) and es_cadena_valida(adn1) and es_cadena_valida(adn2):
        return adn2 in adn1
    if len(adn1) < len(adn2):
        es_cadena_valida(adn1) and es_cadena_valida(adn2)
        return adn1 in adn2
    if adn1 == adn2:
        es_cadena_valida(adn1) and es_cadena_valida(adn2)
        return 'Las cadenas son iguales'
    if len(adn1) == len(adn2):
        es_cadena_valida(adn1) and es_cadena_valida(adn2)
        return 'Las cadenas deben ser de diferente tamanio'

def reparar_dano(adn, base):
    """

    Ingresa una cadena de adn y si no es calida, repara con una base valida

    (Str, Str) -> Str

    :param adn: Una cadena de adn valida
    :param base: Una base valida
    :return: Insertarla en una posicon favorable

    >>> reparar_dano(['I','A','T','A'],'G')
    ['G', 'A', 'T', 'A']
    >>> reparar_dano(['G','P','C','G'],'H')
    Traceback (most recent call last):
    ..
    ValueError: ('H', 'no es una base')
    >>> reparar_dano(['C','A','B'],'C')
    ['C', 'A', 'C']
    >>> reparar_dano(['T','U','A'],'A')
    ['T', 'A', 'A']
    >>> reparar_dano(['A','P','S','T','G'],'G')
    ['A', 'G', 'G', 'T', 'G']
    >>> reparar_dano(['A','G','T','C'],'T')
    Traceback (most recent call last):
    ..
    ValueError: esa cadena esta bien
    >>> reparar_dano(['C','V','T','A'],'C')
    ['C', 'C', 'T', 'A']
    >>> reparar_dano(['A','C','D','T'],'G')
    ['A', 'C', 'G', 'T']

    """

    lista_2 = []

    if not es_cadena_valida(adn) and not es_base(base):
        raise ValueError(base, 'no es una base')
    elif es_cadena_valida(adn):
        raise ValueError('esa cadena esta bien')
    elif not es_cadena_valida(adn) and es_base(base):
        for letra in adn:
            if es_base(letra):
                lista_2 += letra
            if not es_base(letra):
                lista_2 += base
        return lista_2


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

