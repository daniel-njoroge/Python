import pygame

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Square properties
x, y = 50, 150
velocity = 2

# Game loop
running = True
while running:
    pygame.time.delay(10)  # Delay for smooth movement
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move square
    x += velocity
    if x > WIDTH - 50 or x < 0:
        velocity *= -1  # Reverse direction
    
    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.display.update()

pygame.quit()
