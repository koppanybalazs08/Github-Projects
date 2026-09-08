#Külső modulok importálása
from tkinter import simpledialog as sd, messagebox as msgbox

#output.txt fájl takarítása
def del_output():
    output = open('output.txt','r')
    file_content = output.readlines()
    listnum = 0
    for i in file_content:
        listnum += 1
    if listnum >= 5:
        output.close
        output = open('output.txt','w')
        output.close
    else:
        output.close

#információ mentése az output.txt fájlba
def save_output(list_creatable,list_out):
    try:
        if list_creatable == True:
            str_out = str(list_out).replace('[','').replace(']','').replace(',','')
            msgbox.showinfo('A kódod: ', str_out)
            savefile = open('output.txt','a')
            savefile.write(str_out + '\n')
            savefile.close()
            list_out.clear()
        else:
            list_out.clear()
    except Exception:
        list_out.clear()

#ABC frissítése
def refresh_abc():
    abc_txt=open('abc.txt','w')
    abc_txt.write("a,á,b,c,d,e,é,f,g,h,i,í,j,k,l,m,n,o,ó,ö,ő,p,q,r,s,t,u,ú,ü,ű,v,w,x,y,z, ,0,1,2,3,4,5,6,7,8,9,?,!,.,:,(,),/,_,-,*")
    abc_txt.close()

#ABC megnyitása
def open_abc():
    try:
        abc_txt= open('abc.txt','r')
        abc = abc_txt.read( )
        abc=abc.replace('\n    ','').split(',')
        abc_txt.close()
        return abc
    except TypeError:
        pass

#Új ABC hozzáadása
def add_abc():
    str_in = sd.askstring('Saját kód hozzáadása',
    'Adjon meg egy saját abc-t hogy saját kódrendszert tudjon használni!')
    abc_txt = open('abc.txt','w', encoding = "utf-8")
    abc_txt.write(str_in)
    abc_txt.close

