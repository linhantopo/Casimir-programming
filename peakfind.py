import matplotlib.pyplot as plt import numpy as np from scipy.optimize import curve_fit %matplotlib inline def 
fig(r):
    return np.sin(r)/r def gaus(x, amp, cen, wid):
    return amp * np.exp(-(x-cen)**2 / wid) x = np.linspace(10, 50, 101) noise = 0.02*np.random.random_sample(101) y 
= fig(x)+noise plt.plot(x, y)
#----find the local peak----
""" for i in range(len(x)-2):
    if y[i+1]>y[i] and y[i+1]>y[i+2]:
        plt.plot(x[i+1],y[i+1],"bo")
    else:
        i=i """
#----to be resistant against noise----
peakdist = 5 #in number of points for i in range(len(x)-2):
    if y[i+1]>y[i] and y[i+1]>y[i+2]:
        plt.plot(x[i+1],y[i+1],"bo")
    else:
        i=i init_vals = [1, 0, 1] popt,pcov = curve_fit(gaus,x,y,p0=init_vals)
