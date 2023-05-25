from tkinter import*
from tkinter import messagebox

window=Tk()
window.title("crypthographie")
window.geometry("720x480")

window.config(background='#DAF7A6')
frame=Frame(window,bg='#DAF7A6')

label_title=Label(window,text="Bienvenue sur l'application",font=("Helvetica",40),bg='#DAF7A6',fg="#581845")
label_title.grid(row=1,column=1)
label_subtitle=Label(window,text="crypthographie",font=("Helvetica",20),bg='#DAF7A6',fg="#581845")
label_subtitle.grid(row=2,column=1)
message=Label(window,text="Saisir votre message a chiffré",font=("Helvetica",15),bg='#DAF7A6',fg="#581845")
message.grid(row=4,column=1)
message_entry=Text(window,height=10,width=50,bg="#d8e9e3")
message_entry.grid(row=5,column=1)
algo=Label(window,text="choisir l'algorithme de chiffrement",font=("Helvetica",15),bg='#DAF7A6',fg="#581845")
algo.grid(row=6,column=1)

liste = Listbox(window,selectmode ="SINGLE",bg='#d8e9e3',fg="#581845",height=4,width=40,)
liste.insert(1,"Algorithme de chiffrement de cesar ")
liste.insert(2,"Algorithme de chiffrement de Rotate ")
liste.insert(3,"Algorithme de chiffrement par substitution ")
liste.insert(4,"Algorithme de chiffrement de Vigenere ")
liste.insert(5,"Algorithme de chiffrement par transposition ")
liste.grid(row=7,column=1)
def cesar_chiffre_nb(x,k):
     return (x+k)%26

def funct_cesar (mot,k):
      listecrypte =[]
      for lettre in mot :
          nb = ord(lettre)-65
          nb_crypte = cesar_chiffre_nb(nb,k)
          lettre_crypte=chr(nb_crypte+65)
          listecrypte.append(lettre_crypte)
      mot_crypte="".join(listecrypte)
      return(mot_crypte)


def funct_rotate(mot, k):
    listecrypte = []
    for lettre in mot:
        nb = ord(lettre) - 65
        nb_crypte = cesar_chiffre_nb(nb, k)
        lettre_crypte = chr(nb_crypte + 65)
        listecrypte.append(lettre_crypte)
    mot_crypte = "".join(listecrypte)
    return (mot_crypte)


def funct_substitution(msg):
    cle='HYLUJPVREAKBNDOFSQZCWMGITX'
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res=''
    for caractere in msg:
        indice = alpha.find(caractere)
        res+= cle[indice]
    return res




def vigenere(msg,cle):
    message_code=[]
    k=len(cle)
    i=0
    for lettre in msg:
        nomb= ord(lettre)-65
        x=int(cle[i])
        nomb_code= (nomb+x)%26
        lettre_code= chr(nomb_code+65)
        i=(i+1)%k
        message_code.append(lettre_code)
    message_code="".join(message_code)
    return(message_code)




def execute_selected_item():
    for i in liste.curselection():
        x=liste.get(i)
        print(x)
    if x== "Algorithme de chiffrement de cesar ":
        print (message_entry.get("1.0",END))
        k= int (input("entrer un clé de chiffrement : "))
        cryptogramme = funct_cesar(message_entry.get("1.0",END),k)
    if x== "Algorithme de chiffrement de Rotate ":
        print (message_entry.get("1.0",END))
        k= int (13)
        cryptogramme = funct_rotate(message_entry.get("1.0",END),k)
    if x=="Algorithme de chiffrement par substitution":
        print (message_entry.get("1.0",END))
        msg=message_entry.get("1.0",END).upper()
        cryptogramme =funct_substitution(msg)
    if x=="Algorithme de chiffrement de Vigenere ":
        print (message_entry.get("1.0",END))
        cle= list (input("entrer un clé de chiffrement : "))
        msg=message_entry.get("1.0",END).upper()
        cryptogramme= vigenere(msg,cle)
    messagebox.showinfo("cryptogramme",cryptogramme)
    


yt_button =Button(window,text="chiffrer mon message !!!", font=("courrier",10),bg="#581845",fg='#DAF7A6',command= execute_selected_item)
yt_button.grid(row=11,column=1)


window.mainloop()
