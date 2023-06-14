# [Converter uma lista ordenada em uma árvore de busca binária](https://leetcode.com/problems/k-closest-points-to-origin/)

**Dificuldade: Média**

Dado um array de `points` onde `points[i] = [xi, yi]` representa um ponto no plano **X-Y** e um número inteiro `k`, retorne os `k` pontos mais próximos da origem `(0, 0)`.

A distância entre dois pontos no plano **X-Y** é a distância euclidiana (ou seja, `√(x1 - x2)2 + (y1 - y2)2`).

Você pode retornar a resposta em qualquer ordem. A resposta é garantida como única (exceto pela ordem em que está).

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

``` bash
Entrada: points = [[1,3],[-2,2]], k = 1
Saída: [[-2,2]]
Explicação:
A distância entre (1, 3) e a origem é sqrt(10).
A distância entre (-2, 2) e a origem é sqrt(8).
Como sqrt(8) < sqrt(10), (-2, 2) está mais próximo da origem.
Nós queremos apenas os k = 1 pontos mais próximos da origem, então a resposta é apenas [[-2,2]].
```
**Exemplo 2:**

``` bash
Entrada: points = [[3,3],[5,-1],[-2,4]], k = 2
Saída: [[3,3],[-2,4]]
Explicação: A resposta [[-2,4],[3,3]] também seria aceita.
```