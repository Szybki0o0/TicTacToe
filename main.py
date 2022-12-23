import pygame

# Inicjalizacja modulu pygame i wyświetlacza
pygame.init()
pygame.display.init()

# Ustawienie parametrów dla okna jak rozmiar i nazwa
def SettingWindow():
    (width, height) = 650, 650
    global screen
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("TicTacToe")

# Główna funkcja odpowiedzialna za to co dzieje się na ekranie
def StartingWindow():
    # Deklaracja zmiennych pomocniczych
    circleTurn = False
    isRunning = True
    activeCoordinateLeft = 0
    activeCoordinateTop = 0
    pygame.display.flip()
    # Główna pętla programu sprawdzająca na bieżąco aktywność użytkownika
    while isRunning:
        # Pętla odpowiedzialna za aktualizowanie wyświetlania figur
        for element in rectList:
            # Usuwanie elemntów z listy gdy została już do nich przypisana figura oraz zmiana tury
            if element.left == activeCoordinateLeft and element.top == activeCoordinateTop:
                # Zmiana tury
                if circleTurn:
                    circleTurn = False
                else:
                    circleTurn = True
                rectList.remove(pygame.Rect(activeCoordinateLeft,activeCoordinateTop,160,160))
                pygame.display.update()
            else:
                # Aktualizowanie pozycji figury do potencjalnego kwadratu
                if element.collidepoint(pygame.mouse.get_pos()):
                    # Dla kółka
                    if circleTurn:
                        pygame.draw.circle(screen, grey,[element.left+80,element.top+80] , 60,15)
                        pygame.display.update()
                    # Dla krzyżyka
                    else:
                        pygame.draw.line(screen,white,[element.left+30,element.top+30],[element.left+130,element.top+130],25)
                        pygame.draw.line(screen,white,[element.left+30,element.top+130],[element.left+130,element.top+30],25)
                        pygame.display.update()
                # Zamalowywanie niepotrzenej figury aby nie pozostawała na niechcianej pozycji
                else:
                    pygame.draw.rect(screen, black, pygame.Rect(element.left+5, element.top+5, 150, 150))
        # Pętla odpowiedzialna za akcje użytkownika
        for event in pygame.event.get():
            # Warunek monitorujący przyciśnięcie przycisku myszki
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Pętla aktualizująca aktywne pozycje chcianego kwadratu
                for element in rectList:
                    if element.collidepoint(pygame.mouse.get_pos()):
                        activeCoordinateLeft = element.left
                        activeCoordinateTop = element.top
                        pygame.display.update()
            # Warunek monitorujący czy użytkownik zamknął okno
            if event.type == pygame.QUIT:
                isRunning = False
            if isRunning == False:
                pygame.quit()

# Funkcja odpowiedzialna za ustawienie i przechowywanie kolorów potrzebnych na planszy
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

# Wywołanie dwóch wyżej opisanych funkcji
SettingColors()
SettingWindow()

# Funkcja rysująca planszę gry i definiująca poszczególne pola gry
def DrawingBoard():
    # Narysowanie lini
    pygame.draw.line(screen, lightBlue,[230,60],[230,580],20)
    pygame.draw.line(screen, lightYellow,[60,410],[580,410],20)
    pygame.draw.line(screen, lightGreen,[60,230],[580,230],20)
    pygame.draw.line(screen, lightRed,[410,60],[410,580],20)

    # Korekcja dwóch lini tak, aby się przeplatały
    pygame.draw.rect(screen,lightBlue,pygame.Rect(221,221,20,20))
    pygame.draw.rect(screen,lightGreen,pygame.Rect(401,221,20,20))

    # Stworzenie i dodanie do listy poszczególnych 9 pól gry
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

# Wywołanie wyżej opisanych funkcji
DrawingBoard()
StartingWindow()

