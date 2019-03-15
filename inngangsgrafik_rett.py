import pygame
from Spurningaleikur_grafik_rett import Question
#from Púsluspil import pusluspil

class Inngangur:
    breidd = 800
    haed = 600
    level=0
    size = [breidd,haed]
    gameDisplay = pygame.display.set_mode(size)
    leikmadur = 0

    #Myndir
    mynd = pygame.image.load('mikkimina_valmynd.png')
    bakg_mynd = pygame.image.load('volundur_opnun.png')

    #Litir
    BLACK = (0, 0, 0)
    GRAY = (211,211,211)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    def __init__(self):
        pass

    def setup(self):
        global done
        global screen
        global clock
        pygame.init()

        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Völundarmús")

    def setup2(self):
        screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Viltu vera Mína eða Mikki?")
    #Tónlist
    def music(self,tune):
        pygame.init()
        pygame.mixer.music.load(tune)
        pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
        pygame.mixer.music.play()
    #Valmynd fyrir karaktera
    def picture(self):
        Völundarmús = pygame.transform.scale(self.bakg_mynd,self.size)
        self.gameDisplay.blit(Völundarmús,(0,0))

    def picture2(self):
        Mikkimina = pygame.transform.scale(self.mynd,self.size)
        self.gameDisplay.blit(Mikkimina,(0,0))
    #Game start level board
    def leikurIntro(self):
        self.picture()
        self.messageDisplayLevel('Völundarmús',2)
        self.takkar("Hefja Leik",337,450,150,75,self.GRAY,self.RED,'Byrja')
    #Level 1 board
    def level1Intro(self):
        self.picture()
        self.messageDisplayLevel('Velkomin/nn í völundarmús leikinn!', 4.5)
        self.messageDisplayLevel('Viltu velja leikmann?', 3)
        self.takkar("Já!",150,450,150,75,self.GRAY,self.RED,'Velja leikmann')
        self.takkar("Nei",550,450,150,75,self.GRAY,self.RED,'quit')
    #Val á leikmanni
    def velja_leikmann(self):
        self.picture2()
        self.messageDisplayLevel('Viltu vera Mikki eða Mína?', 8)
        self.takkar("Mikki",150,495,150,75,self.GRAY,self.RED,'mikki mús')
        self.takkar("Mína",500,495,150,75,self.GRAY,self.RED,'mína mús')
    #Birta texta
    def messageDisplayLevel(self,text,lina):
        introtexti = pygame.font.Font('Boogaloo.ttf', 60)
        litur0 = self.RED
        self.textSurf, self.textRect = self.textObjectsBlack(text, introtexti,litur0)
        self.textRect.center = ((self.breidd/2),(self.haed/lina))
        self.gameDisplay.blit(self.textSurf, self.textRect)
    #Hjálparfall fyrir takka
    def textObjectsBlack(self,text, font, litur0):
        textSurface = font.render(text, True, litur0)
        return textSurface, textSurface.get_rect()
    #Takkar
    def takkar(self,text,x,y,breidd,haed,litur1,litur2,action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #Gera kassa gráa ef músin fer yfir kassana
        if x+breidd > mouse[0] > x and y+haed > mouse[1] > y:
            pygame.draw.rect(self.gameDisplay, litur2,(x,y,breidd,haed))
            if click[0] == 1 and action != None:
                if action == "Byrja":
                    self.level = 1
                    return
                elif action == 'Velja leikmann':
                    self.velja_leikmann()
                    self.level = 2
                elif action == 'quit':
                    self.level= 0
                elif action == "mikki mús":
                    self.leikmadur=0
                    bord5 = Question(self,self.leikmadur)
                    bord5.spurningaIntro()
                    bord5.gameLoop()
                elif action == "mína mús":
                    self.leikmadur=1
                    bord5 = Question(self,self.leikmadur)
                    bord5.spurningaIntro()
                    bord5.gameLoop()
        else:
            pygame.draw.rect(self.gameDisplay, litur1,(x,y,breidd,haed))

        litur0= self.BLACK
        takkar2 = pygame.font.Font('Raleway.ttf', 30)
        textSurf, textRect = self.textObjectsBlack(text, takkar2, litur0)
        textRect.center = ((x+(breidd/2)),(y+(haed/2)))
        self.gameDisplay.blit(textSurf, textRect)

    def byrja(self):
        self.music('tonlist.mp3')
        self.setup()
        done = False
        #state_tune=1
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if self.level ==0:
                #self.music('tonlist.mp3')
                #state_tune=0
                self.leikurIntro()
            elif self.level ==1:
                #self.music('tonlist.mp3')
                #state_tune =1
                self.level1Intro()
            elif self.level == 2:
                #self.music('tonlist.mp3')
                #state_tune=2
                self.velja_leikmann()
            pygame.display.update()
            pygame.display.flip()

        pygame.quit()
