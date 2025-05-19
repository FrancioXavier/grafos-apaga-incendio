## Decisões de Implementação

### 1. Utilização de Programação Orientada a Objetos (POO)
- **Abstração:** Facilita o entendimento e manutenção do código.
- **Modularização:** Evita repetição e promove reutilização.
- **Object Calisthenics:** Técnicas aplicadas para manter o código limpo e de fácil manutenção.

### 2. Entrada via Arquivo TXT
- **Facilidade de uso:** Permite extração e manipulação simples dos dados.
- **Usabilidade:** Torna o sistema mais acessível ao usuário final.

### 3. Algoritmo de Dijkstra para Caminho Mínimo
- **Desempenho:** Escolhido por ser eficiente na extração do caminho e custo mínimos.
- **Compatibilidade:** Atende bem ao problema proposto.

### 4. Heap Binário no Dijkstra
- **Complexidade:** Reduz para O((V + E) * log V), tornando-se a opção mais eficiente para o algoritmo.

---

## Análise dos Resultados

Com base na entrada do arquivo `data.txt`, obtivemos o seguinte resultado:

```sh
--- Rodada 0 ---
Vértices que pegarão fogo: {1, 2, 4, 6, 7}
Estado atual dos vértices em chamas:

--- Rodada 1 ---
Caminhão 0 apagou o fogo no vértice 6.
Caminhão 3 apagou o fogo no vértice 4.
Caminhão 4 apagou o fogo no vértice 1.
Vértices que pegarão fogo: {10, 5}
Estado atual dos vértices em chamas:

--- Rodada 2 ---
Vértices que pegarão fogo: {8}
Estado atual dos vértices em chamas:

--- Rodada 3 ---
O fogo não pode mais se espalhar.
Estado atual dos vértices em chamas:

Total de vértices salvos: 8

Total de água utilizada: 30

Caminho percorrido por cada caminhão:
Caminhão 0: [6, 9, 6]
Caminhão 1: [6, 3, 7, 6]
Caminhão 2: [6, 3, 7, 6]
Caminhão 3: [4, 3, 6]
Caminhão 4: [4, 1, 3, 6]
Caminhão 5: [4, 3, 7, 6]
Caminhão 6: [1, 3, 7, 6]
Caminhão 7: [1, 3, 7, 6]
Caminhão 8: [1, 3, 7, 6]
Simulação encerrada após 4 rodadas.
```

> **Observações:**
> - A simulação terminou pois o fogo não tinha mais para onde se alastrar.
> - Alguns caminhões optaram por caminhos com mais arestas, porém de menor custo, devido ao cálculo do Dijkstra. Mesmo que um vértice seja vizinho imediato, o caminho de menor custo pode ser mais vantajoso em termos de rodadas.

---

## Possíveis Melhorias & Desafios

### Melhorias Sugeridas
- Detalhar ainda mais o que ocorre em cada rodada.
- Refatorar partes do código para aprimorar o encapsulamento.

### Desafios Encontrados
- Estruturação do loop principal do algoritmo, responsável pelo controle das rodadas.

---