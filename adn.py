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
        complemento = obtener_complemento(baseAdn1);
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

    :param adn1: represnta el primer ADN
    :param adn2: represneta el segundo ADN
    :return: una cadena true que representa que la correspondiencia es 100% y false si no corresponde
    '''

    return (100.0 == calcular_correspondencia(adn1, adn2))


def es_cadena_valida(adn):
    pass


def es_base(caracter):
    pass


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, base):
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

