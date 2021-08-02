from selenium import webdriver
import pygame

pygame.init()

SW, SH = 1600, 900

screen = pygame.display.set_mode((SW, SH))

BG = pygame.image.load("assets/background.png") 

pygame.display.set_caption("Olympics")
pygame.display.set_icon(pygame.image.load("assets/icon_image.jpg"))

loading_font = pygame.font.Font("assets/RobotoCondensed-Bold.ttf", 65)

options = webdriver.ChromeOptions()
options.add_argument("headless")

url = "https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm"

browser = webdriver.Chrome(chrome_options=options)
browser.get(url)

countries = {}

names = browser.find_elements_by_class_name("playerTag")
golds = []
silvers = []
bronzes = []
data = browser.find_elements_by_css_selector("td")

loading = loading_font.render(f"Loading...", True, "white")

def generate_data():
    global countries, loading
    for name in names:
        if name.text != "":
            new_abbreviation = ''.join([l for l in name.text if l not in ['a', 'i', 'e', 'o', 'u']])
            countries[f"{name.text}"] = {"name": name.text, "abbreviation": new_abbreviation[0:1], "gold": 0, "silver": 0, "bronze": 0}

    for i in range(len(data)):
        if data[i].text != "":
            if data[i].text[0].isalpha():
                countries[data[i].text]["gold"] = data[i+1].text
                countries[data[i].text]["silver"] = data[i+2].text
                countries[data[i].text]["bronze"] = data[i+3].text
                loading = loading_font.render(f"Loading {data[i].text}...", True, "white")
            screen.blit(BG, (0, 0))
        loading_rect = loading.get_rect(center=(800, 450))
        screen.blit(loading, loading_rect)
        pygame.display.update()

    return countries