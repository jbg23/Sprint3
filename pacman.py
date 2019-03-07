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

hradi = pygame.time.Clock()

mus_stadsetning = [100,50]
mus_staerd = [100,50]

pepperoni_stadsetning = [random.randrange(1,50)*10, random.randrange(1,50)*10]
pepperoni = True

att = "RIGHT"
breytt_att = att

stig = 0

class Pacman:
    def __init__(self, breyta1, breyta2):
        self.breyta1 = breyta1
        self.breyta2 = breyta2

    def gameOver():
        letur =  pygame.font.SysFont('Arial', 24, bold=False, italic=False)
        GO_bakg = letur.render("Þú tapaðir!", True, raudur)
        GOrect = GO_bakg.get_rect()
        GOrect.midtop = (360,15)
        bakgrunnur.blit(GO_bakg, GOrect)
        stigafjoldi(0)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    def stigafjoldi(val=1):
        pygame.init()
        skrift = pygame.font.SysFont('Arial', 24, bold=False, italic=False)
        skrift_bakg = skrift.render("Stig : {0}" .format(stig), True, svartur)
        rect = skrift_bakg.get_rect()
        if val == 1:
            rect.midtop = (80,10)
        else:
            rect.midtop = (360,150)

        bakgrunnur.blit(skrift_bakg , rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

        if breytt_att == 'RIGHT' and not att == 'LEFT':
            att = 'RIGHT'
        if breytt_att == 'LEFT' and not att == 'RIGHT':
            att = 'LEFT'
        if breytt_att == 'UP' and not att == 'DOWN':
            att = 'UP'
        if breytt_att == 'DOWN' and not att == 'UP':
            att = 'DOWN'

        if att == 'RIGHT':
            mus_stadsetning[0] += 10
        if att == 'LEFT':
            mus_stadsetning[0] -= 10
        if att == 'UP':
            mus_stadsetning[1] -= 10
        if att == 'DOWN':
            mus_stadsetning[1] += 10

        mus_staerd.insert(0,list(mus_stadsetning))
        if mus_stadsetning[0] == pepperoni_stadsetning[0] and mus_stadsetning[1] == pepperoni_stadsetning[1]:
            stig +=1
            pepperoni = False
        else:
            mus_staerd.pop()

        if pepperoni == False:
            pepperoni_stadsetning = [random.randrange(1,50)*10, random.randrange(1,50)*10]
        pepperoni = True




        bakgrunnur.fill(gulur)
        stigafjoldi()
        pygame.display.flip()
        hradi.tick(10)
