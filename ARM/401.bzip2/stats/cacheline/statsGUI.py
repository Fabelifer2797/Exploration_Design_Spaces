from pylab import *
import sys
import re

size = []
missesdcache = []
missesicache = []
misses2cache = []
hitsdcache = []
hitsicache = []
hits2cache = []


for i in range(3):
    rep = 2**(5+i)
    size.append(rep)
    fileo = "ARM/401.bzip2/stats/cacheline/stats"+str(rep)+".txt"
    with open(fileo) as f:
        datafile = f.readlines()
    for line in datafile:
        if "system.cpu.dcache.overallMisses::total" in line:
            found = (re.search("([0-9]+)",line))
            missesdcache.append(found[0])
        elif "system.cpu.dcache.overallHits::total" in line:
            found = (re.search("([0-9]+)",line))
            hitsdcache.append(found[0])
        elif "system.cpu.icache.overallMisses::total " in line:
            found = (re.search("([0-9]+)",line))
            missesicache.append(found[0])
        elif "system.cpu.icache.overallHits::total" in line:
            found = (re.search("([0-9]+)",line))
            hitsicache.append(found[0])
        elif "system.l2.overallMisses::total " in line:
            found = (re.search(" ([0-9]+)",line))
            misses2cache.append(found[0])
        elif "system.l2.overallHits::total" in line:
            found = (re.search(" ([0-9]+)",line))
            hits2cache.append(found[0])

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
ax1.invert_yaxis()
ax1.plot(missesdcache,'o-')
ax1.xaxis.set_ticks(np.arange(3))
ax1.xaxis.set_ticklabels(size)
ax1.legend(["MissesDCache"])
ax2.plot(hitsdcache,'o-')
ax2.legend(["HitsDCache"])
ax2.xaxis.set_ticks(np.arange(3))
ax2.xaxis.set_ticklabels(size)
ax3.invert_yaxis()
ax3.plot(missesicache,'o-')
ax3.legend(["MissesICache"])
ax3.xaxis.set_ticks(np.arange(3))
ax3.xaxis.set_ticklabels(size)
ax4.plot(hitsicache,'o-')
ax4.legend(["HitsICache"])
ax4.xaxis.set_ticks(np.arange(3))
ax4.xaxis.set_ticklabels(size)
ax5.invert_yaxis()
ax5.plot(misses2cache,'o-')
ax5.legend(["MissesL2Cache"])
ax5.xaxis.set_ticks(np.arange(3))
ax5.xaxis.set_ticklabels(size)
ax6.plot(hits2cache,'o-')
ax6.legend(["HitsL2Cache"])
ax6.xaxis.set_ticks(np.arange(3))
ax6.xaxis.set_ticklabels(size)
show()
