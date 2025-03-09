from deep_translator import GoogleTranslator
import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("French Study App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

# Button class
class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.rect = pygame.Rect(pos[0], pos[1], 500, 50)
        self.color = GRAY
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        screen.blit(text_surf, (self.pos[0] + 10, self.pos[1] + 10))

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.callback()

# Functions
def translate_to_french():
    text = input("Enter text in English: ")
    translation = GoogleTranslator(source='en', target='fr').translate(text)
    print(f"French Translation: {translation}\n")
    return translation

def translate_to_english():
    text = input("Entrez le texte en français: ")
    translation = GoogleTranslator(source='fr', target='en').translate(text)
    print(f"English Translation: {translation}\n")



# Button callbacks
def on_translate_to_french():
    global current_screen
    current_screen = "translate_to_french"

def on_translate_to_english():
    global current_screen
    current_screen = "translate_to_english"


def on_exit():
    pygame.quit()
    sys.exit()

# Create buttons for the main menu
buttons = [
    Button("Translate English to French", (50, 50), on_translate_to_french),
    Button("Translate French to English", (50, 120), on_translate_to_english),
    Button("Exit", (50, 330), on_exit)
]

# Main loop
current_screen = "main_menu"
running = True

def main_menu():
    screen.fill(WHITE)
    for button in buttons:
        button.draw()

def translate_to_french_screen():
    screen.fill(WHITE)
    input_box = pygame.Rect(90, 90, 200, 50)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
 
    print(translate_to_french)
    translate_to_french()

def translate_to_english_screen():
    screen.fill(WHITE)
    translate_to_english()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "main_menu":
                for button in buttons:
                    button.check_click(event.pos)
    
    if current_screen == "main_menu":
        main_menu()
    elif current_screen == "translate_to_french":
        translate_to_french_screen()
    elif current_screen == "translate_to_english":
        translate_to_english_screen()
  
    
    pygame.display.flip()

pygame.quit()