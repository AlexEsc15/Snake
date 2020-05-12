# Libraries

import pygame as pg
import sys

# Inits

pg.font.init()

# Global Variables

# ----- Window properties

WIDTH = 500
HEIGHT = 500
rw = 10
rh = 10

WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (200,200,255)
BLACK = (0,0,0)

# Defaults text

myfont = pg.font.SysFont('Comic Sans MS',12)

class Snake():


    def __init__(self):

        self.speed = 1
        self.posx = WIDTH//2 - rw//2
        self.posy = HEIGHT//2 - rh//2
        self.posx1 = WIDTH//2 - rw//2 
        self.posy1 = HEIGHT//2 - rh//2
        self.body = [pg.Rect((self.posx,self.posy),(rw,rh)), pg.Rect((self.posx1,self.posy1),(rw,rh))]
        
        pass

    def Draw(self,screen,color):
        
        pg.draw.rect(screen,color,self.body[0],0)
        pg.draw.rect(screen,color,self.body[1],0)
        
        
        pass
    
    def Move(self, key):

        if key == pg.K_UP:
            self.body[1].centery = self.body[0].centery  
            self.body[0].centery -= rh
    
            print(self.body[0].centery)
            
            pass

        elif key== pg.K_DOWN:
            pass
        
        elif key== pg.K_RIGHT:
            pass
        
        elif key== pg.K_LEFT:
            pass
        
        else:
            print("Moving")
            pass
        
        pass

    def Eating(self,apple):

        pass

    def Colide(self, array):

        pass
    


class Apple():

    def __init__(self):

        pass
    
    def Draw(self):

        pass
    
    pass


def Main():

    screen = pg.display.set_mode((HEIGHT,WIDTH))
    background = WHITE
    screen.fill(background)

    game_state = ("start","running","pause","gameover")
    current_game_state = "start"


    # INIT SCREEN TEXTS

    Init_Screen_Text = myfont.render(" PRESS SPACE TO PLAY ", False, BLACK)

    # GAME SCREEN TEXTS

    Game_Screen_Pause = myfont.render("PAUSE", False, RED)

    orochi = Snake()

    
    while True:

        pressed = pg.key.get_pressed()
        

        # FIRST SCREEN TO START THE GAME

        if current_game_state == "start":

            #Here goes any display logic to game start screen
            
            #print("start state")
            screen.fill(BLUE)
            screen.blit(Init_Screen_Text,(WIDTH//3,HEIGHT//2))
            
            #Here ends any display logic to game start screen

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        current_game_state = "running"
                        print("Game state changed to RUNNING")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()
               
            pass


        # MAIN GAME SCREEN
        elif current_game_state == "running":

            #Here goes any display logic to game start screen
            screen.fill(WHITE)
            orochi.Draw(screen,GREEN)
            
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    orochi.Move(event.key)                    
                    
                    if event.key == pg.K_SPACE:
                        current_game_state = "pause"
                        print("Game state changed to PAUSE")
                    
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()

            
            #Here ends any display logic to game start screen

            pass

        # PAUSE SCREEN
        elif current_game_state == "pause":

            #Here goes any display logic to game start screen
            screen.fill((200,200,200))
            screen.blit(Game_Screen_Pause,(10,10))
            
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        current_game_state = "running"
                        print("Game state changed to RUNNING")
                if event.type == pg.QUIT:
                    print("QUIT")
                    pg.quit()
                    sys.exit()

            
            #Here ends any display logic to game start screen

            

        # GAMEOVER SCREEN
        elif current_game_state == "gameover":

            #Here goes any display logic to game start screen
            screen.fill(BLACK)

            
            #Here ends any display logic to game start screen

            pass

        # IN CASE OF ERROR
        else:
            print("An error ocured, no game state existing")

        
        # GET QUIT EVENT
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit pressed")
                pg.quit()
                sys.exit()
              

        pg.display.update()
        #print("flipped")
          
          
          
        




if __name__=="__main__":

    Main()
    
    pass
