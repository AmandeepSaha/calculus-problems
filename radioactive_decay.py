import numpy as np
import matplotlib.pylab as plt

def main():
    # for this particular problem we've chosen lambda = 0.1,0.5,1 and n_0 = 1000 at t=0
    for i in range(3):
        lamda = np.array([0.1,0.5,1])
        nn, tt, ddndt = radio_active_decay(1000,0,lamda[i])
        plt.plot(nn,tt)
        plt.style.use("seaborn")
        plt.title(r"$\bf Solution\:\:of\:\:Radioactive\:\:Decay\:\:Equation$")
        plt.legend([r"$When\:\:\lambda = 0.1\:\:n_0=1000\:\:t_0=0$",r"$When\:\:\lambda = 0.5\:\:n_0=1000\:\:t_0=0$",r"$When\:\:\lambda = 1.0\:\:n_0=1000\:\:t_0=0$"])
        plt.grid(True)
        plt.xlabel(r"$Time\longrightarrow$")
        plt.ylabel(r"$n\longrightarrow $")
        plt.savefig("radioactive_decay.jpg")
    plt.show()

def radio_active_decay(n_0,t_0,lamda):
    # storing points
    nn, tt, ddndt =[],[],[]
    # genereal solution
    dt = 0.05
    for i in range(500):
        dndt = - lamda*n_0
        nn.append(n_0); tt.append(t_0); ddndt.append(dndt)
        t_0 += dt
        n_0 += dt*dndt
    return nn, tt, ddndt

if __name__ =="__main__":
    main()