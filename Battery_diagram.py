import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
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

# Annotating
for j in range(jmax):
    for k in range(j+1):
        ax.text(-0.2+k,0.1+j,r'$|'+str(j)+','+str(k)+r'\rangle$')
        ax.text(-0.2+k,-0.2+j,r'$|'+str(j-k)+','+str(k)+r'\rangle$',color='C0')
plt.show()
