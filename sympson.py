import numpy as np
import matplotlib.pyplot as plt

def H(z):
	return 68.*(1.+z)*np.sqrt((0.27*(1.+z) + 0.73*np.power(1.+z,-2)))


def f(z):
	return 1./((z+1.) * H(z)) 


def inte(zi, zf, dz):
	return (dz/3.)*(f(zi) + 4.0*f((zi + zf)/2 + f(zf)))

a = np.linspace(10**-4, 10**-3, 1000)
b = np.linspace(10**-3, 10**-2, 1000)
c = np.linspace(10**-2, 10**-1, 1000)
d = np.linspace(10**-1, 1, 1000)
e = np.linspace(1, 10, 1000)
g = np.linspace(10, 10**5, 100000)
	
zarray = np.concatenate((a,b,c,d,e,g), 0)

print (len(zarray))

dtz = [10**-9]
for i in range(0,len(zarray)-1):
	dtz.append(inte(zarray[i],zarray[i+1],zarray[i+1] - zarray[i])+dtz[i-1])
#dtz = np.array([int(i, i+1, (i+1-i)) for i in zarray])
plt.figure()
f = plt.subplot(1,1,1)
f.plot(zarray,dtz)

plt.ylabel('t0-t(z) -->')
plt.xlabel('Cosmological Redshift (z) -->')
plt.title('t0-t(z) vs z')
f.set_xscale('log')
f.set_yscale('log')
plt.show()
