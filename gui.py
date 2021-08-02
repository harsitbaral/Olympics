import pygame
import sys
import webscraper
import country_converter as coco

pygame.init()

SW, SH = 1600, 900

screen = pygame.display.set_mode((SW, SH))

BG = pygame.image.load("assets/background.png") 

# We store the countries with their info as a dictionary.

COUNTRIES = {}

COUNTRIES = webscraper.generate_data()

pygame.display.set_caption("Olympics")
pygame.display.set_icon(pygame.image.load("assets/icon_image.jpg"))

# Function for making the font at the designated size.

def bold(size):
    return pygame.font.Font("assets/RobotoCondensed-Bold.ttf", size)

ALL_DATA = []

# Creation of all the rows of data along with the information in them.

def generate_surfaces():
    for i in range(0, len(COUNTRIES)):
        ALL_DATA.append([pygame.image.load("assets/empty rect.png"), (200, i*125+175)])
        if COUNTRIES[list(COUNTRIES)[i]]["name"] != "ROC":
            abb = bold(60).render(coco.convert(names=COUNTRIES[list(COUNTRIES)[i]]["name"], to='name_short'), True, "white")
        else:
            abb = bold(60).render("ROC", True, "white")
            
        ALL_DATA.append([abb, (210, i*125+185)])
        gold = bold(65).render(str(COUNTRIES[list(COUNTRIES)[i]]["gold"]), True, "white")
        ALL_DATA.append([gold, (625, i*125+185)])
        silver = bold(65).render(str(COUNTRIES[list(COUNTRIES)[i]]["silver"]), True, "white")
        ALL_DATA.append([silver, (925, i*125+185)])
        bronze = bold(65).render(str(COUNTRIES[list(COUNTRIES)[i]]["bronze"]), True, "white")
        ALL_DATA.append([bronze, (1225, i*125+185)])

generate_surfaces()
    
def show_countries(): # Function for displaying countries' info
    global hovering, showing_countries, ALL_DATA
    while True:
        # Scrolling logic
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            for surface in ALL_DATA:
                new_rect = (surface[1][0], surface[1][1] - 20)
                surface[1] = new_rect
        if keys[pygame.K_UP]:
            if ALL_DATA[0][1][1] < 175:
                for surface in ALL_DATA:
                    new_rect = (surface[1][0], surface[1][1] + 20)
                    surface[1] = new_rect
        
        # Quitting logic
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] in range(200, 440) and pygame.mouse.get_pos()[1] in range(50, 145):
                    if showing_countries:
                        showing_countries = False
                        ALL_DATA = []
                    else:
                        showing_countries = True
                        generate_surfaces()
                
        screen.blit(BG, (0, 0))
        
        # Blitting info on the screen
        
        for surface in ALL_DATA:
            if surface[1][1] > 50:
                screen.blit(surface[0], surface[1])
        
        # Blitting titles for Country, Gold, Silver, Bronze
        
        screen.blit(pygame.image.load("assets/country V2.png"), (200, 50))
        screen.blit(pygame.image.load("assets/gold V2.png"), (525, 50))
        screen.blit(pygame.image.load("assets/silver V2.png"), (825, 50))
        screen.blit(pygame.image.load("assets/bronze V2.png"), (1125, 50))
        
        pygame.display.update()
    
show_countries()