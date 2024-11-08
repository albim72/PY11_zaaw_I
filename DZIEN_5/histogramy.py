

import numpy as np
import matplotlib.pyplot as plt
     

np.random.seed(19680801)
n_bins = 10
x = np.random.randn(1000,3)
     

fig,((ax0,ax1),(ax2,ax3)) = plt.subplots(nrows=2,ncols=2)
colors = ['red','tan','lime']
ax0.hist(x,n_bins,density=True,histtype='bar',color=colors,label=colors)
ax0.legend(prop={'size':10})
ax0.set_title('słupki z legendą!')

ax1.hist(x,n_bins,density=True,histtype='bar',stacked=True)
ax1.set_title('słupki kumulacyjne')

ax2.hist(x,n_bins,density=True,histtype='step',stacked=True,fill=False)
ax2.set_title('stos schodków(bez wypełnienia)')

x_multi = [np.random.randn(n) for n in [10000,5000,2000]]
ax3.hist(x_multi,n_bins,density=True,histtype='bar')
ax3.set_title('3 histogramy o różnych wartościach')

fig.tight_layout()
plt.show()
     
