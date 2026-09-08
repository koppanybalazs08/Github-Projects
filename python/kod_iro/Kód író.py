#Külső modulok importálása
from Coder_Decoder import coder_decoder as cd
from FileManager import file_manager
from tkinter import *
from tkinter import messagebox as msgbox, Tk

#Fő ablak megnyitása
window = Tk()
window.title('Kód író/olvasó')
window.geometry('400x200')
window.minsize(400,200)
window.maxsize( 800,400 )

#Szöveg Írása
label = Label(window,text = 'Kód írása vagy olvasása?',font = (10))
label.place(relx = 0.47,anchor = N)


#Kódíró funkció
def Coder(): 
    cd.coder()

#Kód olvasó funkció
def Decoder():
    cd.decoder()


#Saját ABC létrehozása
def Add_ABC():
    global abc
    abc=file_manager.add_abc()


#'Alap ABC visszaállítása'
def Refresh_ABC():
    file_manager.refresh_abc()
    msgbox.showinfo('Alap ABC visszaállítása','Alap ABC visszaállítva')

#Gombok
#'Kód írása' gomb létrehozása
button1 = Button(window,text = 'Kód írása',font = (10))
button1.place(anchor = NW)
button1.config(command = Coder)

#'Kód olvasása' gomb létrehozása
button2 = Button(window,text = 'Kód olvasása',font = (10))
button2.place(relx = 1,anchor = NE)
button2.config(command = Decoder)

#'Saját ABC hozzáadása' gomb létrehozása
button3 = Button(window,text = 'Saját ABC hozzáadása',font = (10))
button3.place(rely = 0.5,relx = 0.5,anchor = CENTER)
button3.config(command = Add_ABC)

#'Alap ABC visszaállítása' gomb létrehozása
button4 = Button(window,text = 'Alap ABC visszaállítása',font=(10))
button4.place (rely = 1,relx = 0.5,anchor = S)
button4.config(command = Refresh_ABC)

#mainloop vége
window.mainloop()
