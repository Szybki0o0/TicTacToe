import pygame

pygame.init()
pygame.display.init()


def SettingWindow():
    (width, height) = 650, 650
    global screen
    global font
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe")
    font = pygame.font.Font(None, 45)


def StartingWindow():
    isRunning = True
    pygame.display.flip()
    while isRunning:
        print(pygame.mouse.get_pos())
        # Makes closing window available
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if isRunning == False:
                pygame.quit()


def SettingColors():
    global lightBlue
    global white
    global red
    global black
    global lightGreen
    global lightRed
    global lightYellow
    black = (0, 0, 0)
    red = (255, 0, 0)
    lightBlue = (24, 146, 239)
    lightGreen = (128,237,153)
    lightRed = (219,80,74)
    lightYellow = (255,209,102)
    white = (255, 255, 255)



SettingColors()
SettingWindow()
def Board():
    #pygame.draw.rect(screen, white, pygame.Rect(60, 60, 151, 151))
    #pygame.draw.rect(screen, white, pygame.Rect(231, 60, 151, 151))


    pygame.draw.line(screen, lightBlue,[220,60],[220,580],20)
    pygame.draw.line(screen, lightYellow,[60,400],[580,400],20)
    pygame.draw.line(screen, lightGreen,[60,220],[580,220],20)
    pygame.draw.line(screen, lightRed,[400,60],[400,580],20)

    pygame.draw.rect(screen,lightBlue,pygame.Rect(211,211,20,20))
    pygame.draw.rect(screen,lightGreen,pygame.Rect(391,211,20,20))

Board()

StartingWindow()

