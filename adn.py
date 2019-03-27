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



def calcular_correspondencia(adn1, adn2):
    '''
    (str, str ) -> num

    Calcula la correspondiencia entre dos ADN

    >>> calcular_correspondencia('GATA', 'CATA')
    0.75

    >>> calcular_correspondencia('TCT', 'GAT')
    00.3333333333333333

    >>> calcular_correspondencia('TCT', 'GAT')
    Traceback (most recent call last):
    ..
    TypeError: Una de las cadenas no es valida.

    :param adn1:
    :param adn2:
    :return:
    '''
    pass


def corresponden(adn1, adn2):
    '''
    (str, str) -> boleano

    Valida la correspondiencia entre dos ADN

    >>> corresponden('GATA', 'GATA')
    True

    >>> corresponden('TCT', 'GAT')
    False

    >>> corresponden('TCTG', 'GATC')
    False

    :param adn1: represnta el primer ADN
    :param adn2: represneta el segundo ADN
    :return: una cadena true que representa que la correspondiencia es 100% y false si no corresponde
    '''
    pass


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

