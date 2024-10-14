import numpy as np
import matplotlib.pyplot as plt

# Main function
def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5


def z_gradient(x,y):
    return np.cos(5 * x)*np.cos(5 * y), -np.sin(5 * x)*np.sin(5 * x)

# Generation de vals
x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

learning_rate = 0.001

# dessin du graph
ax = plt.subplot(projection='3d'  , computed_zorder=False)
pt1 = (0.3, 0.4, z_function(0.3, 0.4))

check = False

for _ in range(1000) :
    X_d , Y_d = z_gradient(pt1[0] , pt1[1])
    new_X = pt1[0] - learning_rate * X_d
    new_Y = pt1[1] - learning_rate * Y_d
    pt1_old = pt1[:]
    pt1 = (new_X, new_Y, z_function(pt1[0], pt1[1]))
    ax.plot_surface(X, Y, Z,cmap='viridis' , zorder = 0)
    ax.scatter(pt1[0], pt1[1] ,z_function(pt1[0], pt1[1]),  color="magenta" , zorder=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')

    if abs( pt1[2] - pt1_old[2] )  < 0.0001 and check:
        print(f"Point Minimal : ({pt1[0]} , {pt1[1]} , {pt1[2]})")

        plt.show()
        break
    if abs( pt1[2] - pt1_old[2] )  < 0.0001 and check == False:
        check = True


    plt.pause(0.001)
    ax.clear()
