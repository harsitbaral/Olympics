import pygame
import sys
import json

pygame.init()

SW, SH = 1600, 900

screen = pygame.display.set_mode((SW, SH))

BG = pygame.image.load("assets/background.png") 

COUNTRIES = {}

with open("countries.json", 'r') as c:
    COUNTRIES = json.loads(c.read())

pygame.display.set_caption("Olympics")
pygame.display.set_icon(pygame.image.load("assets/icon_image.jpg"))

def bold(size):
    return pygame.font.Font("assets/RobotoCondensed-Bold.ttf", size)

def regular(size):
    return pygame.font.Font("assets/RobotoCondensed-Regular.ttf", size)

def show_countries():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(BG, (0, 0))
        
        screen.blit(pygame.image.load("assets/country.png"), (200, 50))
        screen.blit(pygame.image.load("assets/gold.png"), (525, 50))
        screen.blit(pygame.image.load("assets/silver.png"), (825, 50))
        screen.blit(pygame.image.load("assets/bronze.png"), (1125, 50))
        
        screen.blit(pygame.image.load("assets/empty rect.png"), (200, 175))
        
        screen.blit(pygame.image.load(COUNTRIES[list(COUNTRIES)[0]]["flag"]), (220, 190))
        abb = bold(65).render(COUNTRIES["United States"]["abbreviation"], True, "white")
        screen.blit(abb, (350, 185))
        
        for i in range(1, len(COUNTRIES)):
            screen.blit(pygame.image.load("assets/empty rect.png"), (200, i*125+175))
            current_flag = pygame.transform.scale(pygame.image.load(COUNTRIES[list(COUNTRIES)[i]]["flag"]), (120, 63))
            screen.blit(current_flag, (220, i*125+190))
            abb = bold(65).render(COUNTRIES[list(COUNTRIES)[i]]["abbreviation"], True, "white")
            screen.blit(abb, (350, i*125+185))
        
        pygame.display.update()
    
show_countries()