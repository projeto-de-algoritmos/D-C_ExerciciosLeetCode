# [Número de Pares Satisfazendo a Desigualdade](https://leetcode.com/problems/number-of-pairs-satisfying-inequality/)

**Nível: Difícil**

Você recebe dois arrays inteiros **indexados por 0** `nums1` e `nums2`, cada um de tamanho `n`, e um `diff` inteiro. Encontre o número de **pares** `(i, j)` tais que:

- `0 <= i < j <= n - 1` **e**
- `nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff`.

Retorne o **número de pares** que satisfazem as condições.

**Exemplo 1:**

``` bash
Input: nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
Output: 3
Explicação: Existem 3 pares que satisfazem as condições: 
1. i = 0, j = 1: 3 - 2 <= 2 - 2 + 1. Como i < j e 1 <= 1, esse par satisfaz as condições. 
2. i = 0, j = 2: 3 - 5 <= 2 - 1 + 1. Como i < j e -2 <= 2, esse par satisfaz as condições. 
3. i = 1, j = 2: 2 - 5 <= 2 - 1 + 1. Como i < j e -3 <= 2, esse par satisfaz as condições. 
Portanto, retornamos 3.
```

**Exemplo 2:**

``` bash
Input: nums1 = [3,-1], nums2 = [-2,2], diff = -1
Output: 0
Explicação: Como não existe nenhum par que satisfaça as condições, retornamos 0.
```