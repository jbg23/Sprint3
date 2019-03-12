import pygame
import sys
import time
import random

bakgrunnur = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Safnaðu pepperóníunum!")

#skilgreinum liti
pepperoni_litur = pygame.Color(153,0,0)
gulur = pygame.Color(255,255,102)
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


hradi = pygame.time.Clock()

mus_stadsetning = [100,50] #upphafsstaðsetning músar
mus_staerd = [[100,50]]

pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10] #Random staðsetning á pepperoni
pepperoni = True

kisa1 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randrange(1,4)] #Random staðsetning og stefna fyrir kisur
kisa2 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randrange(1,4)]
kisa3 = [random.randrange(1,48)*10, random.randrange(1,48)*10, random.randrange (1,4)]

att = "RIGHT"
breytt_att = att

stig = 0


def stigafjoldi(val):
    pygame.init()
    skrift = pygame.font.SysFont('Arial', 24, bold=False, italic=False)
    skrift_bakg = skrift.render("Stig : {0}" .format(stig), True, svartur)
    Srect = skrift_bakg.get_rect()
    if val == 1:
        Srect.midtop = (80,10)
    else:
        Srect.midtop = (250,250)

    bakgrunnur.blit(skrift_bakg , Srect)

def gameOver():
    letur =  pygame.font.SysFont('Arial', 72)
    GO_bakg = letur.render("Þú tapaðir!", True, raudur)
    GOrect = GO_bakg.get_rect()
    GOrect.midtop = (250,150)
    bakgrunnur.blit(GO_bakg, GOrect)
    stigafjoldi(0)
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

def nextLevel():
    letur =  pygame.font.SysFont('Arial', 72)
    GO_bakg = letur.render("Þú kláraðir borðið!", True, raudur)
    GOrect = GO_bakg.get_rect()
    GOrect.midtop = (250,150)
    bakgrunnur.blit(GO_bakg, GOrect)
    stigafjoldi(0)
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
        mus_stadsetning[0] += 10
    if att == 'LEFT':
        mus_stadsetning[0] -= 10
    if att == 'UP':
        mus_stadsetning[1] -= 10
    if att == 'DOWN':
        mus_stadsetning[1] += 10

    mus_staerd.insert(0,list(mus_stadsetning))

    #Árekstur (mús nær pepperoni)
    teljari = 0
    if (pepperoni_stadsetning[0]+10 >= mus_stadsetning[0] and pepperoni_stadsetning[0] <= mus_stadsetning[0]+30) and (pepperoni_stadsetning[1]+10 >= mus_stadsetning[1] and pepperoni_stadsetning[1] <= mus_stadsetning[1]+30):
        stig +=1
        if stig == 10:
            nextLevel()
        pepperoni = False
        teljari += 1
    else:
        mus_staerd.pop()

    #Færir pepperoni á nýjan stað
    if pepperoni == False:
        pepperoni_stadsetning = [random.randrange(1,48)*10, random.randrange(1,48)*10]
    pepperoni = True

    #Setjum myndir, mús og pepperoni á bakgrunn
    bakgrunnur.fill(gulur)
    for pos in mus_staerd:
        bakgrunnur.blit(bleikMus, pygame.Rect(mus_stadsetning[0], mus_stadsetning[1], 10, 10))
    bakgrunnur.blit(pepp_mynd, pygame.Rect(pepperoni_stadsetning[0], pepperoni_stadsetning[1], 10, 10))

    #Kallar á gameOver fall ef mús klessir á vegg
    if mus_stadsetning[0] > 500 or mus_stadsetning[0] < 0:
        gameOver()
    if mus_stadsetning[1] > 500 or mus_stadsetning[1] < 0:
        gameOver()

    #Hreyfa kisur

    



    stigafjoldi(1)
    pygame.display.flip()
    hradi.tick(10)
