import pygame
import sys
import time
import random

class Eltingaleikur:
    bakgrunnur = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Safnaðu pepperóníunum!")

    #skilgreinum liti
    pepperoni_litur = pygame.Color(153,0,0)
    graenn = pygame.Color(124,255,117)
    blar = pygame.Color(0,102,204)
    bleikur = pygame.Color(255,51,255)
    raudur = pygame.Color(255,0,0)
    svartur = pygame.Color(0,0,0)

    #Mynd af pepperoni sem færist
    pepp_mynd = pygame.image.load("pepperoni.png")
    pepp_mynd = pygame.transform.scale(pepp_mynd, (20, 20))

    #Mýs eftir lit, þarf að koma inn hvaða lit á að nota
    minaMus = pygame.image.load("mina.jpg")
    minaMus = pygame.transform.scale(minaMus, (40,40))

    mikkiMus = pygame.image.load("mikki.jpg")
    mikkiMus = pygame.transform.scale(mikkiMus, (40,40))

    tommi = pygame.image.load("kisi.png")
    tommi = pygame.transform.scale(tommi, (40,40))


    hradi = pygame.time.Clock()

    mus_stadsetning = [100,50] #upphafsstaðsetning músar
    mus_staerd = [[100,50]]

    pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10] #Random staðsetning á pepperoni
    pepperoni = True

    kisa1 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)] #Random staðsetning og stefna fyrir kisur
    kisa2 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]
    kisa3 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]

    stig = 0
    #self.byrja()
    def __init__(self):
        pass

    def start_setup(self):
        bakgrunnur = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Safnaðu pepperóníunum!")

        #skilgreinum liti
        pepperoni_litur = pygame.Color(153,0,0)
        graenn = pygame.Color(255,255,102)
        blar = pygame.Color(0,102,204)
        bleikur = pygame.Color(255,51,255)
        raudur = pygame.Color(255,0,0)
        svartur = pygame.Color(0,0,0)

        #Mynd af pepperoni sem færist
        pepp_mynd = pygame.image.load("pepperoni.png")
        pepp_mynd = pygame.transform.scale(pepp_mynd, (20, 20))

        #Mýs eftir lit, þarf að koma inn hvaða lit á að nota
        blaMus = pygame.image.load("BlaMina.png")
        blaMus = pygame.transform.scale(blaMus, (40,40))

        bleikMus = pygame.image.load("BleikMina.png")
        bleikMus = pygame.transform.scale(bleikMus, (40,40))

        raudMus = pygame.image.load("RaudMina.png")
        raudMus = pygame.transform.scale(raudMus, (40,40))

        tommi = pygame.image.load("kisi.png")
        tommi = pygame.transform.scale(tommi, (40,40))


        hradi = pygame.time.Clock()

        mus_stadsetning = [100,50] #upphafsstaðsetning músar
        mus_staerd = [[100,50]]

        pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10] #Random staðsetning á pepperoni
        pepperoni = True

        kisa1 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)] #Random staðsetning og stefna fyrir kisur
        kisa2 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]
        kisa3 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randint(1,4)]

        stig = 0
        self.byrja()

    def hreyfaKisu(self, kisa):
        rand = random.randint(1,20)
        if kisa[2] == 1:
            if kisa[0] + 10 > 460:
                kisa[2] = 2
                kisa[0] -= 10
            else:
                kisa[0] += 10
            if rand == 1:
                kisa[2] = 3
            elif rand == 2:
                kisa[2] = 4
        elif kisa[2] == 2:
            if kisa[0] - 10 < 0:
                kisa[2] = 1
                kisa[0] += 10
            else:
                kisa[0] -= 10
            if rand == 1:
                kisa[2] = 3
            elif rand == 2:
                kisa[2] = 4
        elif kisa[2] == 3:
            if kisa[1] - 10 < 0:
                kisa[2] = 4
                kisa[1] += 10
            else:
                kisa[1] -= 10
            if rand == 1:
                kisa[2] = 1
            elif rand == 2:
                kisa[2] = 2
        elif kisa[2] == 4:
            if kisa[1] + 10 > 460:
                kisa[2] = 3
                kisa[1] -= 10
            else:
                kisa[1] += 10
            if rand == 1:
                kisa[2] = 1
            elif rand == 2:
                kisa[2] = 2

    def stigafjoldi(self, val):
        pygame.init()
        skrift = pygame.font.SysFont('Arial', 24, bold=False, italic=False)
        skrift_bakg = skrift.render("Stig : {0}" .format(self.stig), True, self.svartur)
        Srect = skrift_bakg.get_rect()
        if val == 1:
            Srect.midtop = (80,10)
        else:
            Srect.midtop = (250,250)
        self.bakgrunnur.blit(skrift_bakg , Srect)

    def gameOver(self):
        letur =  pygame.font.SysFont('Arial', 72)
        GO_bakg = letur.render("Þú tapaðir!", True, self.raudur)
        GOrect = GO_bakg.get_rect()
        GOrect.midtop = (250,150)
        self.bakgrunnur.blit(GO_bakg, GOrect)
        self.stigafjoldi(0)
        pygame.display.flip()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(2)
        pygame.quit()
        sys.exit()
        #væri hægt að gera "Reyna aftur" takka?

    def nextLevel(self):
        letur =  pygame.font.SysFont('Arial', 72)
        GO_bakg = letur.render("Þú kláraðir borðið!", True, self.raudur)
        GOrect = GO_bakg.get_rect()
        GOrect.midtop = (250,150)
        self.bakgrunnur.blit(GO_bakg, GOrect)
        self.stigafjoldi(0)
        pygame.display.flip()
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    #Halda áfram í næsta borð eða klára leikinn

    def byrja(self):
        att = "RIGHT"
        breytt_att = att
        while True:
        #Heldur myndinni á skjá þar til leiknum er lokað
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Athugar hvort ýtt sé á takka og skilgreinir rétt átt
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        breytt_att = 'RIGHT'
                    if event.key == pygame.K_LEFT:
                        breytt_att = 'LEFT'
                    if event.key == pygame.K_UP:
                        breytt_att = 'UP'
                    if event.key == pygame.K_DOWN:
                        breytt_att = 'DOWN'
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

            #Passar að ekki er hægt að snúa við
            if breytt_att == 'RIGHT' and not att == 'LEFT':
                att = 'RIGHT'
            if breytt_att == 'LEFT' and not att == 'RIGHT':
                att = 'LEFT'
            if breytt_att == 'UP' and not att == 'DOWN':
                att = 'UP'
            if breytt_att == 'DOWN' and not att == 'UP':
                att = 'DOWN'

            #Breytir hnitum eftir átt
            if att == 'RIGHT':
                self.mus_stadsetning[0] += 10
            if att == 'LEFT':
                self.mus_stadsetning[0] -= 10
            if att == 'UP':
                self.mus_stadsetning[1] -= 10
            if att == 'DOWN':
                self.mus_stadsetning[1] += 10

            self.mus_staerd.insert(0,list(self.mus_stadsetning))

            #Árekstur (mús nær pepperoni)
            teljari = 0
            if (self.pepperoni_stadsetning[0]+10 >= self.mus_stadsetning[0] and self.pepperoni_stadsetning[0] <= self.mus_stadsetning[0]+30) and (self.pepperoni_stadsetning[1]+10 >= self.mus_stadsetning[1] and self.pepperoni_stadsetning[1] <= self.mus_stadsetning[1]+30):
                self.stig +=1
                if self.stig == 10:
                    self.nextLevel()
                self.pepperoni = False
                teljari += 1
            else:
                self.mus_staerd.pop()

            #Færir pepperoni á nýjan stað
            if self.pepperoni == False:
                self.pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10]
            self.pepperoni = True

            #Setjum myndir, mús og pepperoni á bakgrunn
            self.bakgrunnur.fill(self.graenn)
            self.bakgrunnur.blit(self.minaMus, pygame.Rect(self.mus_stadsetning[0], self.mus_stadsetning[1], 40, 40))
            self.bakgrunnur.blit(self.pepp_mynd, pygame.Rect(self.pepperoni_stadsetning[0], self.pepperoni_stadsetning[1], 20, 20))
            self.bakgrunnur.blit(self.tommi, pygame.Rect(self.kisa1[0], self.kisa1[1], 40, 40))
            self.bakgrunnur.blit(self.tommi, pygame.Rect(self.kisa2[0], self.kisa2[1], 40, 40))
            self.bakgrunnur.blit(self.tommi, pygame.Rect(self.kisa3[0], self.kisa3[1], 40, 40))

            #Kallar á gameOver fall ef mús klessir á vegg
            if self.mus_stadsetning[0] > 460 or self.mus_stadsetning[0] < 0 or self.mus_stadsetning[1] > 460 or self.mus_stadsetning[1] < 0:
                self.gameOver()

            #Kallar á gameOver fall ef mús klessir á kisur
            if (self.kisa1[0]+30 >= self.mus_stadsetning[0] and self.kisa1[0] <= self.mus_stadsetning[0]+30) and (self.kisa1[1]+30 >= self.mus_stadsetning[1] and self.kisa1[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.kisa2[0]+30 >= self.mus_stadsetning[0] and self.kisa2[0] <= self.mus_stadsetning[0]+30) and (self.kisa2[1]+30 >= self.mus_stadsetning[1] and self.kisa2[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()
            if (self.kisa3[0]+30 >= self.mus_stadsetning[0] and self.kisa3[0] <= self.mus_stadsetning[0]+30) and (self.kisa3[1]+30 >= self.mus_stadsetning[1] and self.kisa3[1] <= self.mus_stadsetning[1]+30):
                self.gameOver()

            #Hreyfa kisur
            self.hreyfaKisu(self.kisa1)
            self.hreyfaKisu(self.kisa2)
            self.hreyfaKisu(self.kisa3)

            self.stigafjoldi(1)
            pygame.display.flip()
            self.hradi.tick(10)
