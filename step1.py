import pygame

# Initialise la fenêtre
pygame.init()
window_width = 768
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Geometry Dash")

# Charge les assets
fond_img = pygame.image.load("fond.png").convert_alpha()
sol_img = pygame.image.load("sol.png").convert_alpha()

# Initialises la variable cube_img comme ci-dessus


# Définie les classes
class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # utiliser l'image du cube ici
        self.image = ...
        self.rect = self.image.get_rect()

        # Step1 - Définir la position du cube ici
        self.rect.x = 0
        self.rect.y = 0

# Initialise la boucle de jeu
images = pygame.sprite.Group()

# Step1 - Créer un Cube ici
cube = ...

images.add(cube)
play = True
sol_y = window_height - sol_img.get_height()

while play:
    # Gère les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # Bouge le fond et le sol
    window.blit(fond_img, (0, 0))
    window.blit(sol_img, (0, sol_y))

    # Dessine les objets
    images.draw(window)

    # Mets a jour l'écran
    pygame.display.update()

# Nettoie la fenêtre
pygame.quit()

