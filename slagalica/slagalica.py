import random
resenje=[]
mogucnosti=["tref","karo","pik","herc","skocko","zvezda"]
for i in range(0,4):#generise kombinaciju za skocka
   resenje.append(mogucnosti[random.randint(0,5)])
print('\033[38;2;0;185;255m')#plava kao u slagalici

file = open("korak.txt","r",encoding="utf-8")

def korak():
    linbr = random.randint(0,2)
    for i in range(0,linbr+1):
        linija=file.readline()

    linija=linija.split("|")
    tacanodg=linija[0]
    unos=0
    pokusaj=0

    for i in range(1,6):#koraci
        print(linija[i])
        unos=input("Unesite resenje ili napisite dalje: ")
        unos=unos.lower()
        unos=unos.replace("č","c") #sisanje latinice
        unos=unos.replace("ć","c")
        unos=unos.replace("š","s")
        unos=unos.replace("ž","z")
        unos=unos.replace("đ","dj")
        if unos==tacanodg:
            brpoena= (6-i)*15
            print("Tacan odgovor!\nOsvojili ste ",brpoena," poena!")
            print("--------------------------------------------------------------------------------------------")
            break
        elif unos=="dalje":
            pokusaj=pokusaj+1
            continue
        else:
            print("Netacan odgovor!\n")
            print("--------------------------------------------------------------------------------------------")
            pokusaj=pokusaj+1
    if pokusaj>4:
        print("Izgubili ste :(\n Tacan odgovor je bio: ",tacanodg)
        print("--------------------------------------------------------------------------------------------")
    

def skocko(): 
    tmpres=resenje.copy()
    crvena=0
    zuta=0
    bela=0
    pokus=[]
    display=""
    for i in range(0,4):
        unos=-1
        while(unos!="tref" and unos!="karo"  and unos!="pik" and unos!="herc" and unos!="skocko" and unos!="zvezda"):#unos
            unos=input("Unesite "+str(i+1)+ ". clan kombinacije: ")
            unos = unos.replace("č","c")
            if (unos!="tref" and unos!="karo"  and unos!="pik" and unos!="herc" and unos!="skocko" and unos!="zvezda"):
                print("Unestie validan clan kombinacije!(tref,karo,pik,herc,skocko,zvezda)")
        pokus.append(unos)
        display = display + " " + unos
        if tmpres[i]==pokus[i]:#crvena
            crvena = crvena +1
            pokus[i]=0
            tmpres[i]=0
    for clan in mogucnosti:#zuta
        if tmpres.count(clan)>=pokus.count(clan):
                zuta = zuta + pokus.count(clan)
        elif tmpres.count(clan)<pokus.count(clan):
                zuta = zuta + tmpres.count(clan)         
    bela=4-crvena-zuta
    print("--------------------------------------------------------------------------------------------") #display
    print(display)
    print("\033[1;31;40m 0"*crvena+"\033[1;33;40m 0"*zuta+"\033[1;37;40m 0"*bela+'\033[38;2;0;185;255m ')#semafor i reset boje
    print("--------------------------------------------------------------------------------------------")
    if crvena==4:#pobeda
        print("Tacna kombinacija!")
        return 1
    return 0

if __name__ == "__main__":
    x=-1
    opet="da"
    while(opet.lower()=="da"):
        while(x!=1 or x!=2):
            x=eval(input("Dobrodosli u slagalicu!\n1-Korak po korak\n2-Skocko\nUnesite broj igre koju zelite da igrate:\n"))
            if x==1:
                korak()
                break
            elif x==2:
                pobeda=0
                brpok=0
                print("Unesite clanove kombinacije jednog po jednog(skocko, tref, pik, karo, zvezda, herc):")
                while brpok<7 and pobeda==0:
                    pobeda=skocko()
                    brpok = brpok+1
                if brpok==7 and pobeda==0:
                    print("Izgubili ste :(\nTacna kombinacija je bila: ",resenje)
                    break
                if pobeda==1:
                    print("Osvojili ste ",50-5*brpok ," poena! Svaka cast!")
                    break
            else:
                print("Unesite 1 ili 2:")
        opet = input("Da li zelite da se igrate opet?\n")
    file.close()