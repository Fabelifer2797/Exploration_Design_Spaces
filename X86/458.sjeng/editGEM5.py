import os
import subprocess
import fileinput
import shutil
insts = """export GEM5_DIR=/home/isaacpope/Documents/GEM5/gem5
export OPT=$GEM5_DIR/build/X86/gem5.opt
export PY=$GEM5_DIR/configs/example/se.py
export BENCHMARK=./src/benchmark
export ARGUMENT=./data/input.program
time $OPT -d m5out/ $PY -c $BENCHMARK -o $ARGUMENT -I 100000000 --cpu-type=TimingSimpleCPU --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=128kB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=2 --cacheline_size=32"""
rep = 128
"""

#l1d size
for i in range(10):
    insts2 = insts
    rep = 2**(7+i)
    reptext = "--l1d_size="+str(rep)+"kB"
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--l1d_size=128kB",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/l1d_size/'+newfile)
#l1i size
for i in range(10):
    insts2 = insts
    rep = 2**(7+i)
    reptext = "--l1i_size="+str(rep)+"kB"
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--l1i_size=128kB",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/l1i_size/'+newfile)
#l2 size
for i in range(10):
    insts2 = insts
    rep = 2**(7+i)
    reptext = "--l2_size="+str(rep)+"kB"
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--l2_size=128kB",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/l2_size/'+newfile)
#l1d assoc
for i in range(10):
    insts2 = insts
    rep = 2**(1 + i)
    reptext = "--l1d_assoc="+str(rep)
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--l1d_assoc=2",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/l1d_assoc/'+newfile)
#l1i assoc
for i in range(10):
    insts2 = insts
    rep = 2**(1 + i)
    reptext = "--l1i_assoc="+str(rep)
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--l1i_assoc=2",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/l1i_assoc/'+newfile)
#l2 assoc
for i in range(10):
    insts2 = insts
    rep = 2**(1 + i)
    reptext = "--l2_assoc="+str(rep)
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--l2_assoc=2",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/l2_assoc/'+newfile)
"""
#line size
for i in range(10):
    insts2 = insts
    rep =  2**(5+i)
    reptext = "--cacheline_size="+str(rep)
    newfile = "stats"+str(rep)+".txt"
    insts2 = insts2.replace("--cacheline_size=32",reptext)
    f = open("exGEM5.sh", "w")
    f.write(insts2)
    f.close()
    os.system('sh exGEM5.sh')
    os.system('cp m5out/stats.txt stats/cacheline/'+newfile)