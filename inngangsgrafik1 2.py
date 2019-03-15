"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
Uppfært V2019 (ingolfuh@hi.is)
"""

import pygame
from veljalit import Veljalit
from Spurningaleikur import spurningaleikur
from Púsluspil import pusluspil

#Define some parameters
breidd = 800
haed = 600
startImage = pygame.image.load('volundarmus_titill.png')
bakgrunnurGameIntro = pygame.image.load('volundarhus.png')
level=0

#Myndir fyrir val á leikmanni
breidd2 = 800
haed2 = 600
mynd = pygame.load('mikkimina_valmynd.png')


#Skjár
size = [breidd,haed]
display_breidd = 800
display_haed = 600
gameDisplay = pygame.display.set_mode(size)

# Define some colors
BLACK = (0, 0, 0)
GRAY = (211,211,211)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup
def setup():
    global done
    global screen
    global clock
    pygame.init()

    # Set the width and height of the screen [width,height]
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Völundarmús")

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Hide the mouse cursor
    pygame.mouse.set_visible(0)

def setup():
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Viltu vera Mína eða Mikki?")
    clock = pygame.time.Clock()


#Draw figure cursor
"""def draw_stick_figure(screen):
    global x
    global y

    pos = pygame.mouse.get_pos()
    x= pos[0]
    y= pos[1]

    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)"""

#pyGame music
def music(tune):
    pygame.mixer.music.load(tune)
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()

#pyGame picture
def picture(mmmynd):
    mmmynd = pygame.transform.scale(mmmynd,size)
    gameDisplay.blit(mmmynd,(0,0))

#Game start level board
def leikurIntro():
    picture(startImage)
    draw_stick_figure(screen)
    #messageDisplayLevel
    takkar("Hefja Leik",337,450,150,75,GRAY,RED,'StartLevel1')
#Level 1 board
def level1Intro():
    picture(bakgrunnurGameIntro)
    draw_stick_figure(screen)
    messageDisplayLevel('Velkomin/nn í völundarmús leikinn!', 4.5)
    messageDisplayLevel('Viltu velja leikmann?', 3)
    takkar("Já!",150,450,150,75,GRAY,RED,'StartLevel1B')
    takkar("Nei",550,450,150,75,GRAY,RED,'quit')


def velja_leikmann():
    picture(mynd)
    draw_stick_figure(screen)
    messageDisplayLevel('Veldu leikmann', 3)
    takkar("Mikki",150,450,150,75,GRAY,RED,'mikki mús')
    takkar("Mína",550,450,150,75,GRAY,RED,'mína mús')
#Display text on board
def messageDisplayLevel(text,lina):
    if level ==0:
        introtexti = pygame.font.Font('HPfont.ttf', 65)
        litur0= BLACK
    elif level ==1:
        introtexti = pygame.font.Font('Boogaloo.ttf', 35)
        litur0= RED
    textSurf, textRect = textObjectsBlack(text, introtexti,litur0)
    textRect.center = ((display_breidd/2),(display_haed/lina))
    gameDisplay.blit(textSurf, textRect)
#Support function for buttons
def textObjectsBlack(text, font, litur0):
    textSurface = font.render(text, True, litur0)
    return textSurface, textSurface.get_rect()

######## TAKKAR ########
def takkar(text,x,y,breidd,haed,litur1,litur2,action=None):
    global level
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #gera kassa gráa ef músin fer yfir kassana
    if x+breidd > mouse[0] > x and y+haed > mouse[1] > y:
        pygame.draw.rect(gameDisplay, litur2,(x,y,breidd,haed))
        if click[0] == 1 and action !=None:
            if action == "StartLevel1":
                level= 1
                return
            elif action == 'mikki mús' or action == 'mína mús':
                litur= Veljalit()
                litur.veljalit_litur(litur)
            elif action == 'quit':
                level= 0
    else:
        pygame.draw.rect(gameDisplay, litur1,(x,y,breidd,haed))

    litur0= BLACK
    takkar2 = pygame.font.Font('Raleway.ttf', 30)
    textSurf, textRect = textObjectsBlack(text, takkar2, litur0)
    textRect.center = ((x+(breidd/2)),(y+(haed/2)))
    gameDisplay.blit(textSurf, textRect)

# -------- Main Program Loop -----------
def main():
    setup()
    done = False
    state_tune=1
    # Loop until the user clicks the close button.
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if level ==0:
            if state_tune !=0:
                music('tonlist.mp3')
                state_tune=0
            leikurIntro()
        elif level ==1:
            if state_tune == 0:
                music('tonlist.mp3')
                state_tune =1
            level1Intro()
        elif level == 2:
            if state_tune == 1:
                music('tonlist.mp3')
                state_tune=2
            velja_leikmann()
        #elif level == 3:

        pygame.display.update()
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 20 frames per second
        clock.tick(80)
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__=='__main__':
    main()
else:
    print('No just imported by another class')
