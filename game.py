import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Simple")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
GREEN = (34, 177, 76)
BROWN = (139, 69, 19)

# Images
player_img = pygame.image.load("mario.png")  # Ajouter une image "mario.png" dans le même dossier
player_img = pygame.transform.scale(player_img, (40, 40))

# Joueur
player = pygame.Rect(100, 300, 40, 40)
player_speed = 5
player_gravity = 0
jumping = False

# Plateformes
platforms = [
    pygame.Rect(0, 350, WIDTH, 50),
    pygame.Rect(300, 250, 100, 20),
    pygame.Rect(500, 200, 150, 20),
    pygame.Rect(700, 150, 100, 20)
]

# Ennemi
enemy = pygame.Rect(600, 310, 40, 40)
enemy_speed = 2

# Police et score
font = pygame.font.SysFont("comicsans", 30)
score = 0

# Boucle principale
clock = pygame.time.Clock()

def draw():
    screen.fill(BLUE)  # Fond
    pygame.draw.rect(screen, GREEN, (0, 350, WIDTH, 50))  # Sol

    # Plateformes
    for platform in platforms:
        pygame.draw.rect(screen, BROWN, platform)

    # Joueur
    screen.blit(player_img, player)

    # Ennemi
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    # Score
    score_text = font.render(f"Score : {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mouvements du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed
    if keys[pygame.K_SPACE] and not jumping:
        player_gravity = -15
        jumping = True

    # Gravité
    player_gravity += 1
    player.y += player_gravity

    # Collision avec le sol
    if player.y >= 310:
        player.y = 310
        jumping = False

    # Collision avec les plateformes
    for platform in platforms:
        if player.colliderect(platform) and player_gravity > 0:
            player.y = platform.y - player.height
            jumping = False

    # Mouvement ennemi
    enemy.x += enemy_speed
    if enemy.x <= 0 or enemy.x >= WIDTH - enemy.width:
        enemy_speed *= -1

    # Collision avec l'ennemi
    if player.colliderect(enemy):
        print("GAME OVER!")
        running = False

    # Score
    if player.x > WIDTH - 50:
        score += 1
        player.x = 0

    draw()
    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
