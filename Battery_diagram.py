import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('text', usetex=True)

plt.figure(1,figsize=[10,8])
plt.clf()

jmax=5
ax = plt.gca()
# Ploting the levels
for j in range(jmax):
    for k in range(j+1):
        ax.plot([-0.2+k,0.2+k],[j,j],'k',lw=2)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_lw(2)
ax.spines['bottom'].set_lw(2)

ymin,ymax = ax.get_ylim()
ax.set_ylim([-0.5,ymax])
ax.set_xticks(range(jmax))
ax.set_yticks(range(jmax))
ax.tick_params(labelsize=20)

ax.set_xlabel(r'$k$', fontsize=25, x=1,y=1)
ax.set_ylabel(r'$j$', fontsize=25, x=1,y=1)

ax.text(3.5,0.2,r'$|j,k\rangle$',fontsize=15)
ax.text(3.5,0,r'$|l,p\rangle$',fontsize=15,color='C0')

#%%
# Annotating for states
for j in range(jmax):
    for k in range(j+1):
        ax.text(-0.2+k,0.1+j,r'$|'+str(j)+','+str(k)+r'\rangle$',fontsize=20) # |j,k>
        ax.text(-0.2+k,-0.2+j,r'$|'+str(j-k)+','+str(k)+r'\rangle$',color='C0',fontsize=20) #|l,k>

#%%
## Transitions
## j transitions (greens)
#for j in range(jmax-1):
#    ax.annotate('', xy=(-0.2+j, 1+j), xytext=(-0.2+j, 0+j),
#            arrowprops=dict(facecolor='C0',edgecolor='none',shrink=0.1,connectionstyle="arc3,rad=-0.2"),
#            )
##    ax.annotate('', xy=(0.2+j, 0+j), xytext=(0.2+j, 1+j),
##            arrowprops=dict(facecolor='C2',edgecolor='none',shrink=0.1,connectionstyle="arc3,rad=-0.2"),
##            )
#    ax.annotate('', xy=(0.8+j, 1.05+j), xytext=(0.2+j, 1.05+j),
#            arrowprops=dict(facecolor='C2',edgecolor='none',shrink=0.1,connectionstyle="arc3,rad=-0.2"),
#            )
#    ax.annotate('', xy=(0.2+j, 1+j), xytext=(0.8+j, 1+j),
#            arrowprops=dict(facecolor='C3',edgecolor='none',shrink=0.1,connectionstyle="arc3,rad=-0.2"),
#            )
#    ax.plot(0.5+j,0.93+j,'kx',markeredgewidth=2,markersize=12,zorder=10)
#    
#ax.text(-0.2,0.4,r'$a^\dagger$',fontsize=25,color='C0')
#ax.text(0.4,1.3,r'$b_q^\dagger$',fontsize=25,color='C2')
#ax.text(0.4,0.6,r'$b_q$',fontsize=25,color='C3')
#plt.draw()
plt.show()
