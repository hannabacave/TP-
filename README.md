# TP- Jeu de la vie

On se propose durant tout ce TP de modéliser le *jeu de la vie*. Il se joue sans joueur sur une grille à deux dimensions composée de cellules ayant un état binaire, elles prennent la valeur 1 si elles sont vivantes et 0 si elles sont mortes. Ainsi, à chaque étape que l'on appelle *génération*, les cellules évoluent. Leur évolution se fait en fonction de leur voisinage selon les règles suivantes :

 - si une cellule est isoléee, c'est-à-dire qu'elle possède 0 ou 1 voisin alors elle meurt à la génération suivante, elle meurt par *isolement* ;
 
 - si une cellule est entourée par 2 ou 3 voisins alors elle reste en vie à la génération suivante, on parle d'*équilibre* ; 
 
 - si une celllule cellule est entourée par trop de voisins, c'est-à-dire qu'elle possède 4 voisins ou plus alors elle meurt à la génération suivante, elle meurt par *étouffement*
 
De plus, si une cellule **morte** possède exactement 3 voisins alors elle sera vivante à la génration suivante, on parle donc de *naissance*.

Ainsi, nous allons implémenter toutes ces règles afin de modéliser, au mieux, le jeu de la vie. 