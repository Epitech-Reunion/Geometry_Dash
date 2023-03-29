import pygame

# Initialse la fenêtre
pygame.init()
window_width = 768
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Geometry Dash")

# Charge les assets
fond_img = pygame.image.load("fond.png").convert_alpha()
sol_img = pygame.image.load("sol.png").convert_alpha()
cube_img = pygame.image.load("cube.png").convert_alpha()
FPS = 60
clock = pygame.time.Clock()

# Definie les classes
class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cube_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = window_height - 176

# Initialise la boucle de jeu
images = pygame.sprite.Group()
cube = Cube()
images.add(cube)
play = True
fond_x = fond_img.get_width()

# Step2 - Donner comme valeur à sol_x la largeur de sol_img
sol_x = sol_img.get_width()
sol_y = window_height - sol_img.get_height()

while play:
    # Gère les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    clock.tick(FPS)
    fond_x = (fond_x - 1) % fond_img.get_width()
    sol_x = (sol_x - 8) % sol_img.get_width()

    # Déplace l'arrière plan
    window.blit(fond_img, (fond_x, 0))
    window.blit(fond_img, (fond_x - fond_img.get_width(), 0))

    # Step2 - Bouger le sol ici de la même manière que l'arrière plan

    window.blit(sol_img, (sol_x, sol_y))
    window.blit(sol_img, (sol_x - sol_img.get_width(), sol_y))
    
    
    # Dessine les objets
    images.draw(window)

    # Mets a jour l'écran
    pygame.display.update()

# Nettoie la fenêtre
pygame.quit()

