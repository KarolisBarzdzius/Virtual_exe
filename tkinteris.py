from tkinter import *

saug=""
langas=Tk()
def patvirtinti():
    global saug
    ivesta=laukas.get()
    retur["text"]=(f"Sveikas, {ivesta}")
    status["text"] = "Sukurta"
    saug=(f"Sveikas, {ivesta}")

def patvirtinti2(event):
    global saug
    ivesta=laukas.get()
    retur["text"]=(f"Sveikas, {ivesta}")
    status["text"] = "Sukurta"
    saug=(f"Sveikas, {ivesta}")
def istrinti():
    retur["text"]=""
    status["text"] = "Isvalyta"
    laukas.delete(0,END)
def atkurti():
    retur["text"]=saug
    status["text"] = "Atkurta"
def iseiti():
    langas.destroy()
def iseiti2(event):
    langas.destroy()


meniu=Menu(langas)
langas.config(menu=meniu)

submen=Menu(meniu,tearoff=0)
submen2=Menu(meniu,tearoff=0)
submen3=Menu(meniu,tearoff=0)

meniu.add_cascade(label="Meniu",menu=submen)
submen.add_command(label="Istrinti",command=istrinti)
submen.add_command(label="Atkurti paskutini",command=atkurti)
submen.add_separator()
submen.add_command(label="Iseiti",command=iseiti)


uzrasas=Label(langas, text="Iveskite Varda", width=10,height=5)
langas.title("Pavadinimassssssss")
langas.iconbitmap(r'asmenys.ico')

laukas=Entry(langas)

laukas.bind("<Return>", patvirtinti2)
laukas.bind("<Escape>",iseiti2)

mygtukas=Button(langas,text="Patvirtinti",command=patvirtinti)
status=Label(langas,text="Status",bd=1,relief=SUNKEN,anchor=W)

retur=Label(langas,text="")

uzrasas.grid(row=0,column=0)
laukas.grid(row=0,column=1)
mygtukas.grid(row=0,column=2)
retur.grid(row=1,columnspan=3)
status.grid(row=2,columnspan=3)

langas.mainloop()