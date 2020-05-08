import pygame


def main():
    # inicializa Pygame
    pygame.init()

    # establece el título de la ventana
    pygame.display.set_caption('Crear ventana')

    # establece el tamaño de la ventana
    pygame.display.set_mode((600, 400))

    # bucle infinito
    while True:
        # retorna un solo evento de la cola de eventos
        event = pygame.event.wait()

        # si se presiona el botón 'cerrar' de la ventana
        if event.type == pygame.QUIT:
            # detiene el bucle
            break

    # finaliza Pygame
    pygame.quit()

class Snake():


    def __init__(self):

        pass

    def Draw(self):

        pass
    
    def Move(self, key):
        
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



class Screens():

    def __init__(self):

        pass

    pass




if __name__=="__main__":

    main()
