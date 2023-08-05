import pygame
pygame.init()
def SetUpTile(screen,tmap,dictionary={},TileSize=10):
    x=0
    y=0
    stuff=tmap.split(',')
    for i in stuff:
        print(x,':',y)
        if i!='n':
            if i!=' ':
                for key,val in dictionary.items():
                    if key==i:
                        val.Draw(x,y)
                        x+=TileSize
            else:
                x+=TileSize
        else:
            y+=TileSize
            x=0
class Tile:
    def __init__(self,screen,**kwarg):
        self.size=(10,10)
        self.yn=False
        self.screen=screen
        self.color=(0,0,0)
        for key,val in kwarg.items():
            if key=='img':
                self.Surf=pygame.image.load(val)
                self.yn=True
            elif key=='Size':
                self.size=val
            elif key=='Color':
                self.color=val
            else:
                print(f'Value Error! No Attribute to {key}')
                quit()
        if self.yn:
            self.Surf=pygame.transform.scale(self.Surf,self.size)
        else:
            self.Surf=pygame.Surface(self.size)
            self.Surf.fill((0,0,0))
    def Draw(self,x,y):
        self.screen.blit(self.Surf,(x,y))