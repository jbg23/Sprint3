from veljalit import Veljalit
from Spurningaleikur import spurningaleikur
from Púsluspil import pusluspil

#Segja velkominn, viltu spila
#Velja lit á karakter
#Spila borðin

class inngangur:
    pass

    def tilbaka_inngangur(self):
        pass

#Runnar veljalit - virkar ekki
def main():
    byrja = input('Viltu spila leikinn? Sláðu inn 1 fyrir já eða 0 fyrir nei\n')
    #byrja = 1
    #Viltu velja lit?
    if byrja=='1':
        litur= Veljalit()
        litur.veljalit_litur(litur)

        #Kalla á spurningaleik
        bord1= spurningaleikur()
        bord1.spurningar_bord1(bord1, litur)

        #Kalla á púsluspil
        bord2 = pusluspil()
        bord2.pusluspil_bord2(bord2, litur)

        #Kalla á kisuborð
        bord4 = Eltingaleikur()
        bord4.start_setup(bord4, litur)

if __name__=='__main__':
    main()
