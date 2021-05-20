def celsius_para_kelvin(temperatura_celsius):
    """
    - Função para converter temperatura de Celsius para Kelvin.
    - Formula: (celsius) + 273.15
    :param temperatura_celsius: Entrada, temperatura em Celsius.
    :return: Retorna a temperatura em Kelvin.
    """
    temperatura_kelvin = temperatura_celsius + 273.15
    return temperatura_kelvin


def celsius_para_fahrenheit(temperatura_celsius):
    """
    - Função para converter temperatura de Celsius para Fahrenheit.
    - Formula: (celsius * (9 / 5)) + 32
    :param temperatura_celsius: Entrada, temperatura em Celsius.
    :return: Retorna a temperatura em Fahrenheit.
    """
    temperatura_fahrenheit = (temperatura_celsius * (9 / 5)) + 32
    return temperatura_fahrenheit
