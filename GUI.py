import tkinter as tk
import os
from typing import Text
from PIL import Image, ImageTk


root = tk.Tk()
root.geometry("1100x600")
root.title('Exploración espacios de diseño con GEM5')
root.configure(background="gray26")
image = Image.open('1.png').resize((200,200))
photo_image = ImageTk.PhotoImage(image)
labelI = tk.Label(root, image = photo_image)
v = tk.IntVar()
v.set(1)  
param = tk.IntVar()
param.set(10)

benchmarks = {1: '429.mcf', 2 : '456.hmmer', 3 : "458.sjeng", 4 : "401.bzip2" ,  5 :"429.mcf" , 6: "458.sjeng"}
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
                "python3 ARM/" + benchmarks.get(v.get()) + "/stats/" +bpTypes.get(bp.get())+"/"+ bpData.get(bpD.get()) + "/statsGUI.py ")
        else:
            os.system(
                "python3 X86/" + benchmarks.get(v.get()) + "/stats/" +bpTypes.get(bp.get())+"/"+ bpData.get(bpD.get()) + "/statsGUI.py ")
    else :
        if (v.get() > 3):
            os.system(
                "python3 ARM/" + benchmarks.get(v.get()) + "/stats/" + params.get(param.get()) + "/statsGUI.py ")
        else:
            os.system(
                "python3 X86/" + benchmarks.get(v.get()) + "/stats/" + params.get(param.get()) + "/statsGUI.py ")



tk.Label(root, text="""Seleccione el ISA que desea probar\n con los benchmarks de SPEC:""", justify = tk.LEFT, padx = 5,background="gray26", fg="white", font=("Courier bold", 12)).grid(row=0, column=0)

row = 0
i = row + 2

columna = 0
specLabel = tk.Label(root, text="X86:", background="gray26", fg="white").grid(row=i, column=columna, sticky = tk.W)
i = i + 1

mcfRB = tk.Radiobutton(root,text="429.mcf",background="gray26", fg="white", padx = 20, variable=v, command=ShowChoice, value=1,).grid(row=i, column=columna, sticky = tk.W)
i = i + 1

hmmerRB=tk.Radiobutton(root,text="456.hmmer",background="gray26", fg="white", padx = 20, variable=v, command=ShowChoice,value=2, ).grid(row=i, column=columna, sticky = tk.W)
i = i + 1

sjengRB = tk.Radiobutton(root,text="458.sjeng",background="gray26", fg="white", padx = 20, variable=v, command=ShowChoice,value=3).grid(row=i, column=columna, sticky = tk.W)
i = i + 1

j = row + 2
columna = 2
parsecLabel = tk.Label(root, text="ARM:",background="gray26", fg="white").grid(row=j, column=columna, sticky = tk.W)

j =j+ 1

blackscholesRB = tk.Radiobutton(root,text="401.bzip2", background="gray26", fg="white", padx = 20, variable=v, command=ShowChoice, value=4).grid(row=j, column=columna, sticky = tk.W)
j =j+ 1

freqmine = tk.Radiobutton(root,text="429.mcf",background="gray26", fg="white", padx = 20, variable=v, command=ShowChoice,value=5).grid(row=j, column=columna, sticky = tk.W)
j =j+ 1

swaptions = tk.Radiobutton(root,text="458.sjeng",background="gray26", fg="white", padx = 20, variable=v, command=ShowChoice,value=6).grid(row=j, column=columna, sticky = tk.W)
j =j+ 4



tk.Label(root, text="""Seleccione el parámetro que desea variar:""",background="gray26", fg="white", justify = tk.RIGHT, padx = 20, font=("Courier bold", 10)).grid(row=j, column=0, sticky = tk.W)
j = j + 2

columnaAtributos = 0
l1dzRB = tk.Radiobutton(root,text="SIZE::Caché L1 de Datos",background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=12,)
l1dzRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l1isRB = tk.Radiobutton(root,text="SIZE::Caché L1 de Instrucciones", background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=14,)
l1isRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l2sRB = tk.Radiobutton(root,text="SIZE::Caché L2",background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=16,)
l2sRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

j = j + 1
columnaAtributos = 0
l1dassRB = tk.Radiobutton(root,text="ASSOC::Caché L1 de Datos", background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=11,)
l1dassRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l1iassRB = tk.Radiobutton(root,text="ASSOC::Caché L1 de Instrucciones",background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=13,)
l1iassRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

l2assRB = tk.Radiobutton(root,text="ASSOC::Caché L2",background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=15,)
l2assRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1

j = j + 1
columnaAtributos = 1
cachelineRB = tk.Radiobutton(root,text="SIZE::Cacheline",background="gray26", fg="white", padx = 20, variable=param, command=ShowParam,value=10,)
cachelineRB.grid(row=j, column=columnaAtributos, sticky = tk.W)
columnaAtributos = columnaAtributos + 1


paramsRB = [l1dzRB,l1isRB, l2sRB, l1dassRB, l1iassRB, l2assRB, cachelineRB]





j = j + 5

bpTypes = {201: 'Sin Branch Predictor', 202 : 'BiModeBP', 203 : "LocalBP", 204 : "TournamentBP" }
tk.Label(root, text="""Seleccione una opción de BP:""",background="gray26", fg="white", justify = tk.RIGHT, padx = 20, font=("Courier bold", 10)).grid(row=j, column=0, sticky = tk.W)

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
tk.Radiobutton(root,text="Sin Branch Predictor",background="gray26", fg="white", padx = 20, variable=bp, command=ShowBP,value=201,).grid(row=j, column=columnaAtributos, sticky = tk.W)


columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="LocalBP", background="gray26", fg="white",padx = 20, variable=bp, command=ShowBP,value=203,).grid(row=j, column=columnaAtributos, sticky = tk.W)

columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="TournamentBP",background="gray26", fg="white", padx = 20, variable=bp, command=ShowBP,value=204,).grid(row=j, column=columnaAtributos, sticky = tk.W)

columnaAtributos = columnaAtributos + 1

tk.Radiobutton(root,text="BiModeBP",background="gray26", fg="white", padx = 20, variable=bp, command=ShowBP,value=202,).grid(row=j, column=columnaAtributos, sticky = tk.W)
j = j + 1




bpData = {301: 'BTBEntries', 302 : 'choicePredictorSize', 303 : "globalPredictorSize", 304 : "localPredictorSize" }
bpD = tk.IntVar()
bpD.set(301)
tk.Label(root, text="""Seleccione el parámetro que desea variar del BP:""",background="gray26", fg="white", justify = tk.RIGHT, padx = 20, font=("Courier bold", 10)).grid(row=j, column=0, sticky = tk.W)


def ShowBPData():
    return
j = j + 1

bbtRB = tk.Radiobutton(root,text="BTBEntries",background="gray26", fg="white", padx = 20, variable=bpD, command=ShowBPData,value=301,)
bbtRB.grid(row=j, column=0, sticky = tk.W)
j = j + 1

choicePRB = tk.Radiobutton(root,text="choicePredictorSize", background="gray26", fg="white",padx = 20, variable=bpD, command=ShowBPData,value=302,)
choicePRB.grid(row=j, column=0,sticky = tk.W)
j = j + 1

globalPRB = tk.Radiobutton(root,text="globalPredictorSize",background="gray26", fg="white", padx = 20, variable=bpD, command=ShowBPData,value=303,)
globalPRB.grid(row=j, column=0, sticky = tk.W)
j = j + 1

localPRB = tk.Radiobutton(root,text="localPredictorSize",background="gray26", fg="white", padx = 20, variable=bpD, command=ShowBPData,value=304,)
localPRB.grid(row=j, column=0, sticky = tk.W)
j = j + 1

datBP = [bbtRB,choicePRB, globalPRB, localPRB]

for item in datBP:
    item.config(state='disable')

exitButton = tk.Button(root, text="Ejecutar", command=ejecutar, bg='white').grid(row=j, column=0, sticky = tk.W)
labelI.grid(row=25, column=1)


root.mainloop()
