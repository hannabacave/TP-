import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def affichagede10iterations(init, funciteration):
    plt.figure(figsize=(12,6))
    for i in range(10):
        if i == 0:
            plt.subplot(2,5,1)
            plt.imshow(init)
        else:
            plt.subplot(2, 5, i+1)
            plt.imshow(funciteration(init))
        plt.title("itération" + " " + str(i + 1))

def anim(mat):
    fig = plt.gcf()
    im = plt.imshow(mat)
    plt.show()

    def animate(frame):
        im.set_data(iteration_jeu_np(mat))
        return im,

    ani = animation.FuncAnimation(fig, animate, frames=200)
    return(ani)
