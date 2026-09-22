# 2. Add Two Numbers

**Nível:** medium
**Link:** https://leetcode.com/problems/add-two-numbers/

## Descrição do problema

Você recebe dois números **não negativos**, representados como **listas encadeadas** (linked lists). Cada nó da lista guarda um único dígito, e os dígitos estão armazenados em **ordem inversa** — ou seja, o primeiro nó da lista representa a unidade, o segundo a dezena, e assim por diante.

O desafio é somar os dois números e retornar o resultado também como uma lista encadeada, seguindo o mesmo formato (ordem inversa).

Pode-se assumir que nenhum dos dois números tem zero à esquerda, exceto o próprio número 0.

## Exemplos

**Exemplo 1:**
```
Entrada: l1 = [2,4,3], l2 = [5,6,4]
Saída: [7,0,8]
Explicação: 342 + 465 = 807
```
*(Repare que [2,4,3] representa o número 342, já que está em ordem inversa: 2 é a unidade, 4 é a dezena, 3 é a centena.)*

**Exemplo 2:**
```
Entrada: l1 = [0], l2 = [0]
Saída: [0]
```

```
Entrada: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Saída: [8,9,9,9,0,0,0,1]
Explicação: 9999999 + 9999 = 10009998
```

## Restrições

- Cada lista encadeada tem entre 1 e 100 nós.
- Cada nó guarda um valor entre 0 e 9.
- É garantido que os números representados não possuem zeros à esquerda.
