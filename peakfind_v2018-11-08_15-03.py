import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

%matplotlib inline 
def fig(r):
    return np.sin(r)/r
def gaus(x, a, x0, sigma, b):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))+b
#    return a*np.exp(-(x-x0)**2/sigma)

fitrange = 8 #in number of points
guess_peaktomidgaus=0.9 #how far is our middle point of gauss-fit away from the peak we fit
guess_peakdist = 5 #in number of x coordinate

x = np.linspace(10, 50, 201)
noise = 0.02*np.random.random_sample(size=len(x))
y = fig(x)+noise
plt.figure(figsize=(15,5))

plt.plot(x, y)

#----find the local peak----
"""
for i in range(len(x)-2):
    if y[i+1]>y[i] and y[i+1]>y[i+2]:
        plt.plot(x[i+1],y[i+1],"bo")
    else:
        i=i
"""
#----to be resistant against noise----
peakloc_x = []
peakloc_y = []
peak_num = []
numloc = 0
for i in range(len(x)-2):
    if y[i+1]>y[i] and y[i+1]>y[i+2]:
        plt.plot(x[i+1],y[i+1],"bo")  #plot the blue spots
        peakloc_x.append(x[i+1])
        peakloc_y.append(y[i+1])
        peak_num.append(i+1)
        numloc +=1 
    else:
        i=i
print(peak_num)#the x coordinate of the peak is the peak_num th value in x range
print(len(peak_num))
#----test the gaus function in finding local peaks---- 
"""
x0=x[20:30]
y0=y[20:30]
popt, pcov = curve_fit(gaus, x0, y0, p0=(200, 20, 5, 0.05))#, maxfev=1000)
plt.plot(x0,y0,'y')
ym = gaus(x0, popt[0], popt[1], popt[2], popt[3])
plt.plot(x0, ym, 'r*')
"""
#----start to find real peaks and kickout local ones----
for k in range(len(peak_num)):
    n=peak_num[k]
    
    if n>=fitrange and n<=len(x)-fitrange:
        x0=x[n-fitrange:n+fitrange]
        y0=y[n-fitrange:n+fitrange]    
    elif n<fitrange:
        x0=x[0:n+fitrange]
        y0=y[0:n+fitrange]
    else:
        x0=x[n-fitrange:len(x)]
        y0=y[n-fitrange:len(x)]
    popt, pcov = curve_fit(gaus, x0, y0, p0=(20, x[n], 5, y[n]), maxfev=int(1e7))
    if popt[0]>0 and x[n]-guess_peaktomidgaus<popt[1]<x[n]+guess_peaktomidgaus:
        print("chozen popt")
        plt.plot(x0,y0,'y')
        ym = gaus(x0, popt[0], popt[1], popt[2], popt[3])
        plt.plot(x0, ym, 'r-')
    else:
        k=k
#----try to identify the real peak instead of the local peak