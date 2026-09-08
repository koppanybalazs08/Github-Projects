#Külső modulok importálása
from FileManager import file_manager
from tkinter import messagebox as msgbox, simpledialog as sd

#Alap változók megadása, fájl menedzselés
file_manager.del_output()

list_out = []
list_creatable = False

#Kódíró funkció
def coder():
    global list_creatable
    
    #Input
    abc = file_manager.open_abc()
    str_in = sd.askstring('Kód író', 'Írjon be egy szöveget ide:')
    char_in = sd.askstring('Kód író', 'Írjon be egy karaktert ide:').lower()

    #módosító karakter feldolgozása
    if len(char_in) == 1 and char_in in abc:
        modifier = abc.index(char_in)
    else:
        msgbox.showinfo('Hiba','A karakter nincs a program szótárában, vagy több karakter lett megadva!')
        list_creatable = False
        list_out.clear()

    #Szöveg fordítás
    if isinstance(str_in, str) and str_in != '':
        for i in str_in:
                if i.lower() in abc:
                    character = abc.index(i.lower()) + modifier
                    list_out.append(character)
                    list_creatable = True
                else:
                    msgbox.showinfo('Hiba','Az egyik karakter nincs a program szótárában!')
                    list_creatable = False
                    list_out.clear()
                    break

        #Végeredmény mentése, kiírása
        file_manager.save_output(list_creatable,list_out)


#Kód olvasó funkció
def decoder():
    global list_creatable

    #Input
    abc = file_manager.open_abc()
    str_in = sd.askstring('Kód olvasó','Írjon be egy egész számokból álló számsort ide:') 
    char_in = sd.askstring('Kód író', 'Írjon be egy karaktert ide:').lower()

    #módosító karakter feldolgozása
    if len(char_in) == 1 and char_in in abc:
        modifier = abc.index(char_in)
    else:
        msgbox.showinfo('Hiba','A karakter nincs a program szótárában, vagy több karakter lett megadva!')
        list_creatable = False
        list_out.clear()

    #Kód fordítás
    if isinstance(str_in,str) and str_in != '':
        str_to_list = str_in.split(' ')
        for i in str_to_list:
            try:
                if int(i) - modifier < len(abc):
                    character = abc[int(i) - modifier]
                    list_out.append(character)
                    list_creatable = True
                else:
                    msgbox.showinfo('Hiba','Az egyik karakter nincs a program szótárában!')
                    list_creatable = False
                    list_out.clear()
                    break
            except Exception:
                msgbox.showinfo('Hiba','Nem megfelelő típusú input!')
                list_creatable = False
                break

        #Végeredmény mentése, kiírása
        file_manager.save_output(list_creatable,list_out)