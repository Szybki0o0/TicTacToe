import pygame

# Initialization of pygame module and display
pygame.init()
pygame.display.init()

# Function called when someone wins
def endWin(result):
    pygame.draw.rect(screen,black,pygame.Rect(60,60,550,550))
    screen.blit(title.render(f'Winner: {result}', False, white), (150, 60))
    screen.blit(table.render(f'Number of wins', False, white), (180, 240))
    screen.blit(table.render(f'X: {nowX}       O: {nowO}', False, white), (210, 300))
    screen.blit(press.render(f'Press Space to continue', False, white), (210, 480))
    global isEnd
    isEnd = True

# Function called when there is a draw
def endDraw(x,o):
    pygame.draw.rect(screen,black,pygame.Rect(60,60,550,550))
    screen.blit(title.render(f'Draw', False, white), (220, 60))
    screen.blit(table.render(f'Number of wins', False, white), (180, 240))
    screen.blit(table.render(f'X: {x}       O: {o}', False, white), (210, 300))
    screen.blit(press.render(f'Press Space to continue', False, white), (210, 480))
    global isEnd
    isEnd = True

# Setting parameters for screen
def SettingWindow():
    # Screen, its size and display name
    (width, height) = 650, 650
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe")
    # 3 fonts of different size
    global title
    global table
    global press
    pygame.font.init()
    title = pygame.font.SysFont('Copper Black', 100)
    table = pygame.font.SysFont('Copper Black', 50)
    press = pygame.font.SysFont('Copper Black', 25)

# Main function responsible for what's on the screen
def StartingWindow():
    # Declaration of assistant variables
    global isEnd
    global board
    global nowX
    global nowO
    nowX = 0
    nowO = 0
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] # list representing game board
    circleTurn = False
    isRunning = True
    isEnd = False
    activeCoordinateLeft = 0
    activeCoordinateTop = 0
    pygame.display.flip()
    # Main program loop monitoring user actions
    while isRunning:
        # Loop responsible for dynamic actualizing box content
        for element in rectList:
            # Deleting elements from list when there is figure assigned to it and turn change
            if element.left == activeCoordinateLeft and element.top == activeCoordinateTop:
                # Turn change
                if circleTurn:
                    circleTurn = False
                else:
                    circleTurn = True
                rectList.remove(pygame.Rect(activeCoordinateLeft,activeCoordinateTop,160,160))
                if len(rectList) == 0 and isEnd == False:
                    endDraw(nowX,nowO)
                pygame.display.update()
            else:
                # Actualising figure position to potential box
                if element.collidepoint(pygame.mouse.get_pos()) and isEnd == False:
                    # For o
                    if circleTurn:
                        pygame.draw.circle(screen, grey,[element.left+80,element.top+80] , 60,15)
                        pygame.display.update()
                    # For x
                    else:
                        pygame.draw.line(screen,white,[element.left+30,element.top+30],[element.left+130,element.top+130],25)
                        pygame.draw.line(screen,white,[element.left+30,element.top+130],[element.left+130,element.top+30],25)
                        pygame.display.update()
                # Covering unwanted figure so that it doesn't stay in a box
                elif isEnd == False:
                    pygame.draw.rect(screen, black, pygame.Rect(element.left+5, element.top+5, 150, 150))
        # Pętla odpowiedzialna za akcje użytkownika
        # Loop responsible for user actions
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and isEnd:
                    pygame.draw.rect(screen, black, pygame.Rect(60, 60, 550, 550))
                    isEnd = False
                    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
                    activeCoordinateLeft = 0
                    activeCoordinateTop = 0
                    DrawingBoard()
            # Condition monitoring if mouse button was clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Loop actualising active box position
                for element in rectList:
                    if element.collidepoint(pygame.mouse.get_pos()):
                        activeCoordinateLeft = element.left
                        activeCoordinateTop = element.top
                        pygame.display.update()

                        # Checking in which column is new figure
                        if activeCoordinateLeft == 60:
                            i = 0
                        elif activeCoordinateLeft == 240:
                            i = 1
                        elif activeCoordinateLeft == 420:
                            i = 2

                        # Checking in which row is new figure
                        if activeCoordinateTop == 60:
                            j = 0
                        elif activeCoordinateTop == 240:
                            j = 1
                        elif activeCoordinateTop == 420:
                            j = 2

                        # Editing list
                        if circleTurn:
                            board[j][i] = 'O'
                        else:
                            board[j][i] = 'X'

                        if isEnd == False:
                            # Checking columns
                            for i in range(3):
                                if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                                    if board[0][i] == 'X':
                                        nowX += 1
                                    else:
                                        nowO += 1
                                    endWin(board[0][i])
                                    break
                            # Checking rows
                            for i in range(3):
                                if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                                    if board[i][0] == 'X':
                                        nowX += 1
                                    else:
                                        nowO += 1
                                    endWin(board[i][0])
                                    break
                            # Checking diagonals
                            if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
                                if board[1][1] == 'X':
                                    nowX += 1
                                else:
                                    nowO += 1
                                endWin(board[1][1])
                            elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
                                if board[1][1] == 'X':
                                    nowX += 1
                                else:
                                    nowO += 1
                                endWin(board[1][1])
            # Condition monitoring if window is closed
            if event.type == pygame.QUIT:
                isRunning = False
            if isRunning == False:
                pygame.quit()

# Function responsible for setting and storing colors needed on the board
def SettingColors():
    global white
    global black
    global lightBlue
    global lightGreen
    global lightRed
    global lightYellow
    global grey
    grey = (105,105,105)
    black = (0, 0, 0)
    white = (255, 255, 255)
    lightBlue = (24, 146, 239)
    lightGreen = (128,237,153)
    lightRed = (219,80,74)
    lightYellow = (255,209,102)

# Function call
SettingColors()
SettingWindow()

# Function drawind game board and defining boxes
def DrawingBoard():
    # Drawing lines
    pygame.draw.line(screen, lightBlue,[230,60],[230,580],20)
    pygame.draw.line(screen, lightYellow,[60,410],[580,410],20)
    pygame.draw.line(screen, lightGreen,[60,230],[580,230],20)
    pygame.draw.line(screen, lightRed,[410,60],[410,580],20)

    # Corecting two lines so they interwine
    pygame.draw.rect(screen,lightBlue,pygame.Rect(221,221,20,20))
    pygame.draw.rect(screen,lightGreen,pygame.Rect(401,221,20,20))

    # Creation and addition 9 boxes to list
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

# Function call
DrawingBoard()
StartingWindow()
