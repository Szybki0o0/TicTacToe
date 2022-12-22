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
    circleTurn = False
    isRunning = True
    activeCoordinateLeft = 0
    activeCoordinateTop = 0
    pygame.display.flip()
    while isRunning:
        # print(pygame.mouse.get_pos())
        for element in rectList:
            if element.left == activeCoordinateLeft and element.top == activeCoordinateTop:
                rectList.remove(pygame.Rect(activeCoordinateLeft,activeCoordinateTop,160,160))
                pygame.display.update()
            else:
                if element.collidepoint(pygame.mouse.get_pos()):
                    if circleTurn:
                        pygame.draw.circle(screen, white,[element.left+80,element.top+80] , 60,15)
                        pygame.display.update()
                    else:
                        pygame.draw.line(screen,white,[element.left+30,element.top+30],[element.left+130,element.top+130],25)
                        pygame.draw.line(screen,white,[element.left+30,element.top+130],[element.left+130,element.top+30],25)
                        pygame.display.update()
                else:
                    pygame.draw.rect(screen, black, pygame.Rect(element.left+5, element.top+5, 150, 150))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if circleTurn:
                    circleTurn = False
                else:
                    circleTurn = True
                for element in rectList:
                    if element.collidepoint(pygame.mouse.get_pos()):
                        activeCoordinateLeft = element.left
                        activeCoordinateTop = element.top
                        pygame.display.update()
            if event.type == pygame.QUIT:
                isRunning = False
            if isRunning == False:
                pygame.quit()

def SettingColors():
    global white
    global black
    global lightBlue
    global lightGreen
    global lightRed
    global lightYellow
    global purpureus
    global darkerPurpureus
    black = (0, 0, 0)
    white = (255, 255, 255)
    lightBlue = (24, 146, 239)
    lightGreen = (128,237,153)
    lightRed = (219,80,74)
    lightYellow = (255,209,102)
    purpureus = (161,70,165)
    darkerPurpureus = (125,70,150)

SettingColors()
SettingWindow()
def DrawingBoard():
    pygame.draw.line(screen, lightBlue,[230,60],[230,580],20)
    pygame.draw.line(screen, lightYellow,[60,410],[580,410],20)
    pygame.draw.line(screen, lightGreen,[60,230],[580,230],20)
    pygame.draw.line(screen, lightRed,[410,60],[410,580],20)

    pygame.draw.rect(screen,lightBlue,pygame.Rect(221,221,20,20))
    pygame.draw.rect(screen,lightGreen,pygame.Rect(401,221,20,20))

    global rectList
    rectList = []
    x = 60
    y = 60
    for row in range(0,3):
        for col in range(0,3):
            if row == 0:
                rectList.append(pygame.Rect(x,y,160,160))
                x+=180
            elif row == 1:
                rectList.append(pygame.Rect(x,y,160,160))
                x+=180
            else:
                rectList.append(pygame.Rect(x,y,160,160))
                x+=180
            if col % 2 == 0 and col != 0:
                x = 60
                y+=180

DrawingBoard()
StartingWindow()

