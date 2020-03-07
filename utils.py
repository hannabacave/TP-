import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def affichagede9iterations(init,  funciteration):
    plt.figure(figsize=(12, 6))
    for i in range(10):
        if i == 0:
            plt.subplot(2, 5, 1)
            plt.imshow(init)
        else:
            plt.subplot(2,  5,  i+1)
            plt.imshow(funciteration(init))
        plt.title("itération" + " " + str(i))


def animer(mat):
    fig = plt.gcf()
    im = plt.imshow(mat)
    plt.show()

    def animate(frame):
        im.set_data(iteration_jeu_np(mat))
        return im,

    ani = animation.FuncAnimation(fig,  animate,  frames=200)

    return(ani)


def animer_tore(mat):
    fig = plt.gcf()
    im = plt.imshow(mat)
    plt.show()

    def animate(frame):
        im.set_data(iteration_jeu_np(mat))
        return im,

    ani = animation.FuncAnimation(fig,  animate,  frames=200)

    return(ani)


def iteration_jeu_np(Z):
    forme = Z.shape
    N = calcul_nb_voisins_np(Z)
    for x in range(1,  forme[0] - 1):
        for y in range(1,  forme[1] - 1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0  # la cellule meurt
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1  # la cellule nait
    return(Z)


def calcul_nb_voisins_np(Z):
    nb_voisins = np.zeros(Z.shape)
    nb_voisins[1:-1,  1:-1] = Z[:-2, :-2] + Z[1:-1, :-2] + Z[2:, :-2] + \
        Z[:-2, 1:-1] + Z[2:, 1:-1] + \
        Z[:-2, 2:] + Z[1:-1, 2:] + Z[2:, 2:]
    return(nb_voisins)
