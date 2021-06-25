import tkinter as tk
import os
#sudo apt-get install python3-tk

root = tk.Tk()
root.geometry("1100x500")
root.title('Ejecutador de Benchmarks para SPEC y PARSEC')
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python
param = tk.IntVar()
param.set(10)

benchmarks = {1: '429.mcf', 2 : '456.hmmer', 3 : "458.sjeng", 4 : "blackscholes" ,  5 :"freqmine" , 6: "swaptions"}
params = {10: 'cacheline', 11: 'l1d_assoc', 12 : "l1d_size", 13 : "l1i_assoc" ,  14 :"l1i_size" , 15: "l2_assoc", 16: "l2_size"}

conBrachPredictor =  False

def ShowChoice():
    return

def ShowParam():
    return



def ejecutar():
    if (conBrachPredictor):
        if (v.get() > 3):
            os.system(
                "python3 PARSEC/" + benchmarks.get(v.get()) + "/stats/" +bpTypes.get(bp.get())+"/"+ bpData.get(bpD.get()) + "/graphics.py ")
        else:
            os.system(
                "python3 SPEC/SPEC/" + benchmarks.get(v.get()) + "/stats/" +bpTypes.get(bp.get())+"/"+ bpData.get(bpD.get()) + "/graphics.py ")
    else :
        if (v.get() > 3):
            os.system(
                "python3 PARSEC/" + benchmarks.get(v.get()) + "/stats/" + params.get(param.get()) + "/graphics.py ")
        else:
            os.system(
                "python3 SPEC/SPEC/" + benchmarks.get(v.get()) + "/stats/" + params.get(param.get()) + "/graphics.py ")



tk.Label(root, text="""Seleccione el Benchmark a Utilizar:""", justify = tk.RIGHT, padx = 20, font=("Courier", 10)).grid(row=0, column=1)

row = 0
i = row + 1

columna = 0
specLabel = tk.Label(root, text="SPEC:").grid(row=i, column=columna, sticky = tk.W)
i = i + 1

mcfRB = tk.Radiobutton(root,text="429.mcf", padx = 20, variable=v, command=ShowChoice, value=1,).grid(row=i, column=columna, sticky = tk.W)
i = i + 1
#print(i)
hmmerRB=tk.Radiobutton(root,text="456.hmmer", padx = 20, variable=v, command=ShowChoice,value=2, ).grid(row=i, column=columna, sticky = tk.W)
i = i + 1
#print(i)
sjengRB = tk.Radiobutton(root,text="458.sjeng", padx = 20, variable=v, command=ShowChoice,value=3).grid(row=i, column=columna, sticky = tk.W)
i = i + 1

j = row + 1
columna = 2
parsecLabel = tk.Label(root, text="PARSEC:").grid(row=j, column=columna, sticky = tk.W)

j =j+ 1

blackscholesRB = tk.Radiobutton(root,text="blackscholes", padx = 20, variable=v, command=ShowChoice, value=4).grid(row=j, column=columna, sticky = tk.W)
j =j+ 1
#print(i)
freqmine = tk.Radiobutton(root,text="freqmine", padx = 20, variable=v, command=ShowChoice,value=5).grid(row=j, column=columna, sticky = tk.W)
j =j+ 1
#print(i)
swaptions = tk.Radiobutton(root,text="swaptions", padx = 20, variable=v, command=ShowChoice,value=6).grid(row=j, column=columna, sticky = tk.W)
j =j+ 1



tk.Label(root, text="""Seleccione el parametro que quiere variar:""", justify = tk.RIGHT, padx = 20, font=("Courier", 10)).grid(row=j, column=0, sticky = tk.W)
j = j + 1

columnaAtributos = 0
l1dzRB = tk.Radiobutton(root,text="l1d_size", padx = 20, variable=param, command=ShowParam,value=12,)
l1dzRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l1isRB = tk.Radiobutton(root,text="l1i_size", padx = 20, variable=param, command=ShowParam,value=14,)
l1isRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l2sRB = tk.Radiobutton(root,text="l2_size", padx = 20, variable=param, command=ShowParam,value=16,)
l2sRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

j = j + 1
columnaAtributos = 0
l1dassRB = tk.Radiobutton(root,text="l1d_assoc", padx = 20, variable=param, command=ShowParam,value=11,)
l1dassRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l1iassRB = tk.Radiobutton(root,text="l1i_assoc", padx = 20, variable=param, command=ShowParam,value=13,)
l1iassRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l2assRB = tk.Radiobutton(root,text="l2_assoc", padx = 20, variable=param, command=ShowParam,value=15,)
l2assRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

j = j + 1
columnaAtributos = 1
cachelineRB = tk.Radiobutton(root,text="cacheline", padx = 20, variable=param, command=ShowParam,value=10,)
cachelineRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1


paramsRB = [l1dzRB,l1isRB, l2sRB, l1dassRB, l1iassRB, l2assRB, cachelineRB]





j = j + 1

bpTypes = {201: 'Sin Branch Predictor', 202 : 'BiModeBP', 203 : "LocalBP", 204 : "TournamentBP" }
tk.Label(root, text="""Seleccione una opción de BP:""", justify = tk.RIGHT, padx = 20, font=("Courier", 10)).grid(row=j, column=0, sticky = tk.W)

j = j + 1

columnaAtributos = 0

bp = tk.IntVar()
bp.set(201)

def ShowBP():
    global conBrachPredictor
    #print(bpTypes.get(bp.get()))
    t = bpTypes.get(bp.get())
    if bp.get() != 201:
        conBrachPredictor = True
        for item in paramsRB:
            #print(item)
            item.config(state='disable')
        for item in datBP:
            #print(item)
            item.config(state='normal')
    elif bp.get() == 201:
        conBrachPredictor = False
        for item in paramsRB:
            #print(item)
            item.config(state='normal')
        for item in datBP:
            #print(item)
            item.config(state='disable')
tk.Radiobutton(root,text="Sin Branch Predictor", padx = 20, variable=bp, command=ShowBP,value=201,).grid(row=j, column=columnaAtributos, sticky = tk.W)


columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="LocalBP", padx = 20, variable=bp, command=ShowBP,value=203,).grid(row=j, column=columnaAtributos, sticky = tk.W)

columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="TournamentBP", padx = 20, variable=bp, command=ShowBP,value=204,).grid(row=j, column=columnaAtributos, sticky = tk.W)

columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="BiModeBP", padx = 20, variable=bp, command=ShowBP,value=202,).grid(row=j, column=columnaAtributos, sticky = tk.W)
j = j + 1




bpData = {301: 'BTBEntries', 302 : 'choicePredictorSize', 303 : "globalPredictorSize", 304 : "localPredictorSize" }
bpD = tk.IntVar()
bpD.set(301)
tk.Label(root, text="""Seleccione el dato que quiere variar del BP:""", justify = tk.RIGHT, padx = 20, font=("Courier", 10)).grid(row=j, column=0, sticky = tk.W)


def ShowBPData():
    return
j = j + 1

bbtRB = tk.Radiobutton(root,text="BTBEntries", padx = 20, variable=bpD, command=ShowBPData,value=301,)
bbtRB.grid(row=j, column=0, sticky = tk.W)
j = j + 1

choicePRB = tk.Radiobutton(root,text="choicePredictorSize", padx = 20, variable=bpD, command=ShowBPData,value=302,)
choicePRB.grid(row=j, column=0,sticky = tk.W)
j = j + 1

globalPRB = tk.Radiobutton(root,text="globalPredictorSize", padx = 20, variable=bpD, command=ShowBPData,value=303,)
globalPRB.grid(row=j, column=0, sticky = tk.W)
j = j + 1

localPRB = tk.Radiobutton(root,text="localPredictorSize", padx = 20, variable=bpD, command=ShowBPData,value=304,)
localPRB.grid(row=j, column=0, sticky = tk.W)
j = j + 1

datBP = [bbtRB,choicePRB, globalPRB, localPRB]

for item in datBP:
    item.config(state='disable')

exitButton = tk.Button(root, text="Ejecutar", command=ejecutar, bg='red').grid(row=j, column=1, sticky = tk.W)

root.mainloop()
