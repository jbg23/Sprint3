import sys
import random
import pygame

class Pusluspil:
    myndaskra = "mikkipusl.jpg"
    myndastaerd = (750, 500)
    puslbreidd = 250
    puslhaed = 250
    dalkar = 3
    radir = 2

    #Tómt, svart púsl í neðra hægra horni
    tomur = (dalkar-1, radir-1)
    svartur = (0, 0, 0)

    #Rammi á hvert púsl
    larettur_rammi = pygame.Surface((puslbreidd, 1))
    larettur_rammi.fill(svartur)
    lodrettur_rammi = pygame.Surface((1, puslhaed))
    lodrettur_rammi.fill(svartur)

    #Setja myndaskrá inn í mynd og skipta í púsl
    mynd = pygame.image.load(myndaskra)
    pusluspil = {}
    for d in range(0, dalkar):
        for r in range(0, radir):
            pusl = mynd.subsurface(d*puslbreidd, r*puslhaed, puslbreidd, puslhaed)
            pusluspil[(d,r)] = pusl
            if (d,r) != tomur:
                pusl.blit(larettur_rammi, (1, 1))
                pusl.blit(larettur_rammi, (0, radir-1))
                pusl.blit(lodrettur_rammi, (1, 1))
                pusl.blit(lodrettur_rammi, (dalkar-1,0))
    pusluspil[tomur].fill(svartur)

    #Hvaða púsl er hvar
    stada = {(dal, rad): (dal, rad)
        for dal in range(3)
            for rad in range(2)}

    #Hvar er tómi ?
    (tomurD, tomurR)= tomur

    #Byrjum leikinn og birtum upphaflega mynd
    pygame.init()
    display = pygame.display.set_mode(myndastaerd)
    pygame.display.set_caption("Púslaðu Mikka og félaga!")
    display.blit(mynd, (0, 0))
    pygame.display.flip()

    def __init__(self):
        print('smidur púsluspil')

    def pusluspil_bord2(self, bord):
        print('Velkominn í annað borð.\nTil að vinna borðið þarft þú að púsla púslið.\nGangi þér vel')
        self.pusluspilrun()

    #Skipta á tóma púslinu og púsli (d,r)
    def skipti (self, d,r):
        global tomurD
        global tomurR
    #    print('window_stada:= ', stada[(d,r)])
        self.display.blit(self.pusluspil[self.stada[(d,r)]], (self.tomurD*self.puslbreidd, self.tomurR*self.puslhaed))
        self.display.blit(self.pusluspil[self.tomur], (d*self.puslbreidd, r*self.puslhaed))
        self.stada[(self.tomurD, self.tomurR)]=self.stada[(d,r)]
        self.stada[(d,r)] = self.tomur
        (self.tomurD, self.tomurR) = (d,r)
        pygame.display.flip()

    #Rugla púslbitum
    def rugla(self):
        for i in range(50):
            d = random.randint(0, self.dalkar-1)
            r = random.randint(0, self.radir-1)
            self.skipti(d,r)

    def pusluspilrun(self):
    #Hreyfa púsl með mús
        byrjun = True
        synilausn = False
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if byrjun == True: #Rugla eftir að ýtt er á mús í fyrsta sinn
                    self.rugla()
                    byrjun = False
                else:
                    erSigur = 0
                    for i in range(0, self.dalkar):
                        for j in range(0, self.radir):
                            if self.stada[i,j] == (i,j):
                                erSigur += 1
                    if erSigur == self.dalkar * self.radir:
                        print("Þú vannst!")
                        break
                    if event.button == 1: #Ef ýtt á músina (vinstri), á púsl við hliðina á tómu púsli þá færist púslið.
                        mouse_pos = pygame.mouse.get_pos()
                        d = int(mouse_pos[0] / self.puslbreidd)
                        r = int(mouse_pos[1] / self.puslhaed)
                        if((abs(d-self.tomurD)==1 and r==self.tomurR)or (abs(r-self.tomurR) == 1 and d == self.tomurD)):
                            self.skipti(d, r)
                    elif event.button == 3:
                    #Hægri klikk, sýnir lausn myndar
                        vistud_mynd=self.display.copy()
                        self.display.blit(self.mynd, (0, 0))
                        pygame.display.flip()
                        synilausn = True
            elif synilausn and (event.type == pygame.MOUSEBUTTONUP):
                #Hætta að sýna lausnina
                self.display.blit(vistud_mynd, (0, 0))
                pygame.display.flip()
                synilausn = False
        pygame.quit()

def main():
    pass

if __name__== '__main__':
    main()
else:
    print('þú ert innportuð í púsluspil')
