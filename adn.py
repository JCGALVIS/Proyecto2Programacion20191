def obtener_complemento(base):
    '''
    str -> str

    Obtiene el complemento de una base de ADN

    >>> obtener_complemento('A')
    'T'

    >>> obtener_complemento('C')
    'G'

    >>> obtener_complemento('t')
    'A'

    >>> obtener_complemento('B')
    Traceback (most recent call last):
    ..
    TypeError: B es una base invalida.

    :param base: Base del ADN a obtener el complemento
    :return: El complemento de la base ingresada
    '''

    complemento = '';
    letra = base.upper()

    if (letra in ('ATCG')):

        if (letra == 'A'):
            complemento = 'T'
        if (letra == 'T'):
            complemento = 'A'
        if (letra == 'C'):
            complemento = 'G'
        if (letra == 'G'):
            complemento = 'C'
    else:
        raise TypeError(str(base) + ' es una base invalida.')

    return complemento


def generar_cadena_complementaria(adn):
    '''
    str -> str

    Genera la cadena de complemento del ADN ingresado

    >>> generar_cadena_complementaria('GATA')
    'CTAT'

    >>> generar_cadena_complementaria('CTGT')
    'GACA'

    >>> generar_cadena_complementaria('GCTH')
    Traceback (most recent call last):
    ..
    TypeError: H es una base invalida.

    :param adn: AND a obneter complemento
    :return: El complemento deL AND ingresado
    '''

    cadenaComplementaria = ''
    complemento = ''

    for base in adn:
        cadenaComplementaria += obtener_complemento(base);

    return cadenaComplementaria


def calcular_correspondencia(adn1, adn2):
    '''
    (str, str ) -> num

    Calcula la correspondiencia entre dos ADN

    >>> calcular_correspondencia('GATA', 'CTAT')
    100.0

    >>> calcular_correspondencia('TCT', 'GGA')
    66.66666666666666

    >>> calcular_correspondencia('TCTA', 'AGGT')
    75.0

    >>> calcular_correspondencia('GATA', 'CTA')
    75.0

    :param adn1: represnta el primer ADN
    :param adn2: represneta el segundo ADN
    :return:
    '''

    complemento = ''
    contador = 0
    baseAdn2 = ''
    mayorLongitud = 0
    contadorCorrespondencia = 0

    if len(adn1) >= len(adn2):
        mayorLongitud = len(adn1)
    else:
        mayorLongitud = len(adn2)

    for baseAdn1 in adn1:
        baseAdn2 = ''
        complemento = obtener_complemento(baseAdn1)

        if len(adn2) > contador:
            baseAdn2 = adn2[contador]

        contador += 1

        if complemento == baseAdn2:
            contadorCorrespondencia += 1

    return (contadorCorrespondencia / mayorLongitud) * 100



def corresponden(adn1, adn2):
    '''
    (str, str) -> boleano

    Valida la correspondiencia entre dos ADN

    >>> corresponden('GATA', 'CTAT')
    True

    >>> corresponden('TCT', 'GAT')
    False

    >>> corresponden('TCTG', 'GATC')
    False

    >>> corresponden('GATA', 'CTA')
    False

    :param adn1: represnta el primer ADN
    :param adn2: represneta el segundo ADN
    :return: una cadena true que representa que la correspondiencia es 100% y false si no corresponde
    '''

    return (100.0 == calcular_correspondencia(adn1, adn2))


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



