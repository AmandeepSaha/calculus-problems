import numpy as np
import matplotlib.pyplot as plt

def main():
    # for this particular problem we've chosen E = 10, R = 100, C = 0.015 & given initial conditions q = 0 at t = 0
    q,t = rc(0,0,100,0.015,10)
    plt.plot(t,q)
    plt.grid(True)
    plt.style.use("seaborn")
    plt.xlabel(r"$\sf{Time}\longrightarrow$")
    plt.ylabel(r"$\sf{q}\longrightarrow$")
    plt.text(5,0.13,r"$\frac{dq}{dt}+\frac{q}{RC}-\frac{E}{R}=0$",fontsize=12)
    plt.title(r"$\circ\mathcal{Charging \:\:of\:\: Capacitor\:\: in\:\: R-C\:\: Circuit}\circ$")
    plt.show()

def rc(q_0,t_0,R,C,E):
    dt = 0.05
    qq,tt=[],[]
    for i in range(500):
        qq.append(q_0);tt.append(t_0)
        dqdt = -q_0/(R*C)+E/R
        dq = dt*dqdt
        q_0 += dq
        t_0 += dt
    return np.array(qq), np.array(tt)

if __name__=="__main__":
    main()