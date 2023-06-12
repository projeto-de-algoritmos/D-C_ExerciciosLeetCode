# [Número de maneiras de reordenar a matriz para obter o mesmo BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

**Nível: Difícil**

Dado um array `nums` que representa uma permutação de inteiros de `1` a `n`. Vamos construir uma árvore de busca binária (BST) inserindo os elementos de `nums` em ordem em uma BST inicialmente vazia. Encontre o número de maneiras diferentes de reordenar `nums` de modo que o BST construído seja idêntico ao formado a partir do array original `nums`.

- Por exemplo, dado `nums = [2,1,3]`, teremos 2 como raiz, 1 como filho esquerdo e 3 como filho direito. A matriz `[2,3,1]` também produz o mesmo BST, mas `[3,2,1]` produz um BST diferente.

Retorne o número de maneiras de reordenar `nums` de modo que o BST formado seja idêntico ao BST original formado a partir de `nums`.

Como a resposta pode ser muito grande, retorne o módulo `10⁹ + 7`.

**Exemplo 1:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/08/12/bb.png)

``` bash
Input: nums = [2,1,3]
Output: 1
Explicação: Podemos reordenar nums para [2,3,1] que resultará no mesmo BST. Não há outras maneiras de reordenar nums que produzirão o mesmo BST.
```

**Exemplo 2:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/08/12/ex1.png)

``` bash
Input: nums = [3,4,5,1,2]
Output: 5
Explicação: As 5 matrizes a seguir produzirão o mesmo BST: 
[3,1,2,4,5] 
[3,1,4,2, 5] 
[3,1,4,5,2] 
[3,4,1,2,5] 
[3,4,1,5,2]
```

**Exemplo 3:**

![App Screenshot](https://assets.leetcode.com/uploads/2020/08/12/ex4.png)

``` bash
Input: nums = [1,2,3]
Output: 0
Explicação: Não há outras ordenações de nums que produzirão o mesmo BST.
```