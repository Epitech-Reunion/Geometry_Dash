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
cube_img = pygame.image.load("cube.png").convert_alpha()
obstacle_img = pygame.image.load("obstacle.png").convert_alpha()
jump_sound = pygame.mixer.Sound("saut.wav")
FPS = 60
clock = pygame.time.Clock()

# Définie les classes
class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cube_img
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = window_height - 176
        self.jump = False
        self.jump_height = 10

    def update(self):
        # Gère les mouvements et le saut du cube
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.jump:
            self.jump = True
        if self.jump:
            jump_sound.play()
            if self.jump_height >= -10:
                neg = 1
                if self.jump_height < 0:
                    neg = -1
                self.rect.y -= self.jump_height**2 * 0.5 * neg
                self.jump_height -= 1
            else:
                self.rect.y = window_height - 176
                self.jump = False
                self.jump_height = 10

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstacle_img
        self.rect = self.image.get_rect()

        # Step4 - Définir la position de l'obstacle
        self.rect.x = ...
        self.rect.y = ...

    def update(self):
        # Gère les mouvements de l'obstacle

        # Step4 - Déplacer l'obstacle
        ...
        if self.rect.right < 0:

            # Step4 - Réinitialiser la position de l'obstacle
            pass

# Initialise la boucle de jeu
images = pygame.sprite.Group()
cube = Cube()
images.add(cube)

# Step4 - Créer un obstacle ici

obstacle = ...
images.add(obstacle)

play = True
fond_x = fond_img.get_width()
sol_x = sol_img.get_width()
sol_y = window_height - sol_img.get_height()

while play:
    # Gère les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    # Met à jour les objets
    images.update()

    # Bouge le fond et le sol
    clock.tick(FPS)
    fond_x = (fond_x - 1) % fond_img.get_width()
    window.blit(fond_img, (fond_x, 0))
    window.blit(fond_img, (fond_x - fond_img.get_width(), 0))
    sol_x = (sol_x - 8) % sol_img.get_width()
    window.blit(sol_img, (sol_x, sol_y))
    window.blit(sol_img, (sol_x - sol_img.get_width(), sol_y))

    # Dessine les objets
    images.draw(window)

    # Met à jour l'écran
    pygame.display.update()

# Nettoie la fenêtre
pygame.quit()
