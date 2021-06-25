from pylab import *
import sys
import re

size = []
BTBHits = []
BTBLookups = []
BTBMissPCT = []
numbranchMispred = []
numBranches = []
BranchMispredPct = []
condPredicted = []
condIncorrect = []


for i in range(3):
    rep = 2**(10+i)
    size.append(rep)
    fileo = "SPEC/SPEC/458.sjeng/stats/BiModeBP/localPredictorSize/stats"+str(rep)+".txt"
    with open(fileo) as f: #localPredictorSize
        datafile = f.readlines()
    for line in datafile:
        if "system.cpu.branchPred.BTBHits" in line:
            found = (re.search("([0-9]+)",line))
            BTBHits.append(found[0])
        elif "system.cpu.branchPred.BTBLookups" in line:
            found = (re.search("([0-9]+)",line))
            BTBLookups.append(found[0])
        elif "system.cpu.Branches" in line:
            found = (re.search("([0-9]+)",line))
            numBranches.append(found[0])
        elif "system.cpu.BranchMispred" in line:
            found = (re.search("([0-9]+)",line))
            BranchMispredPct.append(found[0])
        elif "system.cpu.branchPred.condPredicted" in line:
            found = (re.search("([0-9]+)",line))
            condPredicted.append(found[0])
        elif "system.cpu.branchPred.condIncorrect" in line:
            found = (re.search("([0-9]+)",line))
            condIncorrect.append(found[0])
for i in range(3):
    BTBMissPCT.append((1-(int(BTBHits[i])/int(BTBLookups[i])))*100)
    numbranchMispred.append((int(BranchMispredPct[i])/int(numBranches[i]))*100)


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.plot(BTBMissPCT,'o-')
ax1.xaxis.set_ticks(np.arange(3))
ax1.xaxis.set_ticklabels(size)
ax1.legend(["BTBMissPCT"])
ax2.plot(numbranchMispred,'o-')
ax2.xaxis.set_ticks(np.arange(3))
ax2.xaxis.set_ticklabels(size)
ax2.legend(["NumbMisPredBranches"])
ax3.plot(condPredicted,'o-')
ax3.xaxis.set_ticks(np.arange(3))
ax3.xaxis.set_ticklabels(size)
ax3.legend(["condPredicted"])
ax4.plot(condIncorrect,'o-')
ax4.xaxis.set_ticks(np.arange(3))
ax4.xaxis.set_ticklabels(size)
ax4.legend(["condIncorrect"])
ax4.invert_yaxis()
show()