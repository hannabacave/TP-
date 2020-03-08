import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation


def affichagede9iterations(mat, iteration):
    plt.figure(figsize=(7, 5))
    for i in range(10):
        if i == 0:
            plt.subplot(2, 5, 1)
            plt.imshow(mat)
        else:
            plt.subplot(2,  5,  i+1)
            plt.imshow(iteration(mat))
        plt.title("itération" + " " + str(i))
        plt.suptitle("Affichage des 9 premières itérations du jeu")

# Configurations stables

S1 = np.zeros((50, 50))
S1[25, 24] = S1[24, 24] = S1[24, 25] = S1[25, 26] = \
S1[25, 27] = S1[25, 27] = S1[24, 27] = 1  # serpent

S2 = np.zeros((50, 50))
S2[26, 24] = S2[25, 25] = S2[24, 26] = S2[25, 27] = \
S2[26,27] = S2[27, 26] = S2[27, 25] = 1  # mie de pain

S3 = np.zeros((50, 50))
S3[25, 24] = S3[26, 24] = S3[26, 25] = \
S3[25, 26] = S3[24, 25] = 1  # bateau

# Configuration oscillante

O = np.zeros((50, 50))
O[25, 24] = O[25, 25] = O[25, 26] = 1  # clignotant