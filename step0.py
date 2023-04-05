import pygame

# Initialse la fenêtre
pygame.init()

# Définis les variables window_width et window_height


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Geometry Dash")

# Charge les assets
fond_img = pygame.image.load("fond.png").convert_alpha()
sol_img = pygame.image.load("sol.png").convert_alpha()

# Initialises la boucle de jeu
play = True

while play:
    # Gère les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # Affiche le fond
    window.blit(fond_img, (0, 0))

    # Step0 - Afficher le sol ici

    # Mets a jour l'écran
    pygame.display.update()

# Nettoie la fenêtre
pygame.quit()
