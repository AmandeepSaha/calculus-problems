# we're interested here to solve differential equation dy/dx = y

import numpy as np
import matplotlib.pyplot as plt

def main():
    # plot & evaluation at a certain point
    x,y,dydx = function_defined(0,1)
    plt.plot(x,y,color="red",markersize=2)
    plt.grid()
    plt.title(r"${\bb{Solution\:\:Graph\:\:of}}\:\:\sf\frac{dy}{dx}=y$")
    plt.xlabel("x");plt.ylabel("y")
    plt.xlim(0,3);plt.ylim(0,15)
    plt.show()

def function_defined(x_0,y_0):                          # now we're solving for dy/dx = y but still we took x_0 & y_0 as peremeters of the function, because we will give a try for other similler functions in this program
    dx = 0.05
    xx = []; yy = []; dydx =[]                          # storing points in dictonary
    for i in range(500):
        xx.append(x_0);yy.append(y_0);dydx.append(y_0)
        dy = dx*y_0
        x_0 = x_0 + dx
        y_0 = y_0 + dy
    xx = np.array(xx);yy = np.array(yy); dydx = np.array(dydx)
    return xx, yy, dydx


if __name__ == '__main__':
    main()