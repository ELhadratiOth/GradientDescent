import numpy as np
import matplotlib.pyplot as plt

def fonction(x):
    return np.sin(x) + np.sin(2*x)

def derive(x):
    return np.cos(x) + 2*np.cos(2*x)

#choix d'intervalle
x = np.arange(0 , 7 ,0.1)
y = fonction(x)

pt1 = (1 , fonction(1))
pt2 = (3.8 , fonction(3.8))
L = 0.02

for _ in range(1000):
    new_x = pt1[0] - L * derive(pt1[0])
    new_x2 = pt2[0] - L * derive(pt2[0])
    pt1_old = pt1[:]
    pt2_old = pt2[:]
    pt1 = (new_x , fonction(new_x))
    pt2 = (new_x2 , fonction(new_x2))

    plt.plot(x, y)
    plt.scatter(pt1[0] , pt1[1] , color='red')
    plt.scatter(pt2[0] , pt2[1] , c='b')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Fonction avec deux minima')
    plt.grid(True)

# marge de tolerence
    if abs(pt1[1] - pt1_old[1]) < 1e-6 and abs(pt2[1] - pt2_old[1]) < 1e-6:
        if pt1[1] < pt2[1]:
            print(f"Point Minimal : ({pt1[0]} , {pt1[1]})")

        else:
            print(f"Point Minimal : ({pt2[0]} , {pt2[1]})")

        plt.show()
        break
    plt.pause(0.001)
    plt.clf()


