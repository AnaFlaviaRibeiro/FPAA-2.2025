# 🧩 Caminho Hamiltoniano em Grafos Aleatórios

Este projeto implementa um **gerador e resolvedor de Caminhos Hamiltonianos** em grafos direcionados ou não direcionados.
O programa cria automaticamente um grafo aleatório e tenta encontrar um caminho que visite todos os vértices **exatamente uma vez**, utilizando **backtracking**.

---

## 🚀 Funcionalidades

- Geração automática de grafos aleatórios (direcionados ou não).
- Representação via **matriz de adjacência**.
- Busca de **caminho Hamiltoniano** usando **recursão e backtracking**.
- Visualização gráfica com destaque do caminho encontrado.
- Interface simples via terminal.

---

## 🧠 Conceito: Caminho Hamiltoniano

Um **caminho Hamiltoniano** é uma sequência de vértices em um grafo que:
- Visita cada vértice **exatamente uma vez**.
- Pode (ou não) ser um ciclo, dependendo se há aresta entre o último e o primeiro vértice.

> ⚠️ Encontrar um caminho Hamiltoniano é um problema **NP-completo**, ou seja, não há algoritmo eficiente conhecido que resolva o problema em tempo polinomial para todos os casos.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **NetworkX** – manipulação e visualização de grafos
- **Matplotlib** – renderização dos gráficos
- **Random / Datetime** – geração aleatória controlada

---

## 📦 Instalação

1. **Clone o repositório**
Clone o repositório
```
git clone https://github.com/AnaFlaviaRibeiro/FPAA-2.2025.git
```
```bash
cd ProjetoCaminhoHamiltoniano
python main.py
```

2. **Crie um ambiente virtual (opcional)**
   ```bash
   python -m venv venv
   ```

3. **Instale as dependências**
   ```bash
   pip install networkx matplotlib
   ```

---

## ▶️ Como Executar

Execute o script principal:
```bash
python main.py
```

Durante a execução:
- O programa perguntará se o grafo deve ser **direcionado (s/n)**.
- Ele criará automaticamente um grafo com **5 a 8 vértices**.
- Tentará encontrar e exibir um **caminho Hamiltoniano**, se existir.

---

## 🖼️ Exemplo de Saída

```
Deseja grafo direcionado? (s/n): n
Caminho Hamiltoniano encontrado (não direcionado):
0 → 2 → 3 → 5 → 1 → 4
```

Será exibido um gráfico com:
- **Nós em azul** representando os vértices.
- **Arestas em cinza** (todas as conexões).
- **Arestas vermelhas** indicando o caminho Hamiltoniano encontrado.

---

## 📚 Estrutura do Código

| Arquivo | Descrição |
|----------|------------|
| `main.py` | Código principal com a geração, busca e visualização do grafo. |

### Principais Classes e Métodos

#### `class Grafo`
Responsável por criar o grafo, gerar as conexões e procurar o caminho Hamiltoniano.

| Método | Função |
|--------|---------|
| `_criar_grafo_aleatorio()` | Gera as arestas aleatoriamente. |
| `_pode_visitar(v, caminho, pos)` | Verifica se o vértice pode ser adicionado no caminho. |
| `_busca_hamiltoniana()` | Executa a busca recursiva. |
| `encontrar_caminho_hamiltoniano()` | Controla o processo de busca. |
| `mostrar_grafo()` | Exibe o grafo com o caminho destacado. |

---

## 💡 Possíveis Extensões

- Implementar busca **Hamiltoniana com ciclos**.
- Adicionar **pesos nas arestas** e calcular custo total.
- Implementar **algoritmos heurísticos** (ex.: Algoritmo Genético, Busca Tabu, ACO).
- Exportar resultados para **CSV** ou **JSON**.
