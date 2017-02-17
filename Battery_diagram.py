import matplotlib.pyplot as plt
import numpy as np

plt.figure(1,figsize=[10,8])
plt.clf()

jmax=10
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

ax.set_xlabel(r'$k$', fontsize=20, x=1,y=1)
ax.set_ylabel(r'$j$', fontsize=20, x=1,y=1)

#%%
# Annotating for states
for j in range(jmax):
    for k in range(j+1):
        ax.text(-0.2+k,0.1+j,r'$|'+str(j)+','+str(k)+r'\rangle$') # |j,k>
        ax.text(-0.2+k,-0.2+j,r'$|'+str(j-k)+','+str(k)+r'\rangle$',color='C0') #|l,k>

#%%
# Transitions


plt.show()
