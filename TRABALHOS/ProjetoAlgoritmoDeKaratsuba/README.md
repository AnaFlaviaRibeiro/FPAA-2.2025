# 🚀 Algoritmo de Karatsuba - Implementação e Análise

## 📋 Descrição do Projeto

Este projeto implementa o algoritmo de multiplicação de Karatsuba, um método eficiente para multiplicar números inteiros grandes que supera o algoritmo tradicional de multiplicação escolar em termos de complexidade assintótica.

## 🎯 Objetivos

- Implementar o algoritmo de Karatsuba em Python
- Demonstrar a eficiência do algoritmo para números grandes
- Fornecer uma interface interativa para testar o algoritmo
- Analisar a complexidade computacional e ciclomática

## 🔧 Como Executar

### Pré-requisitos
- Python 3.6 ou superior

### Execução
1. Clone o repositório
```
git clone https://github.com/AnaFlaviaRibeiro/FPAA-2.2025.git
```
```bash
cd ProjetoAlgoritmoDeKaratsuba
python Karatsuba.py
```

### Uso
1. Execute o programa
2. Digite o primeiro número quando solicitado
3. Digite o segundo número quando solicitado
4. Visualize o resultado da multiplicação
5. Digite 'sair' para encerrar o programa

## 📊 Relatório Técnico

### 1. Visão Geral do Algoritmo

O algoritmo de Karatsuba é uma técnica de divisão e conquista que reduz o número de multiplicações necessárias para multiplicar dois números de n dígitos de O(n²) para O(n^log₂(3)) ≈ O(n^1.585).

### 2. Funcionamento do Algoritmo

#### 2.1 Estratégia de Divisão e Conquista

1. **Divisão**: Divide cada número em duas partes de tamanho aproximadamente igual
2. **Conquista**: Realiza três multiplicações recursivas em números menores
3. **Combinação**: Combina os resultados usando operações de adição e deslocamento

#### 2.2 Fórmula Matemática

Para números x e y divididos em:
- x = x₁ × 10^m + x₀
- y = y₁ × 10^m + y₀

O produto é calculado como:
```
x × y = (x₁ × y₁) × 10^(2m) + [(x₁ + x₀)(y₁ + y₀) - x₁y₁ - x₀y₀] × 10^m + (x₀ × y₀)
```

#### 2.3 Implementação Detalhada

```python
def karatsuba(x: int, y: int) -> int:
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
```

### 3. Análise da Complexidade

#### 3.1 Complexidade Assintótica

**Tempo:**
- **Caso Base**: O(1) para números com menos de 10 dígitos
- **Caso Recursivo**: T(n) = 3T(n/2) + O(n)
- **Solução da Recorrência**: T(n) = O(n^log₂(3)) ≈ O(n^1.585)

**Espaço:**
- **Pilha de Recursão**: O(log n) devido à profundidade da recursão
- **Variáveis Temporárias**: O(n) para armazenar as partes divididas

#### 3.2 Vantagens e Desvantagens

**Vantagens:**
- Complexidade assintótica inferior à multiplicação tradicional
- Eficiente para números grandes (geralmente > 100 dígitos)
- Implementação relativamente simples

**Desvantagens:**
- Overhead para números pequenos
- Constantes multiplicativas maiores
- Não é o algoritmo mais eficiente para números extremamente grandes

### 4. Análise da Complexidade Ciclomática

#### 4.1 Definição

A complexidade ciclomática mede o número de caminhos independentes através do código fonte, sendo um indicador de complexidade estrutural e testabilidade.

#### 4.2 Cálculo da Complexidade Ciclomática

**Fórmula Base:**
```
CC = E - N + 2P
```
Onde:
- E = Número de arestas (transições)
- N = Número de nós (instruções)
- P = Número de componentes conectados

**Análise da Função `karatsuba`:**
- **Nós de Decisão**: 4 (três verificações de sinal + uma verificação de caso base)
- **Complexidade Ciclomática**: 5

**Análise da Função `main`:**
- **Nós de Decisão**: 3 (verificação de 'sair' + tratamento de exceção)
- **Complexidade Ciclomática**: 4

**Complexidade Ciclomática Total do Programa**: 9

#### 4.3 Interpretação dos Resultados

- **CC ≤ 10**: Código simples e fácil de manter ✅
- **10 < CC ≤ 20**: Código moderadamente complexo
- **CC > 20**: Código complexo, requer refatoração

**Resultado**: O programa possui complexidade ciclomática baixa (9), indicando boa estrutura e facilidade de manutenção.

### 5. Estrutura do Código

#### 5.1 Tratamento de Sinais
```python
if x < 0 and y < 0:
    return karatsuba(-x, -y)
if x < 0:
    return -karatsuba(-x, y)
if y < 0:
    return -karatsuba(x, -y)
```

#### 5.2 Caso Base
```python
if x < 10 or y < 10:
    return x * y
```

#### 5.3 Divisão dos Números
```python
tamanho_maximo = max(len(str(x)), len(str(y)))
ponto_divisao = tamanho_maximo // 2
parte_alta_x, parte_baixa_x = divmod(x, 10**ponto_divisao)
parte_alta_y, parte_baixa_y = divmod(y, 10**ponto_divisao)
```

#### 5.4 Multiplicações Recursivas
```python
produto_baixo = karatsuba(parte_baixa_x, parte_baixa_y)
produto_alto = karatsuba(parte_alta_x, parte_alta_y)
produto_misto = karatsuba(parte_baixa_x + parte_alta_x, parte_baixa_y + parte_alta_y)
```

#### 5.5 Combinação dos Resultados
```python
return (produto_alto * 10**(2 * ponto_divisao)
       + (produto_misto - produto_alto - produto_baixo) * 10**ponto_divisao
       + produto_baixo)
```

### 6. Testes e Validação

#### 6.1 Casos de Teste Recomendados

1. **Números pequenos**: 5 × 7
2. **Números médios**: 123 × 456
3. **Números grandes**: 12345 × 67890
4. **Números negativos**: -123 × 456
5. **Zero**: 0 × 123
6. **Números iguais**: 999 × 999

#### 6.2 Validação Matemática

O algoritmo pode ser validado comparando seus resultados com a multiplicação padrão do Python:
```python
assert karatsuba(a, b) == a * b
```

### 7. Conclusões

O algoritmo de Karatsuba implementado demonstra:
- **Correção**: Funciona corretamente para todos os casos de teste
- **Eficiência**: Complexidade O(n^1.585) superior ao algoritmo tradicional
- **Simplicidade**: Complexidade ciclomática baixa (9) indica boa estrutura
- **Usabilidade**: Interface interativa e tratamento de erros adequado
---
## Licença
Este projeto está licenciado sob a Licença MIT.