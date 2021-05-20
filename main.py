"""
* Módulo 20 - Conversor de temperaturas
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 20/05/2021
* Programa em Python 3 para converter temperaturas.
"""
from helpers import celsius_para_fahrenheit, celsius_para_kelvin

print("Hello World!")

if __name__ == "__main__":
    print("\n+=+=+=+ Conversor de temperaturas +=+=+=+")

    while True:
        print("\n- Digite a temperatura em Celsius (somente números).")
        print("- Para encerrar digite ( q ).")

        mensagem = "\nPor favor, digite a temperatura em Celsius (ºC): "

        try:
            celsius = input(mensagem)

            if celsius.lower() != 'q':
                print(f"\nTemperatura em Celsius......: "
                      f"{float(celsius)}ºC")

                print(f"Temperatura em Fahrenheit...: "
                      f"{celsius_para_fahrenheit(float(celsius))}ºF")

                print(f"Temperatura em Kelvin.......: "
                      f"{celsius_para_kelvin(float(celsius))} K")
            else:
                print("Encerrando o programa...\n"
                      "Até a Próxima!!!")
                break

        except ValueError:
            print("OOPS!!! Acho que você digitou um caractere invalido!\n"
                  "Digite um número ou 'q' para sair...")
