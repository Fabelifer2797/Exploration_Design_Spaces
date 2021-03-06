from pylab import *
import sys
import re

data = []
size = []
hits = []
numCycles = []
insts = []
CPI = []
writebacks = np.zeros(3)


for i in range(3):
    rep = 2**(1+i)
    size.append(rep)
    fileo = "ARM/401.bzip2/stats/l2_assoc/stats"+str(rep)+".txt"
    with open(fileo) as f:
        datafile = f.readlines()
    for line in datafile:
        if "system.l2.overallMisses::total " in line:
            found = (re.search(" ([0-9]+)",line))
            data.append(found[0])
        elif "system.l2.overallHits::total" in line:
            found = (re.search(" ([0-9]+)",line))
            hits.append(found[0])
        elif "system.l2.writebacks::total" in line:
            found = (re.search(" ([0-9]+)",line))
            writebacks[i] = found[0]
        elif "system.cpu.numCycles" in line:
            found = (re.search("([0-9]+)",line))
            numCycles.append(found[0])
        elif "simInsts" in line:
            found = (re.search("([0-9]+)",line))
            insts.append(found[0])
for i in range(3):	
    CPI.append(int(numCycles[i])/int(insts[i]))

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.invert_yaxis()
ax1.plot(data,'o-')
ax1.xaxis.set_ticks(np.arange(3))
ax1.xaxis.set_ticklabels(size)
ax1.legend(["Misses"])
ax2.plot(hits,'o-')
ax2.legend(["Hits"])
ax2.xaxis.set_ticks(np.arange(3))
ax2.xaxis.set_ticklabels(size)
ax3.plot(writebacks,'o-')
ax3.legend(["WriteBacks"])
ax3.xaxis.set_ticks(np.arange(3))
ax3.xaxis.set_ticklabels(size)
ax4.plot(CPI,'o-')
ax4.legend(["CPI"])
ax4.xaxis.set_ticks(np.arange(3))
ax4.xaxis.set_ticklabels(size)
show()
