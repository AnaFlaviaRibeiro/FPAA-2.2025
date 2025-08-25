def karatsuba(x: int, y: int) -> int:
    """Multiplica dois inteiros usando o algoritmo de Karatsuba."""
    # Tratamento de sinais
    if x < 0 and y < 0:
        return karatsuba(-x, -y)
    if x < 0:
        return -karatsuba(-x, y)
    if y < 0:
        return -karatsuba(x, -y)

    # Caso base: números pequenos
    if x < 10 or y < 10:
        return x * y

    # Define o tamanho máximo dos números
    tamanho_maximo = max(len(str(x)), len(str(y)))
    ponto_divisao = tamanho_maximo // 2

    # Divide os números em parte alta e baixa
    parte_alta_x, parte_baixa_x = divmod(x, 10**ponto_divisao)
    parte_alta_y, parte_baixa_y = divmod(y, 10**ponto_divisao)

    # Três multiplicações recursivas
    produto_baixo = karatsuba(parte_baixa_x, parte_baixa_y)
    produto_alto = karatsuba(parte_alta_x, parte_alta_y)
    produto_misto = karatsuba(parte_baixa_x + parte_alta_x, parte_baixa_y + parte_alta_y)

    # Combinação dos resultados
    return (produto_alto * 10**(2 * ponto_divisao)
           + (produto_misto - produto_alto - produto_baixo) * 10**ponto_divisao
           + produto_baixo)


def main():
    print("🚀 CALCULADORA KARATSUBA")
    while True:
        entrada1 = input("\nDigite o primeiro número (ou 'sair'): ")
        if entrada1.lower() == 'sair':
            break

        entrada2 = input("Digite o segundo número (ou 'sair'): ")
        if entrada2.lower() == 'sair':
            break

        try:
            numero1, numero2 = int(entrada1), int(entrada2)
            resultado = karatsuba(numero1, numero2)
            print(f"\nResultado: {numero1} × {numero2} = {resultado}")
        except ValueError:
            print("❌ Por favor, insira apenas números inteiros.")


if __name__ == "__main__":
    main()
