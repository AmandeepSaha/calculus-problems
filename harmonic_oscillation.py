import numpy as np
import matplotlib.pyplot as plt

def main():
    # for this particular problem we took x_0 = 0, dxdt = 0 at t = 0 & omega_not = f_0 = 1 and w = 0.9 , 1.0
    for i in range(2):
        omega_not = np.array([0.9,1.0])
        x,t,dxdt = forced_harmonic_oscillation(0,0,0,omega_not[i],1,1)
        plt.plot(t,x)
        plt.title(r"$\circ\mathcal{Forced\:\:Harmonic\:\:Oscillation}\circ$")
        plt.legend([r"$at\:\:\omega_0=0.9$",r"$at\:\:\omega_0=1.0$"])
        plt.xlabel(r"$\sf{Time}\longrightarrow$")
        plt.ylabel(r"$\sf{displacement}\longrightarrow$")
        plt.grid(True)
        plt.style.use("seaborn")
        plt.savefig("ForcedHarmonicOscillation.jpg")
    plt.show()

def forced_harmonic_oscillation(x_0,t_0,u_0,omega_not,f_0,w):
    dt = 0.05
    xx,tt,uu=[],[],[]
    for i in range(1000):
        # storing values
        uu.append(u_0);tt.append(t_0);xx.append(x_0)
        # finding u
        dudt = -x_0*omega_not**2-f_0*np.sin(w*t_0)
        du = dt*dudt
        u_0 += du
        # finding x
        dx = dt*uu[i]
        x_0 += dx
        # time incriment
        t_0 += dt
    return np.array(xx),np.array(tt),np.array(uu)

if __name__=="__main__":
    main()