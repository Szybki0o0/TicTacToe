import pygame

pygame.init()
pygame.display.init()


def SettingWindow():
    (width, height) = 650, 650
    global screen
    global font
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Sudoku")
    font = pygame.font.Font(None, 45)


def StartingWindow():
    isRunning = True
    pygame.display.flip()
    while isRunning:
        # print(pygame.mouse.get_pos())
        # Makes closing window available
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if isRunning == False:
                pygame.quit()


def SettingColors():
    global orange
    global white
    global red
    global black
    black = (0, 0, 0)
    red = (255, 0, 0)
    orange = (255, 165, 0)
    white = (255, 255, 255)



SettingColors()
SettingWindow()
pygame.draw.circle(screen, white,[40,40],40,3)
StartingWindow()

