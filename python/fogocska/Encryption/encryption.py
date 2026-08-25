abc = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","_", "-",
    "'","{","}", "," ,"[", "]", "(", ")", "2", "3", "4",  "1", "0", "5","6", "7", "8", "9", ":" , " "    
]
#sztring átalakítás listás listává
def convert_str_to_list_of_lists(str_in):
    str_in = str_in.strip("[]")
    pairs = str_in.split("], [")

    list_out = []
    for pair in pairs:
        sublist = []
        for num in pair.split(", "):
            sublist.append(int(num))
        list_out.append(sublist)
    
    return list_out

#Kódíró funkció
def encrypt(str_in,char_in,abc = abc):
    output = ''

    #módosító karakter feldolgozása
    if len(char_in) == 1 and char_in in abc:
        modifier = abc.index(char_in)
    else:
        output = ''

    #Szöveg fordítás
    if isinstance(str_in, str) and str_in != '':
        for i in str_in:
            if i.lower() in abc:
                character = abc.index(i.lower()) + modifier
                output += str(character)
                output += ' '
            else:
                output = ''
                break

        #Végeredmény mentése, kiírása
        output = output + ' ' + char_in
        
    return output


#Kód olvasó funkció
def decrypt(str_in:str,abc = abc):
    output = ''
    list_in = str_in.split()
    char_in = list_in.pop(-1)

    #módosító karakter feldolgozása
    if len(char_in) == 1 and char_in in abc:
        modifier = abc.index(char_in)
    else:
        output = ''


    #Kód fordítás
    if isinstance(str_in,str) and str_in != '':
        for i in list_in:
            try:
                if int(i) - modifier < len(abc):
                    character = abc[int(i) - modifier]
                    output += str(character)
                else:
                    print(i)
                    output = ''
                    break
            except Exception:
                print(i)
                output = ''
                break

    #Végeredmény mentése, kiírása
    return output