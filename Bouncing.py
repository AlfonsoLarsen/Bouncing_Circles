import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Circles")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colors = [WHITE, (255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Set up the circles' starting positions and directions
circles = []
for i in range(3):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    dx = random.uniform(-2, 2)
    dy = random.uniform(-2, 2)
    circles.append({'x': x, 'y': y, 'dx': dx, 'dy': dy})

# Set up the clock
clock = pygame.time.Clock()
speed = 140

# Main game loop
done = False
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                speed += 50
            elif event.button == 3:
                speed -= 50

    # Move the circles
    for circle in circles:
        circle['x'] += circle['dx']
        circle['y'] += circle['dy']

        # Check if the circle has hit the edges of the screen
        if circle['x'] < 0 or circle['x'] > WIDTH:
            circle['dx'] *= -1
            # Change the circle's color when it hits the edge
            random.shuffle(colors)
        if circle['y'] < 0 or circle['y'] > HEIGHT:
            circle['dy'] *= -1
            # Change the circle's color when it hits the edge
            random.shuffle(colors)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the circles
    for i, circle in enumerate(circles):
        color = colors[i]
        pygame.draw.circle(screen, color, (circle['x'], circle['y']), 15)

    # Update the screen
    pygame.display.flip()

    # Wait for a little bit so the circles don't move too quickly
    clock.tick(speed)

# Quit Pygame
pygame.quit()
