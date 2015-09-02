import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('whistler.csv',delimiter=',')
plt.plot_date(data[:,0],data[:,1])
plt.show()
