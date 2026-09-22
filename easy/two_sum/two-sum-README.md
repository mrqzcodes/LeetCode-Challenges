# 1. Two Sum

**Nível:** easy
**Link:** https://leetcode.com/problems/two-sum/description/

## Descrição do problema

Você recebe uma lista de números inteiros e um valor alvo (`target`). O objetivo é encontrar os **índices** de dois números dentro dessa lista que, somados, resultem exatamente nesse valor alvo.

Algumas regras importantes:
- Existe sempre **exatamente uma solução** possível para cada entrada.
- Você **não pode usar o mesmo elemento duas vezes** (ou seja, não pode somar um número com ele mesmo usando o mesmo índice).
- A ordem dos índices na resposta não importa.

## Exemplos

**Exemplo 1:**
```
Entrada: nums = [2, 7, 11, 15], target = 9
Saída: [0, 1]
Explicação: nums[0] + nums[1] = 2 + 7 = 9
```

**Exemplo 2:**
```
Entrada: nums = [3, 2, 4], target = 6
Saída: [1, 2]
```

**Exemplo 3:**
```
Entrada: nums = [3, 3], target = 6
Saída: [0, 1]
```

## Restrições

- A lista tem entre 2 e 10.000 elementos.
- Cada número da lista pode variar de -1.000.000.000 a 1.000.000.000.
- O valor alvo também pode variar nesse mesmo intervalo.
- Sempre existe uma única resposta válida.

## Desafio extra (Follow-up)

Dá pra resolver com uma complexidade de tempo **menor que O(n²)**? (Dica: pensar em uma estrutura que permita consultas rápidas, tipo um hash map/dicionário.)
