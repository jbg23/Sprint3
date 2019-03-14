import sqlite3
import pygame
import time
import sys
pygame.init()

class Question():
    #Tengingar vid gagnagrunn
    conn = sqlite3.connect('spurningar.db')
    c = conn.cursor()
    Stig = 0
    level = 1

    white = (255,255,255)
    black = (0, 0, 0)
    red = (255,0,0)
    green = (0,255,0)

    small = pygame.font.SysFont("algerian", 35)
    medium = pygame.font.SysFont("algerian", 50)
    large = pygame.font.SysFont("broadway", 50)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)


    display_width = 800
    display_height = 600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.update()

    #Byrjum leikinn og birtum upphaflega mynd
    pygame.display.set_caption('Spurningaleikur')
    image = pygame.image.load('bakgrunnur.png')

    def __init__(self):
        print('smidur Spurningaleikur')

    #def __del__(self):
        #pass
        #loka a gagnagrunn?

    def texts(self, text, color, size):
        if size == "small":
            textSurface = self.small.render(text, True, color)
        elif size == "medium":
            textSurface = self.medium.render(text, True, color)
        elif size == "large":
            textSurface = self.large.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def screenMessage(self, msg,color, height = 0, size = "small"):
        textSurf, textRect = self.texts(msg, color, size)
        textRect.center = (self.display_width / 2), (self.display_height / 2) + height
        self.gameDisplay.blit(textSurf, textRect)

    def gameIntro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.level = 1
                        intro = False
                    if event.key == pygame.K_h:
                        pygame.quit()
                        sys.exit()
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage("Velkomin/nn i spurningarleik", self.red, -120, size = "medium" )
            self.screenMessage("völundarmúsarinnar", self.red, -70, size = "medium" )
            self.screenMessage("Þú þarft að svara 4 spurningum rétt i röð til að komast áfram.", self.red, +80, size = "small")
            self.screenMessage("Ýttu á 1 til að byrja", self.red, +110, size = "small")
            #self.music('tonlist.mp3')
            pygame.display.update()

    #Synir fjolda rettra svara i rod
    def gameScore(self):
        text = self.small.render("Rétt svör í röð: " + str(self.Stig), True, self.black)
        self.gameDisplay.blit(text, [0,0])

    #Saekir spurningar ur gagnagrunninum
    def getQuestion(self, level):
        self.c.execute('SELECT count(spurning) FROM Spurningar WHERE level = :level',{'level': level})
        count =  (int)(''.join(map(str,(self.c.fetchone()))))
        self.c.execute('SELECT spurning, SpId FROM Spurningar WHERE level = :level',{'level': level})
        return self.c.fetchmany(count)

    #Saekir svar vid vidkomandi spurningu ur gagnagrunninum
    def getAnswer(self, SpID):
        self.c.execute('SELECT svor FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        return self.c.fetchone()

    #Athugar hvort leikmadur hefur unnid
    def checkScore(self):
        if(self.Stig == 4):
            self.Stig = 0
            self.gameLoop(gameWin = True)

    #Athugar hvort leikmadur setti inn rett svar
    def checkAnswer(self,SpID,svar):
        self.c.execute('SELECT rettSvar FROM Svor WHERE SvID = :SvID',{'SvID': SpID})
        self.gameDisplay.fill(self.white)
        if (svar == ''.join(map(str,(self.c.fetchone())))):
            self.Stig += 1
            self.screenMessage("Rett svar!!",self.green, -20, size = "large")
            pygame.display.update()
            self.checkScore()
        else:
            self.screenMessage("Rangt svar!",self.red, -20, size = "large")
            self.Stig = 0
            pygame.display.update()
        time.sleep(2)

    #Faera thessa adferd inni gameLoop??
    def playGame(self,level):

        x = self.getQuestion(self.level)

        for i in range(0,len(x)):
            inGame = True
            self.gameDisplay.blit(self.image, [0,0, 800, 600])
            self.screenMessage(''.join(map(str,(x[i][0]))),self.black,-150)
            abcd = ''.join(map(str,(self.getAnswer(x[i][1])))).splitlines()
            self.screenMessage(abcd[0],self.red, -90)
            self.screenMessage(abcd[1],self.red, -60)
            self.screenMessage(abcd[2],self.red, -30)
            self.screenMessage(abcd[3],self.red,  0)
            pygame.display.update()

            while inGame:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:

                        self.c.close()
                        self.conn.close()
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            self.checkAnswer(x[i][1], 'a')
                            inGame = False
                        elif event.key == pygame.K_b:
                            self.checkAnswer(x[i][1], 'b')
                            inGame = False
                        elif event.key == pygame.K_c:
                            self.checkAnswer(x[i][1], 'c')
                            inGame = False
                        elif event.key == pygame.K_d:
                            self.checkAnswer(x[i][1], 'd')
                            inGame = False
                    self.gameScore()
                    #self.clock.tick(0)
                    pygame.display.update()

    def gameLoop(self, gameWin = False):
        gameExit =  False

        while not gameExit:

            if gameWin == True:
                self.gameDisplay.blit(self.image, [0,0, 800, 600])
                self.screenMessage("ÞÚ VANNST!!", self.red, -50, size = "large")
                self.screenMessage("Ýttu á s til að spila aftur, h til ad hætta, n fyrir næsta borð ", self.red, 50, size = "small")
                pygame.display.update()

                while gameWin == True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit = True
                            gameWin = False

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_h:
                                gameExit = True
                                gameWin = False
                                pygame.quit()
                                sys.exit()

                            if event.key == pygame.K_s:
                                gameWin = False
                                self.gameIntro()

                            if event.key == pygame.K_n:
                                gameWin = False
                                pygame.mixer.music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True

            self.playGame(self.level)

            if self.Stig == 4:
                gameWin = True

            pygame.display.update()
            #self.clock.tick(0)

        self.c.close()
        self.conn.close()
        pygame.quit()
        sys.exit()

bord5 = Question()
bord5.gameIntro()
bord5.gameLoop()
