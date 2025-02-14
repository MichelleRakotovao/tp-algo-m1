# tp-algo-m1

Classe : ISAIA 4
RAJOHARIVELO Andriarivony Antenaina, numéro: 01
a developpé la partie II "Création d'une interface graphique jouable"
RAHERIMANANA Andriniaina Koloina Mandresy, numéro: 05
a developpé dans la partie 1, les questions: 2, 3, 4, 5
RAKOTOVAO Holiantenaina Josée Michelle, numéro : 17
a aussi developpé la partie II "Création d'une interface graphique jouable"

## Table des matières TOVO Jean Bien aimé, numéro: 15:

1. [Introduction](#introduction)
2. [Règles du jeu](#règles-du-jeu)
3. [Fonctionnalités principales](#fonctionnalités-principales)
   - [Création et gestion des parties](#création-et-gestion-des-parties)
   - [Traitement Bit à Bit](#traitement-bit-à-bit)
   - [Mouvements et Successeurs](#mouvements-et-successeurs)

## Règles du jeu

#### `get_successors(i, j)`

Cette fonction calcule les successeurs possibles pour une position donnée sur le plateau (i, j) :

```python
def get_successors(i, j):
    successors = 0
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (1, 1), (-1, 1), (1, -1)
    ]

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3 and Bits.is_adjacent(i, j, ni, nj):
            position = ni * 3 + nj
            successors |= (1 << position)

    return successors
```
