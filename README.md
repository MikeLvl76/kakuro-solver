<div style="text-align: justify">
# IA

- Année : **2021-2022 (M1 IWOCS)**
- TP : Projet sur la résolution du Kakuro

# Auteur

|Nom|Prénom|
|--|--|
*Louvel* | *Mickael*|

# Présentation
- Principe : **programmer la résolution automatique du [Kakuro](https://fr.wikipedia.org/wiki/Kakuro) en utilisant le [Recuit simulé](https://fr.wikipedia.org/wiki/Recuit_simul%C3%A9) avec une fitness établie**
- Langage utilisé : **Python**

## Implémentation
Nous avons utilisé une classe pour programmer cette résolution. Cette classe nommée `Resolver` contient plusieurs variables globales dont une importante : `grid` qui contient toute la grille et qui sera utilisée lors de cette résolution. Pour créer la grille on utilise un fichier texte externe que l'on lit pour récupérer ses données. Lorsque la grille est créee, on la remplit avec des valeurs aléatoires.

Cette classe permet aussi de donner l'état voisin de la grille grâce à sa méthode `neighbor`, c'est-à-dire qu'on copie la  grille actuelle, on change aléatoirement une valeur parmis celles possibles et on renvoie un nouvel objet contenant la copie modifiée. Cette méthode sert lors de la résolution du problème.

Pour simuler le recuit il faut d'abord prendre en compte un paramètre : la **fitness**. Ce paramètre détermine si la solution a été trouvée ou non, il faut donc calculer ce paramètre.
Le moyen de calculer la fitness peut se faire avec plusieurs méthodes, dans notre cas on peut utiliser le nombre de lignes et de colonnes erronées ou bien la somme des valeurs absolues de la différence entre le résultat attendu et celui obtenu. Ces deux versions offrent le même résultat mais représentent une approche différente du problème. Les deux versions sont implémentées mais une seule est utilisée. La méthode qui en résulte se nomme `get_quality`. 

## Quel choix de fitness faire ?

### <u>Option 1 : **Comparer la valeur obtenu en additionnant celles des cases blanches pour une ligne ou une colonne avec celle de l'indicateur**.</u>

Cette option est la plus simple à appréhender, en effet il faut seulement compter le nombre de lignes ou colonnes fausses. Si une ligne ou colonne est bonne, on ne la compte pas. Le but est d'arriver à 0 erreurs, mais il est possible que cela prenne beaucoup de temps et beaucoup d'itérations ou d'être bloqué temporairement à un minimum local. On peut arriver à un nombre d'erreurs assez important et qui lors de l'implémentation du recuit simulé peut allonger la durée de procédure, de plus il faut comparer la somme obtenue et celle de l'indicateur, ce qui ajoute un peu plus de temps.

### <u>Option 2 : **Calculer la somme des valeurs absolues de la difference entre la valeur de l'indicateur et la valeur de la somme obtenue**.</u>

Cette méthode permet d'éviter de comparer à chaque itération la valeur de l'indiacteur à celle obtenue par la somme des valeurs des cases blanches suivantes. De plus grâce à la valeur absolue on évite une valeur de fitness potentiellement négative. On évite aussi de rester bloqué trop longtemps à un minimum local car on sait que lorsque l'on obtient un écart nul alors la ligne ou la colonne est correcte et on peut passer à la suivante, ce qui permet d'économiser du temps.


### <u>Notre choix :</u>

Notre choix s'est porté vers l'option 2 qui est plus efficace et évite d'effectuer trop d'opérations.

## Recuit simulé

### <u>Implémentation :</u>
Nous avons donc implémenté une nouvelle classe nommée `Solution` permettant de simuler le recuit. Cette dernière contient plusieurs variables globales importantes telles que la `température`, le `refroidissement`, et deux variables pour les itérations permettant de réaliser la descente aléatoire pure. La méthode principale servant à la résolution du puzzle se nomme `resolve` et accepte en argument un objet `Resolver` et retourne cet argument.

### <u>Descente aléatoire pure</u>

Cette classe implémente la descente aléatoire pure et se base via une température qui augmente ou diminue selon plusieurs paramètres. On peut ajouter un autre critère tel que le nombre d'itérations maximum (pour éviter une simulation trop longue), ce que nous utilisons dans notre cas. Lorsque la température est basse et le nombre limite d'itérations est atteint le système s'arrête quitte à tomber dans un minimum local car l'énergie du système est nulle. On peut représenter l'énergie de ce sytème par la fitness de notre programme : c'est elle qui détermine si le système peut passer d'un état à un autre ou non quitte à tomber dans un minimul local. Pour savoir quand la température doit augmenter ou baisser il nous faut un peu d'aléatoire : on génère un nombre aléatoire dans l'intervalle [0,1] et on vérifie que :
```math
random(0,1) < \exp(-\frac{\Delta_{E}}{T})
```
Avec $`\Delta_{E}`$ ici correspondant à la différence entre la fitness de la grille voisine et celle de la grille actuelle et $`T`$ qui est la température. La méthode utilisée pour cette condition se nomme `accept` et prend en argument la différence entre les deux fitness et la température et renvoie `True` ou `False`. Si cette condition est vérifiée alors on accepte de changer d'état (dans notre cas la grille voisine remplace l'ancienne).

Ensuite on vérifie que l'on peut encore changer d'état pour cela on compare la fitness obtenue pour l'état actuelle et celle du premier état au début du programme, si les deux sont égales alors on incrémente un compteur (qui nous servira pour plus tard), sinon on change la fitness de l'état actuelle pour celle du premier état et on remet ce compteur à 0.

Si le compteur dépasse une certaine valeur alors on tombe dans un minimum local et on accepte alors une hausse légère de la température. La méthode `increase_temperature` permet d'augmenter cette température, elle prend en argument cette dernière et lui applique cette formule : $`T + (T - (T \cdot F))`$ avec $`T`$ la température et $`F`$ le facteur de refroidissement (la variable globale déclarée au début). Cette augmentation est légère car on ne veut pas rajouter trop d'états supplémentaires. On remet le compteur à 0.

Enfin il faut naturellement que la température baisse alors à chaque itération on multiplie la température par le facteur de refroidissement, ce dernier étant très proche de 1 on évite un refroidissement trop rapide du système. La méthode qui implémente ceci se nomme `coolen` et prend une température en argument.
</div>

# Résultat obtenu

En paramètrant la température à 1.0, le facteur de refroidissement à 0.9, le nombre max d'itérations à 5000 et le nombre d'itérations pour faire évoluer l'énergie du système à 100, on obtient un temps de résolution correcte pour 3 types de grilles :

- Grille 6x6 : très facile à résoudre, son temps de résolution est très faible et avoisinne la demi-seconde.
- Grille 8x8 : un peu plus compliquée, son temps de résolution avoisinne la seconde voire 2 secondes.
- Grille 14x14 : devient beaucoup plus complexe, son temps de résolution peut avoisinner la minute.
