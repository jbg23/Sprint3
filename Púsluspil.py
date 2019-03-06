import sys
import random
import pygame

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
    for dal in range(dalkar)
        for rad in range(radir)}

#Hvar er tómi ?
(tomurD, tomurR)= tomur

class pusluspil:
    def __init__(self):
        print('smidur púsluspil')

    def pusluspil_bord2(self, bord):
        print('Velkominn í annað borð.\nTil að vinna borðið þarft þú að púsla púslið.\nGangi þér vel')
        self.pusluspilrun()

        #Skipta á tóma púslinu og púsli (d,r)
    def skipti (self, d,r):
        print('test3')
        global tomurD
        global tomurR
    #    print('window_stada:= ', stada[(d,r)])
        display.blit(pusluspil[stada[(d,r)]], (tomurD*puslbreidd, tomurR*puslhaed))
        display.blit(pusluspil[tomur], (d*puslbreidd, r*puslhaed))
        stada[(tomurD, tomurR)]=stada[(d,r)]
        stada[(d,r)] = tomur
        (tomurD, tomurR) = (d,r)
        pygame.display.flip()
        print('test4')

        #Rugla púslbitum
    def rugla(self):
        for i in range(50):
            d = random.randint(0, dalkar-1)
            r = random.randint(0, radir-1)
            print('test2')
            self.skipti(d,r)

    def pusluspilrun(self):
        #Byrjum leikinn og birtum upphaflega mynd
        pygame.init()
        display = pygame.display.set_mode(myndastaerd)
        pygame.display.set_caption("Púslaðu Mikka og félaga!")
        display.blit(mynd, (0, 0))
        pygame.display.flip()

        #kalla á skipti
        #self.skipti()
        #kalla á rugla
        #self.rugla()

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
                    print('test1')
                    self.rugla()
                    byrjun = False
                else:
                    erSigur = 0
                    for i in range(0, dalkar):
                        for j in range(0, radir):
                            if stada[i,j] == (i,j):
                                erSigur += 1
                    if erSigur == dalkar * radir:
                        print("Þú vannst!")
                        break
                    if event.button == 1: #Ef ýtt á músina (vinstri), á púsl við hliðina á tómu púsli þá færist púslið.
                        mouse_pos = pygame.mouse.get_pos()
                        d = int(mouse_pos[0] / puslbreidd)
                        r = int(mouse_pos[1] / puslhaed)
                        if((abs(d-tomurD)==1 and r==tomurR)or (abs(r-tomurR) == 1 and d == tomurD)):
                            skipti(d, r)
                    elif event.button == 3:
                    #Hægri klikk, sýnir lausn myndar
                        vistud_mynd=display.copy()
                        display.blit(mynd, (0, 0))
                        pygame.display.flip()
                        synilausn = True
            elif synilausn and (event.type == pygame.MOUSEBUTTONUP):
                #Hætta að sýna lausnina
                display.blit(vistud_mynd, (0, 0))
                pygame.display.flip()
                synilausn = False
        pygame.quit()



def main():
    pass

if __name__== '__main__':
    main()
else:
    print('þú ert innportuð í púsluspil')
