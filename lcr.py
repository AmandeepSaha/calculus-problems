import numpy as np
import matplotlib.pyplot as plt

def main():
    # for this particular problem I_0 = 0 at t = 0 & dIdt = 1 at t = 0. And I'll use given values of alpha and omega
    for i in range(3):
        alpha = np.array([0.3,0.7,1])
        omega = 1
        I,t,dIdt = lcr(0,0,1,alpha[i],omega)
        plt.plot(t,I)
        plt.style.use("ggplot")
        plt.title(r"$\circ\mathcal{Solution\:\:graph\:\:of\:\:LCR}\circ$")
        plt.legend([r"$At\:\:\alpha=0.3\:\:\omega=1$",r"$At\:\:\alpha=0.7\:\:\omega=1$",r"$At\:\:\alpha=1.0\:\:\omega=1$"])
        plt.xlabel(r"$\sf{Time}\longrightarrow$")
        plt.ylabel(r"$\sf{Current}\longrightarrow$")
        plt.grid()
        plt.savefig("lcr.jpg")
    plt.show()

def lcr(I_0,t_0,u_0,alpha,omega):
    dt = 0.05
    II,tt,uu=[],[],[]
    for i in range(500):
        # finding I and incrimenting t
        t_0 += dt
        II.append(I_0);tt.append(t_0)
        dI = u_0*dt
        I_0 += dI
        # going to find u
        uu.append(u_0)
        du = dt*(-2*alpha*u_0-II[i]*omega**2)
        u_0 += du
    np.array(II);np.array(tt),np.array(uu)
    return II, tt, uu

if __name__=="__main__":
    main()