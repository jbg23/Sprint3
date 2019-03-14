from PIL import Image

class Veljalit:
    def __init__(self):
        print('smidur veljalit')

    def veljalit_litur(self, bord):
        self.veljalitinn()

    def veljalitinn(self):
        #Bjóða upp á að velja leikmann -> sýna myndir -> velja leikmann ->næsta borð
        print('Veldu þann lit á leikmann sem þú vilt vera')
        Mikki = Image.open('mikki.png')
        Mikki.show()
        Mina = Image.open('mina.png')
        Mina.show()

        litur = input('Sláðu inn 1 fyrir Mikka, 2 fyrir Mínu\n')
        if litur == '1':
            print('Þú ert Mikki')
        if litur == '2':
            print('Þú ert Mína')

def main():
    pass

if __name__== '__main__':
    main()
else:
    print('þú ert innportuð í veljalit')
