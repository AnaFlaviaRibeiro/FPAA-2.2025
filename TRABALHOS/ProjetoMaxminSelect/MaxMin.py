def encontrar_min_max(vetor, inicio, fim):
    """
    Função recursiva para determinar o menor e o maior valor de uma lista.
    """
    # Caso base: apenas um elemento
    if inicio == fim:
        return vetor[inicio], vetor[inicio]

    # Caso base: exatamente dois elementos
    if fim == inicio + 1:
        if vetor[inicio] > vetor[fim]:
            return vetor[fim], vetor[inicio]
        else:
            return vetor[inicio], vetor[fim]

    # Divide o problema em duas partes
    meio = (inicio + fim) // 2
    min_esq, max_esq = encontrar_min_max(vetor, inicio, meio)
    min_dir, max_dir = encontrar_min_max(vetor, meio + 1, fim)

    # Combina os resultados das duas metades
    return min(min_esq, min_dir), max(max_esq, max_dir)


if __name__ == "__main__":
    print("=== Busca de mínimo e máximo em uma lista de inteiros ===")
    continuar = True
    while continuar:
        try:
            lista_numeros = []
            print("Informe números inteiros (digite 'FIM' quando acabar):")
            while True:
                valor = input("Número: ")
                if valor.strip().upper() == "FIM":
                    break
                lista_numeros.append(int(valor))

            if lista_numeros:
                menor, maior = encontrar_min_max(lista_numeros, 0, len(lista_numeros) - 1)
                print(f"\nResultado -> Menor: {menor} | Maior: {maior}\n")
            else:
                print("Nenhum valor foi fornecido!")

            opcao = input("Deseja encerrar? Digite 'SAIR' ou pressione Enter para repetir: ")
            if opcao.strip().upper() == "SAIR":
                continuar = False
        except ValueError:
            print("Entrada inválida: insira apenas números inteiros.\n")
